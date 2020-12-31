pur_amt = int(input("Enter the sale ammount: ")) 
discount = 0                                #initial discount is 0
if (pur_amt>0):
    if pur_amt<=100 and pur_amt<=1000:      #discount in between 100 to 1000, no discount
        discount = print(pur_amt)
    
    elif pur_amt> 1000 and pur_amt<=2000:   #discount in between 1000 to 2000 is 10%
        discount = pur_amt * 0.10
    
    elif pur_amt>2000 and pur_amt<=3000:    #discount in between 2000 to 3000 is 20%
        discount = pur_amt * 0.20

    elif pur_amt>3000:                      #25% discount above 3000 
        discount = pur_amt * 0.25

    print("Purchase Ammount : ", pur_amt)   #purchase ammount
    print("Discount   : ", discount)        #given discount 
    print("Total Bill : ", pur_amt - discount)  # final bill ammount

else:
    print('Invalid Ammount')