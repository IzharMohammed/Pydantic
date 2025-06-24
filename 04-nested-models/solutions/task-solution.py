from pydantic import BaseModel
from typing import List,Optional
from datetime import datetime

class Lesson(BaseModel):
    id: int
    title: str
    duration_minutes: float
    content: str
    is_free_preview: bool = False  # Default value
    created_at:datetime=datetime.now()

class Module(BaseModel):
    id:int
    title: str
    description: Optional[str] = None  # Optional field
    lessons:List[Lesson]
    order_in_course: int
    
class Course(BaseModel):
    id: int
    title: str
    instructor: str
    modules:List[Module] # List of Module objects
    price: float
    is_published: bool = False  # Default unpublished
    categories: List[str] = []  # Default empty list
    
    
# Create sample course structure
python_course=Course(
    id=101,
    title="Python mastery",
    instructor="Random",
    price=99.99,
    categories=["programming","python","agentic ai"],
    modules=[
        Module(
            id=1,
            order_in_course=1,
            title="Python Basics",
            description="python ....",
            lessons=[
                Lesson(
                    id=1,
                    title="Introduction to Python",
                    duration_minutes=30.5,
                    content="Python overview...",
                    is_free_preview=True
                ),
                Lesson(
                    id=2,
                    title="Variables and Data Types",
                    duration_minutes=45.0,
                    content="Understanding data types..."
                )
            ]
        ),
        Module(
            id=2,
            title="Advanced Python",
            order_in_course=2,
            lessons=[
                Lesson(
                    id=3,
                    title="Decorators",
                    duration_minutes=60.0,
                    content="Deep dive into decorators..."
                )
            ]
        )
    ]
)