import datetime as dt
from unittest import case

catalog = {
    "Clothing": {
        "T-shirts": 50,
        "Jeans": 60,
        "Jackets": 35,
        "Hoodies": 45,
        "Dresses": 55,
        "Shorts": 30,
        "Socks": 10,
        "Underwear": 15
    },

    "Footwear": {
        "Sneakers": 80,
        "Running Shoes": 90,
        "Sandals": 35,
        "Boots": 120,
        "Flip-flops": 20,
        "Formal Shoes": 110
    },

    "Accessories": {
        "Backpacks": 40,
        "Handbags": 70,
        "Wallets": 25,
        "Belts": 20,
        "Sunglasses": 60,
        "Hats": 30
    },

    "Electronics": {
        "Smartphones": 800,
        "Headphones": 120,
        "Laptops": 1200,
        "Tablets": 600,
        "Smartwatches": 250,
        "Phone Cases": 15,
        "Chargers": 25
    },

    "Beauty": {
        "Perfume": 90,
        "Lipstick": 25,
        "Foundation": 35,
        "Shampoo": 20,
        "Conditioner": 20,
        "Face Cream": 40,
        "Nail Polish": 15
    },

    "Food": {
        "Burgers": 8,
        "Pizza Slices": 6,
        "Ice Cream": 5,
        "Coffee": 4,
        "Smoothies": 6,
        "Donuts": 3
    }
}
cart = {}
Checkout = {}




def full_catalog():
  print(" ")
  
  #LIST OF CATEGORIES
  catalog_categories = list(catalog.keys())

  # SHOW ALL CATEGORIES TO GO SHOP
  print("/"*30)
  print("These are the categories we have for you:")
  i = 1
  for category in catalog:
      print(f"{i}) {category}")
      i += 1

  #BROWSE INSIDE A CATEGORY
  while True:
    try:
        N = int(input("➡️  Enter the index of a category to browse its producs: "))
        N -= 1
        if 0 <= N < i:
          break
        else:
          print("Please enter a valid index for category")
    except ValueError:
      print("Please enter a number")
  
  #SHOW PRODUCTS OF A CATEGORY
  print(" ")
  selected_category = catalog_categories[N]
  print(f"These are the products for {selected_category}:")
  print("0) BACK TO MENU")
  
  i = 0
  for product, price in catalog[selected_category].items():
      print(f"{i+1}) {product}: ${price:.2f}")
      i += 1
  
  #LIST PRODUCTS OF CURRENT CATEGORY
  products_in_category = list((catalog[selected_category].keys()))


  #ADD PRODUCTS OR GO MENU
  print(f"""
A)Enter the index of a product to add it to your card
B)Enter \"0\" to return to the main menu""")
  
  while True:
    
    try:
      M = product_selected = int(input("➡️  type the index of the item: "))
      M -= 1

      if 0 <= M < i:
        #ADD PRODUCT TO CART
        cart[products_in_category[M]] = {"price": catalog[selected_category][products_in_category[M]]}

        #ASK FOR QUANTITY AND ADD IT TO CART
        N = int(input(f"➡️  ¿how many {products_in_category[M]}?: "))
        cart[products_in_category[M]]["#"] = N
        
        #FINAL MESSAGE
        print("✅ ¡succesfully added to cart!")
    
      #GO BACK TO MENU
      elif M == -1:
        print(" ")
        break
      
      else:
          print("Please enter a valid index")
    
    except ValueError:
      print("Please enter a number")

  









