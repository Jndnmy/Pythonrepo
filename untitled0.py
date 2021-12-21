# -*- coding: utf-8 -*-
"""
Created on Sun May 16 10:08:10 2021

@author: Jason
"""

def update_weights(m, b):
    learning_rate = 0.0001
    X = [23,67, 78]
    Y = [41,84,100]
    m_deriv = 0
    b_deriv = 0
    N = len(X)
    print ("m =",m)
    print("b =",b)
    print("Loss =",Y[0] - (m*X[0]+ b),"^2 +", Y[1] - (m*X[1]+ b), "^2 +", Y[2] - (m*X[2]+ b),"^2 =", (Y[0] - (m*X[0]+ b)) * (Y[0] - (m*X[0]+ b)) + (Y[1] - (m*X[1]+ b)) * (Y[1] - (m*X[1]+ b)) + (Y[2] - (m*X[2]+ b)) * (Y[2] - (m*X[2]+ b)) ) 
    for i in range(N):
        print("x =",X[i])
        print("y =",Y[i])
        print("f(x) =", (m*X[i]+ b))
        print (Y[i], "-", (m*X[i]+ b), "=", Y[i] - (m*X[i]+ b)  )
        
        # Calculate partial derivatives
        # -2x(y - (mx + b))
        m_deriv += -2*X[i] * (Y[i] - (m*X[i] + b))

        # -2(y - (mx + b))
        b_deriv += -2*(Y[i] - (m*X[i] + b))

    # We subtract because the derivatives point in direction of steepest ascent
   # a= Y[0] - 
    print ("b gradient =",b,"- -2*(", Y[0] - (m*X[0]+ b),"+", Y[1] - (m*X[1]+ b), "+", Y[2] - (m*X[2]+ b),")/3 * 0.0001") 
    print ("m gradient =",m,"- -2*(",X[0],"*", Y[0] - (m*X[0]+ b),"+",X[1],"*", Y[1] - (m*X[1]+ b), "+",X[2],"*", Y[2] - (m*X[2]+ b),")/3 * 0.0001") 
    m -= (m_deriv / float(N)) * learning_rate
    b -= (b_deriv / float(N)) * learning_rate
    print(m)
    print(b)
    return m, b

a = update_weights(1,7)
d = update_weights(a[0],a[1])
c = update_weights(d[0],d[1])
e = update_weights(c[0],c[1])