def PlayerCode(): #voor pc tegen speler, speler heeft de geheime code
    print("Choose from colors(red, blue, yellow, green, orange, brown, black, white) for 4 pins")
    SecretCode = []
    Colors = ["red", "blue", "yellow", "green", "orange", "brown", "black", "white"]
    #n = 1
    for i in range(1,5):
        PinCode = input(f"choose color pin {i} : ")
        if PinCode not in Colors:
            print("Sorry this color is not used in Mastermind")

        else:
            SecretCode.append(PinCode)
    return SecretCode
print(PlayerCode())

def PCCode():
    import random
    for i in range(1,5):
        PinCode = random.choice(["red", "blue", "yellow", "green", "orange", "brown", "black", "white"])
        print(PinCode)
def MastermindPc(): #Je speelt tegen de pc dus pc geeft feedback en geeft aan of het goed geraden is.
    peeps = 0