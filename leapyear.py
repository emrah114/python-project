year=1
while year!="q":
    year=input ("please enter a year(press q for quit)")
    year=int(year)
    if year %4!=0:
        print(f"{year} is not  a leap year")
    elif year%400==0 :
        print(f"{year} is  a leap year")
    elif year%100==0  :
        print(f"{year} is  not a leap year")
    else :print(f"{year} is a leap year")
print("byebye")