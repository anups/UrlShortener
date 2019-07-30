

Prerequisite :- 

python 3.5
Django 2.1

uses :- 

python manage.py makemigrations urlapp
python manage.py migrate

python manage.py runserver

Hit the url:-
http://localhost:8000/urlapp

Enter the url with http://prefix

Click on the submit button
you will get shorter url like sht.bit/bc3f7f53
Note:- I have fixed (hardcoded) the text "sht.bit" for shrter domain name.

e.g. Original URl:- https://www.w3schools.com/cssref/css3_pr_animation-timing-function.asp
Shorter URL :- sht.bit/4ba40854

Currently I have fixed the expiry time of url as 60 sec.
To see the effect, please click the submit button continuously 
and see the effect till 1 minute. 
As 1 minute completed, url will get inactivated / disabled state