#소프트웨어학부 20171674 이은지
#HW 3-2
def counter(c):
    while c<= 0:
        c = int(input("수를 입력하시오."))
        n = 0
        if c < 0:
            print("양의 정수값을 입력해주시오")
        else:
            for i in range(c, 101, c):
                n +=1
                print (i)
            print ("총 개수는:",n)
a = 0
print (counter(a))
b = input("계속 하시겠습니까?(네 혹은 아니오)")
while b == "네":
    print(counter(a))
    b = input("계속 하시겠습니까?(네 혹은 아니오)")