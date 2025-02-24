import string
import random
if __name__=="__main__":
    string_1=string.digits
    string_2=string.ascii_letters
    length=int(input("define length of password"))
    s=[]
    s.extend(list(string_1))
    s.extend(list(string_2))
    password=random.sample(s,length)
    print("".join(password))