import os
import sys

import pytest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

import pattrn

# each product line is followed by its barcode line
SAMPLE = """CARREFOUR MARKET
2 LAIT DELICE 1.3500
6191234567890
3 EAU SAFIA 0,7000
6191234567891
MERCI
"""


def test_carrefour_line_items():
    ticket = pattrn.pattrcarrf(SAMPLE)
    assert ticket.name == "CARREFOUR"
    assert len(ticket.tup) == 2
    first, second = ticket.tup
    assert first["pname"].strip() == "LAIT DELICE"
    assert first["pquantity"] == 2
    assert first["pupri"] == 1.35
    assert second["pname"].strip() == "EAU SAFIA"
    assert second["pupri"] == 0.7


def test_carrefour_totals_do_not_accumulate():
    ticket = pattrn.pattrcarrf(SAMPLE)
    first, second = ticket.tup
    assert first["ptotal"] == pytest.approx(2.7)
    assert second["ptotal"] == pytest.approx(2.1)
    assert ticket.total == pytest.approx(4.8)


def test_carrefour_date_keeps_year():
    text = "1 PAIN 25/11/2026 14:02 0.8000\n6191234567890\n"
    ticket = pattrn.pattrcarrf(text)
    assert ticket.date == "25/11/2026"
    assert ticket.time == "14:02"


def test_carrefour_empty_text():
    ticket = pattrn.pattrcarrf("")
    assert ticket.tup == []
    assert ticket.total == 0
