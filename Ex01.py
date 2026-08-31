import random
games = ['Tiger','Glouk','Rooster','Prawn','Crab','Fish']
rom = []
for i in range(3):
    chooses = random.choice(games)
    rom.append(chooses) 

price = 100
while True:
    print("===== KHLA KHLOUK GAME HOMEWORK =====")
    print("")
    print(f"You have {price} points:")
    print('''
+------------+------------+-------------+
|   1. Tiger |  2. Glouk  |  3. Rooster |
+------------+------------+-------------+
|   4. Prawn |  5. Crab   |  6. Fish    |
+------------+------------+-------------+
    ''')
    choose = input("Choose 1-6: ")
    match(choose):
        case "1": choose = "Tiger"
        case "2": choose =  "Glouk"
        case "3": choose =  "Rooster"
        case "4": choose =  "Prawn"
        case "5": choose =  "Crab"
        case "6": choose =  "Fish"
    count = 0
    if choose in rom:
        count = rom.count(choose)
    point = int(input(f"Enter points to bet (you have {price}): "))
    print(f"You bet {choose} for {point} points")
    print("")
    print("Rolling...")
    print(f'''
    =============================================
        Results: {rom}
    =============================================
            {choose} appeared {count} time(s)
    ''')
    if choose in rom and count:
            price += (point*count)
            print(f"You win {point} points")
            print(f"Correct Points: {price}")
    else:
        price -= point
        print(f"You lost {point} points")
        print(f"Correct Points: {price}")
    cxit = input("Play again? (y/n): ")
    if cxit == "y" and price > 0:
         continue
    elif cxit == "y" and price == 0:  
        print("")
        print("Game Over")
        print("Because you lost all point",price)
        break
    else:
        print("")
        print("Game Over")
        print("Final Points: ",price)
        break