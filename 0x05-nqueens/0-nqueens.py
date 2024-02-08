#!/usr/bin/python3
"""N Queens Interview task"""

import sys

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print('N must be a number')
        sys.exit(1)

    if n < 4:
        print('N must be at least 4')
        sys.exit(1)

    solutions = []
    queens = []
    row, col = 0, 0

    while row < n:
        is_safe = True
        while col < n:
            for q in queens:
                q_row, q_col = q[0], q[1]
                if col == q_col or row+col == q_row+q_col or row-col == q_row-q_col:
                    is_safe = False
                    break
            
            if is_safe:
                queens.append([row, col])
                if row == n-1:
                    solutions.append(queens[:])
                    queens.pop()
                    if col == n-1:
                        queens.pop()
                        if len(queens) == 0:
                            break
                        col = queens.pop()[1] + 1
                        row -= 1
                    else:
                        col += 1
                else:
                    col = 0
                    row += 1
                break

            if col == n-1:
                queens.pop()
                if len(queens) == 0:
                    break
                col = queens.pop()[1] + 1
                row -= 1
            else:
                col += 1
        
    for sol in solutions:
        print(sol)
