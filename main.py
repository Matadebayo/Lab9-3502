#Matthew Adebayo
message = str(input())
def encode(ori_number):
    finished = ""
    for num in ori_number:
        new = int(num) + 3
        finished += str(new)
    return print(finished)
encode(message)

