class Beverage:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def calculate(self, quantity):
        total_cost = self.price * quantity
        return total_cost

# 음료 객체 생성
Coffee = Beverage("커피", 3000)
GreenTea = Beverage("녹차", 2500)
IceTea = Beverage("아이스티", 3000)

# 첫 번째 사용자 입력 받기
selected_beverage = input("음료를 선택하세요 (커피, 녹차, 아이스티): ")

# 사용자 입력에 따라 calculate() 함수 호출
if selected_beverage == "커피":
    quantity = int(input("수량을 입력하세요: "))
    cost = Coffee.calculate(quantity)
    print(f"{Coffee.name} {quantity}잔의 가격은 {cost}원입니다.")
elif selected_beverage == "녹차":
    quantity = int(input("수량을 입력하세요: "))
    cost = GreenTea.calculate(quantity)
    print(f"{GreenTea.name} {quantity}잔의 가격은 {cost}원입니다.")
elif selected_beverage == "아이스티":
    quantity = int(input("수량을 입력하세요: "))
    cost = IceTea.calculate(quantity)
    print(f"{IceTea.name} {quantity}잔의 가격은 {cost}원입니다.")
else:
    print("올바르지 않은 입력입니다.")
