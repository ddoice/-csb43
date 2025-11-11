# SPDX-FileCopyrightText: 2024 <wmj.py@gmx.com>
#
# SPDX-License-Identifier: LGPL-3.0-or-later

# -*- coding: utf-8 -*-
'''
.. note::

    license: GNU Lesser General Public License v3.0 (see LICENSE)
'''
from __future__ import annotations
from typing import TypeVar
import functools
from decimal import Decimal


T = TypeVar('T')


def b_left_pad(bvalue: bytes, n: int, fill=b' ') -> bytes:
    "pad with `fill` chars at the leftside and return a record of `n` chars"
    return fill * (n - len(bvalue)) + bvalue


def b_right_pad(bvalue: bytes, n: int, fill=b' ') -> bytes:
    "pad with `fill` chars at the rightside and return a record of `n` chars"
    return bvalue + fill * (n - len(bvalue))


def nullable(f):
    """nullable decorator

    Return None if function value is None
    """
    @functools.wraps(f)
    def wrapper(value, *args, **kwds):
        if value is None:
            return value
        return f(value, *args, **kwds)
    return wrapper


@nullable
def export_date(value) -> str:
    "export a date as a string"
    return str(value)


@nullable
def export_currency_code(value) -> str:
    "export currency code as string"
    return str(value.alpha_3 or value.numeric)


@nullable
def export_decimal(
    value: Decimal,
    fallback: T | None = None
) -> Decimal | float | str | T:
    "export decimal as a serializable type"
    if fallback == "float":
        return float(value)
    if fallback == "str":
        return str(value)
    if fallback:
        raise ValueError(f"fallback={fallback!r}")
    return value
