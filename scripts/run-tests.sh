#!/bin/bash
set -e

# You can optionally pass in a test, or test module or class, as an argument.
# e.g.
# ./run_tests.sh tests.myapp.test_urls.UrlsTestCase.test_home_url
TESTS_TO_RUN=${1:tests}

coverage run --branch --source=. --omit=*/migrations/*.py,manage.py,tests/*.py manage.py test --settings=config.settings.tests $TESTS_TO_RUN
coverage report
coverage html
