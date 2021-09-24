# API Customer Django REST
<h3 align="left">Languages and Tools:</h3>
<p align="left"> 
<a href="https://www.gnu.org/software/bash/" target="_blank"> <img src="https://www.vectorlogo.zone/logos/gnu_bash/gnu_bash-icon.svg" alt="bash" width="40" height="40"/>bash </a> /
<a href="https://www.linux.org/" target="_blank"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/linux/linux-original.svg" alt="linux" width="40" height="40"/>linux </a> /
<a href="https://www.python.org" target="_blank"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" alt="python" width="40" height="40"/>python </a> /
<a href="https://www.docker.com/" target="_blank"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/docker/docker-original-wordmark.svg" alt="docker" width="40" height="40"/> </a> /
<a href="https://www.djangoproject.com/" target="_blank"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/django/django-original.svg" alt="django" width="40" height="40"/> </a> /
<a href="https://www.django-rest-framework.org/" target="_blank"> Django REST Framework </a> /
<a href="https://www.postgresql.org/" target="_blank"> Postgree </a>.

</p>

Used versions:<br>
Python 3.8.10 (local - Ubuntu 20.04.2 LTS) <br> 
Django 3.2.6 - Docker-compose 1.21.2.


Consuming API: http://127.0.0.1:8000/
API: http://127.0.0.1:8000/api/v1/

Endpoints:
* list http://127.0.0.1:8000/api/v1/foods   //Listagem das lojas e  Visualização de uma loja específica <br> 
* http://127.0.0.1:8000/create/      //Criação de uma nova loja <br> 
* http://127.0.0.1:8000/update/<int:pk>/    //Atualização dos dados de uma loja <br> 
* http://127.0.0.1:8000/delete/<int:pk>     // Remoção de uma loja <br> 


## Setup

The first thing to do is to clone the repository:

```sh
$ git clone https://github.com/fersoftware/fastfood_indico_api.git
$ cd fastfood_indico_api
```

Create a virtual environment to install dependencies in and activate it:

```sh
$ python3 -m venv venv
$ source env/bin/activate
```
If an error occurs when running, try the command below:
```sh
(venv)$ sudo apt-get install python3-venv
```

Note the `(venv)` in front of the prompt. This indicates that this terminal
session operates in a virtual environment set up by `python3-venv`.

Running Django using Docker-Compose
```sh
(venv)$ sudo docker-compose up -d --build
```
`

Create user admin
```sh
(venv)$ sudo docker-compose exec web python manage.py createsuperuser
```

Migrate
```sh
(venv)$ sudo docker-compose exec web python manage.py migrate
```


Makemigrations
```sh
(venv)$ sudo docker-compose exec web python manage.py makemigrations
```

---

### Installing dependencies without the docker

```sh
(venv)$ pip install -r requirements.txt
```

Once `pip` has finished downloading the dependencies:
```sh
(env)$ cd fastfood_indico_api
(env)$ python manage.py runserver
```
And navigate to `http://0.0.0.0:8000/`.

## Persisting data in Postgree databases

- This script import data from the [Fast_Food_Restaurants_US.csv](https://github.com/fersoftware/fastfood_indico_api/blob/main/Fast_Food_Restaurants_US.csv) file into SQLite.

```sh
(env)$  python importCSVtoPostgre.py -f Fast_Food_Restaurants_US.csv -t fast-food
```
 

