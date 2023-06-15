from tkinter import *

class Product:
    def __init__(self, name, description, price, image):
        self.name = name
        self.description = description
        self.price = price
        self.image = image
        self.added_to_cart = False

class ShoppingCart:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        product.added_to_cart = True
        self.products.append(product)

    def remove_product(self, product):
        product.added_to_cart = False
        self.products.remove(product)

    def increase_amount(self, product):
        product.amount += 1

    def decrease_amount(self, product):
        product.amount -= 1
        if product.amount == 0:
            self.remove_product(product)

class ShoppingApp:
    def __init__(self, root):
        self.root = root
        self.cart = ShoppingCart()

        self.our_products_frame = Frame(root)
        self.our_products_frame.pack(side=LEFT)

        self.cart_frame = Frame(root)
        self.cart_frame.pack(side=RIGHT)

        self.total_price = 0
        self.total_price_label = Label(self.cart_frame, text=f"Total Price: ${self.total_price}")
        self.total_price_label.pack()

    def add_to_cart(self, product):
        self.cart.add_product(product)
        self.update_cart()

    def remove_from_cart(self, product):
        self.cart.remove_product(product)
        self.update_cart()

    def increase_amount(self, product):
        self.cart.increase_amount(product)
        self.update_cart()

    def decrease_amount(self, product):
        self.cart.decrease_amount(product)
        self.update_cart()

    def update_cart(self):
        for widget in self.cart_frame.winfo_children():
            widget.destroy()

        for product in self.cart.products:
            product_frame = Frame(self.cart_frame)
            product_frame.pack()

            product_name = Label(product_frame, text=product.name)
            product_name.pack(side=LEFT)

            product_price = Label(product_frame, text=f"${product.price}")
            product_price.pack(side=LEFT)

            increase_button = Button(product_frame, text="+", command=lambda p=product: self.increase_amount(p))
            increase_button.pack(side=LEFT)

            amount_label = Label(product_frame, text="1")  # Assuming the initial amount is 1
            amount_label.pack(side=LEFT)

            decrease_button = Button(product_frame, text="-", command=lambda p=product: self.decrease_amount(p))
            decrease_button.pack(side=LEFT)

            remove_button = Button(product_frame, text="Remove", command=lambda p=product: self.remove_from_cart(p))
            remove_button.pack(side=LEFT)

        self.total_price = sum([product.price for product in self.cart.products])
        self.total_price_label.config(text=f"Total Price: ${self.total_price}")

    def run(self):
        self.populate_products()
        self.root.mainloop()

    def populate_products(self):
        # Simulated product data
        products_data = [
            {"name": "Product 1", "description": "Description 1", "price": 10, "image": "air-zoom-pegasus-36-mens-running-shoe-wide-D24Mcz-removebg-preview.png"},
            {"name": "Product 2", "description": "Description 2", "price": 20, "image": "air-zoom-pegasus-36-shield-mens-running-shoe-24FBGb__1_-removebg-preview.png"},
            {"name": "Product 3", "description": "Description 3", "price": 30, "image": "cruzrone-unisex-shoe-T2rRwS-removebg-preview.png"},
            {"name": "Product 4", "description": "Description 4", "price": 40, "image": "epic-react-flyknit-2-mens-running-shoe-2S0Cn1-removebg-preview.png"},
            {"name": "Product 5", "description": "Description 5", "price": 50, "image": "odyssey-react-flyknit-2-mens-running-shoe-T3VG7N-removebg-preview.png"},
        ]

        for product_data in products_data:
            product = Product(product_data["name"], product_data["description"], product_data["price"],
                              product_data["image"])
            self.add_product_to_frame(self.our_products_frame, product)

    def add_product_to_frame(self, frame, product):
        product_frame = Frame(frame)
        product_frame.pack()

        product_name = Label(product_frame, text=product.name)
        product_name.pack(side=LEFT)

        product_description = Label(product_frame, text=product.description)
        product_description.pack(side=LEFT)

        product_price = Label(product_frame, text=f"${product.price}")
        product_price.pack(side=LEFT)

        add_to_cart_button = Button(product_frame, text="Add to Cart", command=lambda p=product: self.add_to_cart(p))
        add_to_cart_button.pack(side=LEFT)

        if product.added_to_cart:
            add_to_cart_button.config(text="✓", state=DISABLED)

        product_image = Label(product_frame, text=f"Image: {product.image}")  # Displaying image name for simplicity
        product_image.pack(side=LEFT)

root = Tk()
root.title("Shopping Cart")
app = ShoppingApp(root)
app.run()
