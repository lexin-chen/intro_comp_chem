# scan hf/cc-pvdz geom=connectivity

Title

0 1
O
O   1 B1
H   1 B2 2 A2
H   2 B3 1 A3 3 D3
Variables:
B1        1.4016
B2        0.9474
A2       100.7334 
B3        0.9474 
A3       100.7334 
D3      180.00000 72 5.0

m=connectivity
 1 3 1.0
 2 4 1.0
 3 
 4

