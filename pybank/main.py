import os

filepath = os.path.join('resources','budget_data.csv')
filepath2 = os.path.join('analysis','log.txt')
filtxt = open(filepath2,'w')

import csv
Dates = []
Changebymonth = []
totalrec = 0
totalPL = 0
totaldif = 0

with open(filepath, "r") as f:

    csv_reader = csv.reader(f,delimiter=",")
    next(csv_reader)
    difference = 0
    for row in csv_reader:
        newcol = int(row[1])- difference  
        difference = int(row[1])      
        Dates.append(row [0])
        if totalrec == 0:
            newcol = 0
        Changebymonth.append(newcol)
        totalrec = totalrec + 1
        totalPL = totalPL + int(row[1])
        totaldif = totaldif + newcol


average = ("{:.2f}".format(totaldif/(totalrec-1)))


Maxval = (max(Changebymonth))
Minval = (min(Changebymonth))
Maxval_Index = Changebymonth.index(Maxval)

Minval_Index = Changebymonth.index(Minval)
print ("")
print('Financial Analysis')
print ('------------------------------------')
print ("")
print('Total months:', totalrec)
print('Total: ',("${:.0f}".format(totalPL)))
print ('Average Change: ',("{}".format('$' + average)))
print ('Greatest Increase in profits:' , Dates[Maxval_Index]  , ("{}".format('($' + (str(Maxval)) + ')' )))
print ('Greatest Decrease in profits:' , Dates[Minval_Index]  , ("{}".format('($' + (str(Minval)) + ')' )))

print ("", file = filtxt)
print('Financial Analysis',file = filtxt)
print ('------------------------------------',file = filtxt)
print ("",file = filtxt)
print('Total months:', totalrec, file = filtxt)
print('Total: ',("${:.0f}".format(totalPL)), file = filtxt)
print ('Average Change: ',("{}".format('$' + average)), file = filtxt)
print ('Greatest Increase in profits:' , Dates[Maxval_Index]  , ("{}".format('($' + (str(Maxval)) + ')' )), file = filtxt)
print ('Greatest Decrease in profits:' , Dates[Minval_Index]  , ("{}".format('($' + (str(Minval)) + ')' )), file = filtxt)
filtxt.close()      
        