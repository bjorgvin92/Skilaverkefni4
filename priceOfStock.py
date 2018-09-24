def input_shares(): #Krefst input sem er gilt.
    while True:
        try:
            shares = int(input("Enter number of shares: "))
            return shares
        except ValueError:
            print("Invalid number!")

def input_string(): #Tekur inn streng og krefst þess að hann er gildur
    while True:    
        s = str(input("Enter price (dollars, numerator, denominator): "))
        dollar, numerator, denominator = s.split()
        try:
            dollar = int(dollar)
            numerator = int(numerator)
            denominator = int(denominator)
            return dollar, numerator, denominator
        except ValueError:
            print("Invalid price!")

def calc(shares, dollar, numerator, denominator): #Reiknar úr færibreytunum og skilar niðurstöðu rétt frá sér.
    outcome = shares*(dollar + numerator/denominator)
    print('{} shares with market price {} {}/{} have value ${:.2f}'.format(shares, dollar, numerator, denominator, outcome))

def continue_check(): #Athugar hvort notandi vill halda áfram
    svar = str(input("Continue: "))
    if svar not in ('y', 'Y'):
        return True



while True:
    shares = input_shares() #Tekur inn fjölda bréfa
    dollar, numerator, denominator = input_string() #Tekur inn verð bréfana
    calc(shares, dollar, numerator, denominator) #Reiknar úr færibreytunum
    if continue_check(): #Athugar hvort notandi vill halda áfram
        break