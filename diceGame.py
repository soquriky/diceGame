import random
import math
import time

#p => player
#e => enemy

#player variables to start
pHPMax = 15
pHP = pHPMax
dieSize = 8

#charging variables
ans = ''
nrgMax = 15

#enemy variables
encounter = 0
eHPMax = 10
eHP = eHPMax

#calculating enemy attack
minIndex = 0
dice = [2,   1,   1,   1,   1]
dVal = [4,   6,   8,   10,  12]
dTotal = []

#easy printing

def ePrint(x):
    print("Enemy  HP:", eHP, "/", eHPMax, x)

def pPrint(x):
    print("Player HP:", pHP, "/", pHPMax, x)

def nrgPrint(nrg, x):
    print("Energy:", nrg, "/", nrgMax, x)

#________________________________________________________#

def roll(die):
    return random.randint(1, dieSize)

#________________________________________________________#

def calcEAttack():
    global minIndex
    global dice
    global dVal
    global dTotal

    del dTotal[:]
    dice[minIndex] += 1
    for i in range(5):
        dTotal.append(dice[i] * ((dVal[i] + 1)/2))

    minIndex = dTotal.index(min(dTotal))

#________________________________________________________#

def newEnemy():
    global encounter
    global eHPMax
    global eHP
    global pHPMax
    global pHP
    global nrgMax
    
    defeatText = "\nEnemy defeated!"
    encounter += 1
    
    if encounter%4 == 0:
        pHPMax += 5
        pHP = pHPMax
        defeatText += " Your max health increased by 5!"

    elif encounter%4 == 2:
        nrgMax += 2
        defeatText += " Your max energy increased by 2!"

    eHPMax = math.floor(eHPMax * 1.2)
    eHP = eHPMax
    
    calcEAttack()

    print(defeatText)
    print("\nAnother enemy approaches!")

    pPrint("")
    ePrint("")

#________________________________________________________#

def charge():
    nrg = roll(dieSize)
    ans = 'c'
    nrgPrint(nrg, '')
    
    while ans != 'r':
        ans = input("Charge (d8) or Release energy? [c/r] " ).lower()

        if ans == 'r':
            print("\nYou release your beam of energy!")

        elif ans == 'c':
            result = roll(dieSize)
            nrg += result
            nrgPrint(nrg, "(+" + str(result) + ")")

            if nrg > nrgMax:
                print("\nOvercharged! You deal no damage.")
                nrg = 0
                ans = 'r'
            
            elif nrg == nrgMax:
                print("\nFully charged! Double damage!")
                nrg *= 2
                ans = 'r'

        elif ans != 'r':
            print("That is not a valid input.")

    attack(nrg)

#________________________________________________________#

def eAttack():
    global pHP
    
    eTotal = 0
    
    print("\nThe enemy strikes!")
    eAttack = str(dice[minIndex]) + "d" + str(dVal[minIndex]) + ": "

    for i in range(dice[minIndex]):
        eRoll = roll(dVal[minIndex])
        eTotal += eRoll
        eAttack += str(eRoll) + ", "

    eAttack = eAttack[:len(eAttack) - 2]

    pHP -= eTotal
    pPrint("(" + eAttack + " = " + str(eTotal) + ")")
    
#________________________________________________________#

def attack(dmg):
    global eHP
    
    eHP -= dmg
    ePrint("(-" + str(dmg) + ")")

    if eHP <= 0:
        newEnemy()
    else:
        eAttack()
        
#________________________________________________________#

def turnLoop():
    while pHP > 0:
        print()
        charge()

#________________________________________________________#

print("An enemy approaches!")
pPrint("")
ePrint("")

turnLoop()

print("You have perished. You defeated", encounter, "monsters.")
time.sleep(5)
