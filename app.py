import streamlit as st

st.set_page_config(
    page_title="Mini Business Management System",
    page_icon="🛍️"
)

# -----------------------------
# STORE DATA IN SESSION
# -----------------------------

if "products" not in st.session_state:
    st.session_state.products = []

if "cart" not in st.session_state:
    st.session_state.cart = []

if "sales" not in st.session_state:
    st.session_state.sales = []

if "expenses" not in st.session_state:
    st.session_state.expenses = []


products = st.session_state.products
cart = st.session_state.cart
sales = st.session_state.sales
expenses = st.session_state.expenses


# -----------------------------
# TITLE
# -----------------------------

st.title("🛍️ Mini Business Management System")
st.write("Welcome to the Mini Business Management System.")


# -----------------------------
# MAIN MENU
# -----------------------------

user = st.radio(
    "Who are you?",
    ["Seller", "Buyer"]
)


# ============================================================
# SELLER MENU
# ============================================================

if user == "Seller":

    st.header("👩🏽‍💼 Seller Menu")

    seller_option = st.selectbox(
        "Select an option",
        [
            "Add a new product",
            "Update a product",
            "Remove a product",
            "View current stock",
            "Restock",
            "Add expense",
            "View sales/business summary"
        ]
    )


    # -------------------------
    # 1. ADD PRODUCT
    # -------------------------

    if seller_option == "Add a new product":

        st.subheader("Add a New Product")

        product_name = st.text_input("Enter the product")

        cost_price = st.number_input(
            "How much did you get this product for? ₦",
            min_value=0,
            step=100
        )

        price = st.number_input(
            "Enter the selling price: ₦",
            min_value=0,
            step=100
        )

        quantity = st.number_input(
            "How many?",
            min_value=0,
            step=1
        )

        units = st.text_input(
            "What are they measured in?"
        )

        if st.button("Add Product"):

            if product_name == "" or units == "":
                st.warning("Please fill in all the fields.")

            else:

                product = {
                    "name": product_name.lower(),
                    "cost_price": cost_price,
                    "price": price,
                    "quantity": quantity,
                    "units": units
                }

                products.append(product)

                st.success("ADDED SUCCESSFULLY!")


    # -------------------------
    # 2. UPDATE PRODUCT
    # -------------------------

    elif seller_option == "Update a product":

        st.subheader("Update a Product")

        if len(products) == 0:

            st.info("You have not added any product to stock.")

        else:

            product_names = [
                product["name"]
                for product in products
            ]

            selected_name = st.selectbox(
                "Which product do you want to update?",
                product_names
            )

            selected_product = next(
                product
                for product in products
                if product["name"] == selected_name
            )

            update_choice = st.selectbox(
                "What do you want to update?",
                [
                    "Name",
                    "Cost price",
                    "Selling price",
                    "Quantity",
                    "Units"
                ]
            )

            if update_choice == "Name":

                new_name = st.text_input(
                    "Enter the new name",
                    value=selected_product["name"]
                )

                if st.button("Update Name"):

                    selected_product["name"] = new_name.lower()

                    st.success(
                        "Name updated successfully!"
                    )


            elif update_choice == "Cost price":

                new_cost_price = st.number_input(
                    "Enter the new cost price: ₦",
                    min_value=0,
                    value=int(selected_product["cost_price"]),
                    step=100
                )

                if st.button("Update Cost Price"):

                    selected_product["cost_price"] = new_cost_price

                    st.success(
                        "Cost price updated successfully!"
                    )


            elif update_choice == "Selling price":

                new_price = st.number_input(
                    "Enter the new selling price: ₦",
                    min_value=0,
                    value=int(selected_product["price"]),
                    step=100
                )

                if st.button("Update Selling Price"):

                    selected_product["price"] = new_price

                    st.success(
                        f"Price updated successfully! "
                        f"New price: ₦{new_price:,.0f}"
                    )


            elif update_choice == "Quantity":

                new_quantity = st.number_input(
                    "Enter the new quantity",
                    min_value=0,
                    value=int(selected_product["quantity"]),
                    step=1
                )

                if st.button("Update Quantity"):

                    selected_product["quantity"] = new_quantity

                    st.success(
                        f"Quantity updated successfully! "
                        f"New quantity: {new_quantity} "
                        f"{selected_product['units']}"
                    )


            elif update_choice == "Units":

                new_unit = st.text_input(
                    "Enter the new unit",
                    value=selected_product["units"]
                )

                if st.button("Update Units"):

                    selected_product["units"] = new_unit

                    st.success(
                        "Unit updated successfully!"
                    )


    # -------------------------
    # 3. REMOVE PRODUCT
    # -------------------------

    elif seller_option == "Remove a product":

        st.subheader("Remove a Product")

        if len(products) == 0:

            st.info("You have not added any product to stock.")

        else:

            product_names = [
                product["name"]
                for product in products
            ]

            selected_name = st.selectbox(
                "Which product do you want to remove?",
                product_names
            )

            confirmation = st.radio(
                f"Are you sure you want to remove "
                f"{selected_name}?",
                ["No", "Yes"]
            )

            if st.button("Remove Product"):

                if confirmation == "Yes":

                    selected_product = next(
                        product
                        for product in products
                        if product["name"] == selected_name
                    )

                    products.remove(selected_product)

                    st.success(
                        f"{selected_name} removed from products!"
                    )

                else:

                    st.info("REMOVAL CANCELLED!")


    # -------------------------
    # 4. VIEW CURRENT STOCK
    # -------------------------

    elif seller_option == "View current stock":

        st.subheader("📦 Your Current Stock")

        if len(products) == 0:

            st.info("Stock is empty.")

        else:

            for number, item in enumerate(
                products,
                start=1
            ):

                st.write(
                    f"**{number}. {item['name']}** — "
                    f"₦{item['price']:,.0f} — "
                    f"{item['quantity']} "
                    f"{item['units']}"
                )

                if item["quantity"] == 0:

                    st.error(
                        f"⚠️ OUT OF STOCK! "
                        f"{item['name']} is finished."
                    )

                elif item["quantity"] <= 2:

                    st.warning(
                        f"⚠️ LOW STOCK! "
                        f"Only {item['quantity']} "
                        f"{item['units']} left."
                    )


    # -------------------------
    # 5. RESTOCK
    # -------------------------

    elif seller_option == "Restock":

        st.subheader("Restock Product")

        if len(products) == 0:

            st.info("Stock is empty.")

        else:

            product_names = [
                product["name"]
                for product in products
            ]

            selected_name = st.selectbox(
                "Which product do you want to restock?",
                product_names
            )

            selected_product = next(
                product
                for product in products
                if product["name"] == selected_name
            )

            st.write(
                f"Current stock: "
                f"**{selected_product['quantity']} "
                f"{selected_product['units']}**"
            )

            restock_quantity = st.number_input(
                "How many do you want to restock?",
                min_value=1,
                step=1
            )

            if st.button("Restock"):

                selected_product["quantity"] += restock_quantity

                st.success(
                    f"RESTOCK SUCCESSFUL! "
                    f"Current stock: "
                    f"{selected_product['quantity']} "
                    f"{selected_product['units']}"
                )


    # -------------------------
    # 6. ADD EXPENSE
    # -------------------------

    elif seller_option == "Add expense":

        st.subheader("Add Expense")

        expense_name = st.text_input(
            "What is the expense for?"
        )

        expense_amount = st.number_input(
            "What is the cost? ₦",
            min_value=0,
            step=100
        )

        if st.button("Record Expense"):

            if expense_name == "":

                st.warning(
                    "Please enter the expense name."
                )

            else:

                expenses.append({
                    "name": expense_name.lower(),
                    "amount": expense_amount
                })

                st.success(
                    "Expense recorded successfully!"
                )


    # -------------------------
    # 7. SALES/BUSINESS SUMMARY
    # -------------------------

    elif seller_option == "View sales/business summary":

        st.subheader("📊 Sales Summary")

        if len(sales) == 0:

            st.info("No sales yet.")

        else:

            total_sales = 0
            total_profit = 0
            total_expenses = 0

            st.write("### Sales")

            for sale in sales:

                st.write(
                    f"{sale['name']} — "
                    f"{sale['quantity']} "
                    f"{sale['units']}"
                )

                total_sales += (
                    sale["price"]
                    * sale["quantity"]
                )

                total_profit += (
                    (sale["price"] - sale["cost_price"])
                    * sale["quantity"]
                )

            for expense in expenses:

                total_expenses += expense["amount"]

            net_profit = (
                total_profit
                - total_expenses
            )

            st.divider()

            st.write(
                f"**Total sales:** "
                f"₦{total_sales:,.0f}"
            )

            st.write(
                f"**Total profit:** "
                f"₦{total_profit:,.0f}"
            )

            st.write("### Your Expenses")

            if len(expenses) == 0:

                st.write("No expenses recorded.")

            else:

                for expense in expenses:

                    st.write(
                        f"{expense['name']} — "
                        f"₦{expense['amount']:,.0f}"
                    )

            st.write(
                f"**Total expenses:** "
                f"₦{total_expenses:,.0f}"
            )

            st.write(
                f"**Net profit:** "
                f"₦{net_profit:,.0f}"
            )


