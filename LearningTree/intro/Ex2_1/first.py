#!/usr/local/bin/python

greeting = "hello"
print (greeting)


num1 = '5'
num2 = '9'

ratio = float(num1)/float(num2)

print(float(num1)/float(num2))

paris_temp = '25'
honolulu_temp = '81'

def C_to_F(cTemp):
    return (float(cTemp)*9.0/5.0) + 32.0
def F_to_C(fTemp):
    return (float(fTemp) - 32.0) *5.0/9.0


print(C_to_F(paris_temp))
print(F_to_C(honolulu_temp))

price = '199.95'

discount_small = .05
discount_med = .10
discount_big = .15

print(float(price)*discount_small)
print(float(price)*discount_med)
print(float(price)*discount_big)

