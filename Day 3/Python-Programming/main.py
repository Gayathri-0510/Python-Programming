import e_comBilling as ec  

def main():
    cart = {
        "Laptop": 55000,
        "Phone": 30000,
        "Headphones": 2000
    }

    ec.generate_invoice(cart, discount_percent=10, gst_percent=10)

if __name__ == "__main__":
    main()
