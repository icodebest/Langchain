from pydantic import BaseModel, EmailStr, Field
from typing import Optional

class Student(BaseModel):
    name: str= 'Waleed'
    age:Optional[int] = None
    email: EmailStr
    cgpa: float=Field(default=0.0, gt=0.0, le=4.0, description="CGPA must be between 0 and 4")

new_student={'age':20, 'email':'abc@gmail.com', 'cgpa':3.45}

student = Student(**new_student)

print(student)