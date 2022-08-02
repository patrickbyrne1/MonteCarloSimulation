import os, subprocess
import csv


perf_with_one = 0
perf_with_four = 0
test = 0

data_list = []
#fhand = open("proj1.txt", "a")
#fhand.write("Threads\tTrials\tProbability\tPerformance\n")
#fhand.close()
# chose to only use 1, 2, 4, 8, 12, 16 threads
for t in range(1, 9):
    #print ("NUMT = %d" % t)
    # loop through trial using powers of 2 (2^1 - 2^16)
    for s in [1, 10, 100, 1000, 10000, 100000, 1000000]:
        #print("NUMS = %d" %s)
        cmd = "g++ -DNUMTRIALS=%d -DNUMT=%d mCarlo.cpp -o mCarlo -lm -fopenmp" % (s,t)
        #cmd = "g++ -DNUMT=%d mCarlo.cpp -o mCarlo -lm -fopenmp" % (t)
        os.system(cmd)
        
        cmd = "./mCarlo"
        #os.system(cmd)

        result = subprocess.check_output(cmd, shell=True)
        print(result.decode())
        data_list.append(result.decode())
        #test = subprocess.call("./proj0")
        #subprocess.call(["./mCarlo >> proj1.txt"], shell=True)
        #subprocess.call(["\n >> proj1.txt"], shell=True)
        #print()

print(data_list)

with open("data_table.csv", "w") as fh:
    fh.write("Threads,Trials,Probab,MaxPerf") # all kept around 6-7 characters long
    fh.write("\n")
    for x in data_list:
        fh.write(x)

list1=[]
list2=[]
with open("data_table.csv") as fh:
    stuff = fh.read()
    list1 = stuff.split("\n")
    #list2 = list1.split(",")

print(list1)

for x in range(1,len(list1)-1):
    temp_list = list1[x].split(",")
    print("""
Threads: {}
Trials: {}
Probability: {} 
Max Performance: {}
""".format(temp_list[0],temp_list[1],temp_list[2],temp_list[3]))


#print(data_list)

dataFreq = {}
probPerf = {}


threadList = []
perfList = []
probPerfList = []


for x in range(len(data_list)):
    #print(data_list[x], end="")
    numThreads = int(data_list[x].split(",")[0])
    threadList.append(numThreads)
    maxPerf = float(data_list[x].rsplit(",", 1)[1])
    prob = float(data_list[x].split(",")[2])
    perfList.append(maxPerf)
    probPerfList.append([prob,maxPerf])
    if (x+1)%7 == 0 and x != 0:
        dataFreq.update({ threadList[x]: perfList})
        probPerf.update({ threadList[x]: probPerfList})
        perfList = []
        probPerfList = []
    #print("Threads: {}   Max Performance: {}".format(numThreads, maxPerf))
#print(dataFreq)
#print(probPerf)

#print(threadList)
#print(perfList)
#threadSet = set(threadList)
#print(threadSet)



with open("proj1.csv", "w") as dfile:
    dfile.write(",1, 10,100,1000,10000,100000,1000000")
    dfile.write("\n")
    for key in dataFreq.keys():
        dfile.write(str(key) + ",")
        for x in dataFreq.get(key):
            dfile.write(str(x) + ",")
        dfile.write("\n")

#for x in [10,50,100,500,1000,5000,10000,50000,100000,500000,1000000]:
    #print("Trials:",x)
    
    #print("Threads:",)


"""
with open("proj1Table.csv", "w") as dfile:
    dfile.write("Threads,Trials,Prob,MaxPerf")
    dfile.write("\n")
    for key in probPerf.keys():
        dfile.write(str(key) + ",")
        for x in dataFreq.get(key):
            dfile.write(str(x) + ",")
        dfile.write("\n")
"""


#new_list = data_list.split("\t")

#print(new_list)


#def data_table(data_list):





"""
fhand = open("proj1.csv")
s = fhand.read()
dataList = s.split(",")
count = 0
for ch in dataList:
    if(count == 0):
        print(ch.strip(), end="\t")
    else:
        print(ch.strip(), end="\t\t")
    count+=1
"""


"""

column = 4
peak1thrd = float(dataList[column].strip())
peak4thrd = float(dataList[column+4].strip())

# calculate speedup
S = peak4thrd/peak1thrd
print("\n\nThe speedup is %f" % S)

# calculate parallel fraction
# from notes: float Fp = (4./3.)*( 1. - (1./S) )
pFraction = (4/3)*(1-(1/S))
print("\nThe parallel fraction is %f" % pFraction)
"""