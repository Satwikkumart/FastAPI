from fastapi import FastAPI

app = FastAPI()

@app.get('/').  #Endpoint -> where on the URL the below message must be displayed
def greet():
    return {"Hello and welceom to AI school"}