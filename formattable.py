# Takes a csv file with numbers above
# three percentages and returns
# A csv with num(%) format
import csv
import os

k = 1;
os.chdir(r'C:\Users\nsd004\Desktop')

output_ary = []
with open("temp.csv",'rt') as f:
    reader = csv.reader(f, delimiter= ',')
    zerovar = 0
    for row in reader:
        if zerovar in range(0,3):
            output_ary.append(row)
        elif (zerovar+1) % 4 == 0 :
            temp = row
        elif (zerovar)%4 == k :
            if temp[0] != 'Total':
                for i in range(1,(len(temp)-1)):
                    temp[i] += ('('+row[i]+'%)')                            
                output_ary.append(temp)
                temp = []
        zerovar = zerovar + 1
with open("output.csv",'wt') as f2:
    for row in output_ary:
        for item in row[:-1]:
            f2.write(item + ",")
        f2.write(row[-1]+"\n")
