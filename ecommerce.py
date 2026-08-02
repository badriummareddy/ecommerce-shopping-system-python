class ECommerce:

    def __init__(self):
        self.products = {
            "Laptop": 50000,
            "Mobile": 20000,
            "Headphones": 2000,
            "Smartwatch": 5000,
            "Keyboard": 1500
        }
        self.cart = {}
        self.total = 0

    def show_products(self):
        print("\n===== AVAILABLE PRODUCTS =====")
        for product, price in self.products.items():
            print(product, "- ₹", price)

    def add_to_cart(self):
        product = input("Enter Product Name: ")

        if product in self.products:
            qty = int(input("Enter Quantity: "))
            self.cart[product] = qty
            print("Product Added to Cart Successfully!")
        else:
            print("Product Not Available!")

    def view_cart(self):
        if len(self.cart) == 0:
            print("Your Cart is Empty!")
        else:
            print("\n===== YOUR CART =====")
            self.total = 0
            for product, qty in self.cart.items():
                amount = self.products[product] * qty
                self.total += amount
                print(product, " x ", qty, "= ₹", amount)

            print("--------------------------")
            print("Total Amount: ₹", self.total)

    def checkout(self):
        if len(self.cart) == 0:
            print("Cart is Empty!")
            return

        gst = self.total * 0.18
        final_amount = self.total + gst

        print("\n===== PAYMENT SUMMARY =====")
        print("Subtotal : ₹", self.total)
        print("GST (18%): ₹", round(gst, 2))
        print("--------------------------")
        print("Total Bill: ₹", round(final_amount, 2))
        print("Order Placed Successfully!")


shop = ECommerce()

while True:
    print("\n===== E-COMMERCE SHOPPING SYSTEM =====")
    print("1. View Products")
    print("2. Add to Cart")
    print("3. View Cart")
    print("4. Checkout")
    print("5. Exit")

    choice = int(input("Enter Your Choice: "))

    if choice == 1:
        shop.show_products()

    elif choice == 2:
        shop.add_to_cart()

    elif choice == 3:
        shop.view_cart()

    elif choice == 4:
        shop.view_cart()
        shop.checkout()

    elif choice == 5:
        print("Thank You for Shopping!")
        break

    else:
        print("Invalid Choice!")
