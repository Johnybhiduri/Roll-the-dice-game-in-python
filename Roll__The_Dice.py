
import os , time , random

x1 = random.randint(1,6)
x2 = random.randint(1,6)
def player1():
    if x1 == 1 :
        print("           =============")
        print("           =           =")
        print("           =     O     =")
        print("           =           =")
        print("           =============")
    elif x1 == 2:
        print("           =============")
        print("           =           =")
        print("           =   O   O   =")
        print("           =           =")
        print("           =============")
    elif x1 == 3:
        print("           =============")
        print("           =           =")
        print("           =  O  O  O  =")
        print("           =           =")
        print("           =============")
    elif x1 == 4:
        print("           =============")
        print("           =   O   O   =")
        print("           =           =")
        print("           =   O   O   =")
        print("           =============")
    elif x1 == 5:
        print("           =============")
        print("           =   O   O   =")
        print("           =     O     =")
        print("           =   O   O   =")
        print("           =============")
    elif x1 == 6 :
        print("           =============")
        print("           =   O O O   =")
        print("           =           =")
        print("           =   O O O   =")
        print("           =============")

    
    if x2 == 1 :
        print("           =============")
        print("           =           =")
        print("           =     O     =")
        print("           =           =")
        print("           =============")
    elif x2 == 2:
        print("           =============")
        print("           =           =")
        print("           =   O   O   =")
        print("           =           =")
        print("           =============")
    elif x2 == 3:
        print("           =============")
        print("           =           =")
        print("           =  O  O  O  =")
        print("           =           =")
        print("           =============")
    elif x2 == 4:
        print("           =============")
        print("           =   O   O   =")
        print("           =           =")
        print("           =   O   O   =")
        print("           =============")
    elif x2 == 5:
        print("           =============")
        print("           =   O   O   =")
        print("           =     O     =")
        print("           =   O   O   =")
        print("           =============")
    elif x2 == 6 :
        print("           =============")
        print("           =   O O O   =")
        print("           =           =")
        print("           =   O O O   =")
        print("           =============")

x3 = random.randint(1,6)
x4 = random.randint(1,6)
def player2():
    if x3 == 1 :
        print("           =============")
        print("           =           =")
        print("           =     O     =")
        print("           =           =")
        print("           =============")
    elif x3 == 2:
        print("           =============")
        print("           =           =")
        print("           =   O   O   =")
        print("           =           =")
        print("           =============")
    elif x3 == 3:
        print("           =============")
        print("           =           =")
        print("           =  O  O  O  =")
        print("           =           =")
        print("           =============")
    elif x3 == 4:
        print("           =============")
        print("           =   O   O   =")
        print("           =           =")
        print("           =   O   O   =")
        print("           =============")
    elif x3 == 5:
        print("           =============")
        print("           =   O   O   =")
        print("           =     O     =")
        print("           =   O   O   =")
        print("           =============")
    elif x3 == 6 :
        print("           =============")
        print("           =   O O O   =")
        print("           =           =")
        print("           =   O O O   =")
        print("           =============")

    
    if x4 == 1 :
        print("           =============")
        print("           =           =")
        print("           =     O     =")
        print("           =           =")
        print("           =============")
    elif x4 == 2:
        print("           =============")
        print("           =           =")
        print("           =   O   O   =")
        print("           =           =")
        print("           =============")
    elif x4 == 3:
        print("           =============")
        print("           =           =")
        print("           =  O  O  O  =")
        print("           =           =")
        print("           =============")
    elif x4 == 4:
        print("           =============")
        print("           =   O   O   =")
        print("           =           =")
        print("           =   O   O   =")
        print("           =============")
    elif x4 == 5:
        print("           =============")
        print("           =   O   O   =")
        print("           =     O     =")
        print("           =   O   O   =")
        print("           =============")
    elif x4 == 6 :
        print("           =============")
        print("           =   O O O   =")
        print("           =           =")
        print("           =   O O O   =")
        print("           =============")

print('                                 **********************************************************           ')
print('                                 *                     _______________                    *           ')
print('                                 *                      ROLL THE DICE                     *           ')
print('                                 *                                                        *           ')
print('                                 *                                       By Johny Bhiduri *           ')
print('                                 **********************************************************           ')

p1name = input("\n\n    Enter your name player 1 : ")
p2name = input('\n    Enter your name player 2 : ')

print(f'\n    {str(p1name)} Its your turn !!')
p1start = int(input("\n    Enter 1 to start : "))
if p1start == 1 :
    player1()
else : player1()
p1sum = x1 + x2
print(f"\n    {p1name} your score is {p1sum}")
print(f"\n    {p2name} Its your turn!! ")
p2start = int(input("\n    Enter 2 to start :"))
if p1start == 2 :
    player2()
else : player2()
p2sum = x3 + x4
print(f"\n    {p2name} your score is {p2sum}")

if p1sum > p2sum :
    print(f'\n    {p1name} Won the game!!')
elif p2sum > p1sum :
    print(f'\n    {p2name} Won the game!!')
else : 
    print('\n    Its a tie, Try Again !')

input('\n\n\n\n    Press ENTER to Re-start')
while 1:
    os.system("python Roll__The_Dice.py")
    print("Restarting...")
    time.sleep(0.2)