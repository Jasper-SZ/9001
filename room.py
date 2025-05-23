def display_map(grid: list[list[str]]):
    for i in range(len(grid)):
        s = ''
        for j in range(len(grid)):
            if  j == len(grid)-1:
                s = s + ' ' + grid[i][j]
            else:
                s = s + ' ' + grid[i][j] + ' '
        print(s)

#display_map(default_map)
