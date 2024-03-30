tree= {
    'S': [['A',1],['B',5],['C',8]],
    'A': [['S',1],['D',3],['E',7],['G',9]],
    'B': [['S',5],['G',4]],
    'C': [['S',8],['G',5]],
    'D': [['A',3]],
    'E': [['A',7]]
}

heuristic_table = {
    'S':8, 'A':8, 'B':4, 'C':3, 'D':99, 'E':99, 'G':0
}

cost_table = {
    'S':0
}

def AStarSearchAlgorithm():
    global tree, heuristic_table
    closed_nodes = []
    opened_nodes = [['S',8]]

    while True:
        fn = [i[1] for i in opened_nodes] # fn = f(n) = h(n) + g(n)
        chosen_node = fn.index(min(fn)) # Choose the node with the minimum f(n) value
        node = opened_nodes[chosen_node][0] # Get the node with the minimum f(n) value
        closed_nodes.append(opened_nodes[chosen_node]) # Add the node to the closed list
        del opened_nodes[chosen_node] # Remove the node from the opened list

        if closed_nodes[-1][0] == 'G':  # If the goal node is reached
            break

        for item in tree[node]:  # Expand the chosen node
            if item[0] in [closed_nodes[i][0] for i in range(len(closed_nodes))]:  # If the node is already visited,
                continue
            cost_table.update({item[0]: cost_table[node] + item[1]})  # Update the cost table
            fn = cost_table[node] + heuristic_table[item[0]] + item[1]  # Calculate f(n) = g(n) + h(n)
            temp = [item[0], fn]  # Store the f(n) value
            opened_nodes.append(temp)  # Add the node to the opened list

    return closed_nodes

if __name__ == '__main__':
    visited_nodes = AStarSearchAlgorithm()
    print("Visited Nodes: ",visited_nodes)


