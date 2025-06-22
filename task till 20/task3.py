matrix = [[1,  2,  3,  4],
[5,  6,  7,  8],
[9, 10, 11, 12],
[13,14, 15,16]]
#           ij      00 01  02  03  || 13   23   33   ||  32   31   30   ||  
# expected output = 1 , 2 , 3 , 4 ,||  8 , 12 , 16 , ||  15 , 14 , 13 , || 9 , 5 ,  6,7,  11,  10
top=0
for i in range(len(matrix[0])):
    print(matrix[top][i])