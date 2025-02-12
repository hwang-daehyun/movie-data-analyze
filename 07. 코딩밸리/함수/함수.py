
# 중첩 함수
def calculate(num1, num2, operator):
    def add(n1, n2):  # 덧셈 연산을 수행하는 함수
        return n1 + n2

    def subtract(n1, n2):  # 뺄셈 연산을 수행하는 함수
        return n1 - n2

    if operator == "add":
        return add(num1, num2)  # 덧셈 함수 호출
    elif operator == "subtract": 
        return subtract(num1, num2) # 뺄셈 함수 호출


print(f"덧셈 결과: {calculate(10, 2, 'add')}")
print(f"뺄셈 결과: {calculate(10, 2, 'subtract')}")


# 재귀 함수
# -> 자기 자신을 호출하는 함수를 의미합니다.
# -> base case란 재귀 함수가 호출을 중단하는 조건으로, 재귀 함수 내에 반드시 설정되어야 합니다.
def recursive_function(n):
    """숫자를 재귀적으로 감소시키며 출력하는 재귀 함수"""

    if n == 0:  # base case
        print("n이 0입니다.")
        print("base case에 해당되어 재귀 함수 호출을 종료합니다.")
        return

    print(n)

    recursive_function(n - 1)  # 재귀 호출


recursive_function(3)


def get_factorial(n):
    """n!의 값을 돌려준다."""

    if n == 0:  # base case
        return 1

    return n * get_factorial(n - 1)  # 재귀 호출


for item in range(6):
    print(f"{item}! = {get_factorial(item)}")



# 다른 for문 방법
def get_factorial(n):
    """n!의 값을 돌려준다."""

    result = 1

    for item in range(1, n + 1):
        result *= item

    return result


for item in range(6):
    print(f"{item}! = {get_factorial(item)}")



def get_power_of_two(n):
    """2^n의 값을 돌려준다."""

    if n == 0:  # base case
        return 1

    return 2 * get_power_of_two(n - 1)  # 재귀 호출


for item in range(11):
    print(f"2^{item} = {get_power_of_two(item)}")






fizz = 3
buzz = 3

def fizz_buzz(buzz):
    fizz = 5
    return buzz - 1

for i in range(3):
    buzz = fizz_buzz(buzz)

print(fizz+buzz)

a= 100
tt = (a,)
print(type(tt))


from random import randrange
for i in range(randrange(2,3)): #randrange(2,3) -> 결국 2만 나옴 randrange(시작(이상),끝(미만))
    print("A")



