def check (grid,row,colm,num):
    for i in range(9):
        if grid[row][i] == num or grid[i][colm]==num:
            return False
    
    choti_grid_row=3*(row//3)
    choti_grid_colm=3*(colm//3)
    for i in range(3):
        for j in range (3):
            if grid[choti_grid_row+i][choti_grid_colm+j]==num:
                return False
        
    return True

def khaali_finder(grid):
    for row in range (9):
        for colm in range (9):
            if grid[row][colm]==0:
                return row,colm
    return None

def dimaag_solver(grid):
    flag = True 
    while flag:
        flag=False
        possible=[]
        for row in range (9):
            row_possible=[]
            for colm in range (9):
                if grid[row][colm]==0:
                    valid_possibilities=[num for num in range (1,10) if check (grid,row,colm,num)]
                    row_possible.append(valid_possibilities)
                else:
                    row_possible.append([])
            possible.append(row_possible)

        for row in range(9):
            for colm in range(9):
                if len(possible[row][colm])==1:
                    grid[row][colm]=possible[row][colm][0]
                    flag=True

        for num in range (1,10):
            for choti_grid_row in range (0,9,3):
                for choti_grid_colm in range (0,9,3):
                    positions = [(row, colm) for row in range(choti_grid_row, choti_grid_row + 3)
                                 for col in range(choti_grid_colm, choti_grid_colm + 3)
                                 if grid[row][colm] == 0 and num in possible[row][colm]]
                    if len(positions)==1:
                        row,colm=positions[0]
                        grid[row][colm]==num
                        flag=True

def last_resort(grid):
    khaali=khaali_finder(grid)
    if not khaali:
        return True
    else:
        row,colm=khaali
        for num in range (1,10):
            if check(grid,row,colm,num):
                grid[row][colm]=num
                if last_resort(grid):
                    return True
                
                grid [row][colm]=0
        return False
    
def efficient_solver(grid):
    dimaag_solver(grid)
    if khaali_finder(grid):
        print("\nGoing to backtrack\n")
        last_resort(grid)

def output(grid):
    for i,row in enumerate(grid):
        if i%3==0 and i!=0:
            print("-"*21)
        print(" | ".join(" ".join(str(num)if num!=0 else '.' for num in row[j:j+3]) for j in range(0,9,3)))

sudoko=[]
print("Enter the sudoku puzzle rowwise and use 0 for empty cell.")
for i in range(9):
    while True:
        print(f"Enter row {i+1} (seperated by spaces): ")
        x=input().strip()
        try:
            row=list(map(int,x.split()))
            if len(row)==9 and all(0<=num <=9 for num in row):
                sudoko.append(row)
                break
            else:
                print("Invalid input")
        except ValueError:
            print("Invalid input, enter numbers")

print("\nOriginal Puzzle:- \n")
output(sudoko)
print("\nSolved Puzzle:- \n")
efficient_solver(sudoko)
output(sudoko)






    