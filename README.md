# BigDataFed_Test
# Requirements:
```
Python 3.6
Flask 1.1.1
```

# Installation:
### Docker:
> build a docker image
```
docker build -t <imageName:version> .
```
> run a docker container
```
docker run -d <app_name>
```
> Browse to 
```
http://localhost:8080
```

### Local:

> Create a virtual environment inside the application:
```
virtualenv -p /usr/bin/python3 venv    
source venv/bin/activate
```

> Install Python modules
```
pip3 install -r requirements.txt 
```

> Run the application
```
python app.py
```

> Browse to 
```
http://localhost:8080
```

# Additional Info
1. For parsing xlsx files, insert them to **xlsx** folder
2. Run *xlsx_parser.py* inside **xlsx_parser** folder
3. Your data is available in data.json file

> FlaskApp checks for *data.json* file on startup, 
> if file is missing it generates one automatically

