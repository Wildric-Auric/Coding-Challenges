
Nm1 = 0
Nm2 = 1
i = 2
n = 100
Fibo_Serie = [0,1]
for x in range(n):
    Nm1 += Nm2
    Nm2 += Nm1
    Fibo_Serie.extend([Nm1, Nm2])

print(Fibo_Serie)
