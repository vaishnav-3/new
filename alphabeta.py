#alphabeta
max_value = 1000
min_value = -1000

def minmax(depth, node_index, maximizing_player, values, alpha, beta):
    if depth == 3:
        return values[node_index]
    
    if maximizing_player:
        best = min_value
        for i in range(2):
            child_index = node_index * 2 + i
            if child_index < len(values):
                val = minmax(depth + 1, child_index, False, values, alpha, beta)
                best = max(best, val)
                alpha = max(alpha, best)
                if beta <= alpha:
                    break
        return best
    else:
        best = max_value
        for i in range(2):
            child_index = node_index * 2 + i
            if child_index < len(values):
                val = minmax(depth + 1, child_index, True, values, alpha, beta)
                best = min(best, val)
                beta = min(beta, best)
                if beta <= alpha:
                    break
        return best

if __name__ == "__main__":
    values = []
    n = int(input("Enter the number of elements in the values array: "))
    for _ in range(n):
        value = int(input("Enter a value: "))
        values.append(value)

    result = minmax(0, 0, True, values, min_value, max_value)
    print("The result of the minmax algorithm is:", result)



#chatbot 
def simple_chatbot():
    print("Chatbot: Hi! I'm a simple chatbot. Type 'bye' to exit.")
    
    while True:
        user_input = input("You: ")
        
        # Convert the user input to lowercase for case-insensitive matching
        user_input_lower = user_input.lower()
        
        if user_input_lower == 'bye':
            print("Chatbot: Goodbye! Have a great day.")
            break
        elif 'how are you' in user_input_lower:
            print("Chatbot: I'm just a computer program, but I'm doing well. How can I help you?")
        elif 'your name' in user_input_lower:
            print("Chatbot: I'm just a chatbot, so I don't have a name.")
        elif 'thank you' in user_input_lower:
            print("Chatbot: You're welcome!")
        else:
            print("Chatbot: I'm sorry, I didn't understand that. Can you please rephrase or ask something else?")

if __name__ == "__main__":
    simple_chatbot()


#selection

def selection_sort(arr):
    n = len(arr)

    for i in range(n - 1):
        # Find the index of the minimum element in the unsorted part
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        # Swap the found minimum element with the first element
        arr[i], arr[min_index] = arr[min_index], arr[i]

if __name__ == "__main__":
    # Take user input for the array
    user_input = input("Enter elements separated by space: ")
    input_array = list(map(int, user_input.split()))

    print("Original Array:", input_array)

    # Apply Selection Sort
    selection_sort(input_array)

    print("Sorted Array:", input_array)




#nqueen

def is_safe(board, row, col):

    for i in range(row):
        if board[i][col] == 1:
            return False

    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    return True

def solve_n_queens(N):
    board = [[0] * N for _ in range(N)] 
    solutions = []

    def backtrack(row):
        if row == N:
            solutions.append(["".join("Q" if cell == 1 else "." for cell in row) for row in board])
            return

        for col in range(N):
            if is_safe(board, row, col):
                board[row][col] = 1  
                backtrack(row + 1) 
                board[row][col] = 0 

    backtrack(0) 
    return solutions

def print_solutions(solutions):
    for i, solution in enumerate(solutions):
        print(f"Solution {i + 1}:")
        for row in solution:
            print(row)
        print()

N = 4
solutions = solve_n_queens(N)

if solutions:
    print_solutions(solutions)
else:
    print("No solutions found")




#bfsdfs
from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def dfs_recursive(self, vertex, visited):
        visited[vertex] = True
        print(vertex, end=' ')

        for neighbor in self.graph[vertex]:
            if not visited[neighbor]:
                self.dfs_recursive(neighbor, visited)

    def dfs(self, start_vertex):
        visited = [False] * len(self.graph)
        print("Depth-First Search (DFS):")
        self.dfs_recursive(start_vertex, visited)
        print()

    def bfs(self, start_vertex):
        visited = [False] * len(self.graph)
        queue = [start_vertex]
        visited[start_vertex] = True

        print("Breadth-First Search (BFS):")
        while queue:
            current_vertex = queue.pop(0)
            print(current_vertex, end=' ')

            for neighbor in self.graph[current_vertex]:
                if not visited[neighbor]:
                    queue.append(neighbor)
                    visited[neighbor] = True
        print()

# Example usage:
g = Graph()
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 0)
g.add_edge(2, 3)
g.add_edge(3, 3)

start_vertex = 0

g.dfs(start_vertex)
g.bfs(start_vertex)
