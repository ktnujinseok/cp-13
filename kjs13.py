class baverage:
    def __init__(self):
        self.manu = {"커피": 3000, "녹차": 2500, "아이스티": 3000}

    def calculate(self, name, num):
        if name in self.manu:
            all_price = self.manu[name] * num
            return all_price
        else:
            print("없는 메뉴입니다.")
            return None

음료 = baverage()

baverage_name = input("주문할 음료를 입력하세요: ")
baverage_num = int(input("수량을 입력하세요: "))

all_price = 음료.calculate(baverage_name, baverage_num)

if all_price is not None:
    print(f"{baverage_name} {baverage_num}잔의 가격은 {all_price}입니다.")
else:
    print("다시 입력하세요.")