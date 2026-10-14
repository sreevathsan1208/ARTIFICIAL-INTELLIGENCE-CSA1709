from collections import deque

def water_jug_bfs(jug1_cap, jug2_cap, target):
    visited = set()
    queue = deque()
    
    # Store tuples of (Jug1, Jug2, path_taken)
    queue.append((0, 0, []))
    
    while queue:
        j1, j2, path = queue.popleft()
        
        # If target is reached
        if j1 == target or j2 == target:
            path.append((j1, j2))
            for step in path:
                print(f"Jug1: {step[0]}L, Jug2: {step[1]}L")
            return True
            
        if (j1, j2) in visited:
            continue
            
        visited.add((j1, j2))
        path.append((j1, j2))
        
        # All possible operations
        transitions = [
            (jug1_cap, j2), # Fill Jug 1
            (j1, jug2_cap), # Fill Jug 2
            (0, j2),        # Empty Jug 1
            (j1, 0),        # Empty Jug 2
            # Pour Jug 1 -> Jug 2
            (j1 - min(j1, jug2_cap - j2), j2 + min(j1, jug2_cap - j2)),
            # Pour Jug 2 -> Jug 1
            (j1 + min(j2, jug1_cap - j1), j2 - min(j2, jug1_cap - j1))
        ]
        
        for state in transitions:
            if state not in visited:
                queue.append((state[0], state[1], path.copy()))
                
    print("No solution possible.")
    return False

# Example: 4L jug, 3L jug, target = 2L
print("Steps to solve Water Jug Problem:")
water_jug_bfs(4, 3, 2)
