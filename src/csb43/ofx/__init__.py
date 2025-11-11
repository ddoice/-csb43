# SPDX-FileCopyrightText: 2024 <wmj.py@gmx.com>
#
# SPDX-License-Identifier: LGPL-3.0-or-later

'''
Partial implementation of a OFX file writer.

This package is not intended to fully implement the OFX Spec. Its final purpose
is the conversion from CSB43 (norma 43 del Consejo Superior Bancario). That is,
only transaction response is (partially) implemented.

References
----------

.. [OFX] [http://www.ofx.net/] Open Financial Exchange, Specification 2.2 (nov 26, 2017).
   Intuit Inc.  Envestnet
'''
from __future__ import annotations

from .bank_account import BankAccount
from .payee import Payee
from .balance import Balance
from .transaction import Transaction, TransactionList
from .file import File, SignOnResponse, Response

__all__ = [
    "File",
    "SignOnResponse",
    "Response",
    "Transaction",
    "TransactionList",
    "Balance",
    "Payee",
    "BankAccount",
]
