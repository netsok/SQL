import copy

grid = [['.', '.', '.', '.', '.', '.',],
        ['.', '0', '0', '.', '.', '.',],
        ['0', '0', '0', '0', '.', '.',],
        ['0', '0', '0', '0', '0', '.',],
        ['.', '0', '0', '0', '0', '0',],
        ['0', '0', '0', '0', '0', '.',],
        ['0', '0', '0', '0', '.', '.',],
        ['.', '0', '0', '.', '.', '.',],
        ['.', '.', '.', '.', '.', '.',]]

# grid[x][y]
# Eerst van 0 naar 9 op x (eerste coordinaat, verticaal)
# Dan van 0 naar 6 op y (tweede coordinaat, horizontaal)

# First create empty new list
grid2 = []

# Now add needed number of sublists (=equal to length of current sublists)
# grid2 bevat 6 lists
for i in range(len(grid[0])):
    grid2.append(list())

# Now populate the sublists in grid2 from grid1:
for i in range(len(grid)):
    for j in range(len(grid[i])):
        grid2[j].insert(i, grid[i][j])

# Finally, print the result of grid and grid2 (method join() helps us):
print('Original grid: ')
for i in range(len(grid)):
    print(''.join(grid[i]))
    
print('\nTransformed grid: ')
for i in range(len(grid2)):
    print(''.join(grid2[i]))

print('\nOriginal grid (without using join method): ')
# Print without new list:
for i in range(len(grid)):
    for j in range(len(grid[i])-1):
        print(grid[i][j], end='')
    
    print(grid[i][len(grid[i])-1])
        
print('\nTransformed grid (without using join method or creating a new grid): ')
# Print without new list:
for j in range(len(grid[i])):
    for i in range(len(grid)-1):
        print(grid[i][j], end='')
    
    print(grid[i][len(grid[j])-1])
