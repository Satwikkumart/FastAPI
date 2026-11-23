from fastapi import FastAPI
import json

app = FastAPI()



"""
HTTP Method:
1. GET -> to just show or display any message on the website or the page 
or the application"""

@app.get('/')  #Endpoint -> where on the URL the below message must be displayed
def greet():
    return {"Hello and welceom to AI school"}


@app.get('/hello')
def hello():
    return {"THis is Hello Page"}

#Helper function
def load_data():
    with open("students.json", "r") as file:
        return json.load(file)


@app.get('/student')
def student():
    return load_data()