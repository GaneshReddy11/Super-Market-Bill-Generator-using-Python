from datetime import datetime

name = input("Enter your name:")
# lists of items
lists = """
Rice     Rs 20/kg
oil      Rs 80/ltr
salt     Rs 20/kg
sugar    Rs 40/kg
colgaate Rs 85/each
maggi    Rs 60/each
Boost    Rs 90/each
Brushes  Rs 120/set
paneer   Rs 110/kg
"""
# declaration
price = 0
pricelist = []
totalprice = 0
finalprice = 0
ilist = []
qlist = []
plist = []
# rates for items
items = {
    "rice": 20,
    "oil": 80,
    "salt": 20,
    "sugar": 40,
    "colgate": 85,
    "maggi": 60,
    "Boost": 90,
    "Brushes": 120,
    "paneer": 110,
}
option = 0
if option == 1:
    print(lists)
for i in range(len(items)):
    intp1 = int(input("if you want buy 1 or 2 for exit:"))
    if intp1 == 2:
        break
    if intp1 == 1:
        item = input("Enter your item:")
        quantity = int(input("Enter your quantity:"))
        if item in items.keys():
            price = quantity * (items[item])
            pricelist.append((item, quantity, items, price))
            totalprice += price
            ilist.append(item)
            qlist.append(quantity)
            plist.append(price)
            gst = (totalprice * 5) / 100
            finalamount = gst + totalprice
        else:
            print("sorry you entered item is not available")
    else:
        print("you entered wrong number")
    inp = input("can i bill the items yes or no:")
    if inp == "yes":
        pass
        if finalamount != 0:
            print(25 * "=", "Food supermarket", 25 * "=")
            print(25 * "", "Punjab", 25 * "")
            print("Name:", name, 30 * "", "Date:", datetime.now())
            print(75 * "-")
            print("sno", 8 * "", "items", 8 * "", "quantity", 3 * "", "price")
            for i in range(len(pricelist)):
                print(i, 8 * " ", 8 * " ", ilist[i], 3 * " ", qlist[i], plist[i])

            print(75 * "-")
            print(50 * "", "TotalAmount:", "Rs", totalprice)
            print("gst amount", 50 * " ", "Rs", gst)
            print(75 * "-")
            print(50 * "", "finalAmount:", "Rs", finalamount)
            print(75 * " ")
            print(50 * " ", "Thanks for visiting")
            print(75 * "-")
