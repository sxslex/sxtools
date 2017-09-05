# -*- coding: utf-8 -*-

name = 'sxtools'
__version__ = '1.0'
__description__ = (
    'Useful Functions Set: Remove Accents, Pluralize, Deep Encode and etc..'
)

from .string_utils import remove_accents
from .string_utils import pluralize
from .string_utils import join_plus
from .string_utils import deep_decode
from .string_utils import deep_encode
from capitalize_name import capitalize
