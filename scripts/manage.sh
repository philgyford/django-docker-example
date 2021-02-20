# Runs Django's manage.py command within the web container
# Passes any arguments

docker exec -it myproject_web pipenv run python manage.py "$@"