
import numpy as np
import math

# Hi guys , I'm Javad and my student number is 9831025 , so let's dive in 

def add_row(A,k,j,i):
    # Add k times row j to row i in matrix A
    n = A.shape[0]
    E = np.eye(n)
    if i == j:
        E[i,i] = k + 1
    else:
        E[i,j] = k
    # print(E)
    return E @ A
    # this operation "@" use for multiplication of two matrices
    # reference to https://www.geeksforgeeks.org/multiplication-two-matrices-single-line-using-numpy-python/

"""
explanation for add_row : We do it for Add k times row j to row i
To add k times row j to row u in a matrix A, we multiply A by the matrix E where 
E is equal to the identity matrix except the i,j entry is E(i,j) = k
"""

"""
@ <==>
for i in range(len(matrix1)): 
    for j in range(len(matrix2[0])): 
        for k in range(len(matrix2)): 
            res[i][j] += matrix1[i][k] * matrix2[k][j] 
"""

def switch_rows(A,i,j):
    # Switch rows i and j in matrix A
    n = A.shape[0]
    E = np.eye(n)
    E[i,i] = 0
    E[j,j] = 0
    E[i,j] = 1
    E[j,i] = 1
    return E @ A
 
"""
explanation for switch_rows : We do it for switch row i and row j in a matrix A
we multiply A by the matrix E where E is equal to the identity matrix except E(i,i) = 0, E(j,j) = 0, E(i,j) = 1  and E(j,i) = 1
"""


def scale_row(A,k,i):
    # Multiply row i by k in matrix A
    n = A.shape[0]
    E = np.eye(n)
    E[i,i] = k
    return E @ A

"""
explanation for scale_row : come on , you expect me to explain everything; please think and look at 
previous explanations again :)))
it is the same when you want to add_row(A,k-1,i,i)
"""

def find_answer(q,x,y,n):
    str_answer = "X{} = ".format(y+1)
    for j in range(n,y,-1):
        if q[x][j] == 0:
            continue
        if j==n:
            str_answer += "{} ".format(round(q[x][j],2))
        else:
            str_answer += "+ ({})X{} ".format(round(q[x][j]*-1,2),j+1)
    print(str_answer)

"""
explanation for find_answer : this function produce answer like : X1 = (5)X2 + 25
"""

# def solve_floating_point(ans):
#     if math.ceil(ans) - ans < 0.00000000001:
#         ans = math.ceil(ans)
#     elif ans - math.floor(ans) < 0.00000000001:
#         ans = math.floor(ans)
#     return ans


# system of inputing
print("coefficient matrix : ")
print("Enter number of rows and columns:")
r = int(input().split(" ")[0])
qa = []
for num in range(r):
    print("Enter row {}: ".format(num))
    qa.append(list(map(int,input().split())))
print("Enter constant valuesv:")
qq = list(map(int,input().split()))
qqq = []
for num in qq:
    qqq.append([num])
q = np.hstack([qa,qqq])


# some example
# a = np.array([[1, -2, 1], [0, 2, -8], [5, 0, -5]])
# b = np.array([[0],[8],[10]]) 
# q = np.hstack([a,b])
# q = np.array([[0, 0, 1, -2, -3], [1, -7, 0, 6, 5],[-1, 7, -4, 2, 7]])
# q = np.array([[1, -7, 0, 6, 5], [0, 0, 1, -2, -3], [-1, 7, -4, 2, 7], ])
# q = np.array([[0, 3, -6, 6, 4, -5], [3, -9, 12, -9, 6, 15], [3, -7, 8, -5, 8, 9]])
# q = np.array([[6, 15, 1, 2], [8, 7, 12, 14],[2, 7, 8, 10]])
# q = np.array([[4, 3, 2, 25], [-2, 2, 3, -10], [3, -5, 2, -4]])
# q = np.array([[0, 1, -4, 8], [2, -3, 2, 1], [4, -8, 12, 1]])


