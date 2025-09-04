def pattern(rows, col):
    for i in range (rows):
        for j in range(col):
            print('*', end=" ")
        print()
pattern(5,5)