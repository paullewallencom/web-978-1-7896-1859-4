#! /usr/bin/python

print 'Content-type: text/html'
print ''

def sayHello():
    print "Hello!"
    
sayHello()

def saySomething(something):
    print something
    
saySomething("Hi there!")

def multiplyTwoNumbers(x, y):
    return x * y

print multiplyTwoNumbers(4, 6)

# Create a function highestCommonFactor which returns the highest number that divides into two other numbers exactly

def highestCommonFactor(x, y):
    for i in range (1, x + 1):
        if x % i == 0 and y % i == 0:
            hcf = i
    return hcf

print highestCommonFactor(15, 10)

a = 5
b = 6

def addTwoNumbers():
    c = 8
    return a + b

print addTwoNumbers()
print c
