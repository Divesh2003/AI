def printLatin(n):
    k = n + 1

    # Loop to print rows
    for i in range(1, n + 1, 1):

        temp = k
        while temp <= n:
            print(temp, end=" ")
            temp += 1

        for j in range(1, k):
            print(j, end=" ")

        k -= 1
        print()


# Driver Code
n = 5
printLatin(n)