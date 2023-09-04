def Fact(N):
   if N == 1:
       return N
   else:
       return N*Fact(N-2)



print(Fact(5))