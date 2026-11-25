import os
import sys

import pytest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

import pattrn

SAMPLE = """CITY MARKET
2 LAIT DEMI ECREME 1.350
1 PAIN COMPLET 0,800
TOTAL 3.500
"""


def test_citymarket_line_items():
    ticket = pattrn.pattrcitymarket(SAMPLE)
    assert ticket.name == "City Market"
    assert len(ticket.tup) == 2
    first, second = ticket.tup
    assert first["pname"].strip() == "LAIT DEMI ECREME"
    assert first["pquantity"] == 2
    assert first["pupri"] == 1.35
    assert first["ptotal"] == pytest.approx(2.7)
    assert second["pupri"] == 0.8


def test_citymarket_total_is_sum_of_lines():
    ticket = pattrn.pattrcitymarket(SAMPLE)
    assert ticket.total == pytest.approx(3.5)


@pytest.mark.parametrize("price", ["1 350", "1. 350"])
def test_citymarket_tolerates_ocr_separators(price):
    ticket = pattrn.pattrcitymarket("1 HUILE " + price)
    assert ticket.tup[0]["pupri"] == 1.35
