def gcd(a, b):
  if a == 0:
    return b
  return gcd(b % a, a)
a=int(input("Enter the first number :"))
b=int(input("Enter the second number :"))
print("The GCD of {} and {} is {}".format(a,b,gcd(a,b)))