rm detectme/default.db
python manage.py syncdb <<< "no"
python manage.py migrate
python manage.py check_permissions
python manage.py createsuperuser

