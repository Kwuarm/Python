from random import randint

def delbar(num1, num2): #får 2 värden från program.py, sätter de till num1 och num2.
    numlist = []
    for x in range (1,1000):
        if ((x % num1) == 0) and ((x % num2) == 0): #om resten är 0 för både numren...
            numlist.append(x)
    print(numlist)

def slumpa():
    value = randint(1,100)
    amt_guessed = []
    intuserguess = 0 #
    print(f'the number is {value}')
    while intuserguess != value : #under tiden våran guess inte är rätt
        userguess = input("Skriv in ett tal!\n")
        intuserguess = int(userguess)
        amt_guessed.append(1)
        if intuserguess < value:
            print("Ow! You guessed too low!")
        if intuserguess > value:
            print("Ouch! You guessed too high!")
    else:
        print(f'Congratulations! The number was: {value}')
        print(f'You guessed a grand total of {len(amt_guessed)} times!') #antalet items i amt_guessed

