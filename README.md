# WISET
What I Should Eat Today.<br/>
Site that generate to buy list of products
## Getting started

Create virtual environment and activate it
```
python3 -m venv venv && source venv/bin/activate
```
Install dependencies
```
pip install -r requirements.txt
```
Apply migrations
```
python manage.py migrate
```
Create an admin account
```
python manage.py createsuperuser
```
Run app
```
python manage.py runserver
```