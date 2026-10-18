items = {
    "SDB":2,
    "SDO":2,
    "SDR":2,
    "SMK":5,
    "SKS":5,
    "CK":10,
    "SKB":10,
    "Un":10,
    "LA":20,
    "LD":20,
    "LS":20,
    "CP":25,
    "CS":15,
    "SC":10,
    "M":5
}

taxed_price = 0
note = ""
while True:
    item_k = input("Item keyword (S to stop):  ")
    if item_k in items:
        amount = int(input("Amount: "))
        taxed_price += items[item_k]*amount
        note += str(amount) + " " + item_k + ", "
    elif item_k=="S":
        print("Untaxed price: ", taxed_price/1.0975)
        print("Notes: ", note)
        break
    else:
        print("Invalid keyword")
