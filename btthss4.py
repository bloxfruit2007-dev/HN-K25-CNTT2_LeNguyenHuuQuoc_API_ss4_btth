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
    result = []
    if not mode and not category:
        result =  courses
    if mode and category:
        result =  [course for course in courses if course["category"] == category and course["mode"] == mode]
    if mode:
        result =  [course for course in courses if course["mode"] == mode]
    if category:
        result =  [course for course in courses if course["category"] == category]
    
    if not result:
        return {
            "detail": "Không có khóa học phù hợp"
        }
    return {
        "Danh sách khóa học": result
    }

@app.get("/courses/{course_id}")
def get_student(course_id:int):
    if not any(course["id"] == course_id for course in courses):
        return {
            "detail": "Không tìm thấy khóa học"
        }
    return {
        "Môn hoch chi tiết":courses[course_id]
    }