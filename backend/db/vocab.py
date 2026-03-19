from typing import NamedTuple

class SchoolEntity(NamedTuple):
    id : int
    name : str
    country : str
    state : str
    city : str
    zip_code : str
    address : str
    grade_level : str