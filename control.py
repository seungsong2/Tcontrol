# 조건문 기본
print("hello world")

if 3> 1 :
    print("3은 1보다 큽니다.")
    print("연산을 종료합니다.")
print("-"*15)
print("저는 들여쓰기를 하지 않은 라인입니다.")

# 논리연산 기호
a = "이승연"
b = "강혜나"
if a == b :
    print("두 사람의 이름은 같습니다.")

# 여러 조건을 입력 (위의 조건을 만족하지 않아도 실행됨)
elif a != b :
    print("두 사람의 이름은 다릅니다.")

num_1 =10
num_2 = 3

if num_1 < num_2 :
    print('num_1은 num_2 보다 크기가 작습니다.')

elif num_1 == num_2 :
    print('num_1은 num_2랑 크기가 같습니다.')

elif num_1 > num_2 :
    print('num_1은 num_2보다 크기가 큽니다.')



# 연습문제 1
# 1. 안녕하세요를 입력했을 때
#
# 3. 반갑습니다가 실행되게
text = input("안녕하세요를 입력하세요:")

if  text == '안녕하세요' :
    print("반갑습니다.")

#  연습문제2
#  1.사용자로부터 값을 입력 받아 (문자열)
#  *num = int(input('임의의 숫자를 입력하세요')) 와 밑의 값은 동일하다.
num = input("임의의 숫자를 입력하세요:")
# 문자열로 인식된 숫자를 바꾸는 함수
num = int(num)
print(num, type(num))
# 2.해당 값에 100을 더한 값이
# 2-1 입력받은 값에 100을 더할 때 데이터 타입을 변환 (문자열 -> 숫자열)
# data_2 = int(data) + 100
a = num+100
# 3.더한 값이 150 초과인 경우, 사용자 입력 값을 출력
if a > 150 :
    print(num)
# 4.더한 값이  150 이하인 경우, 값이 모자랍니다 를 출력
elif a <= 150 :
    print("값이 부족합니다.")

# 연습문제 3
x = int(input("임의의 값을 입력해주세요:"))
if 5 < x < 10 :
    print('ok')

else:
    print("no")


#  and, or 연산자
apple = '사과'
banana = '바나나'

if apple == '사과' or banana == '바나나' :
    print("문자열이 모두 정확합니다.")

#많이 쓰는 <조회> 문법
 var = [1,2,3]
if 3 in var:
    print("숫자 3이 변수에 있습니다요")
# 연습문제
fruit = ['사과','포도','홍시']
a = input("승연이가 좋아하는 과일은 무엇일까요?:")
if a in fruit :
    print('정답입니다.')
else :
    print('오답입니다.')

#해답
# 사용자로부터 입력받아
#  fruit 변수는 리스트
# 입력받은 값이 fruit에 요소로 있는지 확인 / if 조회할 값 in 조회할 대상

# 딕셔너리 값 입력이 키에 있으면 정답입니다 라고하기
 a = input("딸기, 토마토, 사과 중 하나를 골라 열리는 계절을 입력해주세요")
 fruit = {"봄": "딸기", "여름": "토마토", "가을":"사과"}
 if a in fruit
     print('정답입니다.')
else:
 print('오답입니다.')
# 딕셔너리는 key 값이 우선됨

