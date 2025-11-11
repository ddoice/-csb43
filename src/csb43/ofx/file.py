#!/usr/bin/env python

# SPDX-FileCopyrightText: 2024 <wmj.py@gmx.com>
#
# SPDX-License-Identifier: LGPL-3.0-or-later
"""
OFX: File and Response structures
"""
from __future__ import annotations
from typing import (
    Sequence,
    Any,
)
import dataclasses
from datetime import datetime

from ..utils.currency import AnyCurrency
from .base import (
    date_to_str,
    currency_to_str,
    text_to_str,
    OfxObject,
)
from .bank_account import BankAccount
from .balance import Balance
from .transaction import TransactionList


@dataclasses.dataclass
class SignOnResponse(OfxObject):
    """
    `SONRS`

    See [OFX]_ 2.5.1
    """
    tag_name: str = "sonrs"

    def _get_content(self) -> str:
        elem = self._elem_f
        aggr = self._aggr_f
        code = elem("code", 0)
        severity = elem("severity", "INFO")
        status = aggr("status", code + severity)
        dtserver = elem("dtserver", date_to_str(datetime.utcnow()))
        language = elem("language", "SPA")

        return aggr(self.tag_name, status + dtserver + language)


@dataclasses.dataclass
class Response(OfxObject):
    """
    `STMTRS`

    See [OFX]_ 11.4.2.2 Response
    """
    tag_name: str = "stmtrs"
    currency: AnyCurrency | None = None
    account_from: BankAccount | None = None
    transaction_list: TransactionList | None = None
    ledger_balance: Balance | None = None
    available_balance: Balance | None = None
    balances: list[Balance] = dataclasses.field(default_factory=list)
    mktginfo: Any | None = None

    def _get_content(self) -> str:
        elem = self._elem_f
        aggr = self._aggr_f
        str_c = elem("curdef", currency_to_str(self.currency))
        str_c += aggr("bankacctfrom", self.account_from)
        str_c += aggr("banktranlist", self.transaction_list)
        str_c += aggr("ledgerbal", self.ledger_balance)
        str_c += aggr("availbal", self.available_balance)
        if len(self.balances) > 0:
            str_c += aggr(
                "ballist",
                "".join(aggr(x.tag_name, x) for x in self.balances)
            )
        str_c += elem("mktginfo", text_to_str(self.mktginfo))

        return str_c


@dataclasses.dataclass
class File(OfxObject):
    '''
    An OFX file

    See [OFX]_ 2.4.1

    Fields
    ------
    responses
    '''
    tag_name: str = "ofx"
    responses: list[Response] = dataclasses.field(default_factory=list)

    def _get_content(self) -> str:
        elem = self._elem_f
        aggr = self._aggr_f
        if self.sgml:
            header = (
                "OFXHEADER:100\n"
                "DATA:OFXSGML\n"
                "VERSION:103\n"
                "ENCODING:UNICODE\n\n"
            )
        else:
            header = (
                '<?xml version="1.0" encoding="UTF-8"?>\n'
                '<?OFX OFXHEADER="200" VERSION="211" SECURITY="NONE"'
                ' OLDFILEUID="NONE" NEWFILEUID="NONE"?>'
            )
        content = ""
        for r in self.responses:
            aux = elem("trnuid", 0)
            aux += aggr("status",
                        elem("code", 0) + elem("severity", "INFO"))
            aux += aggr(r.tag_name, r)
            content += aggr("stmttrnrs", aux)
        content = (
            aggr("signonmsgsrsv1", SignOnResponse(sgml=self.sgml))
            + aggr("bankmsgsrsv1", content)
        )
        return header + aggr(self.tag_name, content)
