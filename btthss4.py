from fastapi import FastAPI
app = FastAPI()

courses = [
    {
        "id": 1,
        "name": "Python Basic",
        "category": "backend",
        "price": 3000000,
        "mode": "online"
    },
    {
        "id": 2,
        "name": "Java Web",
        "category": "backend",
        "price": 5000000,
        "mode": "offline"
    },
    {
        "id": 3,
        "name": "Web Frontend",
        "category": "frontend",
        "price": 4000000,
        "mode": "online"
    }
]

@app.get("/courses")
def show_all_couses():
    return courses

@app.get("/courses/search")
def search_the_course(
    mode:str = "",
    category: str = ""
):
    result=[]
    if not mode and not category:
        result = courses
    elif mode and category:
        for course in courses:
            if course ["mode"] == mode and course["category"] == category:
                result.append(course)
    elif mode:
        for course in courses:
            if course["mode"]== mode:
                result.append(course)
    elif category:
        for course in courses:
            if course["category"] == category:
                result.append(course)
    if len(result)==0:
        return{
            "detail":"khong co khoa hoc phu hop"
        }
    return{
        "danh sach khoa hoc":result
    }
@app.get("/courses/{course_id}")
def get_course(course_id: int):
    for course in courses:
        if course["id"]== course_id:
            return{
                "mon hoc chi tiet": course
            }
        
    return {
        "detail":"khong tim thay khoa hoc"
    }