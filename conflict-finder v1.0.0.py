import re, sys

if len(sys.argv) != 2: raise Exception("No schedule provided" if len(sys.argv)<2 else "Too many arguments (only one schedule in string format)")

schedule = "?"+re.sub(r"[^a-zA-Z0-9$]+", '', sys.argv[1])              #'?' is just for offseting the string by 1
transactions, res, conflicts = [], [], []
ruleset = {"rr":1, "rw":0, "wr":0, "ww":0}

res = list(set([x for x in schedule[::3]][1:]))                        #extracts every unique resource in given string
#Groups transactions by used resources
for i, x in enumerate(res):
    transactions += [[schedule[c-2:c] for c,a in enumerate(schedule) if a is x]]

#finds conflicts by checking every entry 
for x, g in zip(transactions, res):
    if len(x)==1: continue
    for a in range(len(x)):                                             #a is the current referenced entry in sublist of transactions (x)
        for b in range(a, len(x)):                                      #b is every entry after a, thus reducing the number of comparisons by half
            try:                                                        #checks a against b based on given ruleset and if a == b        
                conflicts += [] if ruleset[x[a][0]+x[b][0]] or x[a][1] == x[b][1] else [[x[a],g,x[b],g]]    
            except:
                print("\nCouldn't check against ruleset. Format of schedule has to be 'w1(x),r2(y)...' or 'w1x,r2y...'")
                sys.exit(1)
                
print("\n>>>>Conflicts<<<<\n")
for i, x in enumerate(conflicts, start=1): print("%s : (%s(%s), %s(%s))" % (i, x[0],x[1],x[2],x[3]))






