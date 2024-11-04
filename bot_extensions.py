import random,string
class internal:
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
            for i in range(int(length)):
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

class password:
    def get(num):
        rndmi = internal.get_random_string(num)
        while rndmi == None:
            rndmi = internal.get_random_string(num)
        return rndmi
