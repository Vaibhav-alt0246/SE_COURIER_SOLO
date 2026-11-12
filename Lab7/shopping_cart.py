"""Shopping cart input processing functions hardened against invalid input."""

ZONES = {
    "1": "North", "2": "North", "3": "West", "4": "West",
    "5": "South", "6": "South", "7": "East", "8": "East",
}


def cart_total(cart):
    """Return the total price for a cart string: name:pricexqty,... .

    Invalid input is rejected with ValueError; non-string input raises TypeError.
    Prices and quantities must be non-negative integers and item names non-empty.
    """
    if not isinstance(cart, str):
        raise TypeError("cart must be a string")
    if not cart.strip():
        raise ValueError("cart must contain at least one item")

    total = 0
    for raw_item in cart.split(","):
        item = raw_item.strip()
        if not item:
            raise ValueError("cart contains an empty item")
        if item.count(":") != 1:
            raise ValueError("each item must contain exactly one ':'")

        name, details = item.split(":", 1)
        if not name.strip():
            raise ValueError("item name must not be empty")
        if details.count("x") != 1:
            raise ValueError("item details must use the format pricexqty")

        price_text, qty_text = details.split("x", 1)
        price_text, qty_text = price_text.strip(), qty_text.strip()
        if not price_text.isdecimal() or not qty_text.isdecimal():
            raise ValueError("price and quantity must be non-negative integers")

        price, quantity = int(price_text), int(qty_text)
        total += price * quantity
    return total


def promo_percent(code):
    """Extract a discount percentage from an OFF<n> promo code."""
    if not isinstance(code, str):
        raise TypeError("promo code must be a string")
    normalized = code.strip().upper()
    if not normalized.startswith("OFF"):
        raise ValueError("promo code must start with 'OFF'")

    percentage_text = normalized[3:]
    if not percentage_text or not percentage_text.isdecimal():
        raise ValueError("promo code must be in the format OFF followed by digits")

    percentage = int(percentage_text)
    if not 0 <= percentage <= 100:
        raise ValueError("discount percentage must be between 0 and 100")
    return percentage


def delivery_zone(pincode):
    """Return the delivery zone for a six-digit Indian pincode."""
    if not isinstance(pincode, str):
        raise TypeError("pincode must be a string")
    if len(pincode) != 6 or not pincode.isascii() or not pincode.isdigit():
        raise ValueError("pincode must contain exactly six ASCII digits")
    if pincode[0] not in ZONES:
        raise ValueError("pincode does not belong to a supported delivery zone")
    return ZONES[pincode[0]]


def main():
    print("==== Running cart_total ====")
    user_input = input("Enter cart as name:pricexqty CSV (e.g. pen:10x2,book:250x1): ")
    try:
        print("Cart Total:", cart_total(user_input))
    except (TypeError, ValueError) as exc:
        print("Invalid cart:", exc)

    print("\n==== Running promo_percent ====")
    user_input = input("Enter a promo code (e.g. OFF20): ")
    try:
        print("Discount Percent:", promo_percent(user_input))
    except (TypeError, ValueError) as exc:
        print("Invalid promo code:", exc)

    print("\n==== Running delivery_zone ====")
    user_input = input("Enter a 6 digit pincode (e.g. 560085): ")
    try:
        print("Delivery Zone:", delivery_zone(user_input))
    except (TypeError, ValueError) as exc:
        print("Invalid pincode:", exc)


if __name__ == "__main__":
    main()
