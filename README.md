# Building Extraction Evaluation (Bee) Service

A RESTful web service to perform polygon comparison for building extraction evaluation (Polis). The service is implemented with the [Django](https://www.djangoproject.com/) framework and deployed in an [Azure App Service Web App](http://azure.microsoft.com/en/marketplace/partners/PTVS/Django). This repository has been tested to continuously deploy to Azure from GitHub.

## Deployment steps
1. Create virtual environment: python -m virtualenv env
2. Install external packages: ./env/bin/pip install -r requirements.txt
3. Install other packages: e.g. ./env/bin/pip install azure
4. Create a superuser: ./env/bin/python manage.py createsuperuser
5. Run server locally: ./env/bin/python manage.py runserver
6. Update dependencies: ./env/bin/pip freeze > requirements.txt
7. Git push to GitHub deploys code to Azure

1. git clone https://github.com/toddstavish/bee-service.git
2. cd bee-service
3. Allow external network access to your VM
4. gunicorn -b 0.0.0.0:8000 [--workers=5] django_rest.wsgi

## To Do
1. Create JSON on request
2. Add IoU evaluation

## Django Security concerns pre-deployment
1. Turn off debug
2. Define allowable hosts
3. Remove csrf_exempt
4. Define DEFAULT_PERMISSION_CLASSES

## License
See [LICENSE](./LICENSE).
