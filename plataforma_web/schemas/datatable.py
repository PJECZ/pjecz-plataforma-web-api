"""
DataTable schema
"""
from typing import List, Optional
from pydantic import BaseModel


class DataTableBase(BaseModel):
    """DataTableBase"""

    draw: int = 1


class DataTableRequest(DataTableBase):
    """DataTableRequest"""

    start: int = 0
    length: int = 10


class DataTableResponse(DataTableBase):
    """DataTableResponse"""

    recordsTotal: int
    recordsFiltered: int
    # data: List[Part] = []
    error: Optional[str] = None
