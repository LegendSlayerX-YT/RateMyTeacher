from typing import NamedTuple, Optional
from dataclasses import dataclass

@dataclass
class SchoolEntity:
    id : int
    name : str
    country : str
    state : str
    city : str
    zip_code : str
    address : str
    grade_level : str

@dataclass
class SchoolQueryCondition:
    id: Optional[int]
    name : Optional[str]
    country : Optional[str]
    state : Optional[str]
    city : Optional[str]
    zip_code : Optional[str]
    address : Optional[str]
    grade_level : Optional[str]

@dataclass
class TeacherEntity:
    id: int
    school_id: int
    name: str
    email: str

@dataclass
class TeacherQueryCondition:
    id: Optional[int]
    school_id: Optional[int]
    name: Optional[str]
    email: Optional[str]