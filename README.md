# django-rblreport
Intend to monitor many ips in many RBLs and get online report.
For now it is checking a ip against many rbls.


## Dependencies:

* [Python 3](https://www.python.org/downloads/)
* [pip](https://pip.pypa.io/en/stable/installing/)
```
pip3 install -r requirements.txt
```


## Creating envinronment 

Create database
```
$ python manage.py migrate
```
Load initial data
```
$ python3 manage.py loaddata initial_data
```

Create superuser
```
$ python3 manage.py createsuperuser
```


## Usage 

You can run a management command
```
$ python3 manage.py ipsearch 127.0.0.2
```

or access in a browser running the server
```
python3 manage.py runserver
```

Check ip on any rbl on database
```
[http://127.0.0.1:8000/iplookup/127.0.0.2/blacklist/all](http://127.0.0.1:8000/iplookup/127.0.0.2/blacklist/all)
```
or check ip specifying rbl
```
[http://127.0.0.1:8000/iplookup/127.0.0.2/blacklist/zen.spamhaus.org](http://127.0.0.1:8000/iplookup/127.0.0.2/blacklist/zen.spamhaus.org)
```

or admin it
```
[http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)
```

---