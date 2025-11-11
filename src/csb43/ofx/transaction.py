#!/usr/bin/env python

# SPDX-FileCopyrightText: 2024 <wmj.py@gmx.com>
#
# SPDX-License-Identifier: LGPL-3.0-or-later

"""
OFX Transaction structure
"""
from __future__ import annotations
from typing import Sequence, Any, ClassVar
import datetime as dt
from decimal import Decimal
import dataclasses
import enum


from ..utils.currency import (
    AnyCurrency,
)
from . import base
from .bank_account import BankAccount
from .payee import Payee


#: type of transaction
class TransactionType(enum.Enum):
    """
    transaction types used in TRNTYPE

    See [OFX]_ Section 11.4.4.3
    """
    # Generic credit
    CREDIT = 0
    # Generic debit
    DEBIT = 1
    # Interest earned or paid
    INT = 2
    # Dividend
    DIV = 3
    # FI fee
    FEE = 4
    # Service charge
    SRVCHG = 5
    # Deposit
    DEP = 6
    # ATM debit or credit
    ATM = 7
    # Point of sale debit or credit
    POS = 8
    # Transfer
    XFER = 9
    # Check
    CHECK = 10
    # Electronic payment
    PAYMENT = 11
    # Cash withdrawal
    CASH = 12
    # Direct deposit
    DIRECTDEP = 13
    # Merchant initiated debit
    DIRECTDEBIT = 14
    # Repeating payment/standing order
    REPEATPMT = 15
    # Other
    OTHER = 16
    # Only valid in <STMTTRNP>; indicates the amount is under a hold
    HOLD = 17


@dataclasses.dataclass
class Transaction(base.OfxObject):
    '''
    A OFX transaction

    See [OFX]_ 11.4.4.1
    '''
    tag_name: str = "stmttrn"
    type: str = TransactionType.OTHER.name
    date_posted: dt.datetime | dt.date | None = None
    date_initiated: dt.datetime | dt.date | None = None
    date_available: dt.datetime | dt.date | None = None
    amount: int | float | Decimal | None = None
    transaction_id: str | None = None
    correct_fit_id: str | None = None
    correct_action: str | None = None
    server_tid: str | None = None
    check_num: str | None = None
    ref_num: str | None = None
    standard_industrial_code: str | None = None
    payee: Payee | None = None
    bank_account_to: BankAccount | None = None
    cc_account_to: BankAccount | None = None
    memo: str | None = None
    image_data: Any | None = None
    currency = None
    origin_currency: AnyCurrency | None = None
    origin_amount: int | float | Decimal | None = None
    inv401ksource: Any | str = None
    payeeid: str | None = None
    name: str | None = None
    extended_name: str | None = None

    def _get_content(self) -> str:
        elem = self._elem_f
        aggr = self._aggr_f

        str_c = elem("trntype", self.type)
        str_c += elem("dtposted", base.date_to_str(self.date_posted))
        str_c += elem("dtuser", base.date_to_str(self.date_initiated))
        str_c += elem("dtavail", base.date_to_str(self.date_available))
        str_c += elem("trnamt", self.amount)
        str_c += elem("fitid", base.text_to_str(self.transaction_id))
        str_c += elem("correctfitid", base.text_to_str(self.correct_fit_id))
        str_c += elem("correctaction", self.correct_action)
        str_c += elem("srvrtid", base.text_to_str(self.server_tid))
        str_c += elem("checknum", base.text_to_str(self.check_num))
        str_c += elem("refnum", base.text_to_str(self.ref_num))
        str_c += elem("sic", base.text_to_str(self.standard_industrial_code))
        str_c += elem("payeeid", base.text_to_str(self.payeeid))
        str_c += elem("name", base.text_to_str(self.name))
        str_c += elem("extdname", base.text_to_str(self.extended_name))
        str_c += aggr("payee", self.payee)
        str_c += aggr("bankacctto", self.bank_account_to)
        str_c += aggr("ccacctto", self.cc_account_to)
        str_c += elem("memo", base.text_to_str(self.memo))
        str_c += aggr("imagedata", self.image_data)
        str_c += elem("currency", base.currency_to_str(self.currency))
        str_curr = None
        if self.origin_currency and (self.amount is not None) and self.origin_amount:
            ratio = round(float(self.amount) / float(self.origin_amount), 20)
            str_curr = elem("currate", ratio)
            str_curr += elem("cursym", base.currency_to_str(self.origin_currency))
        str_c += aggr("origcurrency", str_curr)
        str_c += elem("inv401ksource", self.inv401ksource)

        return str_c


@dataclasses.dataclass
class TransactionList(base.OfxObject):
    '''
    Transaction list aggregate
    '''
    tag_name: str = "banktranlist"
    date_start: dt.datetime | dt.date | None = None
    date_end: dt.datetime | dt.date | None = None
    transactions: list[Transaction] = dataclasses.field(default_factory=list)

    def _get_content(self) -> str:
        elem = self._elem_f
        str_c = elem("dtstart", base.date_to_str(self.date_start))
        str_c += elem("dtend", base.date_to_str(self.date_end))
        for t in self.transactions:
            str_c += self._aggr_f(t.tag_name, t)

        return str_c
