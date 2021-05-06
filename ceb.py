#https://ceb.mu/customer-corner/tariff/domestic-tariff
MINIMUM_CHARGE = 44
FIRST25 = 3.16
NEXT25 = [4.38, 4.74, 5.45]
NEXT100 = 6.15
NEXT50 = [7.02, 7.90]
ADDITIONAL = 8.77

#user input
unit = int(input('CEB kWh used: '))

UNIT = unit
rate = 'MINIMUM_CHARGE'
charge = MINIMUM_CHARGE
savings = [0, 0]

#FIRST25
gamut = 25
if unit > gamut:
    charge += gamut * FIRST25
    unit -= gamut
else:
    rate = 'FIRST25'
    charge += unit * FIRST25
    savings[0] = unit
    savings[1] = unit * FIRST25
    
#NEXT25 
gamut = 25
for i in range(3):
    if unit > gamut:
        charge += gamut * NEXT25[i]
        unit -= gamut
    elif rate == 'MINIMUM_CHARGE':
        rate = 'NEXT25(' + str(i + 1) + ')'
        charge += unit * NEXT25[i]
        savings[0] = unit
        savings[1] = unit * NEXT25[i]

#NEXT100  
gamut = 100
if unit > gamut:
    charge += gamut * NEXT100
    unit -= gamut
elif rate == 'MINIMUM_CHARGE':
    rate = 'NEXT100'
    charge += unit * NEXT100
    savings[0] = unit
    savings[1] = unit * NEXT100
    
#NEXT50
gamut = 50
for i in range(2):
    if unit > gamut:
        charge += gamut * NEXT50[i]
        unit -= gamut
    elif rate == 'MINIMUM_CHARGE':
        rate = 'NEXT50(' + str(i + 1) + ')'
        charge += unit * NEXT50[i]
        savings[0] = unit
        savings[1] = unit * NEXT50[i]
    
#ADDITIONAL  
if rate == 'MINIMUM_CHARGE':
    rate = 'ADDITIONAL'
    charge += unit * ADDITIONAL
    savings[0] = unit
    savings[1] = unit * ADDITIONAL
    
print("Charge is Rs {} under the {} rate for {} units.".format(charge, rate, UNIT))

if savings[0] < (UNIT / 2):
    print("But... you could save Rs {} if you remove {} units off the cardboard...".format(savings[1], savings[0]))
