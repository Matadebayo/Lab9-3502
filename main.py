#Matthew Adebayo

def encode(ori_number):
    finished = ""
    for num in ori_number:
        new = int(num) + 3
        finished += str(new)
    return print(finished)
encode(message)

def main():
    while True:
        print("Menu")
        print("_____________")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")
        userchoice = input("Please enter an option:")
        if userchoice == 1:
            message = (input("Please enter an 8 digit password:"))

            try:
                if len(message) == 8:
                    break
                else:
                    print("Please enter your password to encode:")
            except ValueError:
                print("Please enter a valid password")
            print("Your password has been encoded and stored!")
            encode(message)
        if userchoice == 2:
            Decode(message)


def Decode():
    DecodedPswrd = ""
    for i in finished:
        update = int(i) - 3
        if update > 0:
            update = str(update)
        else:
            if update == 0:
                update = "7"
            if update == 1:
                update = "8"
            if update == 2:
                update = "9"
        DecodedPswrd += (update)
    print(DecodedPswrd)

