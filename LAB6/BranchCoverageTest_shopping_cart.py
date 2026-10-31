"""Branch coverage tests for shopping_cart.py.

The cases deliberately exercise both outcomes of every conditional, including
short-circuit outcomes in compound conditions.
"""

import pytest

from shopping_cart import item_total, cart_discount, shipping_fee


@pytest.mark.parametrize(
    ("category", "price", "qty", "expected"),
    [
        ("food", 100, 1, 105),                 # valid category, no bulk discount
        ("electronics", 100, 1, 118),           # another GST branch
        ("clothing", 100, 10, 1008),            # bulk discount and clothing GST
        ("food", 100, 10, 945),                 # bulk discount
    ],
)
def test_item_total_valid_branches(category, price, qty, expected):
    assert item_total(category, price, qty) == expected


def test_item_total_unknown_category_branch():
    with pytest.raises(ValueError, match="unknown category"):
        item_total("toys", 100, 1)


def test_item_total_negative_price_branch():
    with pytest.raises(ValueError, match="invalid price or quantity"):
        item_total("food", -1, 1)


def test_item_total_nonpositive_quantity_branch():
    with pytest.raises(ValueError, match="invalid price or quantity"):
        item_total("food", 100, 0)


@pytest.mark.parametrize(
    ("cart_value", "is_prime", "coupon", "expected"),
    [
        (5000, False, None, 500),       # >= 5000 true
        (4999, False, None, 200),       # >= 5000 false; >= 2000 true
        (1999, False, None, 0),         # both tier checks false
        (2000, True, None, 300),        # prime adjustment
        (1000, False, "FLAT10", 100),   # coupon match and threshold true
        (999, False, "FLAT10", 0),      # coupon match, threshold false
        (2000, False, "SAVE10", 200),  # coupon comparison false
    ],
)
def test_cart_discount_branches(cart_value, is_prime, coupon, expected):
    assert cart_discount(cart_value, is_prime, coupon) == expected


@pytest.mark.parametrize(
    ("cart_value", "is_prime", "is_express", "expected"),
    [
        (100, True, False, 0),       # prime branch
        (500, False, False, 0),      # non-prime, free-shipping threshold true
        (499, False, False, 40),     # non-prime, free-shipping threshold false
        (100, False, True, 140),     # express true, inner prime false
        (100, True, True, 50),       # express true, inner prime true
        (100, False, False, 40),     # express false
    ],
)
def test_shipping_fee_branches(cart_value, is_prime, is_express, expected):
    assert shipping_fee(cart_value, is_prime, is_express) == expected
