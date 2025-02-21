def calculate():
    number_1=int(input("enter the 1st no.:"))
    number_2=int(input("enter the 2nd no."))
    while True:
        operation=int(input(f"enter:\n1-add\n2-substract\n3-multiply\n4-divide"))
        if operation==1:
            sum=number_1+number_2
            print(f"sum of two no.is:{sum}")
        elif operation==2:
            substract=number_1-number_2
            print(f"substraction of two no.is:{substract}")
        elif operation==3:
            multiply=number_1*number_2
            print(f"multiplication of two no.is:{multiply}")
        elif operation==4:
            divide=number_1/number_2
            print(f"division of two no.is:{divide}")
        else:
            print("invalid input")
            break
calculate()


 








    