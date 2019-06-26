from __future__ import with_statement
import csv
import datetime

filename = input("Enter file name - ")
#filename with current time
dt = str(datetime.datetime.now().strftime('%Y%m%d%H%M%S'))
#report file
report = 'Report'+dt+'.txt'

#reading csv file
#marks list variable for storing all student marks
marks = []
try:
    #Data files always storing in StudentData folder
    with open('StudentData/'+filename) as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        next(readCSV, None) # skip header line
        for tot,row in enumerate(readCSV):
                marks += [int(row[1])]

        fcount=scount=tcount=flcount = 0
        for fc in marks:
                if(fc>=80):
                        fcount += 1
                elif(fc>65 and fc<80):
                        scount += 1
                elif(fc>45 and fc<65):
                        tcount += 1
                elif(fc<30):
                        flcount += 1
except EnvironmentError:
    print("File Not Found")
    exit()
               
#creating Report file in folder - ReportData
rp = open('ReportData/'+report,'w')

#writing to text file Total Students,First Class,Second Class,Third Class,Failed Students,Highest Mark,Average Mark,Lowest Mark 
rp.write("Student Report - Dated on "+str(datetime.datetime.now())+"\n\n\n")
rp.write("Total Students:"+str(len(marks))+"\n")
rp.write("Highest Mark:"+str(max(marks))+"\n")
rp.write("Lowest Mark:"+str(min(marks))+"\n")
rp.write("Average Mark:"+str(round(sum(marks)/len(marks)))+"\n")
rp.write("First Class:"+str(fcount)+"\n")
rp.write("Second Class:"+str(scount)+"\n")
rp.write("Third Class:"+str(tcount)+"\n")
rp.write("Failed Students:"+str(flcount)+"\n")

#close file
rp.close()

print(report+ " Generated Successfully")

# if __name__ == '__main__':
#     main()
