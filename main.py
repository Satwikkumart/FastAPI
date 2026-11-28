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


"""
PATH - PARARMETER
student_id -> this is our Path Parameter
"""
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

"""
QUERY - PARAMTER
filter -> This is our Query Parameter
"""

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


SORT_FIELDS = ["marks", "age", "name"]
SORT_ORDER = ["asc", "desc"]

@app.get('/sort')
def sort_students(
    sort_by : str = Query(None, description="Sort by marks, age, name", examples=["marks"]),
    order : str = Query("asc", description="asc or desc", examples=["asc", "desc"])
):
    #If the given sort_by input doesn't belongto  (marks, age, name) we will raise an error
    if sort_by not in SORT_FIELDS:
        raise HTTPException(
            status_code=404,
            detail=f"Invalid sort_by '{sort_by}', choose from {SORT_FIELDS}"
        )

    #If the given order input doesn't give to any (asc, desc) we will raise an error
    if order not in SORT_ORDER:
        raise HTTPException(
            status_code=404,
            detail=f"Invalid order '{order}', chosse from {SORT_ORDER}"
        )

    data = load_data()

    #step-1 Turn the dictionary into a list, putting the ID inside each student
    student = []
    for student_id, info in data.items():
        info["id"] = student_id
        student.append(info)

    #step-2 Sort the list by the choosen field
    reverse = (order=="desc")
    sorted_students = sorted(student, key=lambda s:s[sort_by],reverse=reverse)

    return sorted_students


"""
PAGINATION
http://127.0.0.1:8000/paginate?page=1&limit2

page -> which page you want
limit -> how many students(records) on one page

Formula:
start: (page - 1) * limit
end : start + limit
"""
@app.get('/pagination')
def paginate_student(page:int, limit:int):
    data =load_data()

    #step-1 Turn the dictionary into a list, putting the ID inside each student
    student = []
    for student_id, info in data.items():
        info["id"] = student_id
        student.append(info)

    start = (page-1) * limit
    end = start + limit

    page_student = student[start : end] 

    total_students = len(student)

    return {
        "page": page,
        "limit": limit,
        "total_students": total_students,
        "students": page_student 
    }