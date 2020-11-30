#Recursive Sudoku Solver from Computerphile by Professor Thorsten Altenkirch
import time
grid = [[5,3,0,0,7,0,0,0,0],
        [6,0,0,1,9,5,0,0,0],
        [0,9,8,0,0,0,0,6,0],
        [8,0,0,0,6,0,0,0,3],
        [4,0,0,8,0,3,0,0,1],
        [7,0,0,0,2,0,0,0,6],
        [0,6,0,0,0,0,2,8,0],
        [0,0,0,4,1,9,0,0,5],
        [0,0,0,0,8,0,0,0,0]]

#Checks if number is present in rows, coloums and 3x3 grid
#Returns True if the number is able to be placed there
def possible(y,x,n):
    global grid
    #Check rows to see if number is present
    for i in range(0,9):
        if grid[y][i]==n:
            return False
    #Check column to see if number is present
    for i in range(0,9):
        if grid[i][x]==n:
           return False

    #Find which 3 by 3 grid the number is in
    x0 = (x//3)*3
    y0= (y//3)*3
    #Check the 3 by 3 grid to see if the number is present
    for i in range(0,3):
        for j in range(0,3):
            if grid[y0+i][x0+j]==n:
                return False

    return True

def solve():
    global grid
    #Find an empty position
    for y in range(9):
        for x in range(9):
            if grid[y][x] == 0:
                #Test all numbers which can be placed there
                for n in range(1,10):
                    if possible(y,x,n):
                        grid[y][x]=n
                        #Recur back
                        solve()
                        #Executed only if backtracked from recursion loop
                        #Showing that the number placed there has created a deadlock
                        grid[y][x] = 0
                #If all the numbers tested fail, then we need to backtrack
                return
    #Executed when there is no more empty spaces
    output()


def output():
    global grid
    print("+" + "---+"*9)
    #Enumerate over rows of the board and get index
    for i, row in enumerate(grid):
        #Formatting and removing 0's
        print(("|" + " {}   {}   {} |"*3).format(*[x if x != 0 else " " for x in row]))
        if i % 3 == 2:
            print("+" + "---+"*9)
        else:
            print("+" + "   +"*9)

    time.sleep(0.5)
    #Backtracks and finds other solutions by pretending the solution has failed
    input("\nPress enter for another solution! ")

    #for i in range(9):
        #print(grid[i])
            
def main():
    solve()
    print("\nNo more solutons! ")
        


