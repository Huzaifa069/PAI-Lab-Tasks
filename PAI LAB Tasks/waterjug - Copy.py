from collections import deque

def waterJugProblem(capacity1, capacity2, goal):
    queue = deque([(0, 0)])
    visited = set([(0, 0)])

    while queue:
        jug1, jug2 = queue.popleft()
        print(jug1, jug2)

        if jug1 == goal or jug2 == goal:
            print("Solution Found")
            return True

        # Possible actions
        moves = [
            (capacity1, jug2),  # Fill jug1
            (jug1, capacity2),  # Fill jug2
            (0, jug2),          # Empty jug1
            (jug1, 0),          # Empty jug2
            (jug1 - min(jug1, capacity2 - jug2), jug2 + min(jug1, capacity2 - jug2)),  # Pour jug1 → jug2
            (jug1 + min(jug2, capacity1 - jug1), jug2 - min(jug2, capacity1 - jug1))   # Pour jug2 → jug1
        ]

        for state in moves:
            if state not in visited:
                visited.add(state)
                queue.append(state)

    print("No Solution Found")
    return False

# Example usage
waterJugProblem(4, 3, 2)
