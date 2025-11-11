#!/usr/bin/env python

# SPDX-FileCopyrightText: 2024 <wmj.py@gmx.com>
#
# SPDX-License-Identifier: LGPL-3.0-or-later
"""
OFX BankAccount structure
"""
from __future__ import annotations
import dataclasses

from .base import (
    text_to_str,
    OfxObject,
)


#: account type
TYPE = ("CHECKING", "SAVINGS", "MONEYMRKT", "CREDITLINE")


@dataclasses.dataclass
class BankAccount(OfxObject):
    '''
    A bank account

    See [OFX]_ 11.3.1 Banking Account

    Fields
    ------
    bank_id
        `BANKID` bank identifier (Spain: banco, entidad)
    branch_id
        `BRANCHID` branch identifier (Spain: sucursal, oficina)
    id
        `ACCTID` account identifier
    type
        `ACCTTYPE` type of account.
    key
        `ACCTKEY` checksum (Spain: digitos de control)
    '''
    tag_name: str = "bankaccfrom"
    bank_id: str | None = None
    branch_id: str | None = None
    id: str | None = None
    type: str = TYPE[1]
    key: str | None = None

    def _get_content(self) -> str:
        elem = self._elem_f

        str_content = elem("bankid", text_to_str(self.bank_id))
        str_content += elem("branchid", text_to_str(self.branch_id))
        str_content += elem("acctid", text_to_str(self.id))
        str_content += elem("accttype", self.type)
        str_content += elem("acctkey", text_to_str(self.key))

        return str_content
