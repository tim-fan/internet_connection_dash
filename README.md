# internet_connection_dash

Dashboard for monitoring internet connectivity, as monitored by [internet_connection_monitor](https://github.com/tim-fan/internet_connection_monitor) and recorder by [internet_connection_datalogging](https://github.com/tim-fan/internet_connection_datalogging).

This package was bootstrapped by [cookiecutter-dash](https://chrisvoncsefalvay.com/2019/09/11/cookiecutter-dash/), hence there are a few components initialised but unused (the dockerfile, makefile, assets/components/data subdirectories, etc).


## Running locally

To run a development instance locally, create a virtualenv, install the 
requirements from `requirements.txt` and launch `app.py` using the 
Python executable from the virtualenv.

## Deploying on ECS

Use `make image` to create a Docker image. Then, follow [these 
instructions](https://www.chrisvoncsefalvay.com/2019/08/28/deploying-dash-on-amazon-ecs/) 
to deploy the image on ECS.