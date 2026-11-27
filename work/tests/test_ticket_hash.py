import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

import pattrn


def make_ticket(time):
    products = [{"pname": "PAIN", "pquantity": 1, "pupri": 0.8, "ptotal": 0.8}]
    return pattrn.tickt("Aziza", 0.8, products, "25/11/2026", time, 3)


def test_same_receipt_has_same_hash():
    assert hash(make_ticket("14:02")) == hash(make_ticket("14:02"))


def test_receipts_at_different_times_are_not_duplicates():
    assert hash(make_ticket("09:15")) != hash(make_ticket("18:40"))
