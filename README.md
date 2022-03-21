# Shopee-Xpress-Delivery-SCL2022-

Description  
<img align="center" width="256" height="256" src="https://user-images.githubusercontent.com/69421979/159207874-b985a10b-3d3b-4af7-8425-ca57fd90fe39.png">


Bob is a Shopee Xpress deliveryman and is delivering a package to his destination. He started his
journey from one of our Shopee warehouses at position (0, 0), and his destination is at the bottom-right
corner of the map. For example, if the map is an 8x8 grid, the destination is (7, 7).
Each step, his car can move 1 square up, down, left, or right. If his car reaches a black hole, it can
teleport to any other location connected to the black hole at no cost, he also can skip the teleport
feature. For example, if the car reaches black hole A at position (1, 1), Bob can teleport to position (0, 5)
without costing an additional step.
Find the least number of steps (shortest path) that Bob can take to move from (0, 0) to the destination.

So, one path of least steps for example map is:
0,0 -> 0,1 -> 1,1/0,5 -> 1,5-> 1,6/7,3 -> 7,2 -> 6,2/6,7-> 7.7 ,
the answer is
7.


**Input**:
The first line contains two numbers
M
,
N
(
)
.
M
refers to the number of rows in themap, and
N
refers to the number of columns in the map.
The next
M
rows contain
N
values
x
ij
(
)
, where 0 means that position
( i, j ) i
s anempty square, and non-zero values mean that a black hole is present in the square. Non-zero values areguaranteed to have at least
2
or more instances on the map. 

**Output**:
To print the integer of the least number of steps needed.
