import random


def updown_game(best_score=0):

    try_num = 0     # 정답까지 시도한 횟수

    random_number = random.randint(1, 100)

    if best_score != 0:
        print(f"최고 기록은 {best_score}회입니다.")

    while True:

        num = int(input('1에서 100 사이 숫자를 입력하세요: '))
        try_num += 1

        if not (1 <= num <= 100):
            print("숫자를 제대로 입력하세요!")

        elif num == random_number:
            print(f"정답! {try_num}번만에 맞췄어요!")
            best_score = min(best_score or try_num, try_num)
            break

        elif num < random_number:
            print("업")
        elif num > random_number:
            print("다운")

    while True:
        yn = input('게임을 또 하고싶습니까? Y/N: ')

        if yn.lower() not in ["y", "n"] :
            print("제대로 입력해주세요")
        elif yn.lower() == 'y':
            updown_game(best_score)
        elif yn.lower() == 'n':
            print("END")
            break




updown_game()
