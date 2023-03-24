%chk=peroxide.chk
#P hf/cc-pvdz geom=connectivity opt=z-matrix

Title Card Required

0 1
 O
 H                  1            B1
 O                  1            B2    2            A1
 H                  3            B3    1            A2    2            D1    0

   B1             0.96000000
   B2             1.32000000
   B3             0.96000000
   A1           109.50000006
   A2           109.50000006
   D1           90.00000000 10 5.0

 1 2 1.0 3 1.0
 2
 3 4 1.0
 4

