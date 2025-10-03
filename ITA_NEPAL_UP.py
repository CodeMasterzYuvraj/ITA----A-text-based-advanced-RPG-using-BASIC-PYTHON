import random
import time

print("Do you want to live The begining: type 'y'")
ask_for_begining = input(": ")
if ask_for_begining == 'y': import The_begining
time.sleep(1)
print("....")
time.sleep(2)

name = input("Enter your name: ")

print("\nEntering RPG Simulation #2725vj7_ITA\n")
print(".....")
time.sleep(1)
print("....")
time.sleep(2)
print("...")

print("**************************************** GAME HELP CENTER AND BASIC KNOWLEDGE***********************************")
print(f"-->{name} Explore nepal and UP\ntype 'w','a','s','d' to move\n'bag' to see items, ammos, kills, tools\n'i' to interact and 'map' for nearest bar,A.stn.,training camps and more\n'e' to enter permises\n't' to teleport to any bar across.\n'g' to give money | 'pay' to pay |Other commands will be places specific.")

print("-->DON owns the ammo houses and he is very impatient and inhumane..")
print("Watch you tongue before him or else it may be cut in half!!!")

print("-->THE MOST POWERFUL WEAP{}N of GAME IS '''AK_47'''")
print("This luxury though may cost you some fortune")

print("-->Labs and Training centers are not gang owned and are private centers.")
print("They may not use any slang and be work specific and to dot about entries and transactions.")

print("-->Interactive panel--> health|cash...(x,y)| PLACE| NPC name: ")

print("-->UP has a more aggressive population and you may find yourself held by anyone, anywhere!!")
print("UP gangsters are rich but most of them are well trained, aggressive and carry stronger weapons.\n")
print("X < 7 is all NEPAL and X >= 7 is all UP")
print("********************************************TAKE TIME TO READ******************************************************")
time.sleep(8)
print("\n\n\n\nMOTIVE OF ITA: YOU HAVE TO BE ONE WITH BEST POSSIBLE GEARS IN GAME and 50000 or more in hand")
print("rise from 0 cash to owning AKs and some good old dodges, becoming the invincible in TOWNS\n\n")
time.sleep(5)

valid_moves = ["e", "w", "a", "s", "d", "bag", "map", "i",'t']
msg = 0

# Can edit and add dialoges 1, 2, 3
dialog1 = ["Ye goli CHALegi nhi MAARegi...", "Abe CHHOTU chai toh laa.", "Violence! Violence! Violence.. I like violence", "Violence, Violence, Violence, I don't like violence, I avoid but violence likes money and I can't avoid it honey.", "Aisa MAAROONGA ki shakal bigadjayegi.", "HEY! give me some CASH.", "I just beat DON! and now I will kill you.","nikaal jaldi paise, mujhse bhaage ga kaise","Bonjour donne-moi de l'argent!!"]
dialog2 = [f"Tu toh gya thaakur..", "I guess you know DON, I have just beaten him..", "Another day, Another newbie", "I am trying hard not to laugh!", "You met a wrong guy!", "I guess today you are my food", "Even DON can't scare me, who are you to try!"]
dialog3 = ["Will just pay money to you rather than to hospitals..", "sorry sorry , Take the money but leave me", "As you say sir..", "I owe you", "Life >>>> Money", "Will always remember that you let me go..", f"I lost today but I will come back strong", "Remember my name! {name}. I will meet you soon."]


x = 0
y = 0

health = 600
cash = 2000
dodge = 0  # dodge chances +20% till 60% by going to gang training centers (2)
teleport_tool = 0
teleport = ["Locked", "Unlocked"]
items = ["m"]  # a, d, k, s
ammo_stock = [0, 0]  # d, k
total_kills = 0
# w,a, s,d  b--buy    i--interact  f - fire
np = ["a", "d", "m", "k", "k", "d", "k", "s", "m", "m","s", "d", "d", "k", "m", "d", "s", "k", "s", "s", "d", "m", "m"]  # can exchange or edit any value
cash_ask = [5000, int(cash/5), int(cash/2), int(cash/3), 1000, 1000, int(cash/3), int(cash/4), int(cash), 500, 500, 500]  # can exchange or edit any value
xup = 7

