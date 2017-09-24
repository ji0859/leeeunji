#소프트웨어학부 20171674 이은지
#HW 3-1
def store (k):
    a = ""  # 문자
    b = ""  # 숫자
    c = "1234567890"
    for i in k:
        if i in c:
            b +=i
        else:
            a+=i
    print ("문자:",a)
    print ("숫자",b)
s = input("문자와 숫자를 입력하시오")
print (store(s))
z = input("계속 하시셌습니까?(yes or no):")
while z == "yes":
    s = input("문자와 숫자를 입력하시오.")
    print(store(s))
    z = input("계속 하시셌습니까?(yes or no):")