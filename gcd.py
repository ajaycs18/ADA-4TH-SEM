def gcd(a, b):
    if not b:
        print('GCD is', a)
        return
    elif not a:
        print('GCD is', b)
        return

    gcd(b, a%b)

a, b = int(input()), int(input())
gcd(a, b)