npc_cashlist = [500, 1000, cash/3, cash/2, cash, cash, cash/3, 500, 1000, 10000, 10000, cash, 5000, 5000, cash/2]  # can exchange or edit any value


ammunation_items = ["m", "k", "s", "d", "a"]
full_forms = ["melee","knife", "sword", "desi katta", "AK-47"]
ammos = [750, 2500]  # d,k, can edit here and change rate in ammu nation's menu
damage = [20, 60, 90, 120, 200]  # m,k, s, d, a
weapon_price = [1000, 4500, 12000, 40000]

npc_chance_outof10_np = [1, 2, 0, 1, 2, 3, 1, 3, 2, 0]
npc_chance_outof10_up = [1, 1, 3, 1, 3, 2, 1, 3, 3, 3]

npc_names = ["Rao Saab", "Raka", "Boom Boom","Rowdy","Sam Saibo","Sanju Lemon","Sasta Don","Bahu Bahadur","Pungi Singh","Palti Shukla","Sonu Kheni","Moga","Gaama"
    ,"Vimal", "Topi Kapoor","Gunpowder Singh","Jolie Kills","Dolly Chapri","Singham","Chaapman","Nigga Kumar"]

bars = [[4, 0], [5, 3], [3, 5], [6, 7], [1, 8], [7,6], [8, 10], [9, 8], [10, 0], [8, 3]]
ammo_houses = [[1, 5], [3, 7], [6, 2], [1, 10], [7, 3], [8, 9], [9, 0], [10, 10], [8, 2]]
training_center = [[4, 4], [8, 8]]
labs = [[9,9], [7,7]]



def ammo_house():
    demand = ""
    bill = 0
    print(f"\t\t\t\t\t\t\t\t\t\t\t\t\t{name} swaagat hai aapka illegal bhandaar mein... \n\t\t\t\t\t\t\t\t\t\t\t\t\t"
          f"Yaahan mazaak kiya toh pitte jaonge")
    time.sleep(1)
    print("\t\t\t\t\t\tDon says: ", ["jaldi varna police ajayegi", "desi katta yaa anrezi AK",
                                     "khoon bhi milega aur khooni bhi", "chaaku bhi hai talwaar bhi"
        , "gang se ho kya"][random.randint(0,4)])
    time.sleep(1)

    print(f"\t\t\t\t\t\t\t\t\t\t\t\t\tmenu:[60] knife(k) - 1000\n"
          f"\t\t\t\t\t\t\t\t\t\t\t\t\t[90] sword(s) - 4500\n\t\t\t\t\t\t\t\t\t\t\t\t\t[120] desi katta(d) - 12000, 5 bullets : 750"
          f"\n\t\t\t\t\t\t\t\t\t\t\t\t\t[200] AK 47 (a) - 40000, 5 bullets : 2500\n\t\t\t\t\t\t\t\t\t\t\t\t\t"
          f"if only ammo type - ammo\n\t\t\t\t\t\t\t\t\t\t\t\t\tdookaan se nikalne ke liye - checkout")

    while demand.lower() != "checkout":
        demand = input("\t\t\t\t\t\t\t\t\t\t\t\t\t: ").lower()
        if demand in ammunation_items and demand not in items:
            price = weapon_price[ammunation_items.index(demand)-1]
            bill += price
            items.append(demand)
            if demand == 'a':
                time.sleep(1)
                print("You bought the OG AK-47")
                print("The beast is with you with damage of")
                time.sleep(2)
                print("....\n")
                print("200 hp per bullet that may cost around 500 each")
            print(f"\t\t\t\t\t\tAdded in cart:  {full_forms[ammunation_items.index(demand)]}")
        elif demand == "ammo":
            print("\t\t\t\t\t\t\t\t\t\t\t\t\td or a")
            dem_ammo = input("\t\t\t\t\t\t\t\t\t\t\t\t\t: ")
            print("\t\t\t\t\t\t\t\t\t\t\t\t\tHow many sets of 5 ammos ?")

            while True:
                try:
                    dem_q = int(input("\t\t\t\t\t\t\t\t\t\t\t\t\t: "))
                    break
                except ValueError:
                    print("\t\t\t\t\t\t\t\t\t\t\t\t\tPlease enter a valid number.")

            if dem_ammo == "d":
                ammo_stock[0] += 5*dem_q
                bill += dem_q*ammos[0]
                print(f"\t\t\t\t\t\tAddded in cart: {5*dem_q} {full_forms[ammunation_items.index(dem_ammo)]} ammos")
            elif dem_ammo == "a":
                ammo_stock[1] += 5*dem_q
                bill += dem_q*ammos[1]
                print(f"\t\t\t\t\t\tAddded in cart: {5*dem_q} {full_forms[ammunation_items.index(dem_ammo)]} ammos")
            else: bill += 999999
        elif demand in items:
            print("\t\t\t\t\t\tDon says: Bro you already have one !!")
        else:
            if demand != "checkout":
                bill += 999999
    global cash
    if cash - bill < 0:
        time.sleep(3)
        print(f"\t\t\t\t\t\tDon says: Koi toh jhol kiya hai tune {name}, mera time barbaad kaise kiya !!!!!"
              f"\n\t\t\t\t\t\tabb tu gya")
        time.sleep(5)
        print("YOU HAVE BEEN CHAIN SAWED IN HALF !!")
        global health
        health = 0
    else:
        cash = cash - bill
        print(f"\t\t\t\t\t\t\t\t\t\t\t\t\t Thanks for shopping {name}, cart cleared of rs {bill}")




