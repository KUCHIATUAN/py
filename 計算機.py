n1 = float(input("請輸入第一個數字:"))
aa = input("請輸入運算符號:")
n2 = float(input("請輸入第二個數字:"))


if aa == "+":
    print(n1+n2)
elif aa == "-":
    print(n1-n2)
elif aa == "*":
    print(n1*n2)
elif aa == "/":
    print(n1/n2)
else:
   print("不支援此運算")    