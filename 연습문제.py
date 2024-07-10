text= input("문자메세지를 작성하세요")
print(len(text),'bytes')
if len(text) <= 20 :
    print("요금은 50원 입니다.")
elif len(text) > 20 :
    print('요금은 100원 입니다.')