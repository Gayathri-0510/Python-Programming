def apply_discount(price, discount_percent):
    """Apply discount and return discounted price"""
    if discount_percent < 0 or discount_percent > 100:
        raise ValueError("Discount percent must be between 0 and 100")
    return price - (price * discount_percent / 100)


def add_gst(price, gst_percent=18):
    """Add GST (default 18%) and return new price"""
    if gst_percent < 0:
        raise ValueError("GST percent cannot be negative")
    return price + (price * gst_percent / 100)


def generate_invoice(cart, discount_percent=0, gst_percent=18):
    """Generate and print a detailed invoice"""
    print("------ INVOICE ------")
    subtotal = 0

    for item, price in cart.items():
        print(f"{item:<15} : ₹{price}")
        subtotal += price

    print("---------------------")
    print(f"Subtotal: ₹{subtotal}")

    if discount_percent > 0:
        discounted = apply_discount(subtotal, discount_percent)
        print(f"After {discount_percent}% discount: ₹{discounted:.2f}")
    else:
        discounted = subtotal

    final_price = add_gst(discounted, gst_percent)
    print(f"After {gst_percent}% GST: ₹{final_price:.2f}")
    print("---------------------")
    print("Thank you for shopping with us!")
