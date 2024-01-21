# the design of the test cases

## base case
There are 7 cases of converting: I, V, X, L, C, D, M

## boundary value Condition
1. Min case: 1 <-> I
2. Max case: 3999 <-> MMMCMXCIX

## 1st Approach
### addition case
Arabic | Roman
----------|-----------
2 | II
3 | III
6 | VI
7 | VII
...

### subtraction case
Arabic | Roman
----------|-----------
4 | IV
9 | IX
49 | IL
99 | IC
...

### mixed case 
Arabic | Roman
----------|-----------
42 | XLII
24 | XXIV
256 | CCLVI
...

## 2nd approach
### unit case
Arabic | Roman
----------|-----------
1 | I
2 | II
3 | III
4 | IV
5 | V
6 | VI
7 | VII
8 | VIII
9 | IX

### ten case 
Arabic | Roman
----------|-----------
10 | X
11 | XI
12 | XII
...