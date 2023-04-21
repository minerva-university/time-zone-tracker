# Welcome to the barebones barely working version of our project: 


Get stuff runnning with this:
```
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
python3 app.py
```

# Bash instructions to run Dockerfile

```
docker build -t time-zone-tracker .
docker run -p 80:80 time-zone-tracker
```

# Instructions to run the unit tests

```
pytest -v test_frontend.py 
```


```
time-zone-tracker
├─ Dockerfile
├─ README.md
├─ app.py
├─ requirements.txt
├─ static
│  ├─ home_style.css
│  ├─ overlaps_style.css
│  └─ settings_style.css
├─ templates
│  ├─ base.html
│  ├─ home.html
│  ├─ overlaps.html
│  ├─ settings.html
│  └─ users.html
└─ test_frontend.py

```