def smart_map(xx, yy):
    bar_check = [99999999, 10]
    for i in bars:
        x_diff = xx - i[0]
        y_diff = yy -i[1]
        square = (x_diff*x_diff) + (y_diff*y_diff)
        if square < bar_check[0]:
            bar_check[0] = square
            bar_check[1] = i
    ammo_check = [99999999, 10]
    for i in ammo_houses:
        x_diff = xx - i[0]
        y_diff = yy -i[1]
        square = (x_diff*x_diff) + (y_diff*y_diff)
        if square < ammo_check[0]:
            ammo_check[0] = square
            ammo_check[1] = i
    lab_check = [99999999, 10]
    for i in labs:
        x_diff = xx - i[0]
        y_diff = yy -i[1]
        square = (x_diff*x_diff) + (y_diff*y_diff)
        if square < lab_check[0]:
            lab_check[0] = square
            lab_check[1] = i
    training_check = [99999999, 10]
    for i in training_center:
        x_diff = xx - i[0]
        y_diff = yy -i[1]
        square = (x_diff*x_diff) + (y_diff*y_diff)
        if square < training_check[0]:
            training_check[0] = square
            training_check[1] = i
    print(f"\t\t\t\t\t\tNearest bar at {bar_check[1]} |  Nearest ammo station at {ammo_check[1]}\n\t\t\t\t\t\t"
          f"Nearest training center at {training_check[1]} | Nearest lab at {lab_check[1]}")




def inbar():
    while True:
        try:
            askfh = int(input("\t\t\t\t\t\t\t\t\t\t\t\t\tfull(1200)/half(600) or any money for equivalent gain | BUDGET: "))
            break
        except ValueError:
            print("Please enter a valid number.")

    global cash, health
    if health < 600 and cash >= askfh:
        if askfh > 1200:
            print("\n\t\t\t\t\t\t\t\t\t\t\t\t\tThanks for supplying extra sums!")
            print("\t\t\t\t\t\t\t\t\t\t\t\t\tWe can use this extra as funds to cure poor in town!!  -health team")
            a3 = input("\t\t\t\t\t\t\t\t\t\t\t\t\tYou can have it back by typing anything except donate: 'donate' : ").lower()
            if a3 != 'donate': askfh = 1200
            else: print(f"\t\t\t\t\t\t\t\t\t\t\t\t\tYou are a good man. Thanks for donating {askfh-1200}!!\n")
        health_gained = int((askfh/1200)*600)
        cash -= askfh
        health += health_gained
        if health >600:
            health_gained -= health - 600
            health = 600
        print(f"\t\t\t\t\t\t\t\t\t\t\t\t\tGained {health_gained} hp!")
    else: print("\t\t\t\t\t\t\t\t\t\t\t\t\tservice failed! retry!")


