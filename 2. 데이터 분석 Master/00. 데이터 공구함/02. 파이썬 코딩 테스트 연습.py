# 숫자의 합 구하기

# 1번째 줄에 숫자의 개수 N(1<=N<=100),2번째 줄에 숫자 N개가 공백 없이 주어진다 
# 입력으로 주어진 숫자 N개의 합을 출력한다.

# number = int(input())

# if number>=1 or number<=100:
#     a=0
#     for i in range(1, number+1):
#         a=a+i
# print(a)

n = input()
numbers = list(input())
sum = 0
for i in numbers:
    sum = sum + int(i)
print(sum)
