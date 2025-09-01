# 초기 설정

FLOORS = 3   
SPOTS = 10   
PARKING = [["[]" for _ in range(SPOTS)] for _ in range(FLOORS)]

# 정기차량 
REGULAR_CARS = {
    "123가4567": 0.5,
    "11가1111": 0.3
}

# 주차 기록 
parking_log = {}


# 주차장 출력 함수

def show_parking():
    print("\n=== 현재 주차장 상태 ===")
    for floor in range(FLOORS-1, -1, -1):  # 위층부터 출력
        print(f"{floor+1}층:", " ".join(PARKING[floor]))
    print("=====================\n")

# 입차 기능

def car_in():
    show_parking()
    car_num = input("차량번호 입력: ")
    in_time = int(input("입차 시각(시간 단위, 예: 10): "))

    # 빈자리 안내 (아래층부터 확인)
    for f in range(FLOORS):
        for s in range(SPOTS):
            if PARKING[f][s] == "[]":
                print(f"추천 자리: {f+1}층 {s+1}번")
                break
        else:
            continue
        break

    floor = int(input("원하는 층 입력: ")) - 1
    spot = int(input("원하는 자리 입력: ")) - 1

    if PARKING[floor][spot] == "[]":
        PARKING[floor][spot] = "[X]"
        parking_log[car_num] = {"floor": floor, "spot": spot, "in_time": in_time}
        print(f"{car_num} 차량 입차 완료!")
    else:
        print("이미 주차된 자리입니다!")

    show_parking()


# 출차 기능

def car_out():
    car_num = input("출차 차량번호 입력: ")
    if car_num not in parking_log:
        print("해당 차량은 주차 기록이 없습니다.")
        return

    out_time = int(input("출차 시각(시간 단위, 예: 12): "))
    info = parking_log[car_num]
    in_time = info["in_time"]

    # 시간 계산
    total_time = out_time - in_time
    if total_time <= 0:
        total_time = 1

    # 요금 계산 
    fee = total_time * 1000

    # 정기차량 할인 적용
    if car_num in REGULAR_CARS:
        discount = REGULAR_CARS[car_num]
        fee = int(fee * (1 - discount))
        print(f"정기차량 할인 적용({int(discount*100)}%)!")

    print(f"총 주차 시간: {total_time}시간, 요금: {fee}원")




while True:
    cmd = input("명령 입력 (in: 입차, out: 출차, exit: 종료): ")

    if cmd == "in":
        car_in()
    elif cmd == "out":
        car_out()
    elif cmd == "exit":
        print("시스템 종료!")
        break
    else:
        print("잘못된 입력입니다.")