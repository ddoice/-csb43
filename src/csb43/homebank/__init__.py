#!/usr/bin/env python
# SPDX-FileCopyrightText: 2024 <wmj.py@gmx.com>
#
# SPDX-License-Identifier: LGPL-3.0-or-later

'''
Homebank CSV format

References:

    [http://homebank.free.fr/help/06csvformat.html]
'''
from __future__ import annotations

import datetime
from decimal import Decimal

import dataclasses

'''
0. tarjeta de credito
1. cheque
2. efectivo
3. transferencia
4. transferencia interna
5. tarjeta de debito
6. orden de posicion
7. pago electronico
8. deposito
9. honorarios FI
'''

def to_str(data) -> str:
    "convert to str or return the empty string"
    if data is None:
        return ""
    return str(data)


@dataclasses.dataclass
class HomebankCsvTransaction:
    """
    Homebank CSV transaction
    """
    date: datetime.date | None = None
    mode: int | None = None
    info: str | None = None
    payee: str | None = None
    description: str | None = None
    amount: Decimal | None = None
    category: str | None = None

    def to_tuple(self):
        "return data as a tuple ready for CSV writing"
        if self.date is not None:
            mdate = self.date.strftime("%d-%m-%y")
        else:
            mdate = ""
        return (
            mdate,
            to_str(self.mode),
            to_str(self.payee),
            to_str(self.description),
            to_str(self.amount),
            to_str(self.category),
        )
