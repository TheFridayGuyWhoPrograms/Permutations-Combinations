def permutation():
    n=int(input("Enter the value for n:"))
    r=int(input("Enter the value for r:"))
    some=n-r
    fact_n=fact_nr=1
    for i in range(1,n+1):
        fact_n*=i
    for j in range(1,some+1):
       fact_nr*=j
    print(f"The permutation where n is {n} and r is {r}:",fact_n/fact_nr)
def combination():
    n=int(input("Enter the value of n:"))
    r=int(input("Enter the value of r:"))
    fact_n=fact_nr=fact_r=1
    some=n-r
    for i in range(1,n+1):
        fact_n*=i
    for j in range(1,some+1):
        fact_nr*=j
    for k in range(1,r+1):
        fact_r*=k
    print(f"The combination where n is {n} and r is {r}:",fact_n/(fact_r*fact_nr)) 
print("Welcome to <<Permutation and Combinations program>>!")
print("\n----------------------------------------------")
print("\n")
n=int(input("How many times do you want to run the program:"))
i=0
while i<=n:
    ques=input("Which function do you want to use (Permutation/Combination):")
    if ques.lower()=="permutation":
        permutation()
    elif ques.lower()=="combination":
        combination()
    else:
        print("There are no functions available at the moment")
    i+=1