def cart_options():
  print(" ")
  print("/"*30)
  
  #SHOW PRODUCTS IN CART
  if not cart:
    print("⚠️  Your cart is empty. Please add some products first!")
    return
  
  else:
    print("This is your current cart:")

    i = 1
    for product, data in cart.items():
        print(f"{i}) {product}: ${data["price"]:.2f} x {data["#"]} ")
        i += 1
  

  #ASK FOR AN OPTION
  while True:
  
    print("/"*30)
    print(f"""These are the options you have to choose from:
1) Delete products
2) Change amount of a product
3) Show total price
4) GO BACK TO MENU""")
  
    N = int(input("➡️  Enter your option: "))
    
    match N:
      
      #DELETE PRODUCTS
      case 1:
        print("/"*30)
        
        i = len(cart)
        print("Enter 0 to go back")
        X = product_to_delete = int(input("➡️  Enter the index of the product you want to delete: "))
        if 0 < X <= i:
          del cart[list(cart.keys())[X-1]]
          print("✅ Product deleted successfully!")
        elif X == 0:
          pass
        else:
          print("Please enter a valid index for a product")
      
      #CHANGE AMOUNT OF A PRODUCT
      case 2:
        print("/"*30)

        i = len(cart)
        print("Enter 0 to go back")
        X = product_to_change = int(input("➡️  Enter the index of the product you want to change the amount: "))
        if 0 < X <= i:
          new_amount = int(input("➡️  Enter the new amount: "))
          cart[list(cart.keys())[X-1]]["#"] = new_amount
          print("✅ Amount changed successfully!")
        elif X == 0:
          pass
        else:
          print("Please enter a valid index for a product")
      
      #SHOW TOTAL PRICE
      case 3:
        print("/"*30)
        
        total_price = 0
        i = 0
        for product, data in cart.items():
          product_total = int(data["price"] * data["#"])
          #print(f"{i}) {product}: ${data["price"]:.2f} x {data["#"]} ")
          total_price += product_total
          i += 1
        print(f"The total price is: ${total_price}")
      
      #GO BACK TO MENU
      case 4:
        print(" ")
        break
      
      #ERROR MESSAGE
      case _:
        print("/"*30)
        print("Please enter a valid index for an option")









def checkout_options():
  print(" ")

  #SHOW PRODUCTS IN CART
  if not cart:
    print("/"*30)
    print("⚠️  Your cart is empty. Please add some products first!") 
    return

  #SHOW CHECKOUT
  else:
    print("/"*30)
    print("🧾 MY STORE INC. 🧾")
    print("     CHECKOUT     ")
    print(f"Date: {dt.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("-"*30)
    

    for product, data in cart.items():
        print(f"-{product}: ${data["price"]:.2f} x {data["#"]} ")
    print("-"*30)
 
    total_price = 0
    for product, data in cart.items():
      product_total = int(data["price"] * data["#"])
      #print(f"{i}) {product}: ${data["price"]:.2f} x {data["#"]} ")
      total_price += product_total  

    print(f"TOTAL CHECKOUT: ${total_price:.2f}")
    print("/"*30) 



  #FINAL MESSAGE
  print("""¿Do you want to finish this purchase?
1) YES, pay and go back
2) NO, come back to menu""")
    
  
  while True:
    try:
      choice = int(input("➡️  Enter your option: "))
      if choice == 1:
        print(f"\n🎉 ¡payment made! Thanks for your purchase and enjoy your products. 🎉")
        print("We hope to see you again soon!")
        cart.clear()
        print(" ")
        break
      
      elif choice == 2:
        print(" ") 
        break
        
      else:
        print("Invalid option, please enter 1 or 2")

    except ValueError:
      print("Please enter a number")










def menu():
    while True:
      print("/"*30)
      print(f"""HI! Welcome to my store  (👇 ﾟヮﾟ)👇 
  These are the options you have to choose from:

    1) 🛍️  Browse the catalog
    2) 🛒 View your cart
    3) 🧾 Checkout
    4) 🔙 Exit""")
    
    #ASK FOR AN OPTION
    
      try:
      
        option_selected = int(input("➡️  Enter the index of an option to continue: "))
      
        match option_selected:
            case 1:
              full_catalog()
            case 2:
              cart_options()
            case 3:
              checkout_options()
            case 4:
              print("Thanks for visiting us! See you soon!")
              return
            case _:
              print("Please enter a valid index for an option")
    
      except ValueError:
        print("Please enter a number")








def admin_menu():
    #ASK FOR AN OPTION
  while True:
    print(" ")
    print("/"*30)
    print(f"""These are the options you have to choose from:
1) Delete products
2) Change price of a product
3) Add a new product
4) GO BACK TO MENU""")
    
    while True:
      try:
        N = int(input("➡️  Enter your option: "))
        if 1 <= N <= 4:
          break
        else:
          print("Please enter a valid index for an option")
      except ValueError:
        print("Please enter a number")
    
    match N:
      
      #DELETE PRODUCTS
      case 1:
        print("/"*30)
        print("These are the categories we have in the catalog:")
        print("0) BACK TO MENU")
        i = 1
        for category in catalog:
            print(f"{i}) {category}")
            i += 1
        
        while True:
            try:
                N = int(input("➡️  Enter the index of a category to delete a product: "))
                match N:
                    case 0:
                        return
                    case _ if 0 < N < i:
                        selected_category = list(catalog.keys())[N-1]
                        break
                    case _:
                        print("Please enter a valid index for category")
            except ValueError:
                print("Please enter a valid index")
            

        
        print(f"These are the products for {selected_category}:")
        print("0) BACK TO MENU")
        i = 1
        for product, price in catalog[selected_category].items():
            print(f"{i}) {product}: ${price:.2f}")
            i += 1
        
        while True:
            try:
                N = int(input("➡️  Enter the index of a product to delete it: "))
                match N:
                    case 0:
                        return
                    case _ if 0 < N < i:
                        del catalog[selected_category][list(catalog[selected_category].keys())[N-1]]
                        print("✅ Product deleted successfully!")
                        continue
                    case _:
                        print("Please enter a valid index for category")
            except ValueError:
                print("Please enter a valid index")
    



      #CHANGE PRICE OF A PRODUCT
      case 2:
        print("/"*30)
        print("These are the categories we have in the catalog:")
        print("0) BACK TO MENU")
        i = 1
        for category in catalog:
            print(f"{i}) {category}")
            i += 1
        
        while True:
            try:
                N = int(input("➡️  Enter the index of a category to change the price of a product: "))
                match N:
                    case 0:
                        return
                    case _ if 0 < N < i:
                        selected_category = list(catalog.keys())[N-1]
                        break
                    case _:
                        print("Please enter a valid index for category")
            except ValueError:
                print("Please enter a valid index")
            

        
        print(f"These are the products for {selected_category}:")
        print("0) BACK TO MENU")
        i = 1
        for product, price in catalog[selected_category].items():
            print(f"{i}) {product}: ${price:.2f}")
            i += 1
        
        while True:
            try:
                N = int(input("➡️  Enter the index of a product to change its price: "))
                match N:
                    case 0:
                        return
                    case _ if 0 < N < i:
                        while True:
                            try:
                                new_price = float(input("➡️  Enter the new price: "))
                                catalog[selected_category][list(catalog[selected_category].keys())[N-1]] = new_price
                                print("✅ Product price changed successfully!")
                                break
                            except ValueError:
                                print("Please enter a valid price")
                    case _:
                        print("Please enter a valid index for category")
            except ValueError:
                print("Please enter a valid index")
            
            


      #ADD A NEW PRODUCT
      case 3:
        print("/"*30)
        print("These are the categories we have in the catalog:")
        print("0) BACK TO MENU")
        i = 1
        for category in catalog:
            print(f"{i}) {category}")
            i += 1
        
        while True:
            try:
                N = int(input("➡️  Enter the index of a category to add a product: "))
                match N:
                    case 0:
                        return
                    case _ if 0 < N < i:
                        selected_category = list(catalog.keys())[N-1]
                        break
                    case _:
                        print("Please enter a valid index for category")
            except ValueError:
                print("Please enter a valid index")
            
        
        print(f"These are the products for {selected_category}:")
        print("0) BACK TO MENU")
        i = 1
        for product, price in catalog[selected_category].items():
            print(f"{i}) {product}: ${price:.2f}")
            i += 1
        
        while True:
            Name_of_product = input("➡️  Enter the name of the product to add: ")
            match Name_of_product:
                case "0":
                    return
                case _ if Name_of_product not in catalog[selected_category].keys():
                    while True:
                        try:
                            price_of_product = float(input("➡️  Enter the price of the product to add: "))
                            match price_of_product:
                                case 0:
                                    return
                                case _ if price_of_product > 0:
                                    catalog[selected_category][Name_of_product] = price_of_product
                                    print("✅ Product added successfully!")
                                    break
                                case _:
                                    print("Please enter a valid price for the product")
                        except ValueError:
                            print("Please enter a valid price")
                            continue
                case _:
                    print("This product already exists in the category, try a different one or enter 0 to go back")
                    continue
            

      
      #GO BACK TO MENU
      case 4:
        print(" ")
        return
      
      #ERROR MESSAGE
      case _:
        print("/"*30)
        print("Please enter a valid index for an option")
    
