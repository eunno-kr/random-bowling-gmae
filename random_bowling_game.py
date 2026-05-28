import random

def 볼링점수계산기(기록):
    총점 = 0
    투구횟수 = 0
    프레임모양 = []
    프레임점수 = []

    for 프레임 in range(9):
        if 기록[투구횟수] == 10:  # 스트라이크
            총점 += 10 + 기록[투구횟수 + 1] + 기록[투구횟수 + 2]
            프레임모양.append("X")
            투구횟수 += 1 
        elif 기록[투구횟수] + 기록[투구횟수 + 1] == 10:  # 스페어
            총점 += 10 + 기록[투구횟수 + 2]
            첫구 = "-" if 기록[투구횟수] == 0 else 기록[투구횟수]
            프레임모양.append(f"{첫구}/")
            투구횟수 += 2
        else:  # 오픈 프레임
            첫구 = "-" if 기록[투구횟수] == 0 else 기록[투구횟수]
            두번째구 = "-" if 기록[투구횟수 + 1] == 0 else 기록[투구횟수 + 1]
            총점 += 기록[투구횟수] + 기록[투구횟수 + 1]
            프레임모양.append(f"{첫구}{두번째구}")
            투구횟수 += 2

        프레임점수.append(총점)

    # 10프레임 계산
    마지막프레임 = 기록[투구횟수:]
    총점 += sum(마지막프레임)

    프레임모양10 = []
    for i, 점수 in enumerate(마지막프레임):
        if 점수 == 10:
            프레임모양10.append("X")
        elif i == 1 and 마지막프레임[0] + 점수 == 10 and 마지막프레임[0] != 10:
            프레임모양10.append("/")
        elif 점수 == 0:
            프레임모양10.append("-")
        else:
            프레임모양10.append(str(점수))

    프레임모양.append(" ".join(프레임모양10))
    프레임점수.append(총점)

    return 총점, 프레임모양, 프레임점수


class 볼링플레이어:
    def __init__(self, 이름):
        self.이름 = 이름
        self.기록 = []
        self.총점 = 0
        self.프레임모양 = []
        self.프레임점수 = []

    def 볼링점수계산기(self, 투구기록):
        self.기록 = 투구기록
        self.총점, self.프레임모양, self.프레임점수 = 볼링점수계산기(투구기록)

    def 점수판출력(self):
        print(f"\n[ {self.이름} 님의 경기 결과 ]")
        경계선 = "-" * 85
        print(경계선)
        print(" | ".join([f"{i+1:^7}F" for i in range(10)]))
        print(" | ".join([f"{m:^8}" for m in self.프레임모양]))
        print(" | ".join([f"{s:^8}" for s in self.프레임점수]))
        print(경계선)
        print(f"최종 합계: {self.총점}점")


def 랜덤기록계산기():
    기록 = []
    for 프레임 in range(9):
        첫번째 = random.randint(0, 10)
        기록.append(첫번째)

        if 첫번째 < 10:
            기록.append(random.randint(0, 10 - 첫번째))

    첫번째10 = random.randint(0, 10)
    기록.append(첫번째10)

    if 첫번째10 == 10:
        두번째10 = random.randint(0, 10)
        기록.append(두번째10)
        if 두번째10 == 10:
            세번째10 = random.randint(0, 10)
        else:
            세번째10 = random.randint(0, 10 - 두번째10)
        기록.append(세번째10)
    else:
        두번째10 = random.randint(0, 10 - 첫번째10)
        기록.append(두번째10)
        if 첫번째10 + 두번째10 == 10:
            세번째10 = random.randint(0, 10)
            기록.append(세번째10)

    return 기록


if __name__ == "__main__":
    print("🎳 랜덤 볼링 게임 점수 시뮬레이션을 시작합니다. 🎳")
    
    사용자 = ["김허찬", "김기봉", "정으노"]

    for 이름 in 사용자:
        연습기록 = 랜덤기록계산기()
        최종점수, 프레임모양, 프레임점수 = 볼링점수계산기(연습기록)
        
        print("\n" + "_" * 100)
        print(f"사용자: {이름} 님의 경기 결과")
        print(" | ".join([f"{i+1}프레임" for i in range(10)]))
        print(" | ".join([f"{m:^7}" for m in 프레임모양]))
        print(" | ".join([f"{s:^7}" for s in 프레임점수]))
        print(f"랜덤점수: {연습기록}")
        print(f"최종 점수: {최종점수}점")
        print("_" * 100)