# ============================================================
# BUYER MENU
# ============================================================

elif user == "Buyer":

    st.header("🛒 Buyer Menu")

    buyer_option = st.selectbox(
        "Select an option",
        [
            "View available products",
            "Add to cart",
            "View cart",
            "Remove from cart",
            "Increase/reduce quantity in cart",
            "Checkout"
        ]
    )


    # -------------------------
    # 1. VIEW AVAILABLE PRODUCTS
    # -------------------------

    if buyer_option == "View available products":

        st.subheader("Available Products")

        available_products = [
            product
            for product in products
            if product["quantity"] > 0
        ]

        if len(available_products) == 0:

            st.info(
                "There are no products available."
            )

        else:

            for number, item in enumerate(
                available_products,
                start=1
            ):

                st.write(
                    f"**{number}. {item['name']}** — "
                    f"₦{item['price']:,.0f} — "
                    f"{item['quantity']} "
                    f"{item['units']}"
                )


    # -------------------------
    # 2. ADD TO CART
    # -------------------------

    elif buyer_option == "Add to cart":

        st.subheader("Add to Cart")

        available_products = [
            product
            for product in products
            if product["quantity"] > 0
        ]

        if len(available_products) == 0:

            st.info(
                "There are no products available."
            )

        else:

            product_names = [
                product["name"]
                for product in available_products
            ]

            selected_name = st.selectbox(
                "Select a product",
                product_names
            )

            selected_product = next(
                product
                for product in available_products
                if product["name"] == selected_name
            )

            st.write(
                f"₦{selected_product['price']:,.0f} — "
                f"{selected_product['quantity']} "
                f"{selected_product['units']} available"
            )

            purchase_quantity = st.number_input(
                "How many do you want?",
                min_value=1,
                max_value=int(
                    selected_product["quantity"]
                ),
                step=1
            )

            if st.button("Add to Cart"):

                cart.append({
                    "name": selected_product["name"],
                    "cost_price": selected_product["cost_price"],
                    "price": selected_product["price"],
                    "quantity": purchase_quantity,
                    "units": selected_product["units"]
                })

                st.success(
                    f"{selected_product['name']} "
                    f"added to cart!"
                )


    # -------------------------
    # 3. VIEW CART
    # -------------------------

    elif buyer_option == "View cart":

        st.subheader("🛒 Your Cart")

        if len(cart) == 0:

            st.info(
                "You haven't added anything to cart."
            )

        else:

            total = 0

            for number, item in enumerate(
                cart,
                start=1
            ):

                item_total = (
                    item["price"]
                    * item["quantity"]
                )

                st.write(
                    f"**{number}. {item['name']}** — "
                    f"₦{item['price']:,.0f} — "
                    f"{item['quantity']} "
                    f"{item['units']}"
                )

                total += item_total

            st.divider()

            st.write(
                f"### Total: ₦{total:,.0f}"
            )


    # -------------------------
    # 4. REMOVE FROM CART
    # -------------------------

    elif buyer_option == "Remove from cart":

        st.subheader("Remove from Cart")

        if len(cart) == 0:

            st.info("Your cart is empty.")

        else:

            cart_names = [
                item["name"]
                for item in cart
            ]

            selected_name = st.selectbox(
                "Which product do you want to remove?",
                cart_names
            )

            if st.button("Remove from Cart"):

                selected_item = next(
                    item
                    for item in cart
                    if item["name"] == selected_name
                )

                cart.remove(selected_item)

                st.success(
                    f"{selected_name} removed from cart!"
                )


    # -------------------------
    # 5. CHANGE CART QUANTITY
    # -------------------------

    elif buyer_option == "Increase/reduce quantity in cart":

        st.subheader("Change Cart Quantity")

        if len(cart) == 0:

            st.info("Your cart is empty.")

        else:

            cart_names = [
                item["name"]
                for item in cart
            ]

            selected_name = st.selectbox(
                "Which product do you want to change?",
                cart_names
            )

            selected_item = next(
                item
                for item in cart
                if item["name"] == selected_name
            )

            matching_product = next(
                product
                for product in products
                if product["name"] == selected_item["name"]
            )

            new_quantity = st.number_input(
                "Enter the new quantity",
                min_value=1,
                max_value=int(
                    matching_product["quantity"]
                ),
                value=int(
                    selected_item["quantity"]
                ),
                step=1
            )

            if st.button("Update Quantity"):

                selected_item["quantity"] = new_quantity

                st.success(
                    "Quantity updated successfully."
                )


    # -------------------------
    # 6. CHECKOUT
    # -------------------------

    elif buyer_option == "Checkout":

        st.subheader("Checkout")

        if len(cart) == 0:

            st.info("Your cart is empty.")

        else:

            total = sum(
                item["price"]
                * item["quantity"]
                for item in cart
            )

            st.write(
                f"Your total is "
                f"**₦{total:,.0f}**"
            )

            confirm = st.radio(
                "Do you want to checkout?",
                ["No", "Yes"]
            )

            if st.button("Confirm Purchase"):

                if confirm == "Yes":

                    for cart_item in cart:

                        for product in products:

                            if (
                                cart_item["name"]
                                == product["name"]
                            ):

                                product["quantity"] -= (
                                    cart_item["quantity"]
                                )

                        sales.append(
                            cart_item.copy()
                        )

                    st.success(
                        "🎉 Purchase successful!"
                    )

                    st.subheader(
                        "Your Purchase"
                    )

                    for cart_item in cart:

                        st.write(
                            f"{cart_item['name']} — "
                            f"{cart_item['quantity']} "
                            f"{cart_item['units']}"
                        )

                    st.write(
                        f"### Total: ₦{total:,.0f}"
                    )

                    cart.clear()

                else:

                    st.info(
                        "Checkout cancelled."
                    )