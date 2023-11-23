def calculation(var1,var2):
    ans=f"this is the addition:{var1+var2}\n this is the substraction {var1-var2}"
    return ans
print(calculation(70,10))
def check_multiple_arguments(*deez):
    return sum(deez)

print(check_multiple_arguments(10,20,100,30))

