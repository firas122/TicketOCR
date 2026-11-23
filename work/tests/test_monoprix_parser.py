import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

import pattrn

SAMPLE = """MONOPRIX SOUSSE
24/02/21 14:02
TAMPON EPONGE A RE 1 x 1230
YAOURT AU FRUITS 2 x 720
"""


def test_monoprix_header_fields():
    ticket = pattrn.pattrMonoprix(SAMPLE)
    assert ticket.name == "Monoprix"
    assert ticket.date == "24/02/21"
    assert ticket.time == "14:02"


def test_monoprix_line_items():
    ticket = pattrn.pattrMonoprix(SAMPLE)
    assert len(ticket.tup) == 2
    first, second = ticket.tup
    assert first["pname"].strip() == "TAMPON EPONGE A RE"
    assert first["pquantity"] == 1
    assert first["pupri"] == 1230.0
    assert second["pquantity"] == 2
    assert second["ptotal"] == 1440.0


def test_monoprix_total_is_sum_of_lines():
    ticket = pattrn.pattrMonoprix(SAMPLE)
    assert ticket.total == 1230.0 + 1440.0
