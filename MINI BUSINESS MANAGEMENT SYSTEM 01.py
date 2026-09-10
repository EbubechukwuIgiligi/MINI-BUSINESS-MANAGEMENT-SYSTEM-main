print("welcome to the mini business management system.")

products = []
cart = []
sales = []
expenses = []

main_menu = True
business = True
shopping = True
while main_menu:
    while business:
        user = input("\nwho are you? seller or buyer: ").lower()
        if user == "seller":
            seller_menu = True
            while seller_menu:
                print("\nSELLER MENU: select an option: ")
                seller_options = int(input("1. add a new product \n2. update a product \n3. remove a product \n4. view current stock \n5. restock \n6. add expense  \n7. view sales/business summary \n8. return to main menu \n9. exit \n"))
                if seller_options == 1:
                    add_another_product = True
                    while add_another_product:
                        product_name = input("\nenter the product: ").lower()
                        cost_price = int(input("how much did you get this product for? ₦"))
                        price = int(input("enter the price: ₦"))
                        quantity_available = int(input("how many? "))
                        units = input("what are they measured in? ")
                        product = ({"name": product_name,
                                    "cost_price": cost_price,
                                    "price": price,
                                    "quantity": quantity_available,
                                    "units": units})
                        print("ADDED SUCCESSFULLY!")
                        products.append(product)
                        another_product = input("\ndo you want to add another product? y/n: ").lower()
                        if another_product == "n":
                            add_another_product = False
                    print("\n----------------------- \nCURRENT STOCK \n----------------------- ")
                    for item in products:
                        print(f"{item["name"]} - ₦{item["price"]} - {item["quantity"]} {item["units"]}")

                    return_to_menu = input("\ndo you want to return to the seller's menu? y/n: ").lower()

                    if return_to_menu == "n":
                        main_menu = False

                if seller_options == 2:
                    update = True
                    while update:
                        if len(products) == 0:
                            print("you have not added any product to stock.")
                            update = False
                        else:
                            print("which product do you want to update? ")
                            for number, item in enumerate(products, start = 1):
                                print(f"{number}. {item["name"]}")
                            to_update = int(input("enter the product number: "))
                            if to_update < 1 or to_update > len(products):
                                print("invalid product number. ")
                            else:
                                selected_product = products[to_update - 1]
                                update_choice = int(input("\nwhat do you want to update? \n1. Name \n2. cost price \n3. price \n4. quantity \n5. units \n"))
                                if update_choice < 1 or update_choice > 4:
                                    print("invalid choice")
                                if update_choice == 1:
                                    print(f"current name : {selected_product["name"]}")
                                    new_name = input("enter the new name: ")
                                    selected_product["name"] = new_name
                                    print("name updated successfully! ")
                                if update_choice == 2:
                                    print(f"current cost price: ₦{selected_product["cost_price"]} ")
                                    new_cost_price = int(input("enter the new cost price: ₦"))
                                    selected_product["cost_price"] = new_cost_price
                                    print("cost price updated successfully! ")
                                if update_choice == 3:
                                    print(f"current price: ₦{selected_product["price"]} ")
                                    new_price = int(input("enter the new price: ₦"))
                                    selected_product["price"] = new_price
                                    print(f"price updated successfully! \nNew price: ₦{selected_product["price"]}")
                                if update_choice == 4:
                                    print(f"current quantity: {selected_product["quantity"]} ")
                                    new_quantity = int(input("enter the new quantity: "))
                                    selected_product["quantity"] = new_quantity
                                    print(f"quantity updated successfully! \nNew quantity: {selected_product["quantity"]} {selected_product["units"]} ")
                                if update_choice == 5:
                                    print(f"current unit: {selected_product["units"]} ")
                                    new_unit = input("enter the unit: ")
                                    selected_product["units"] = new_unit
                                    print("unit updated successfully! ")
                            update_another_product = input("\ndo you want to update another product? y/n: ")
                            if update_another_product == "n":
                                update = False

                if seller_options == 3:
                    remove = True
                    while remove:
                        if len(products) == 0:
                            print("you have not added any product to stock.")
                            remove = False
                        else:
                            print("\nCURRENT STOCK")
                            for number, item in enumerate(products, start=1):
                                print(f"{number}. {item["name"]}")
                            to_remove = int(input("enter the product number you want to remove: "))
                            if to_remove < 1 or to_remove > len(products):
                                print("invalid choice.")
                            else:
                                selected_product = products[to_remove - 1]
                                confirmation = input(f"\nare you sure you want to remove {selected_product["name"]}? y/n: ").lower()
                                if confirmation == "y":
                                    to_remove = products.pop(to_remove - 1)
                                    print(f"{to_remove["name"]} removed from products! ")
                                else:
                                    print("REMOVAL FAILED!")
                            remove_another_product = input("\ndo you want to remove another product? y/n: ").lower()
                            if remove_another_product == "n":
                                remove = False

                if seller_options == 4:
                    if len(products) == 0:
                        print("stock is empty.")
                    else:
                        print("\nYOUR CURRENT STOCK")
                        for number, item in enumerate(products, start=1):
                            print(f"{number}. {item["name"]} - ₦{item["price"]} - {item["quantity"]} {item["units"]}")
                            if item["quantity"] == 0:
                                print(f"⚠️⚠️ OUT OF STOCK! {item["name"]} is finished. ")
                            elif item["quantity"] <= 2:
                                print(f"⚠️⚠️LOW STOCK! only {item["quantity"]}{item["units"]} left.")
                        return_to_sellers_menu = input("\ndo you want to return to sellers menu? y/n: ")
                        if return_to_sellers_menu == "n":
                            seller_menu = False

                if seller_options == 5:
                    restock = True
                    while restock:
                        if len(products) == 0:
                            print("stock is empty.")
                            restock = False
                        else:
                            product_for_restock = input("\nwhich product do you want to restock? Name: ").lower()
                            product_found = False
                            for product in products:
                                if product["name"] == product_for_restock:
                                    product_found = True
                                    print(f"current stock: {product["quantity"]} {product["units"]}")
                                    restock_quantity = int(input("how many do you want to restock? "))
                                    product["quantity"] += restock_quantity
                                    print(f"RESTOCK SUCCESSFUL! current stock: {product["quantity"]} {product["units"]} ")
                                    restock_another_product = input("\ndo you want to restock another product? y/n: ").lower()
                                    if restock_another_product == "n":
                                        restock = False
                            if not product_found:
                                print("that product is not available. ")
                                go_back = input("do you want to return to seller's menu? y/n: ").lower()
                                if go_back == "y":
                                    restock = False


                if seller_options == 6:
                    expense = True
                    while expense:
                        expense_name = input("what is the expense for? ").lower()
                        expense_amount = int(input("what is the cost? ₦"))
                        expenses.append({"name": expense_name, "amount": expense_amount})
                        print("expense recorded successfully! ")
                        another_expense = input("\ndo you want to add another expense? y/n: ")
                        if another_expense == "n":
                            expense = False

                if seller_options == 7:
                    print("\nSALES SUMMARY \n")
                    if len(sales) == 0:
                        print("no sales yet.")
                    else:
                        total_sales = 0
                        total_profit = 0
                        total_expenses = 0
                        for sale in sales:
                            print(f"{sale["name"]} - {sale["quantity"]} {sale["units"]}")
                            total_sales += sale["price"]*sale["quantity"]
                            total_profit += (sale["price"] - sale["cost_price"])*sale["quantity"]
                        print(f"\n_____________\nTotal sales: ₦{total_sales}")
                        print(f"\n_____________\nTotal profit: ₦{total_profit} ")
                        print("\n YOUR EXPENSES")
                        for expense in expenses:
                            print(f"{expense["name"]} - {expense["amount"]}")
                            total_expenses += expense["amount"]
                        print(f"\n_____________\nTotal expenses: ₦{total_expenses}")
                        net_profit = total_profit - total_expenses
                        print(f"\nNet profit: ₦{net_profit}")

                if seller_options == 8:
                    seller_menu = False

                if seller_options == 9:
                    print("GOODBYE!")
                    business = False
                    seller_menu = False
                    main_menu = False

                if seller_options > 9:
                    print("INVALID INPUT")




        if user == "buyer":
            buyer_menu = True
            while buyer_menu:
                print("\nBUYER MENU: kindly go through our menu and select an option: ")
                buyer_options = int(input("1. view available products \n2. add to cart \n3. view cart \n4. remove from cart \n5. increase/reduce quantity in cart \n6. checkout \n7. return to main menu \n8. exit \n"))

                if buyer_options == 1:
                    if len(products) == 0:
                        print("there are no products available")
                    else:
                        print("\nAVAILABLE PRODUCTS")
                        for number, item in enumerate(products, start = 1):
                            print(f"{number}. {item["name"]} - ₦{item["price"]} - {item["quantity"]} {item["units"]}")

                if buyer_options == 2:
                    shopping = True
                    while shopping:
                        if len(products) == 0:
                            print("there are no products available")
                            shopping = False
                        else:
                            product_choice = int(input("\nenter the product number: "))
                            if product_choice < 1 or product_choice > len(products):
                                print("invalid product number. ")
                            else:
                                selected_product = products[product_choice - 1]
                                print(f"you selected: {selected_product["name"]} - ₦{selected_product["price"]} - {selected_product["quantity"]} {selected_product["units"]}")
                                purchase_quantity = int(input("\nhow many do you want? "))
                                if purchase_quantity > selected_product["quantity"]:
                                    print(f"sorry, we only have {selected_product["quantity"]} available. ")
                                    break
                                cart.append({"name": selected_product["name"], "cost_price": selected_product["cost_price"], "price": selected_product["price"],
                                             "quantity": purchase_quantity, "units": selected_product["units"]})
                                print("product added to cart!")
                                add_another_product_to_cart = input("\ndo you want to add another product to cart? y/n: ").lower()
                                if add_another_product_to_cart == "n":
                                    shopping = False

                if buyer_options == 3:
                    if len(cart) == 0:
                        print("you haven't added anything to cart.")
                    else:
                        print("\n YOUR CART")
                        total = 0
                        for number, buyers_cart in enumerate(cart, start = 1):
                            print(f"{number}. {buyers_cart["name"]} - ₦{buyers_cart["price"]} - {buyers_cart["quantity"]} {buyers_cart["units"]}")
                            total += buyers_cart["price"] * buyers_cart["quantity"]
                        print(f"Total: ₦{total} ")

                if buyer_options == 4:
                    if len(cart) == 0:
                        print("your cart is empty.")
                    else:
                        print("\n YOUR CART")
                        for number, buyers_cart in enumerate(cart, start = 1):
                            print(f"{number}. {buyers_cart["name"]} - ₦{buyers_cart["price"]} - {buyers_cart["quantity"]} {buyers_cart["units"]}")
                        removed_product = int(input("\nenter the number of product you want to remove: "))
                        if removed_product < 1 or removed_product > len(cart):
                            print("\nInvalid product number!")
                        else:
                            removed_product = cart.pop(removed_product - 1)
                            print(f"{removed_product["name"]} removed from cart! ")

                if buyer_options == 5:
                    changing_quantity = True
                    while changing_quantity:
                        if len(cart) == 0:
                            print("your cart is empty")
                            changing_quantity = False
                        else:
                            for number, item in enumerate(cart, start = 1):
                                print(f"{number}. {item["name"]} - {item["quantity"]} {item["units"]}")
                            cart_choice = int(input("\nwhich product do you want to change? "))
                            if cart_choice < 1 or cart_choice > len(cart):
                                print("invalid choice! ")
                            else:
                                selected_item = cart[cart_choice - 1]
                                new_quantity = int(input("enter the new quantity you want: "))
                                if new_quantity < 1:
                                    print("quantity must be at least 1.")
                                else:
                                    for product in products:
                                        if product["name"] == selected_item["name"]:
                                            if new_quantity > product["quantity"]:
                                                print(f"only {product["quantity"]} {product["units"]} available.")
                                            else:
                                                selected_item["quantity"] = new_quantity
                                                print("quantity updated successfully.")
                            change_another_product = input("do you want to change the quantity of another product? y/n: ")
                            if change_another_product == "n":
                                changing_quantity = False

                if buyer_options == 6:
                    if len(cart) == 0:
                        print("your cart is empty.")
                    else:
                        confirm = input("\ndo you want to checkout? y/n: ").lower()
                        if confirm == "y":
                            for cart_item in cart:
                                for product in products:
                                    if cart_item["name"] == product["name"]:
                                        product["quantity"] -= cart_item["quantity"]
                                sales.append(cart_item)
                            print("purchase successful! ")
                            total = 0
                            print("\n YOUR PURCHASE")
                            for cart_item in cart:
                                print(f"{cart_item["name"]} - {cart_item["quantity"]} {cart_item["units"]}")
                                total += cart_item["price"] * cart_item["quantity"]
                            print(f"Total: ₦{total}")
                            cart.clear()

                if buyer_options == 7:
                    buyer_menu = False

                if buyer_options == 8:
                    print("GOODBYE! thanks for shopping with us.")
                    buyer_menu = False
                    main_menu = False

                if buyer_options > 8:
                    print("INVALID INPUT")
