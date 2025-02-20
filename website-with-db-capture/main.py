from fastapi import FastAPI, Depends
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session
from typing import List

DATABASE_URL = "sqlite:///course_website.db"  # Use SQLite for simplicity

import os

app = FastAPI()

# Get absolute path to the site directory
site_dir = os.path.join(os.path.dirname(__file__), "site")
print(f"Site directory path: {site_dir}")
print(f"Directory exists: {os.path.exists(site_dir)}")
print(f"Script exists: {os.path.exists(os.path.join(site_dir, 'script.js'))}")

# Mount static files at /static
app.mount("/static", StaticFiles(directory=site_dir), name="site")

# Serve index.html at root
@app.get("/")
async def read_index():
    return FileResponse(os.path.join(site_dir, "index.html"))

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

class Course(Base):
    __tablename__ = "courses"

    course_id = Column(Integer, primary_key=True, autoincrement=True)
    course_title = Column(String, nullable=False)
    lectures = relationship("Lecture", back_populates="course")


class Lecture(Base):
    __tablename__ = "lectures"

    lecture_id = Column(Integer, primary_key=True, autoincrement=True)
    course_id = Column(Integer, ForeignKey("courses.course_id"), nullable=False)
    lecture_no = Column(Integer)
    lecture_title = Column(String, nullable=False)
    lecture_description = Column(String)
    course = relationship("Course", back_populates="lectures")


Base.metadata.create_all(bind=engine)


# Dependency to get database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# API endpoints
@app.get("/courses/", response_model=List[dict])
async def read_courses(db: Session = Depends(get_db)):
    courses = db.query(Course).all()
    return [{"course_id": course.course_id, "course_title": course.course_title} for course in courses]


@app.get("/lectures/", response_model=List[dict])
async def read_lectures(db: Session = Depends(get_db)):
    lectures = db.query(Lecture).all()
    return [{
        "lecture_id": lecture.lecture_id,
        "course_id": lecture.course_id,
        "lecture_no": lecture.lecture_no,
        "lecture_title": lecture.lecture_title,
        "lecture_description": lecture.lecture_description
    } for lecture in lectures]


@app.get("/courses/{course_id}/lectures/", response_model=List[dict])
async def read_course_lectures(course_id: int, db: Session = Depends(get_db)):
    lectures = db.query(Lecture).filter(Lecture.course_id == course_id).all()
    return [{
        "lecture_id": lecture.lecture_id,
        "course_id": lecture.course_id,
        "lecture_no": lecture.lecture_no,
        "lecture_title": lecture.lecture_title,
        "lecture_description": lecture.lecture_description
    } for lecture in lectures]