n = q.shape[1]-1
m = q.shape[0]
print("Given Matrix : ")
print(q)


# main algorithm

x_pivot = 0
y_pivot = 0

"""
this part of code use for making matrix to echelon form
"""
while x_pivot != m and y_pivot !=n:

    if_pivot = False
    j = y_pivot
    
    if q[x_pivot][y_pivot] == 0:
        for i in range(x_pivot+1, m):
            if q[i][j] == 0:
                continue
            else:
                q = switch_rows(q, i, x_pivot)
                pivot_position = q[x_pivot][y_pivot]
                if_pivot = True
                break
        if if_pivot is False:
            for j in range(y_pivot,n):
                if q[x_pivot][j] == 0:
                    continue
                else:
                    y_pivot = j
                    pivot_position = q[x_pivot][y_pivot]
                    if_pivot = True
                    break
    else:
        pivot_position = q[x_pivot][y_pivot]

    for i in range(x_pivot+1, m):
        if q[i][j] == 0:
            continue
        q = add_row(q, -(q[i][j]/pivot_position), x_pivot, i)

    x_pivot += 1
    y_pivot += 1


"""
this part of code use for checking if the matrix is inconsistent
"""
for i in range(m):
    consistent = False
    for j in range(n):
        if q[i][j] != 0:
            consistent = True
            break
    if consistent is True:
        continue
    if q[i][n] != 0:
        print("inconsistent")
        exit()


x_pivot = m-1
y_pivot = n-1

"""
this part of code use for making matrix to reduced row echelon form
"""
while x_pivot != 0 and y_pivot != 0:
    
    if_pivot =False
    j = y_pivot
    for j in range(y_pivot,0,-1):
        if q[x_pivot][j] != 0 and q[x_pivot][j-1] == 0:
            y_pivot = j
            pivot_position = q[x_pivot][y_pivot]
            if_pivot = True
            break

    if if_pivot is False:
        x_pivot += -1
        continue

    q = scale_row(q,(1/q[x_pivot][y_pivot]),x_pivot)
    pivot_position = q[x_pivot][y_pivot]

    for i in range(x_pivot-1,-1,-1):
        if q[i][j] == 0:
            continue
        q = add_row(q, -(q[i][j]/pivot_position), x_pivot, i)

    x_pivot += -1
    y_pivot += -1

if q[0][0] != 1:
    q = scale_row(q,(1/q[0][0]),0)

np.set_printoptions(2)
print("Reduced row echelon form : ")
print(q)


# system of outputing

print("answer : ")
x_pivot = 0
y_pivot = 0
pivot_list = []
while x_pivot != m and y_pivot !=n:

    if q[x_pivot][y_pivot] == 1:
        #answer
        # print("x{} ".format(y_pivot+1))
        pivot_list.append(y_pivot+1)
        find_answer(q,x_pivot,y_pivot,n)
        x_pivot += 1
        y_pivot += 1
        continue

    for j in range(y_pivot+1,n):
        if q[x_pivot][j] == 1:
            #answer
            pivot_list.append(j+1)
            # print("x{} ".format(j+1))
            find_answer(q,x_pivot,j,n)
            break

    x_pivot += 1
    y_pivot += 1

            
jj = 0
for j in range(n):
    if pivot_list[jj] == j+1:
        if jj != len(pivot_list)-1:
            jj += 1
        continue
    print("X{} is free variable".format(j+1))
    

"""
and in this part I want to mention that exist easier ways
and they are using :
1- np.linalg.solve(A,B)
2- np.linalg.inv(A).dot(B)
"""

"""
Ok , in this part my code will be finished
and i hope it satisfies you and having a lot of extra point :)))
but if you have any question about my project 
you can contact with me by these ways :
Telegram = @rajabi2001
Email = mjr80.2001@gmail.com , rajabi2001@aut.ac.ir
"""