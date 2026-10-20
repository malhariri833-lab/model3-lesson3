def calclultechange(paid,price):
    change=paid-price 
    return change


snackprice=20
print("snack vending machine")
print("the price of this snack is ",snackprice)
print("acceptid coins are 1,5,10")
totalinsirtedcoins=0
coinsinsirted=0

while True:
    coin=int(input("insert coin 1 5 10 : "))
    if coin !=1 and coin!=5 and coin!=10 :
        print("invalid coins")
        continue
    totalinsirtedcoins += coin
    coinsinsirted +=1
    print("inserted ",coin,"total insirted so far ",totalinsirtedcoins)


    if totalinsirtedcoins>=snackprice:
        print("inoghf ")
        break
    

change_due = calclultechange(totalinsirtedcoins, snackprice)

print("Dispensing your snack...")



if change_due == 0:
    pass

else:
    print(f"Here is your change: {change_due} units")


print("\n===== PURCHASE SUMMARY =====")

print("Snack Price:", snackprice)

print("Coins Inserted:", coinsinsirted)

print("Total Paid:",totalinsirtedcoins )

print("Change Given:", change_due)

print("=============================")

print("Thanks for your purchase!")