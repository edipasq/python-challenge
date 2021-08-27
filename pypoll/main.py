import os


filepath = os.path.join('resources','election_data.csv')
filepath2 = os.path.join('analysis','log.txt')
filtxt = open(filepath2,'w')

import csv
Candlst = []
dict = {}
totalrec = 0


with open(filepath, "r") as f:

    csv_reader = csv.reader(f,delimiter=",")
    next(csv_reader)
    
    for row in csv_reader:
        totalrec = totalrec + 1
        val = dict.get((row[2]),0)
        key = row[2]        
        if val == 0:
             dict[key] = 1
             Candlst.append(key)
            
        else:
            dict[key] = (int(dict[key])) + 1


max_key = max(dict.values())

print ("Election Results")
print ("-------------------------")
print ("Total votes:", totalrec)
print ("-------------------------")

print ("Election Results", file = filtxt)
print ("-------------------------", file = filtxt)
print ("Total votes:", totalrec,    file = filtxt)
print ("-------------------------", file = filtxt)

for i in Candlst:
    porcentage = ("{:.3f}".format(dict[i]/(totalrec)*100))
    porcentage = (str(porcentage + "%"))
    print((i + ":") , porcentage, ("(" + str(dict[i]) + ")") )
    print((i + ":") , porcentage, ("(" + str(dict[i]) + ")") , file = filtxt)
    if dict[i] == max_key:       
        Winner = i

print("--------------------------------", file = filtxt)
print("--------------------------------")
print("Winner:", Winner , file= filtxt)  
print("Winner:", Winner)  
print("--------------------------------", file = filtxt)
print("--------------------------------")
    
filtxt.close()
