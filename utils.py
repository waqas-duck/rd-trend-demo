def total_price(items):
    total = 0
    for item in items:
        total += item.get("price", 0) * item.get("qty", 1)
    return total


def format_name(first, last):
    return f"{first} {last}".strip()


def is_valid_email(value):
    return "@" in value and "." in value.split("@")[-1]