change_npcname = 1
npc_individual_name = "none"
npc_status = 0
npc_cash = 0
enemy_health = [200, 200, 300, 600 , 500, 300, 300, 200, 100, 100, 300, 400, 500, 300, 600, 200, 100, 100, 100, 500, 500, 600, 400]



def fight(weapon, cash_player, cash_npc):  # cash_player is demanded by npc, cash_npc is demanded by player
    dodge_npc = [0 ,0 ,20 ,20 ,40 ,20, 10, 20, 30, 0, 40, 0, 20, 20, 20, 10, 0]
    global cash, health, ammo_stock, items, total_kills, npc_individual_name, npc_status, dodge, change_npcname, x
    if x >= 7:
        dodge_npc = [10, 40, 40, 40, 40, 40, 50, 50, 60, 20, 20, 20, 40, 50, 40, 60, 20, 30, 10]
        cash_npc += 5000

    demand_original = 0
    healthe_original = 0
    dodgee = dodge_npc[random.randint(0,len(dodge_npc)-1)]
    healthe = enemy_health[random.randint(0,len(enemy_health)-1)]
    demand = cash_player

    print(f"\t\t\t\t\t\tEnemy --> {healthe}hp|{dodgee}% dodge|weapon-{full_forms[ammunation_items.index(weapon)]}[{damage[ammunation_items.index(weapon)]}]|demand-{cash_player}")
    print(f"\t\t\t\t\t\tYou --> {health}hp|{dodge}% dodge|demand-{cash_npc}\n")

    conclusion = 0
    weapon_damage = damage[ammunation_items.index(weapon)]
    healthe_original += healthe
    demand_original += demand
    if demand == 0: demand += 9999999
    while conclusion == 0:
        sk = ''
        kk = ''
        if 's' in items: sk = ' s'
        if 'k' in items: kk = ' k'
        dk = ""
        ak = ""
        if 'd' in items: dk = f' d({ammo_stock[0]})'
        if 'a' in items: ak = f' a({ammo_stock[1]})'

        ask = input(f"\t\t\t\t\t\tME-{health}|{cash}..ENEMY-{healthe}|current_demand-{demand}-> give(g) | attack -> m{kk}{sk}{dk}{ak}: ")
        damage_to_give = 0
        if ask in items or ask == 'g':
            if ask in ['m', 'k', 's']:
                damage_to_give = damage[ammunation_items.index(ask)]
            elif ask == 'd':
                if ammo_stock[0] > 0:
                    ammo_stock[0] -= 1
                    damage_to_give = damage[ammunation_items.index(ask)]
                else: print(f"\t\t\t\t\t\tAmmo of {ammunation_items.index(ask)} is 0!!")
            elif ask == 'a':
                if ammo_stock[1] > 0:
                    ammo_stock[1]-=1
                    damage_to_give = damage[ammunation_items.index(ask)]
                else: print(f"\t\t\t\t\t\tAmmo of {ammunation_items.index(ask)} is 0!!")
            elif ask == 'g':
                if cash >= demand:
                    cash -= demand
                    print(f"\n\t\t\t\t\t\tSuccessfully paid rs {demand} to {npc_individual_name}\n\t\t\t\t\t\tI LOST\n")
                    conclusion = 1
                    break
                else: print(f"\t\t\t\t\t\tyou have {demand-cash} ruppees less!!")
        else: print("\t\t\t\t\t\tYou fumbled and chose a wrong move !!")
        dnp = random.randint(1,100)
        dne = random.randint(1,100)

        final_player_damage = 0
        final_npc_damage = 0
        if dnp > dodge: final_player_damage = weapon_damage
        else: print("\t\t\t\t\t\tYou dodged successfully")
        if dne >= dodgee: final_npc_damage = damage_to_give
        else: print("\t\t\t\t\t\tEnemy dodged successfully")

        health -= final_player_damage
        healthe -= final_npc_damage
        demand = int((healthe/healthe_original) * demand_original)

        if health <= 0:
            print(f"{name} was KILLED by {npc_individual_name}\n")
            conclusion = 1
        elif healthe <= 0:
            print(f"\t\t\t\t\t\t{npc_individual_name} was KILLED by {name}\n")
            conclusion = 1
            total_kills += 1
            cash += cash_npc
        else: print(f"\t\t\t\t\t\tYouLost-{final_player_damage}hp | enemyLost-{final_npc_damage}hp")
    npc_status = 0
    npc_individual_name = "none"
    change_npcname = 0





