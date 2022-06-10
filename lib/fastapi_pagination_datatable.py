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
from fastapi_pagination.bases import AbstractParams, RawParams
from fastapi_pagination.limit_offset import (
    LimitOffsetPage as BaseLimitOffsetPage,
    LimitOffsetParams as BaseLimitOffsetParams,
)

T = TypeVar("T")


class Params(BaseLimitOffsetParams, AbstractParams):
    """
    Params transforma los parametros de DataTable para el paginador

    - El paginador requiere limit y offset
    - DataTables entrega start (que comienza en cero) y length
    """

    draw: int = 1
    start: int = Query(0, ge=0, description="Page offset")
    length: int = Query(50, ge=1, le=100, description="Page size limit")

    def to_raw_params(self) -> RawParams:
        """Definir limit y offset a partir de start y length"""
        return RawParams(
            limit=self.length,
            offset=self.start + 1,
        )


class LimitOffsetPage(BaseLimitOffsetPage[T], Generic[T]):
    """LimitOffsetPage"""

    __params_type__ = Params
    data: Sequence[T]
    draw: int
    recordsTotal: int
    recordsFiltered: int
    start: int
    length: int
    limit: int
    offset: int

    class Config:
        """Config"""

        allow_population_by_field_name = True
        fields = {
            "items": {"alias": "data"},
            "total": {"alias": "recordsTotal"},
            "offset": {"alias": "start"},
            "limit": {"alias": "length"},
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
