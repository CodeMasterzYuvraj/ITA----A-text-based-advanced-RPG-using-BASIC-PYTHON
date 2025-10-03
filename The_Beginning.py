import time
print("\n\n\n\n\n\n\n\n\nSome Where in Europe...")
time.sleep(1)
print("...")
print("There is the biggest gang network of the world which controls the europe ''UNOFFICIALLY''")
time.sleep(1)
print("...")
time.sleep(2)
print("Here are the special organisation that create beasts to control this web..")
time.sleep(1)
print("...")
time.sleep(2)
print("Every year hundreds are created but only few survives its exams and criteria tests.")
time.sleep(1)
print("...")
time.sleep(2)
print("These students are called ralph (same name for every student) and they are sent for different tasks")
print("Ralph(You) have to also undergo this process to be a conquerer.")
print("From today Your Journey to Success (or death) begins..")
time.sleep(1)
print("...")
time.sleep(5)
print("\nSomewhere in Europe..")
time.sleep(3)
print("......\n")
time.sleep(2)
print("\nHello ralph, The bank has kept a secret file in sector - 3")
print("I am scooby. Go and get the file. Here u get a pistol. Go and get the file. Bank coordinates (30, -5).\n")
w = ["pistol"]
wd = [40]
adition_move_learn = ["p", "g", "t"]

m = ["w", "a", "s", "d"]
x = 10
y = 15
health = 100
user_input = None
file_pick = 0
file_got = 0
k = 0
call1 = 0
call2 = 0

while file_got != 1:
    user_input = input("{0}:({1},{2}) ".format(health, x, y))
    if user_input in m:
        if user_input == m[0]:
            y += 5
        elif user_input == m[1]:
            x -= 5
        elif user_input == m[2]:
            y -= 5
        elif user_input == m[3]:
            x += 5

    if x == 30 and y == -5 and file_pick == 0 and call1 == 0:
        print("\nPress 't' to take a call of scooby. I think it is some important work! Or might be an information!\n")
        call = input("Dialing! Dialing: ")
        if call == 't':
            print("I had kept my GPS on you. Now if you are at the bank press 'p' to take the file and bring it to my house at (10, 15)")
            print("Ralph, as you take the file the security guard will attack you, That's why i gave you a pistol for self defence. -Scooby\n")
            call1 += 1
    if x == 30 and y == -5 and user_input == "p" and file_pick == 0  and call2 == 0:
        file_pick = 1
        print("File is with you. A gaurd is comming watch out. Fight it or run. But if u run, You can be killed by him also")
        print("Press f to take a fight!\n")
        call2 = 1
        k = 1234

    if k == 1234 and x in range(25, 35) and y in range(-10, 0):
        health -= 10
        print("HP -10. Oh the gaurd is attacking")

    if user_input == 'f' and k == 1234:
        print("Oh! Brilliant you decided to fight.Press enter to attack\n")
        guard_health = 50
        while k != 0:

            a = input(":{0} ".format(health))
            if a == "":
                if guard_health <= 0:
                    print("You killed the guard")
                    k = 0
                    call = input("Scooby - dialling, dialling: ")
                    if call == 't':
                        print("Well done my boy. Now come fast at my house before its too late. House of scooby - (10, 15)\n")
                health -= 10
                guard_health -= 20


    if k == 0 and file_pick == 1 and x == 10 and y ==15:
        print("Well done Ralph!. Here's Your 20 euros (2000 rs) reward! Bro but i have to take the pistol back as you are not yet that capable")
        file_got = 1


print("\n\nTASK 1 COMPLETED...")
time.sleep(1)
print("...")
time.sleep(2)
print("Now you are about to be sent to India where one of the greatest network of multiple gangs runs, Uttar Pradesh!!")
time.sleep(1)
print("...")
time.sleep(2)
print("This will be the most difficult task you have ever done..")
time.sleep(1)
print("...")
time.sleep(2)
print("You have to go and conquer the fields and on right time. I will come again to take you back..")
time.sleep(1)
print("...")
time.sleep(2)
print("This is most important phase to conquer the gang..")
time.sleep(1)
print("...")
time.sleep(2)
print("You will need these 200 euros approx 2000rs and you will know why..")
time.sleep(1)
print("...")
time.sleep(2)
print("You have to make your different identity there with a different and new name.....")
time.sleep(1)
print("...\n")
time.sleep(2)