while health > 0:

    npc_cashlist = [500, 1000, int(cash/3), int(cash/2), cash, cash, int(cash/3), 500, 1000, 10000, 10000, cash, 5000, 5000, int(cash/2)]
    if change_npcname == 1:
        if x < 7: npc_status = (npc_chance_outof10_np)[random.randint(0,9)]
        if x >= 7:  npc_status = (npc_chance_outof10_up)[random.randint(0,9)]
        if npc_status==0: npc_individual_name = "none"
        if npc_status != 0:
            npc_individual_name = npc_names[random.randint(0, 20)]
            npc_cash = npc_cashlist[random.randint(0,len(npc_cashlist)-1)]

    current_permises = ""
    if [x,y] in labs: current_permises = "LABS"
    elif [x,y] in bars: current_permises = "BAR"
    elif [x,y] in ammo_houses: current_permises = "AMMOSTN."
    elif [x,y] in training_center: current_permises = "TRAININGCENTER"
    else:
        if x>=7: current_permises="UP"
        if x>=0 and x<7: current_permises="NEPAL"

    move = input(f"{health}|{cash}..({x},{y}): {current_permises}: {npc_individual_name}: ").lower()
    if move not in valid_moves:
        print("Unknown move")

    if move ==  "w": y+= 1
    elif move == "s": y-=1
    elif move == "d": x+=1
    elif move == "a": x-=1
    elif move == "bag":
        print(f"\t\t\t\t\t\titems = {items}\n\t\t\t\t\t\tammos of desi katta, AK is {ammo_stock}\n\t\t\t\t\t\ttotal "
              f"kills is {total_kills}\n\t\t\t\t\t\tdodge skills(%) = {dodge}  |  teleport = {teleport[teleport_tool]}")
    elif move == "map":
        smart_map(x, y)

    elif move == "e":
        if [x,y] in ammo_houses:
            ammo_house()

        elif [x,y] in bars:
            inbar()

        elif [x,y] in training_center and dodge < 60:
            print("\t\t\t\t\t\t\t\t\t\t\t\t\tpay fees 10000 and choose from A B C D, bot will select any one and you "
                  "will get admission "
                  "\n\t\t\t\t\t\t\t\t\t\t\t\t\tWhat can I do the seats are less!!")
            pay1 = input(f"\t\t\t\t\t\t\t\t\t\t\t\t\tcash avail {cash}: type pay to proceed admission: ").lower()
            if pay1 == "pay" and cash >= 10000:
                cash = cash - 10000
                select1 = input("\t\t\t\t\t\t\t\t\t\t\t\t\tChoose your admission group (A/B/C/D): ")
                if select1 in ["A", "B", "C", "D"]:
                    random1 = random.randint(0,3)
                    print("\t\t\t\t\t\t\t\t\t\t\t\t\tInitiating bot selection..")
                    time.sleep(2)
                    print(f"\t\t\t\t\t\t\t\t\t\t\t\t\tBot slected {['A', 'B', 'C', 'D'][random1]}\n")
                    if select1 ==['A', 'B', 'C', 'D'][random1] :
                        print(f"\t\t\t\t\t\t\t\t\t\t\t\t\tCONGRATULATIONS you got your admission in "
                              f"National training center, {['NEPAL', 'UTTAR PRADESH'][training_center.index([x,y])]}")
                        time.sleep(2)
                        print("\t\t\t\t\t\t\t\t\t\t\t\t\tAfter some time....")
                        time.sleep(5)
                        print("\t\t\t\t\t\t\t\t\t\t\t\t\tResults: Dodge skills +20%")
                        dodge += 20
                    else:
                        print("\t\t\t\t\t\t\t\t\t\t\t\t\tBETTER LUCK NEXT TIME")
            else:
                print("\t\t\t\t\t\t\t\t\t\t\t\t\tTransaction failed!")

        elif [x,y] in labs:
            print("\t\t\t\t\t\t\t\t\t\t\t\t\tWelcome to INTERNATIONAL SCIENCE LAB\n\t\t\t\t\t\t\t\t\t\t\t\t\t"
                  "TELEPORT cost is 7500"
                  "\n\t\t\t\t\t\t\t\t\t\t\t\t\tIt is a random chance out of A/B"
                  " that it will work!\n\t\t\t\t\t\t\t\t\t\t\t\t\tYou can max buy one and will fail the"
                  " next step if try to get 2")

            pay2 = input("\t\t\t\t\t\t\t\t\t\t\t\t\tpay rs 7500 to proceed (pay) - ").lower()
            if pay2 == "pay" and teleport_tool == 0 and cash >=7500:
                cash -= 7500
                select2 = input("\t\t\t\t\t\t\t\t\t\t\t\t\tChoose pack A/B: ")
                if select2 == ['A', 'B'][random.randint(0,1)]:

                    print("\t\t\t\t\t\t\t\t\t\t\t\t\tYou got yourself a teleport tool and it will teleport you"
                          " to any bar across city in danger"
                          ". \n\t\t\t\t\t\t\t\t\t\t\t\t\tYou can need it anytime, anywhere, anyhow !!")

                    teleport_tool += 1
                else:
                    print("\t\t\t\t\t\t\t\t\t\t\t\t\tSorry your pack is faulty !")
            else:
                print("\t\t\t\t\t\t\t\t\t\t\t\t\tTransaction failed!")
        else:
            print("\t\t\t\t\t\tThere is no permises to enter!")



    if npc_individual_name == "none" and move == "i":
        print("\t\t\t\t\t\tOops there's no one to interact with!!!")



    elif move == "i" and (npc_status ==2 or npc_status ==1):
        print(f"\t\t\t\t\t\t{name} says: {dialog1[random.randint(0,len(dialog1)-1)]}")
        time.sleep(1)
        print(f"\t\t\t\t\t\t{npc_individual_name} is thinking")
        print("\t\t\t\t\t\t.....")
        time.sleep(1)
        print("\t\t\t\t\t\t....")
        time.sleep(1)
        if npc_status == 2:
            print(f"\t\t\t\t\t\t{npc_individual_name} gave you {npc_cash} ruppees and ran from violence")
            cash += npc_cash
            npc_individual_name = "none"
            npc_status=0
        elif npc_status == 1:
            print(f"\t\t\t\t\t\t{npc_individual_name} says:", dialog2[random.randint(0, len(dialog2) - 1)])
            print("\t\t\t\t\t\t...\n")
            time.sleep(2)
            npc_weapon = np[random.randint(0,len(np)-1)]
            if x >= 7:
                npc_weapon = ['d', 'a', 's', 'k', 's', 'd', 's', 's', 'a', 'd', 'd', 'd', 'd', 'a', 'a', 'a', 's', 's', 'k', 'a'][random.randint(0, 19)]
            fight(npc_weapon, [int(cash/2), int(cash/4), int(cash/3), 500, int(cash/5), int(cash/2), 1000][random.randint(0,6)], npc_cash)

    if npc_status ==3:
        npc_weapon = np[random.randint(0,len(np)-1)]
        if x >=7:
                npc_weapon = ['d', 'a', 's', 'k', 's', 'd', 's', 's', 'a', 'd', 'd', 'd', 'd', 'a', 'a', 'a', 's', 's', 'k', 'a'][random.randint(0, 19)]

        print(f"\t\t\t\t\t\t{npc_individual_name} shows {full_forms[ammunation_items.index(npc_weapon)]} and says:", dialog1[random.randint(0, len(dialog1) - 1)])
        time.sleep(2)
        cash_wants = [5000, int(cash/5), int(cash/2), int(cash/3), 1000, 1000, int(cash/3), int(cash/4), int(cash), 1000, 69, 6969, int(cash/2)][random.randint(0,12)]
        
        a1 = 'i'
        if cash_wants != 0:
            a1 = input(f"\t\t\t\t\t\t{npc_individual_name} asks for rs {cash_wants}. Do you want to give money(g) or fight(i): ").lower()
        if cash_wants == 0:
            print(f"\t\t\t\t\t\tYou are broke and i will break you more... ")
                  
    
        if a1 == "i":
            print(f"\t\t\t\t\t\t{name} says:", dialog2[random.randint(0,len(dialog2)-1)])
            print("\t\t\t\t\t\t...\n")
            time.sleep(2)
            fight(npc_weapon, cash_wants, npc_cash)
        elif a1 == "g" and cash >= cash_wants:
            time.sleep(1)
            print(f"\t\t\t\t\t\t{name} says:", dialog3[random.randint(0,len(dialog3)-1)])
            time.sleep(1)
            cash -= cash_wants
            print(f"\t\t\t\t\t\tSituation resolved, payed rs {cash_wants}")
            npc_individual_name = "none"
            npc_status=0
        else:
            print("\t\t\t\t\t\tWait! I think I would like to have a kill..")
            print("\t\t\t\t\t\t...\n")
            time.sleep(2)
            fight(npc_weapon, cash_wants, npc_cash)

    elif move == "t" and teleport_tool == 1:
        print("initating teleport...")
        time.sleep(1)
        print("....")
        bar_selected = bars[random.randint(0,len(bars)-1)]
        x = bar_selected[0]
        y = bar_selected[1]
        change_npcname = 0
        npc_status = 0
        npc_individual_name = "none"
        teleport_tool -=1
        inbar()
    elif move == "t" and teleport_tool == 0:
        print("\t\t\t\t\t\tYou don't have a teleport tool can have it from labs!   **(see map) for nearest lab**")
    if move not in ["w", "a", "s", "d"]: change_npcname = 0
    else: change_npcname = 1




    if 'a' in items and cash >= 50000 and dodge == 60 and teleport_tool == 1 and msg == 0:
        x = 0
        y = 0
        print("taken to origin")
        time.sleep(1)
        print("...")
        time.sleep(2)
        print("\n\nYOU HAVE BEEN NAMED THE MAFIA OF UP AND NEPAL. YOU HAVE COMPLETED THE TASK AND REACHED TO TOP")
        time.sleep(1)
        print("...")
        time.sleep(2)
        print("DO YOU REMEMBER, I AM SCOOBY, I AM BACK")
        print("YOU CAN DO RULE HERE FOR A WHILE -- SCOOBY")
        time.sleep(1)
        print("...")
        time.sleep(2)
        print("ONLY WAY TO DEATH LEFT NOW IS SOME VERY SILLY BLUNDER OR MESS WITH DON")
        time.sleep(1)
        print("...")
        time.sleep(2)
        print("I AM PLANNING THE NEXT BIGGER AND EXCITING MISSIONS FOR YOU AS YOU SEEM TO BE A TALENT!!")
        print("THE FUTURE IS WITH MISSIONS, INTERNATIONAL TRIPS, MORE WEAPONS, MORE FUN!!")
        time.sleep(1)
        print("...")
        time.sleep(2)
        print("YOU ARE LIKE MY SON NOW. I HAVE TO MAKE SUCH A TALENT THE CONQUERER..")
        time.sleep(1)
        print("...")
        time.sleep(2)
        time.sleep(2)
        print("MADE IN 10 hours with 500 lines of code..")
        time.sleep(1)
        print("A YS DEVELOPMENT INITIATIVE\n\n")
        time.sleep(2)
        msg = 1
        a5 = input("Leave and rest for future: (y/n)")
        if a5=="y": health = 0
        
print("\n\nLeaving the RPG Simulation...")
time.sleep(5)
