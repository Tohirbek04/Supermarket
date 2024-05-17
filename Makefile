mig:
	python3 manage.py makemigrations
	python3 manage.py migrate


superuser:
	python manage.py createsuperuser
