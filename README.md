# Django and Docker example

This is my example Django setup using Docker for local development.

I am not an expert but it seems to work.

The Django files (in `myproject/`) are a very minimal initial project and app
simply to indicate that things are working. Replace it with your own more
useful code!


## Start it

1. Install Docker, e.g. [Docker for Mac](https://docs.docker.com/docker-for-mac/install/).

2. Download this repository.

3. Optional: In `docker-compose.yml` change the two `container_name` values from `myproject_db` and `myproject_web` to something that makes sense for your project. e.g. `weblog_db` and `weblog_web` if your project is called weblog.

4. If you did that you'll also need to change `myproject_web` in the two scripts within the `/scripts/` directory.

5. Create a `.env` file at the same level as this README, containing the following. This will be used by Docker.

    ```
    # Environment settings for local development.

    POSTGRES_USER=mydatabaseuser
    POSTGRES_PASSWORD=mypassword
    POSTGRES_DB=mydatabase
    POSTGRES_HOST=myproject_db

    DJANGO_SETTINGS_MODULE=myproject.myproject.settings.development
    ```
    
    **NOTE:** If you changed `myproject_db` in the previous step, you should change the `POSTGRES_HOST` value to match it in the `.env` file. You can change the other postgres settings if you like, but it's not required.

6. On the command line, within this directory, do this to build the image and
   start the container:

        docker-compose build

7. If that's successful you can then start it up. This will start up the database and web server, and display the Django `runserver` logs:

        docker-compose up

8. Open http://0.0.0.0:8000 in your browser.


If you want to use a domain for accessing your local development website, instead of the IP address `0.0.0.0`, then:

1. Open the `/etc/hosts` file on your computer (you'll probably have to use `sudo` to be able to save it).

2. Add something like this, choosing your preferred domain name, and save the file:

        127.0.0.1 www.mywebsite.test

3. You might need to flush your DNS cache. [See here for Mac and Linux instructions.](https://help.dreamhost.com/hc/en-us/articles/214981288-Flushing-your-DNS-cache-in-Mac-OS-X-and-Linux)

4. You can then visit http://www.mywebsite.test:8000 (or whatever you set the domain to).


## More explanation

We are creating a "container" that has our web server and database within it. Each of those is constructed from an "image".

The `docker-compose.yml` file describes what we're setting up, the web server and database. ([Here are the docs for docker-compose.yml.](https://docs.docker.com/compose/compose-file/compose-file-v3/))

The database server uses an existing image (`postgres:alpine`) which doesn't require any further configuration. ([Alpine images](https://hub.docker.com/_/alpine) are based on a small version of Linux.)

The web server definition has a `build` option pointing at the current directory (`.`), which is where it will look for a `Dockerfile` describing its image. ([Here are the docs for Dockerfiles.](https://docs.docker.com/engine/reference/builder/))

Our web server image, defined in the `Dockerfile`, is based on an existing image that uses Python 3.8 (`python:3.8-alpine`) and we then install and set up further things within it.

Some python packages might require further Linux packages to be installed before they will work. For example, if you're installing Pillow, for manipulating images, you might need to add something like `jpeg-dev zlib-dev libjpeg` at the end of the list of packages installed by `apk add`. You'll know this is the case if you get errors saying packages are missing when it tries to install python packages. If this happens, alter the `Dockerfile` and run `docker-compose build` again.

The `Dockerfile` installs [pipenv](https://pipenv.readthedocs.io/en/latest/) and then all the python packages defined in the `Pipfile` in a virtual environment. If you were using `pip` you'd do something similar here with a `requirements.txt` file.

The description of the web server in `docker-compose.yml` says that when we start it up, it will always run the Django migrations and then the development webserver.


## Ongoing work

Every time you come to work on the site:

    docker-compose up

Alternatively you can do the following to run it in "detached" mode, in the background, but I like to see the logs during development:

    docker-compose up -d

Use Ctrl-C to stop it (or, in detached mode, `docker-compose stop`). You can see what's running in Docker Desktop.

To access the shell in the web container:

    docker exec -it myproject_web sh

Here, and below, you'll need to change `myproject_web` or `myproject_db` if you changed them to your own names while setting things up.

You can then run Django management commands from there, making sure to do it within the pipenv virtual environment:

    pipenv run ./manage.py help

Because that's a bit of a pain, solely to run `./manage.py`, we have a shortcut script you can run from your own computer (not within the Docker container):

    ./scripts/manage.sh help

So, to create your Django project's superuser:

    .scripts/manage.sh createsuperuser

### Run tests

We also have a script to show one way of running Django tests within the container:

    ./scripts/run-tests.sh

That will run the included shell script that, in turn, logs into the web container, and then runs Django's `./manage.py test` command within the pipenv virtual environment.

You could run a specific test by doing something like:

    ./scripts/run-tests.sh tests.myapp.test_urls.UrlsTestCase.test_home_url

### Making changes

If you change something in `docker-compose.yml` then you'll need to build
things again:

    docker-compose build

If you want to remove the containers and start again, then stop the containers, and:

    docker-compose rm

### Adding or updating python modules with pipenv

I *think* that the way to install new python modules, or update existing ones is to do so within the docker container, e.g.:

    docker exec -it myproject_web sh
    pipenv install django-debug-toolbar


## Get in touch

If you have suggestions for improving this (there are probably many ways to do so) then do let me know:

Phil Gyford  
https://www.gyford.com  
phil@gyford.com  
@philgyford on Twitter
