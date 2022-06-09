"""
DataTable schema
"""
from typing import List, Optional
from pydantic import BaseModel


class DataTableBase(BaseModel):
    """DataTableBase"""

    draw: int


class DataTableRequest(DataTableBase):
    """DataTableRequest"""

    start: int = 0
    length: int = 10


class DataTableResponse(DataTableBase):
    """DataTableResponse"""

    iTotalRecords: int
    iTotalDisplayRecords: int
    # aaData: List[Part] = []
    error: Optional[str] = None
