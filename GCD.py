def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

print(gcd(91, 35))
print("Hi, I'm a bug which kill your cimputer. 😈😈")