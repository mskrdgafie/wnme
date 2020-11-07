# WNME :ethiopia:

WNME is a system which helps customers find workers near them easly. This repo is backend part which is implemented using django RESTfull API.
### Teams:
@Misiker
@Yohannes
@Abrham
@Ruhama
### Features progress to achive it's goal:
> * :goal_net::heavy_minus_sign::heavy_minus_sign::heavy_minus_sign::soccer::heavy_minus_sign::heavy_minus_sign::heavy_minus_sign::heavy_minus_sign::heavy_minus_sign::running_man:booking
> * :goal_net::heavy_minus_sign::heavy_minus_sign::heavy_minus_sign::heavy_minus_sign::heavy_minus_sign::heavy_minus_sign::heavy_minus_sign::soccer::heavy_minus_sign::running_man:payment
> * :goal_net::soccer::heavy_minus_sign::heavy_minus_sign::heavy_minus_sign::heavy_minus_sign::heavy_minus_sign::heavy_minus_sign::heavy_minus_sign::heavy_minus_sign::running_man:chat
> * :goal_net::soccer::heavy_minus_sign::heavy_minus_sign::heavy_minus_sign::heavy_minus_sign::heavy_minus_sign::heavy_minus_sign::heavy_minus_sign::heavy_minus_sign::running_man:rating
> * :goal_net::heavy_minus_sign::soccer::heavy_minus_sign::heavy_minus_sign::heavy_minus_sign::heavy_minus_sign::heavy_minus_sign::heavy_minus_sign::heavy_minus_sign::running_man: account managment
### you can preview wnme <a href="https://wnme.herokuapp.com/">here</a>

Path                  | Description
----------------------|--------------------------------
api/v2/account        | used for login and signup
api/v2/booking        | used for all booking
api/v2/rating         | used for rating
api/v2/chat           | used to chat
api/v2/payment        | used for online payment

## Technologies used in this system are :
* react for web frontend which is found <a href="https://github.com/mskrdgafie/wnme_front_end">here</a>
* django for backend :sparkles:
* flutter for mobile frontend which is found <a href="">here</a>
* postgresql with PostGIS extension
## Web services
* sendinblue to send email confirmation
* yenepay
* googel map
* facebook social authentication
* google social authentication

To run the backend, run:
``` python
virtualenv env
source env/bin/activate
pip install -r requirements.txt
python manage.py runserver
```
   

To run the web frontend:
``` javascript 
npm i
npm start
```

:+1:


https://wnme.herokuapp.com/ | https://git.heroku.com/wnme.git