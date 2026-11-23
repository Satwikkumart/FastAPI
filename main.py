from fastapi import FastAPI, HTTPException, Path, Query
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


#student_id -> this is our Path Parameter
@app.get("/student/{student_id}")
def get_id(student_id : str = Path(...,description="The Id of the student",
            examples=['S001'])):
    data = load_data()
    if student_id not in data:
        raise HTTPException(
            status_code=404,
            detail=f"Student with ID '{student_id}' not found"
        )

    return data[student_id]


@app.get('/filter')
def filter_student(course : str = Query(None, 
                                        description="Show only stundets in this course", examples=["python"])):
    data = load_data()

    if course is None:
        return data

    filtered = {}
    for student_id, info in data.items():
        if info["course"].lower() == course.lower():
            filtered[student_id] = info

    return filtered
