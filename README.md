# Social Media Lists
---
Manage social media posts from different platforms with ease.
It has been built using the following technologies:

- **Django** for building the REST API backend
- **PostgreSQL** as the storage 
- **NGINX** as reverse proxy
- **Docker & docker-compose** on the infrastructure for communication between all services

### Database Structure

![](https://i.imgur.com/MdhVyIr.png)

### Prerequisites

- Docker >= 20.10.11
- docker-compose >= 1.29.2

### Installation
- Clone the repository and `cd` into it 

```
$ git clone https://github.com/cr1g/social-media-lists.git
$ cd social-media-lists
```

- Create an `.env` file in the same folder as `docker-compose.yml` and set the according environment variables:
```
API_HOST=                           # name of the api service in docker-compose.yml
API_PORT=
ACCESS_TOKEN_TTL_MINUTES=
CORS_ORIGIN_WHITELIST=              # a list of hosts separated by commas
ENABLE_DEBUG_TOOLBAR=               # populate the field with any characters to enable it
ENVIRONMENT=                        # dev/prod
POSTGRES_DB=                        
POSTGRES_HOST=                      # name of the postgres service in docker-compose.yml
POSTGRES_PASSWORD=
POSTGRES_USER=
REFRESH_TOKEN_TTL_MINUTES=
REVERSE_PROXY_PORT=
SECRET_KEY=
```

In case you need a valid `.env` file: https://pastebin.com/1QT1daub.
For the next steps, the above `.env` has been used.

- Start the application using docker-compose

```
$ docker-compose up --build -d
```

- Enter the `api` container and create a superuser to use the APIs

```
$ docker-compose exec api bash
$ python manage.py createsuperuser
$ exit
``` 

The next endpoints are available now:
- **REST API** - `http://localhost/api` 
- **API Documentation** - `http://localhost/api/docs`
- **Django Admin-UI** - `http://localhost/admin`

**NOTE:** In the API Documentation you can find the endpoints for JWT Authentication and get an access token to gain access to all the other endpoints.
**NOTE:** Given more time, a lot of things could've been improved. We're talking here about more docker-compose configurations for local environments, better security at nginx level and better documentation.
