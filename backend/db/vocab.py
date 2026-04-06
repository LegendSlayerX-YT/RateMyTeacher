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