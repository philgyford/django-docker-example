# Django and Docker example

This is my example Django setup using Docker for local development.

It's taken me a while to piece the Docker stuff together and I'm definitely not
confident that it's ideal. But, so far, it seems to work.


## Start it

1. Install Docker, e.g. [Docker for Mac](https://docs.docker.com/docker-for-mac/install/).

2. Download this repository.

3. Create a `.env` file within your copy that contains these lines:

    ```
    # Environment settings for local development.

    ALLOWED_HOSTS=*

    DATABASE_URL=postgres://postgres@db:5432/postgres

    DJANGO_SECRET_KEY=ChangeThisForALiveSite

    DJANGO_SETTINGS_MODULE=config.settings.local
    ```

4. On the command line, within this directory, do this to build the image and
   start the container:

        docker-compose up

5. Open http://0.0.0.0:8000 in your browser.

That might work...?


## More explanation

`Dockerfile` describes an image, which will be our web server.

It keeps this directory synced with the `/app/` directory in our web container.

It installs [Pipenv](https://pipenv.readthedocs.io/en/latest/) and then our
project's python requirements from the `Pipfile`.

`docker-compose.yml` describes the two services: the web and postgres servers.
It loads the environment variables we set in the `.env` file.

The web server will run the Django `migrate` command and then `runserver`.

The very small example Django project is in `myproject/`, with its settings and
URL conf in `config/`.


## Run tests

You can run the Django tests within the running web container by doing this:

    docker-compose exec web ./scripts/run-tests.sh

That will run the included shell script that, in turn, runs Django's
`manage.py test` command, and runs `coverage`, generating a report in the,
command line output, and in the `htmlcov/` directory it will create.


## Other commands

Run other Django management commands, e.g.:

    docker-compose exec web ./manage.py createsuperuser

Or get a bash prompt within the web container:

    docker-compose exec web bash

Stop it all running:

    docker-compose down

If you change something in `docker-compose.yml` then you'll need to build
things again:

    docker-compose build

Or, just for the `web` container:

    docker-compose build web


## Keeping Docker tidy

It seems easy to end up with loads of unused images, containers and volumes,
all taking up disk space.

### Images

List all images:

    docker images -a

Delete image(s):

    docker rmi IMAGE_ID IMAGE_ID

## Containers

List running containers:

    docker ps

List containers that aren't running:

    docker ps -a -f status=exited

Delete container(s):

    docker rm CONTAINER_ID CONTAINER_ID

## Volumes

List volumes:

    docker volume ls

Delete volume(s):

    docker volume rm VOLUME_NAME VOLUME_NAME

List volumes not connected to any containers:

    docker volume ls -f dangling=true

Delete those unconnected volumes:

    docker volume prune
