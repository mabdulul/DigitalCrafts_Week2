bill = float(input("Give me the bill amount? "))
service_level = input(" How would like the service? (Good, fair, or bad) ")
tip = ""

if service_level.upper() == "GOOD":
     tip = .20 * bill 
     print("Tip amount: %.2f " % tip )
elif service_level.upper() == "FAIR":
     tip = .15 * bill 
     print("Tip amount: %.2f "% tip)
elif service_level.upper() == "Bad":
     tip = .10 * bill 
     print("Tip amount: %.2f " % tip)
else:
    ("Something went wrong")

