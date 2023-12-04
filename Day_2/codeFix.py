cardvalue = "King"
suitOfcards = "Hearts"

chkCardValue = input("Enter card value: ").title()
chkCardSuit = input("Enter card suit: ").title()

# Add the condition to use the "and" operator to check card value & suit to users inputs
if (chkCardValue == cardvalue and chkCardSuit == suitOfcards):
# King == User Input      and   Hearts    == User Input  
    print("Winner!")
else:
    print("Try Again")