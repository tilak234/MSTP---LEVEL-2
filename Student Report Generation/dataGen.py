import random
import csv
import datetime
#pre-defined list of names included in names.py
import names

#filename with current time
dt = str(datetime.datetime.now().strftime('%Y%m%d%H%M%S'))
filename = 'StudentData'+dt+'.csv'
#By default gave it to generate 4000 students data
num = int(input("Howmany students data needed???"))

#create StudentData file in folder - StudentData
myfile = open('StudentData/'+filename,'w', newline='')
columnTitleRow = "Student Name, Subject-I \n"
myfile.write(columnTitleRow)

for i in range(num):
    #Random Name Generation using names.py data    
    name = random.choice(names.first_names)+' '+random.choice(names.last_names)
    #Random Marks Generation
    s1 = random.randint(0,100)
    row = [name,s1]
    wr = csv.writer(myfile)
    wr.writerow(row)
#close file
myfile.close()
                

print(filename+ " Generated Successfully")
