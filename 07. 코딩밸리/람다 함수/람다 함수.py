
My_list = ['apple', 'banana', 'cat', 'dog', 'elephant']

# lambda 앞에 있는 x는 매개변수
# : 뒤는 매개변수를 활용하여 쓸 표현식
add = lambda x: x+1

# map 함수
# map(function, iterable)

# map과 람다함수 활용
upper_list = list(map(lambda x: x.upper(), My_list))
# map으로 하고 끝나면 맵 객체로 끝나 리스트로 묶어줘야 일반적이게 출력 됨
'''print(upper_list)'''
e_list = list(map(lambda x: x.upper() if 'e' in x else x, My_list))
print(e_list)