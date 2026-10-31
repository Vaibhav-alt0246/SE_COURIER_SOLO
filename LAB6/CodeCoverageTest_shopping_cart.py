"""Statement/code coverage tests for shopping_cart.py."""

import pytest

from shopping_cart import item_total, cart_discount, shipping_fee


def test_item_total_for_each_supported_category():
    assert item_total("food", 100, 2) == 210
    assert item_total("electronics", 100, 1) == 118
    assert item_total("clothing", 100, 1) == 112


def test_item_total_rejects_unknown_category():
    with pytest.raises(ValueError, match="unknown category"):
        item_total("toys", 100, 1)


@pytest.mark.parametrize(
    ("price", "qty"),
    [(-1, 1), (100, 0)],
)
def test_item_total_rejects_invalid_price_or_quantity(price, qty):
    with pytest.raises(ValueError, match="invalid price or quantity"):
        item_total("food", price, qty)


def test_item_total_applies_bulk_discount():
    # 10 * 100 = 1000; bulk discount = 100; GST = 5% of 900.
    assert item_total("food", 100, 10) == 945


def test_item_total_without_bulk_discount():
    assert item_total("food", 100, 2) == 210


def test_cart_discount_all_tiers_and_adjustments():
    assert cart_discount(6000, False, None) == 500
    assert cart_discount(2500, False, None) == 200
    assert cart_discount(500, False, None) == 0
    assert cart_discount(2500, True, None) == 300
    assert cart_discount(2000, False, "FLAT10") == 400


def test_shipping_fee_all_fee_paths():
    assert shipping_fee(100, False, False) == 40
    assert shipping_fee(600, False, False) == 0
    assert shipping_fee(100, True, False) == 0
    assert shipping_fee(100, False, True) == 140
    assert shipping_fee(100, True, True) == 50
