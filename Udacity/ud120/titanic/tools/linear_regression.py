#!/usr/bin/python

def linearReg(x_train, y_strain):
    ### import the sklearn regression module, create, and train your regression
    ### name your regression reg
    
    ### your code goes here!
    from sklearn import linear_model
    reg = linear_model.LinearRegression()
    reg.fit (x_train, y_strain)

    print "new slope", reg.coef_
    
    return reg
