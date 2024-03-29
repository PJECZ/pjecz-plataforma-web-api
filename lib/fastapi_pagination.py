"""
FastAPI Pagination
"""
from typing import TypeVar, Generic
from fastapi import Query
from fastapi_pagination.default import Page as BasePage, Params as BaseParams
from fastapi_pagination.limit_offset import (
    LimitOffsetPage as BaseLimitOffsetPage,
    LimitOffsetParams as BaseLimitOffsetParams,
)

T = TypeVar("T")


class LimitOffsetParams(BaseLimitOffsetParams):
    """Ajuste para que LimitOffsetPage entregue por defecto 50 resultados y tenga 100 como maximo"""

    limit: int = Query(50, ge=1, le=100, description="Page size limit")
    offset: int = Query(0, ge=0, description="Page offset")


class LimitOffsetPage(BaseLimitOffsetPage[T], Generic[T]):
    """Definir nuevos parametros por defecto"""

    __params_type__ = LimitOffsetParams


class PageParams(BaseParams):
    """Ajuste para que Page entregue por defecto 50 resultados y tenga 100 como maximo"""

    size: int = Query(50, ge=1, le=100, description="Page size")


class Page(BasePage[T], Generic[T]):
    """Definir nuevos parametros por defecto"""

    __params_type__ = PageParams
