#!/bin/bash
set -e

# Call this from the host machine to run tests in Docker.

# You can optionally pass in a test, or test module or class, as an argument.
# e.g.
# ./run_tests.sh tests.myapp.test_urls.UrlsTestCase.test_home_url
TESTS_TO_RUN=${1:tests}

docker exec myproject_web /bin/sh -c "pipenv run ./manage.py test --settings=myproject.myproject.settings.tests $TESTS_TO_RUN"

# You could add further commands on to the end of that command, eg:
# docker exec myproject_web /bin/sh -c "pipenv run ./manage.py test --settings=myproject.settings.tests $TESTS_TO_RUN ; pipenv run flake8"