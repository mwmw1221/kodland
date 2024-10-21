import random,string,os

def get_random_string(length):
    type = ""
    temp_type = ""
    result_str = ""
    tt = False
    letters = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation
    while not tt:
        type = ""
        temp_type = ""
        result_str = ""
        tt = True
        for i in range(length):
            rndm = random.choice(letters)
            if rndm in string.ascii_lowercase:
                temp_type = "low"
            elif rndm in string.ascii_uppercase:
                temp_type = "high"
            elif rndm in string.digits:
                temp_type = "num"
            else:
                temp_type = "punct"
            # -
            if temp_type == type:
                tt = False
                break
            else:
                result_str += rndm
                if rndm in string.ascii_lowercase:
                    type = "low"
                elif rndm in string.ascii_uppercase:
                    type = "high"
                elif rndm in string.digits:
                    type = "num"
                else:
                    type = "punct"
    return result_str

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

while True:
    cls()
    print("Podaj długość hasła, CTRL+C aby wyjść")
    ii = int(input("} "))
    cls()
    rndmi = get_random_string(ii)
    while rndmi == None:
         rndmi = get_random_string(ii)
    print(rndmi)
    input()