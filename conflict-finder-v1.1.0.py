import re, sys
from typing import Union

if len(sys.argv) < 2: raise Exception("No schedule provided")

def find_conflicts(transactions:[str], resources:[str]) -> [[str]]:
    conflicts = []
    for x, g in zip(transactions, resources):
        if len(x)==1: continue
        for a in range(len(x)):                                             #a is the current referenced entry in sublist of transactions (x)
            for b in range(a, len(x)):                                      #b is every entry after a, thus reducing the number of comparisons by half
                try:                                                        #checks a against b based on given ruleset and if they are the same transaction 
                    conflicts += [] if ruleset[x[a][0]+x[b][0]] or x[a][1] == x[b][1] else [[x[a],g,x[b],g]]    
                except:
                    return(-1)
    return conflicts

ruleset = {"rr":1, "rw":0, "wr":0, "ww":0}

for count, schedule in enumerate(sys.argv[1:], start=1):
    schedule = "?"+re.sub(r"[^a-zA-Z0-9$]+", '', schedule)                  #deletes special chars to reduce runtime and offsets string by 1 (with '?')
    transactions, resources, conflicts = [], [], []
    resources = list(set([x for x in schedule[::3]][1:]))                   #extracts every unique resourcesource in given string
    
    for i, x in enumerate(resources):                                       #groups transactions by used resources
        transactions += [[schedule[c-2:c] for c,a in enumerate(schedule) if a is x]]
    conflicts = find_conflicts(transactions, resources)
    if conflicts == -1: 
        print("\nSchedule %s could not get resolved due to wrong format" % count)
        print("Format of schedule has to be 'w1(x),r2(y),...' or 'w1x,r2y,...'")
        continue
        
    print("\n>>>> Conflicts of schedule %s <<<<\n" % count)
    if(conflicts == []): print("No conflicts"); continue
    for i, x in enumerate(conflicts, start=1): 
        print("%s : (%s(%s), %s(%s))" % (i, x[0],x[1],x[2],x[3]))
