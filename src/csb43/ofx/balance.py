#!/usr/bin/env python

# SPDX-FileCopyrightText: 2024 <wmj.py@gmx.com>
#
# SPDX-License-Identifier: LGPL-3.0-or-later
"""
An OFX Balance structure
"""
from __future__ import annotations
import datetime as dt
from decimal import Decimal
import dataclasses

from .base import (
    date_to_str,
    OfxObject,
)


@dataclasses.dataclass
class Balance(OfxObject):
    '''
    a balance

    See [OFX]_ 11.4.4.1

    Fields
    ------
    amount
        field `<BALAMT>`
    date
        field `<DTASOF>`
    '''
    tag_name: str = "bal"
    amount: int | float | Decimal | None = None
    date: dt.datetime | dt.date | None = None

    def _get_content(self) -> str:
        elem = self._elem_f
        return f"{elem('balamt', self.amount)}{elem('dtasof', date_to_str(self.date))}"
