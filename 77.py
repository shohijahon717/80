def DigitSum(K):
    if K == 0:
        return 0
    return K%10 + DigitSum(K//10)
    

K = int(input('K = '))
print(DigitSum(K))