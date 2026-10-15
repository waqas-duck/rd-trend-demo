"""Small helpers for the demo shop."""


def total_price(items):
    """Sum price times quantity over the order's items."""
    total = 0
    for item in items:
        total += item.get("price", 0) * item.get("qty", 1)
    return total


def format_name(first, last):
    """Join a first and last name, without stray spaces."""
    return f"{first} {last}".strip()


def is_valid_email(value):
    """A cheap shape check: something@domain.tld."""
    return "@" in value and "." in value.split("@")[-1]


def _vip_item_discount(item, month):
    """Discount for one item of a VIP order."""
    qty = item.get("qty", 0)
    if qty <= 5:
        return 0
    if qty <= 10:
        return 1
    category = item.get("category")
    if category == "bulk":
        return 15 if item.get("price", 0) > 100 else 10
    if category == "seasonal":
        return 8 if month in (11, 12) else 3
    return 2


def _regular_item_discount(item):
    """Discount for one item of a regular order."""
    if item.get("qty", 0) > 20 and item.get("category") == "bulk":
        return 5
    return 0


def order_discount(order):
    """Total discount for an order, from its customer tier and items."""
    if not order or not order.get("customer"):
        return 0
    items = order.get("items", [])
    if order["customer"].get("vip"):
        return sum(_vip_item_discount(item, order.get("month")) for item in items)
    return sum(_regular_item_discount(item) for item in items)
