fizzbuzz=[]
for i in range(1,101): 
    if i%3==0 and i%5==0:
        fizzbuzz.append("fizzbuzz")
    elif i%3==0:
        fizzbuzz.append("fizz")
    elif i%5==0:
        fizzbuzz.append("buzz")
    else:
        fizzbuzz.append(i)
    print(fizzbuzz[i-1])
