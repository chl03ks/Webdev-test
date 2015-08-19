# Webdev-test
a application that interacts with the Twitter and Wikipedia API

# Instalation

1. Clone the repository
```sh
$ git clone git@github.com:gvsdan/Webdev-test.git
```
2. Go to the main folder then create a virtual env to isntall the requirements.txt
```sh
$ (youvirtualenv) pip install -r  requirements.txt
```
3. install the front end dependencies with bower
```sh
$ (youvirtualenv) bower install
```
4. then run the migrations 
```sh
$ (youvirtualenv) python manage.py migrate
```
5.then create a super user(optional)
```sh
$ (youvirtualenv) python manage.py createsuperuser
```
6. then run the server and go to the url
```sh
$ (youvirtualenv) python manage.py runserver
```
7. Open the browser and got o localhost:8000 you should see something like this
    ![Alt text](https://scontent-atl1-1.xx.fbcdn.net/hphotos-xfp1/v/t1.0-9/11870641_390350454469003_4700183762254305022_n.jpg?oh=d10ec6d0375213c077265f6c024f03f6&oe=563E29FC)

