# Building Extraction Evaluation (BEE) Service

A RESTful web service to perform polygon comparison for building extraction evaluation (Polis). The service is implemented with the [Django](https://www.djangoproject.com/) framework and deployed in an [Azure App Service Web App](http://azure.microsoft.com/en/marketplace/partners/PTVS/Django). This repository has been tested to continuously deploy to Azure from GitHub.


## Development steps
### Local
1. git clone https://github.com/toddstavish/bee-service.git
2. cd bee-service
3. docker build -t bee .
4. docker run -it -p 8000:8000 bee
generalized VM - no state
### Remote

## Deployment steps
1. [Deploy an Azure Container Service cluster](https://azure.microsoft.com/en-us/documentation/articles/container-service-deployment/)
2. cd bee-service
3. Allow external network access to your VM
4. gunicorn -b 0.0.0.0:8000 django_rest.wsgi [--workers=5]
generalized VM - no state

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
