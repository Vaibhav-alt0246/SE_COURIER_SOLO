# Lab 7 — Fuzz Testing (Shopping Cart)

This folder contains the Lab 7 implementation based on the provided starter repository.

## Files

- `shopping_cart.py` — hardened implementation of `cart_total`, `promo_percent`, and `delivery_zone`.
- `test_shopping_cart.py` — Hypothesis property-based tests and a few explicit contract examples.

## Setup

Use Python 3.8 or newer. From this folder run:

```bash
python -m pip install hypothesis pytest
```

## Lab workflow

1. Preserve the original starter `shopping_cart.py` and `test_shopping_cart.py` before replacing them, so the initial buggy run and failing fuzz tests can be demonstrated honestly.
2. Run the original buggy app (`python shopping_cart.py`) with representative inputs and capture the output. The app is interactive; enter a cart such as `pen:10x2,book:250x1`, promo `OFF20`, and pincode `560085`.
3. Complete/run Hypothesis tests against the original buggy implementation. The starter tests use the same three public function names.
4. Replace the application with the hardened `shopping_cart.py` and tests with `test_shopping_cart.py` from this folder.
5. Run the fixed app: `python shopping_cart.py`.
6. Run the fixed tests: `python -m pytest -v test_shopping_cart.py`.

## Input contract in the fixed implementation

- Cart: one or more comma-separated `name:pricexqty` entries. Names cannot be empty; price and quantity are non-negative decimal integers. Invalid cart strings raise `ValueError`; non-string values raise `TypeError`.
- Promo: `OFF` followed by decimal digits, case-insensitive, with a percentage from 0 through 100. Invalid strings raise `ValueError`; non-string values raise `TypeError`.
- Pincode: exactly six ASCII digits, with first digit `1`–`8` as supported by the provided `ZONES` mapping. Invalid strings raise `ValueError`; non-string values raise `TypeError`.

## Important note about screenshots

Screenshots must come from your own terminal running the original buggy version, the failing tests, the fixed application, and the passing final tests. Do not label generated or illustrative output as a real run. The attached lab handout asks for a single PDF containing these screenshots.
