grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]

print(grid[0])
print(grid[0][0])
print(len(grid))

total = []
for x in range(len(grid)-3):
    answer = []
    for y in range(len(grid)):
        answer.append(grid[y][x])
    total.append(answer) 

for y in range(6):
    line = ''
    for x in range(9):
        line += total[y][x]
    print(line)
