# DBMS-conflict-finder
A small script I wrote so I don't have to search the schedule conflicts manually. 
Just plug your schedule in the program as the first argument to use it. 

The format has to be "r|w 1-9 a-z, ..." and special characters will be filtered out. Valid inputs would be:

- "w1(x), r2(y), w5(x), w1(y), w3(x), r3(x), w3(y), w1(x), r1(y), w1(z)"
- "w1x, r2y, w5z, r1k"
- "w 9 (A), w 2 b, r 5(K, r7)( K"
