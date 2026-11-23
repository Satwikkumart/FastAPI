data = {
    "S001": {
        "name": "Aarav Sharma",
        "age": 20,
        "email": "aarav.sharma@example.com",
        "course": "Python",
        "marks": 92
    },

    "S002": {
        "name": "Diya Patel",
        "age": 21,
        "email": "diya.patel@example.com",
        "course": "Data Science",
        "marks": 85

    },

    "S003": {
        "name": "Pankaj Patel",
        "age": 20,
        "email": "pankaj.patel@example.com",
        "course": "Data Engineer",
        "marks": 89
    },

    "S004": {
        "name": "Rohith Sharma",
        "age": 20,
        "email": "rohit.sharma@example.com",
        "course": "Machine Learning",
        "marks": 90
    },

    "S005": {
        "name": "Virat Kohli",
        "age": 21,
        "email": "virat.kohli@example.com",
        "course": "Data Science",
        "marks": 98
    }
}

# id = input("Enter id you want (ex: S001): ") #S001

# print(data[id])

# print(data["S005"]["course"])

for student_id, info in data.items():
    if info["course"] == "Data Science":
        print(info)