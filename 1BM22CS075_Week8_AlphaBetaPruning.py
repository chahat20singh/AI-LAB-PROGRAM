import math

# Function to implement Alpha-Beta Pruning
def alpha_beta_pruning(node, depth, alpha, beta, maximizing_player, tree):
    # Base case: If depth is zero or we reach a leaf node
    if depth == 0 or node not in tree:
        return node  # Return the node value (leaf node)

    if maximizing_player:
        max_value = -math.inf
        for child in tree[node]:
            value = alpha_beta_pruning(child, depth-1, alpha, beta, False, tree)
            max_value = max(max_value, value)
            alpha = max(alpha, value)
            if beta <= alpha:
                print(f"Pruning at node {child} as beta ({beta}) <= alpha ({alpha})")
                break  # Beta cutoff
        return max_value

    else:
        min_value = math.inf
        for child in tree[node]:
            value = alpha_beta_pruning(child, depth-1, alpha, beta, True, tree)
            min_value = min(min_value, value)
            beta = min(beta, value)
            if beta <= alpha:
                print(f"Pruning at node {child} as beta ({beta}) <= alpha ({alpha})")
                break  # Alpha cutoff
        return min_value

# Function to create the tree dynamically
def create_tree():
    tree = {}
    nodes = input("Enter the nodes separated by commas (e.g., A, B, C): ").split(", ")
    for node in nodes:
        children = input(f"Enter children for node {node} separated by commas (e.g., 3, 5): ").split(", ")
        tree[node] = [int(child) if child.isdigit() else child for child in children]
    return tree

# Function to get the depth
def get_depth():
    while True:
        try:
            depth = int(input("Enter the depth of the tree: "))
            if depth < 0:
                raise ValueError
            return depth
        except ValueError:
            print("Invalid input. Please enter a non-negative integer.")

# Function to get the starting node (root)
def get_root():
    return input("Enter the root node: ")

# Main function to run the program
def main():
    print("Welcome to Alpha-Beta Pruning with Dynamic Input!")

    # Create the tree dynamically
    tree = create_tree()

    # Get user input for root node, depth, alpha, and beta values
    root = get_root()
    depth = get_depth()
    alpha = -math.inf
    beta = math.inf

    # Call the Alpha-Beta Pruning function
    print("\nRunning Alpha-Beta Pruning...")
    result = alpha_beta_pruning(root, depth, alpha, beta, True, tree)

    # Print the final result
    print(f"The optimal value is: {result}")

# Run the main function
if __name__ == "__main__":
    main()
