# Wolt backend assingment

## Run with docker

```
docker-compose up 
```

Then api runs at: http://localhost:8080/delivery_fee/

## Setup with python

Install requirements in /app folder:

```
python -m pip install -r requirements.txt
```

Run api in /app:

```
uvicorn main:app --reload
```

then app running at: http://127.0.0.1:8000/delivery_fee/

run tests in /app:

```
python -m pytest tests.py
```