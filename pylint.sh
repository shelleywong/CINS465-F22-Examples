python -V
#Change paths to your project/app folders
pylint --load-plugins pylint_django --disable=missing-docstring --disable=django-not-configured --ignore=migrations ./mysite/mysite
pylint --load-plugins pylint_django --disable=missing-docstring --disable=django-not-configured --ignore=migrations ./mysite/myapp
