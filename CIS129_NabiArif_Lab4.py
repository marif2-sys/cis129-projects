def main():
    # Step 1: Declare local variables
    monthlySales = getSales("Enter the monthly sales amount: ")
    storeAmount = calcStoreBonus(monthlySales)
    salesIncrease = getIncrease("Enter the percent of sales increase (in %): ")
    empAmount = calcEmpBonus(salesIncrease)
    
    # Step 6: Print the bonuses
    printBonus(storeAmount, empAmount)

# Step 2: This function gets the monthly sales
def getSales(prompt):
    monthlySales = float(input(prompt))
    return monthlySales

# Step 3: This function determines the storeAmount bonus
def calcStoreBonus(monthlySales):
    if monthlySales >= 110000:
        storeAmount = 6000
    elif monthlySales >= 100000:
        storeAmount = 5000
    elif monthlySales >= 90000:
        storeAmount = 4000
    elif monthlySales >= 80000:
        storeAmount = 3000
    else:
        storeAmount = 0
    return storeAmount

# Step 4: This function gets the percent of increase in sales
def getIncrease(prompt):
    salesIncrease = float(input(prompt))
    salesIncrease = salesIncrease / 100
    return salesIncrease

# Step 5: This function determines the empAmount bonus
def calcEmpBonus(salesIncrease):
    if salesIncrease >= 0.05:
        empAmount = 75
    elif salesIncrease >= 0.04:
        empAmount = 50
    elif salesIncrease >= 0.03:
        empAmount = 40
    else:
        empAmount = 0
    return empAmount

# Step 6: This function prints the bonus information
def printBonus(storeAmount, empAmount):
    print("The store bonus amount is $", storeAmount)
    print("The employee bonus amount is $", empAmount)
    if (storeAmount == 6000) and (empAmount == 75):
        print('Congrats! You have reached the highest bonus amounts possible!')

# Call the main function to run the program
if __name__ == "__main__":
    main()
