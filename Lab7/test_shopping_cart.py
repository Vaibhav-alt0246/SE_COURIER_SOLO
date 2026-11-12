"""Property-based fuzz tests for the shopping cart input functions."""

from hypothesis import given, strategies as st
import pytest

from shopping_cart import cart_total, promo_percent, delivery_zone


@given(st.one_of(st.text(), st.none()))
def test_cart_total_no_crash(s):
    """Any text input is handled deliberately, not by an accidental exception."""
    if s is None:
        with pytest.raises(TypeError):
            cart_total(s)
    else:
        try:
            result = cart_total(s)
        except ValueError:
            return
        assert isinstance(result, int)
        assert result >= 0


@given(st.one_of(st.text(), st.none()))
def test_promo_percent_no_crash(s):
    """A promo input is either a valid bounded integer or a documented error."""
    if s is None:
        with pytest.raises(TypeError):
            promo_percent(s)
    else:
        try:
            result = promo_percent(s)
        except ValueError:
            return
        assert isinstance(result, int)
        assert 0 <= result <= 100


@given(st.one_of(st.text(), st.none()))
def test_delivery_zone_no_crash(s):
    """A pincode is either mapped to a known zone or rejected as invalid."""
    if s is None:
        with pytest.raises(TypeError):
            delivery_zone(s)
    else:
        try:
            result = delivery_zone(s)
        except ValueError:
            return
        assert result in {"North", "West", "South", "East"}


# Valid-input properties complement the no-unexpected-crash fuzz tests.
@given(
    st.lists(
        st.tuples(
            st.text(min_size=1).filter(lambda name: "," not in name and ":" not in name),
            st.integers(min_value=0, max_value=1_000_000),
            st.integers(min_value=0, max_value=1_000_000),
        ),
        min_size=1,
        max_size=20,
    )
)
def test_cart_total_matches_sum(items):
    cart = ",".join(f"{name}:{price}x{qty}" for name, price, qty in items)
    assert cart_total(cart) == sum(price * qty for _, price, qty in items)


@given(st.integers(min_value=0, max_value=100))
def test_valid_promo_codes(percent):
    assert promo_percent(f"OFF{percent}") == percent


@given(st.sampled_from(list("12345678")), st.text(alphabet="0123456789", min_size=5, max_size=5))
def test_valid_pincodes_map_by_first_digit(first_digit, suffix):
    expected = {
        "1": "North", "2": "North", "3": "West", "4": "West",
        "5": "South", "6": "South", "7": "East", "8": "East",
    }[first_digit]
    assert delivery_zone(first_digit + suffix) == expected


# A few explicit examples make the accepted contract easy to understand.
def test_known_examples():
    assert cart_total("pen:10x2,book:250x1") == 270
    assert promo_percent("OFF20") == 20
    assert delivery_zone("560085") == "South"
