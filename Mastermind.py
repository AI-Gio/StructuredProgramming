
#===================================================================================================
#Hier staat de code, voor het player tegen pc, dus pc heeft geheime code en player moet raden
def Guess():
    Colors = ["red", "blue", "yellow", "green", "orange", "brown"]
    Guesses = []
    for i in range(1,5):
        PinCode = None
        while PinCode not in Colors:
            PinCode = input(f"color pin {i} : ")
            if PinCode not in Colors:
                print("Sorry this color is not used in Mastermind")
        Guesses.append(PinCode)
    return Guesses

def PCCode(): #voor player tegen pc, pc heeft geheime code
    import random # header
    SecretCode = []
    for i in range(1,5):
        PinCode = random.choice(["red", "blue", "yellow", "green", "orange", "brown"])
        SecretCode.append(PinCode)
    return SecretCode

def PCFeedback(SecretCode, Guess):
    #print(SecretCode, Guess)
    BlackPins = 0
    WhitePins = 0
    SecretCodeTemp = []
    GuessTemp = []
#Black pins
    for i in range(0,4):
        if Guess[i] == SecretCode[i]:
            BlackPins += 1
        else:
            SecretCodeTemp.append(SecretCode[i])
            GuessTemp.append(Guess[i])
#White pins
    for i in GuessTemp:
        for j in SecretCodeTemp:
            if i == j:
                SecretCodeTemp.remove(j)
                WhitePins += 1
                break
#Data displayed
    feedback = "B"*BlackPins + "W"*WhitePins
    return feedback

def PlayerGuess(): # rename
    SecretCode = PCCode()
    for i in range(1,11):
        print(f"This is guess {i}\n")
        guess = Guess()
        feedback = PCFeedback(SecretCode, guess)
        if feedback == "BBBB":
            return f"After {i} guess(es), the secret code is {SecretCode}" #why?
        elif i == 10:
            print(f"You lost, the secret code was {SecretCode}")
        else:
            print(feedback)
#===================================================================================================
#Hier staat de code voor pc tegen player, dus de player heeft geheime code en pc moet raden
def PlayerCode(): #voor pc tegen speler, speler heeft de geheime code
    print("Put in your secret code")
    SecretCode = []
    Colors = ["red", "blue", "yellow", "green", "orange", "brown"]
    for i in range(1,5):
        PinCode = None
        while PinCode not in Colors:
            PinCode = input(f"color pin {i} : ")
            if PinCode not in Colors:
                print("Sorry this color is not used in Mastermind")
        SecretCode.append(PinCode)
    return SecretCode

def MastermindPc(): #Je speelt tegen de pc dus pc geeft feedback en geeft aan of het goed geraden is.
    import random
    PlayerCodeTemp = PlayerCode()
    FirstGuess = []
    Possibilities = []  # Lst met mogelijke codes
    Colors = ["red", "blue", "yellow", "green", "orange", "brown"]
    for i in Colors:
        for j in Colors:
            for k in Colors:
                for l in Colors:
                    Possibilities.append([l,k,j,i])
    for a in range(1,15):
        if a == 1:
            for i in Possibilities:
                if i[0] == i[1] and i[2] == i[3]:
                    FirstGuess.append(i)
            gok = ["red", "red", "blue", "blue"]
        else:
            gok = random.choice(Possibilities)
        compare = PCFeedback(PlayerCodeTemp, gok)
        if compare == "BBBB":
            print(f"Wow the pc found your code in {a} tries")
            break
        for b in Possibilities:
            if PCFeedback(gok, b) != PCFeedback(PlayerCodeTemp, gok):
                Possibilities.remove(b)
#============================================================================================================
def Choosemenu():
    print("Welcome to mastermind!!!")
    print("Do you want to have the secret code or have to crack the secret code?")
    print("Press 1 to have code     2 to crack the code:")
    while True:
        choose = input("input: ")
        if choose == "1" or choose == "2":
            break
        print("Please give an input of 1/2")
    if choose == "1":
        print(MastermindPc())
    else:
        PlayerGuess()
MastermindPc()
#===============================================================================================================
