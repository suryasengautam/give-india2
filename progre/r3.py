
n =1
m=1
# def rec2(n):
#     return n+1
# m = rec2(n)
def rec(n,m):
    print(n,end="")
    if n <6:
        rec(n+1,m)
    def increaser():

rec(n,m)




# # Python3 code to demonstrate star pattern

# # function to print a row
# def printn(num):
	
# 	# base case
# 	if (num == 0):
# 		return
# 	print("*", end = " ")

# 	# recursively calling printn()
# 	printn(num - 1)

# # function to print the pattern
# def pattern(n, i):
	
# 	# base case
# 	if (n == 0):
# 		return
# 	printn(i)
# 	print("\n", end = "")
	
# 	# recursively calling pattern()
# 	pattern(n - 1, i + 1)

# # Driver Code
# if __name__ == '__main__':
# 	n = 5
# 	pattern(n, 1)

# # This code is contributed by
# # Surendra_Gangwar

