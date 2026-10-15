def total_price(items):
    total = 0
    for item in items:
        total += item.get("price", 0) * item.get("qty", 1)
    return total


def format_name(first, last):
    return f"{first} {last}".strip()


def is_valid_email(value):
    return "@" in value and "." in value.split("@")[-1]


def order_discount(order):
    discount = 0
    if order:
        if order.get("customer"):
            if order["customer"].get("vip"):
                for item in order.get("items", []):
                    if item.get("qty", 0) > 10:
                        if item.get("category") == "bulk":
                            if item.get("price", 0) > 100:
                                discount += 15
                            else:
                                discount += 10
                        elif item.get("category") == "seasonal":
                            if order.get("month") in (11, 12):
                                discount += 8
                            else:
                                discount += 3
                        else:
                            discount += 2
                    elif item.get("qty", 0) > 5:
                        discount += 1
            else:
                for item in order.get("items", []):
                    if item.get("qty", 0) > 20:
                        if item.get("category") == "bulk":
                            discount += 5
    return discount
