def pow(x, y):
    if y == 0:
        return 1

    half = pow(x, y // 2)

    if y % 2 == 0:
        return half * half
    else:
        return half * half * x

if __name__ == '__main__':
    print(pow(10,0))
    print(pow(10,1))
    print(pow(10,2))
    print(pow(10,3))
    print(pow(10,4))
    print(pow(10,5))
    print(pow(10,6))
