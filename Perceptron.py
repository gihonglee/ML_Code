import random
import numpy as np
from itertools import permutations
import math

def sign(n):
    if n >= 0:
        return 1
    else:
        return -1

n = 3 # size of sample & dimension of sample

w = np.random.uniform(-1, 1,n) #   define w (-1 ~ 1)
order = list(permutations(range(n), n)) # define the order permuation

X = [] # list of data
X_collection = [] # permutation of list of d ata
w_prime_list = [] # w_prime list, which is the answer of the question
result_list = [] # Trained or not trained
mistake_list = np.zeros(math.factorial(n)) # how many mistakes has been made by X_i

for i in range(n):
    X.append(np.random.uniform(-1, 1,n))

result_wx = []
for i in range(n):
    result_wx.append(np.dot(w,X[i]))
result_wx = [sign(i) for i in result_wx]


for i in range(math.factorial(n)):
    x_temp = []
    for j in order[i]:
        x_order = X[j]
        x_temp.append(x_order)
    X_collection.append(x_temp)


for i in range(math.factorial(n)):
    w_prime = np.zeros(n)
    mistake = 0
    for j in range(100):
        anw = sign(np.dot(X_collection[i][j%n],w))
        attemp = sign(np.dot(X_collection[i][j%n],w_prime))
        if anw * attemp == -1:
            w_prime = w_prime + sign(anw) * X_collection[i][j%n]
            mistake += 1  
            
    w_prime_list.append(w_prime)
    result_wprimex = np.dot(X,w_prime)
    result_wprimex = [sign(i) for i in result_wprimex]

    
    if result_wx == result_wprimex:
        result_list.append("Trained")
    else:
        result_list.append("Not Trained")

    mistake_list[i] = mistake



# Print the setting of this simulation / X, w
print(f"Data, X, {X}")
print(f"weight vector w, {w}")


# # 0) I have to fix number of iteration "n", which "completely" train all the w_prime for all permuation of orders in data
# # so here I will choose large n, and simply comfirm that all the training set has been trained by checking the y(result) 
# # and w_prime * X

print(f"Has it been trained? {result_list}")

# # # 1) comparison of w_prime based on the order of the training set
for i,w_prime in enumerate(w_prime_list):
    print(f"{i}the w_prime")
    print(w_prime_list[i])

# # # 2) comparison of mistakes based on the order of the training set
print(f"# of mistakes {mistake_list}")





