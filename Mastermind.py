
print("Choose from colors(red, blue, yellow, green, orange, brown) for 4 pins")

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
    import random
    SecretCode = []
    for i in range(1,5):
        PinCode = random.choice(["red", "blue", "yellow", "green", "orange", "brown"])
        SecretCode.append(PinCode)
    return SecretCode
#print(PCCode())

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

def PlayerGuess():
    SecretCode = PCCode()

    for i in range(1,11):
        print(f"This is guess {i}\n")
        guess = Guess()
        feedback = PCFeedback(SecretCode, guess)
        if feedback == "BBBB":
            return f"After {i} guess(es), the secret code is {SecretCode}"
        elif i == 10:
            print(f"You lost, the secret code was {SecretCode}")
        else:
            print(feedback)
#===================================================================================================
#Hier staat de code voor pc tegen player, dus de player heeft geheime code en pc moet raden
def PlayerCode(): #voor pc tegen speler, speler heeft de geheime code
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
    S = []
    for i in range(1,6667):
        S.append(str(i))
    Color = ["red", "blue", "yellow", "green", "orange", "brown"]
    #first guess
    if