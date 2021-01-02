#! /usr/bin/python

print 'Content-type: text/html'
print ''

for i in range(5, 11):
    print i
    
print "Rob"

favouriteFoods = ["Pizza", "Chocolate", "Ice Cream"]

for food in favouriteFoods:
    print "I like eating " + food + "."
    

x = 0
while x <= 10:
    print x
    x += 1
    

# Dictionary - 4 names (key) and ages (value) of people
# Loop which prints. eg. Sam is 7

ages = {}
ages["Rob"] = 35
ages["Kirsten"] = 36
ages["Tommy"] = 5
ages["Ralphie"] = 1

for age in ages:
    print age + " is " + str(ages[age])




