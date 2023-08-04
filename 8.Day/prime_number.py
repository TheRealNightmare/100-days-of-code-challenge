def check_prime(x):
    isprime = True
    
    for i in range(2,x):
        if x%i==0:
            isprime = False
    if isprime:
        print("It is prime number")
    else:
        print("it is not prime number")


num = int(input("enter number: "))
check_prime(num)