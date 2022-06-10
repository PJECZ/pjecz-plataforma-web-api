"""
FastAPI pagination for DataTables

Usa la paginacion combinada con SQLAlchemy para entregar una respuesta compatible con DataTables, por ejmplo...

    {
    "data": [
        { ... },
        { ... },
        ...
    ],
    "recordsTotal": 0000,
    "start": 1,
    "length": 50,
    "recordsFiltered": 0000
    }

"""
from typing import TypeVar, Generic, Sequence

from fastapi import Query
from fastapi_pagination.bases import AbstractParams
from fastapi_pagination.limit_offset import (
    LimitOffsetPage as BaseLimitOffsetPage,
    LimitOffsetParams as BaseLimitOffsetParams,
)

T = TypeVar("T")


class Params(BaseLimitOffsetParams):
    """LimitOffsetParams"""

    draw: int = 1
    start: int = Query(1, ge=1, description="Page offset")
    length: int = Query(50, ge=1, le=100, description="Page size limit")


class LimitOffsetPage(BaseLimitOffsetPage[T], Generic[T]):
    """LimitOffsetPage"""

    __params_type__ = Params
    data: Sequence[T]
    draw: int
    recordsTotal: int
    recordsFiltered: int
    start: int
    length: int

    class Config:
        """Config"""

        allow_population_by_field_name = True
        fields = {
            "items": {"alias": "data"},
            "total": {"alias": "recordsTotal"},
            "limit": {"alias": "start"},
            "offset": {"alias": "length"},
        }

    @classmethod
    def create(
        cls,
        items: Sequence[T],
        total: int,
        params: AbstractParams,
    ) -> BaseLimitOffsetPage[T]:
        """Create"""
        return cls(
            data=items,
            draw=params.draw,
            length=params.length,
            start=params.start,
            recordsTotal=total,
            recordsFiltered=total,
        )
