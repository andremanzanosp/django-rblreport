# django-rblreport
Intend to monitor many ips in many RBLs and get online report.
For now it is checking an ip against many rbls.


## Dependencies:

* [Python 3.9](https://www.python.org/downloads/)
* [pip](https://pip.pypa.io/en/stable/installing/)
```
pip3 install -r requirements.txt
```


## Creating envinronment 

Create Python Virtual environment
```
python3 -m venv /path/app/venv
source /path/app/venv/bin/activate
```

Install requirements
```
pip install --upgrade pip
pip install -r requirements.txt
```

Create database
```
python3 manage.py migrate
```
Load initial data
```
python3 manage.py loaddata initial_data
```

* A superuser will be created with the loaddata (admin/admin)



## Usage 


### Management command

You can run on a terminal
```
python3 manage.py ipsearch --ips 127.0.0.2 192.168.0.1 --rbls zen.spamhaus.org
```


### API

Start server
```
python3 manage.py runserver
```
or
```
gunicorn --bind 0.0.0.0:8000 django_rblreport.wsgi:application -w 2 --log-level debug
```

Interact with ips
<http://127.0.0.1:8000/ips/>

Interact with rbls
<http://127.0.0.1:8000/rbls/>

or admin
<http://127.0.0.1:8000/admin/>


### OLD
Check ip on any rbl on database
<http://127.0.0.1:8000/iplookup/127.0.0.2/blacklist/all>


or check ip specifying rbl
<http://127.0.0.1:8000/iplookup/127.0.0.2/blacklist/zen.spamhaus.org>



---