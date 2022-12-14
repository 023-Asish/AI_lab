start =[3,3,1]
end = [0,0,0]

def move(state,action):
    if state[2] == 1:
        return [state[i] - action[i] for i in range(3)]
    else:
        return [state[i] + action[i] for i in range(3)]

def is_legal(state):
    if 0 <= state[0] <= 3 and 0 <= state[1] <= 3:
        return True
    else:
        return False

def is_bank_safe(bank):
    if bank[1] > bank[0] and bank[0] != 0:
        return False
    else:
        return True

def is_state_safe(Left_bank_state):
    right_bank_state = [start[i]-Left_bank_state[i] for i in range(3)]
    if is_bank_safe(Left_bank_state) and is_bank_safe(right_bank_state) :
        return True
    else:
        return False

def next_possible_moves(state):
    moves_list = [[1,0,1],[0,1,1],[1,1,1],[2,0,1],[0,2,1]]
    moves = []
    for i in moves_list:
        j = move(state,i)
        if is_legal(j) and is_state_safe(j):
            moves.append(j)
    return moves

solutions = []
def generate_sol(next_state,curPath):
    sol_path = curPath.copy()
    if next_state == end:
        curPath.append(next_state)
        solutions.append(sol_path)
        return
    elif next_state in curPath:
        return
    else:
        sol_path.append(next_state)
        for i in next_possible_moves(next_state):
            generate_sol(i,sol_path)

generate_sol([3,3,1],[])
print("\nPossible way to solve for final state :- ",end= "\n\n")
for path in solutions:
    print("[ ",end = "")
    for state in path:
        print("{} -> ".format(state),end = "")
    print("{} ]".format(end),end = "\n\n")