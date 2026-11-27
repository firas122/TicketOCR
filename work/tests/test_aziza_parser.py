import os
import sys

import pytest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

import pattrn

SAMPLE = """AZIZA
LAIT DELICE = 1.350
EAU SAFIA 3x 0.700 = 2.100
MERCI
"""


def test_aziza_line_items():
    ticket = pattrn.pattraziza(SAMPLE)
    assert ticket.name == "Aziza"
    assert len(ticket.tup) == 2
    first, second = ticket.tup
    assert first["pname"].strip() == "LAIT DELICE"
    assert first["pquantity"] == 1
    assert first["pupri"] == 1.35
    assert second["pname"].strip() == "EAU SAFIA"
    assert second["pquantity"] == 3
    assert second["pupri"] == 0.7
    assert second["ptotal"] == pytest.approx(2.1)


def test_aziza_total_is_sum_of_lines():
    ticket = pattrn.pattraziza(SAMPLE)
    assert ticket.total == pytest.approx(3.45)


@pytest.mark.parametrize("line", ["PAIN = 0,800", "PAIN 2x 0,400 = 0,800", "PAIN 2x 0.400 = 0,800"])
def test_aziza_comma_decimals(line):
    ticket = pattrn.pattraziza(line)
    assert len(ticket.tup) == 1
    assert ticket.tup[0]["ptotal"] == pytest.approx(0.8)


def test_aziza_empty_text():
    ticket = pattrn.pattraziza("")
    assert ticket.tup == []
    assert ticket.total == 0
