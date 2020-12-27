n = [0]*16

#get known values
n[1] = int(input("n1 : "))
n[4] = int(input("n4 : "))
n[6] = int(input("n6 : "))
n[11] = int(input("n11 : "))
n[15] = int(input("n15 : "))

#build the base of the pyramid
n[13] = ( (n[1] + n[11] + n[15] ) - 2*( n[6] + n[4] ) ) / 2
n[12] = ( n[4] - n[11] - n[13] ) / 2
n[14] = ( n[6] - n[13] - n[15] ) / 2

#the variabl i_max represents the bigger i value in each row
i_max = 15

#a loop to build the rest of the pyramid
for l in reversed(range(2, 6)):
    stop = i_max - l + 2
    for i in reversed(range((stop), (i_max+1))):
        n[ i - l ] = n[i] + n[ i-1 ]
    i_max -= l

# d represents the index
d = 1

# number of spaces
k = 8

#a loop to print the pyramid
for l in range(1, 6):
    #inner loop to print spaces
    for j in range(1, k):
        print(" ",end="")
    k-=1 
    #inner loop to print values
    for i in range(1, l+1):
        print("#",n[d],"#", end="")
        d+=1
    #break the line after each loop
    print("\r")