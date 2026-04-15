
correct_pin = "1234"

while True:
    pin = input("Enter your PIN: ")

    if pin == correct_pin:
        print("Login Successful")
        break
    elif pin == "0000":
        print("Account Locked")
        break
    else:
        print("Incorrect PIN. Try again.")

roads = {"A": 1, "B": 0, "C": 1}  
last_green = None
total_cost = 0

def choose_road(roads, last_green):

    for road, traffic in roads.items():
        if traffic == 1 and road != last_green:
            return road
        
    for road, traffic in roads.items():
        if traffic == 0 and road != last_green:
            return road
    return None

while any(t == 1 for t in roads.values()):
    selected = choose_road(roads, last_green)
    print(f"GREEN -> Road {selected}")
    roads[selected] = 0  
    last_green = selected
    total_cost += 2

print("All roads cleared!")
print("Total Path Cost:", total_cost)
