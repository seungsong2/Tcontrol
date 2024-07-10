score = input("본인의 시험점수를 입력하세요")
print(score,'점' type(score))

x= int(score)
if 0<=x<=20 :
    print("학점은 E입니다.")
if 21 <= x <= 40 :
    print("학점은 D입니다.")
if 41 <= x <= 61 :
    print("학점은 C입니다.")
if 61 <= x <= 80 :
    print("학점은 B입니다.")
if 81 <= x <= 100 :
    print("학점은 A입니다.")

#해설
#사용자로부터 값을 입력
# 사용자로부터 입력받은 값을 숫자형으로 데이터 타입을 변환
# 변화된 값을 각 조건에 따라 학점으로 출력