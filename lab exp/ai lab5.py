from collections import deque

def is_valid(state):
    m_left, c_left, b_pos, m_right, c_right = state
    # Check for negative counts
    if m_left < 0 or c_left < 0 or m_right < 0 or c_right < 0: 
        return False
    # Check if cannibals outnumber missionaries on either side
    if m_left > 0 and m_left < c_left: 
        return False
    if m_right > 0 and m_right < c_right: 
        return False
    return True

def get_successors(state):
    m_left, c_left, b_pos, m_right, c_right = state
    successors = []
    # Possible moves: (M, C) to transfer
    moves = [(1, 0), (0, 1), (2, 0), (0, 2), (1, 1)]
    
    for m, c in moves:
        if b_pos == 1: # Boat on the left side
            new_state = (m_left - m, c_left - c, 0, m_right + m, c_right + c)
        else:          # Boat on the right side
            new_state = (m_left + m, c_left + c, 1, m_right - m, c_right - c)
            
        if is_valid(new_state):
            successors.append(new_state)
    return successors

def solve():
    # State: (m_left, c_left, boat_on_left, m_right, c_right)
    start_state = (3, 3, 1, 0, 0)
    goal_state = (0, 0, 0, 3, 3)
    
    queue = deque([(start_state, [])])
    visited = set([start_state])

    while queue:
        current_state, path = queue.popleft()
        if current_state == goal_state:
            print("Solution path:")
            for p in path + [current_state]:
                print(p)
            return
            
        for next_state in get_successors(current_state):
            if next_state not in visited:
                visited.add(next_state)
                queue.append((next_state, path + [current_state]))

solve()
