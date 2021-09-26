
import random

xc = "xc"
hh = "hh"
gs = "gs"

a = [xc, hh, gs]
# for person in a:
#     choices = a[:]
#     choices.remove(person)
#     chance = random.random()
#     rslt = ''
    
#     if chance < 0.1:
#         rslt = person
#     elif chance < 0.55:
#         rslt = choices[0]
#     else:
#         rslt = choices[1]
#     print(person, rslt)

done = False
while not done:
    rsltset = []
    twoEqual = False
    for person in a:
        choices = a[:]
        choices.remove(person)
        chance = random.random()
        rslt = ''
        
        if chance < 0.1:
            rslt = person
        elif chance < 0.55:
            rslt = choices[0]
        else:
            rslt = choices[1]
        print(person, rslt)
        if rslt in rsltset and twoEqual:
            twoEqual = False
            break
        if rslt in rsltset and not twoEqual:
            twoEqual = True
        rsltset.append(rslt)
    print("===========================")
    if twoEqual:
        done = True
    