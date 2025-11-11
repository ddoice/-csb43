# SPDX-FileCopyrightText: 2024 <wmj.py@gmx.com>
#
# SPDX-License-Identifier: LGPL-3.0-or-later

from datetime import date
import pytest

from .. import utils


@pytest.mark.parametrize("bvalue,n,fill,ref", [
    (b"abc", 5, None, b"  abc"),
    (b"abc", 3, None, b"abc"),
    (b"abc", 0, None, b"abc"),
    (b"abc", 5, b"0", b"00abc"),
    (b"abc", 3, b"0", b"abc"),
    (b"abc", 0, b"0", b"abc"),
])
def test_b_left_pad(bvalue, n, fill, ref):
    "check b_left_pad"
    if fill is not None:
        result = utils.b_left_pad(bvalue, n, fill=fill)
    else:
        result = utils.b_left_pad(bvalue, n)
    assert result == ref


@pytest.mark.parametrize("bvalue,n,fill,ref", [
    (b"abc", 5, None, b"abc  "),
    (b"abc", 3, None, b"abc"),
    (b"abc", 0, None, b"abc"),
    (b"abc", 5, b"0", b"abc00"),
    (b"abc", 3, b"0", b"abc"),
    (b"abc", 0, b"0", b"abc"),
])
def test_b_right_pad(bvalue, n, fill, ref):
    "check b_left_pad"
    if fill is not None:
        result = utils.b_right_pad(bvalue, n, fill=fill)
    else:
        result = utils.b_right_pad(bvalue, n)
    assert result == ref


@pytest.mark.parametrize("value,ref", [
    (date(2020, 5, 5), "2020-05-05"),
    (None, None),
])
def test_export_date(value, ref):
    "check export_date"
    assert utils.export_date(value) == ref
