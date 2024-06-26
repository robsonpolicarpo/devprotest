# dev.pro qa challenge


1. You can use virtualenv or other python env manager
```commandline
virtualenv -p python3 venv
source venv/bin/activate
```

2. Install dependencies:
```commandline
pip3 install -r requirements.txt
```


### Run:

Run all tests with the command above:
```commandline
python3 -m pytest --html=reports/html/report.html
```


### Report

You can check a html report generated in '/reports'