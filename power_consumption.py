#Function to calculate Power Consumption
#units = 0
def calculateBill(units):

    if (units >=1 and units<=50):               #units 1 to 50 rate 3
        return units * 3
    
    elif (units >=51 and units<=100):           #units 51 to 100 rate 6
        return((50 * 3)+(units - 50)*6)         #first 50 units mul by 3 and add with other remain units
    
    elif (units >=101 and units<=150):          #units 101 to 150 rate 9
        return ((50 * 3)+(50 * 6)+(units - 100)*9) #mul and add previously units and sub prev unit from units i.e 100 and then mul with 9

    
    elif (units >=151 and units<=200):
        return ((50 * 3)+(50 * 6)+(50 * 9)+(units - 150)*12)

    
    elif (units >=201):
        return ((50 * 3)+(50 * 6)+(50 * 9)+(50 * 12)+(units - 200)*15)
    return 0

units = int(input("Enter Units Consumed : "))       #enter consumed units
print("Bill Ammount : ",calculateBill(units))       #Total Bill ammount