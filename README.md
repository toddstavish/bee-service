# Building Extraction Evaluation (BEE) Service

A RESTful web service to perform polygon comparison for building extraction evaluation (Polis). The service is implemented with the [Django](https://www.djangoproject.com/) framework and deployed in the [Azure Container Service ](https://azure.microsoft.com/en-us/services/container-service/). This repository has been tested to continuously deploy to Azure from GitHub. The container is stateless and lightweight.

## Development steps
1. git clone https://github.com/toddstavish/bee-service.git
2. cd bee-service
3. Python code dev just run gunicorn locally (avoid container rebuilds)
* gunicorn -b :8000 --timeout 120 django_rest.wsgi
4. docker build -t bee .
5. docker run -it -p 8000:8000 bee

## Deployment steps
1. Deploy container to Azure
* [Deploy a single instance via docker-machine](https://docs.docker.com/machine/drivers/azure/)
* [Deploy an Azure Container Service cluster](https://azure.microsoft.com/en-us/documentation/articles/container-service-deployment/)
2. eval $(docker-machine env <machine name>) <-machine name is from first step
3. Allow external network access to your VM (firewall in your resource group)

## To Do
1. Create JSON on request
2. Add IoU evaluation

## Security\Performance concerns pre-deployment
1. Turn off debug
2. Define allowable hosts
3. Remove csrf_exempt
4. Define DEFAULT_PERMISSION_CLASSES
5. Remove prints from python code base

## License
See [LICENSE](./LICENSE).
