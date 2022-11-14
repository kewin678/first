A=[2, 3, 9, 2, 5, 1, 3, 7, 10]
B=[2, 1, 3, 4, 3, 10, 6, 6, 1, 7, 10, 10, 10] 
A.extend(B)


for iter in range(2,11):
    for i in range(2,iter):
        if iter % i == 0:
            break
        else:
            A.remove(iter)
           


print(A)