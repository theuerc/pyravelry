"""Endpoints for Ravelry"""

from . import base
from .color_families import ColorFamiliesResource
from .current_user import CurrentUserResource
from .fiber_attributes import FiberAttributesResource
from .fiber_categories import FiberCategoriesResource
from .people import PeopleResource
from .search import SearchResource
from .yarn_attributes import YarnAttributesResource
from .yarn_companies import YarnCompaniesResource
from .yarn_weights import YarnWeightsResource

__all__ = [
    "ColorFamiliesResource",
    "CurrentUserResource",
    "CurrentUserResource",
    "FiberAttributesResource",
    "FiberCategoriesResource",
    "PeopleResource",
    "SearchResource",
    "YarnAttributesResource",
    "YarnCompaniesResource",
    "YarnWeightsResource",
    "base",
]
