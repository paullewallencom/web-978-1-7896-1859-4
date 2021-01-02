#! /usr/bin/python

print 'Content-type: text/html'
print ''

name = "Kirsten"

if name == "Rob" or name == "Kirsten" :
    print "Hello " + name
else:
    print "I don't know you"

# Create a program which displays the first 50 prime numbers 2, 3, 5, 7, 11...

numberOfPrimes = 0
number = 2

while numberOfPrimes < 50:
    isPrime = True
    
    for i in range(2, number):
        if number % i == 0:
            isPrime = False
    
    if isPrime == True:
        print number
        numberOfPrimes += 1
    
        
    number += 1
