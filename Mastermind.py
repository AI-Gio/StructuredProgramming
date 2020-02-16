
#===================================================================================================
#Hier staat de code, voor het player tegen pc, dus pc heeft geheime code en player moet raden
def Guess(): # Dit zorgt ervoor dat de player een gok kan doen
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

def PCFeedback(SecretCode, Guess): # Deze code geeft een feedback terug met input de secret code en een gok
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
    # feedback = "B"*BlackPins + "W"*WhitePins
    return BlackPins, WhitePins

def PlayerGuess(): # rename
    SecretCode = PCCode()
    for i in range(1,11):
        print(f"This is guess {i}\n")
        guess = Guess()
        Blackpins, Whitepins = PCFeedback(SecretCode, guess)
        if Blackpins == 4:
            return f"After {i} guess(es), the secret code is {SecretCode}" #why?
        elif i == 10:
            print(f"You lost, the secret code was {SecretCode}")
        else:
            print((Blackpins,Whitepins))
#===================================================================================================
#Hier staat de code voor pc tegen player, dus de player heeft geheime code en pc moet raden
def PlayerCode(): #Deze functie vraagt om een secret code van de player
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
    print("Choose difficulty, 1(easy), 2(medium), 3(Beast mode)")
    DiffChoose = input("Input 1/2/3: ")
    for i in Colors: # genereerd alle mogelijke codes
        for j in Colors:
            for k in Colors:
                for l in Colors:
                    Possibilities.append([l,k,j,i])
    while True:
        if DiffChoose == "1":  # Hier word de simple strategy gebruikt
            for a in range(1, 15):  # Dit is een teller om te meten hoeveel guesses de pc nodig had
                if a == 1:  # Dit is simple strategy met knuths first guess
                    for i in Possibilities:
                        if i[0] == i[1] and i[2] == i[3]:
                            FirstGuess.append(i)
                    gok = FirstGuess[0]
                else:
                    gok = random.choice(Possibilities)
                Blackpins, Whitepins = PCFeedback(PlayerCodeTemp,
                                                  gok)  # PCFeedback(PlayerCodeTemp, gok)/ dit is een forced feedback moet alleen nog kunnen veranderen
                if Blackpins == 4:
                    print(f"Wow the pc found your code in {a} tries")
            for b in Possibilities:  # pakt alle items in Posibilities lst en vergelijkt of feedback niet hetzelfde is aan forced feedback en daarna remove je die mogelijkheid
                if PCFeedback(gok, b) != (Blackpins, Whitepins):  # PCFeedback(PlayerCodeTemp, gok):
                    Possibilities.remove(b)
            break
        elif DiffChoose == "2":  # Hier komt eigen algoritme
            break
        elif DiffChoose == "3":  # Hier wordt de expected size algoritme gebruikt
            gok = 0 # Dit moet nog verandert worden
            BestSize = float("inf")
            DataLst = []
            allFeedback = [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4),
                           (1, 0), (1, 1), (1, 2), (1, 3),
                           (2, 0), (2, 1), (2, 2),
                           (3, 0), (4, 0)]

            # Dit stukje berekent per soort vraag het x aantal mogelijkheden zijn als itemsFeedback de SecretCode is
            for itemsFeedback in allFeedback:
                NewLst = []  # lijst van codes die geschrapt worden
                for b in Possibilities:
                    if PCFeedback(gok, b) != itemsFeedback:  # PCFeedback(PlayerCodeTemp, gok)
                        NewLst.append(b)
                Calc = len(Possibilities) - len(NewLst)  # geef getal lengte terug van geschrapte lijst
                DataLst.append(Calc)
            # Dit stukje berekent wat de beste keuze moet zijn
            ExSize = 0
            for i in DataLst:  # pakt alle waardes van een soort vraag
                ExSize += (i ** 2) / len(Possibilities)  # Berekent de expected size
            if ExSize < BestSize:
                BestSize = ExSize
                BestComb = gok
            print(BestSize)
            print(BestComb)
            break
        else:
            print("You have to put in a number!")
            DiffChoose = input("Input 1/2/3: ")

#============================================================================================================
def Choosemenu():   # Deze functie zorgt voor een keuze menu waar de speler kan kiezen of ze zelf Secret code hebben of dat ze moeten raden
    print("Welcome to mastermind!!!")
    print("Do you want to have the secret code or have to crack the secret code?")
    print("Press 1 to have code     2 to crack the code:")
    while True:
        choose = input("input: ")
        if choose == "1" or choose == "2":
            break
        print("Please give an input of 1/2")
    if choose == "1":
        MastermindPc()
    else:
        PlayerGuess()
#===============================================================================================================
Choosemenu()

