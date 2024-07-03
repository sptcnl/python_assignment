import random

def rsp(win=0, lose=0, tie=0):

    rsp_list = ["가위", "바위", "보"]
    
    random_rsp = random.choice(rsp_list)

    
    while True:
        
        my_rsp = input("'가위, 바위, 보' 중 하나를 선택하세요: ")

        if my_rsp not in rsp_list:
            print("제대로 입력하세요!")

        else:
            if my_rsp == random_rsp:
                tie += 1
                print(f"컴퓨터: {random_rsp}, 비김")

            elif my_rsp == "가위" and random_rsp == "보" or \
            my_rsp == "바위" and random_rsp == "가위" or \
            my_rsp == "보" and random_rsp == "바위":
                win += 1
                print(f"컴퓨터: {random_rsp}, 이김")

            else:
                win += 1
                print(f"컴퓨터: {random_rsp}, 이김")

            break


    while True:
        yn = input('게임을 또 하고싶습니까? Y/N: ')

        if yn.lower() not in ["y", "n"] :
            print("제대로 입력해주세요")
        elif yn.lower() == 'y':
            rsp(win, lose, tie)
        elif yn.lower() == 'n':
            print(f"승:{win}, 패:{lose}, 무승부:{tie}")
            print("END")
            break

rsp()