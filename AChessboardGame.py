from TreeDirectedGraph import DirectedGraph, AddConnectedNode, highlightPath

def chessboardGame(x, y, make_graph=False):
    player_turn = True
    available_moves = [
        [-2, +1],
        [-2, -1],
        [-1, -2],
        [+1, -2],
    ]
    traversal = []

    if make_graph:
        graph = DirectedGraph(str((x,y)), f"{x},{y}", 'black')

    def check_valid_moves(x, y):
        valid_moves_resp = []
        for move_set in available_moves:
            newx = x
            newy = y
            newx += move_set[0]
            newy += move_set[1]
            if newx > 0 and newy > 0:
                valid_moves_resp.append(move_set)
        return valid_moves_resp
    
    def will_player_win_dfs(player_turn, path):
        nonlocal traversal
        nonlocal graph
        nonlocal make_graph

        x,y = path[-1]
        valid_moves = check_valid_moves(x,y)

        if player_turn:
            player_can_force_win = False
            for move in valid_moves:
                newx = x + move[0]
                newy = y + move[1]

                path.append((newx, newy))
                if make_graph: AddConnectedNode(graph, str((x,y)), str((newx,newy)), 'red', f"{newx},{newy}", len(path))
                player_can_force_win = player_can_force_win or will_player_win_dfs(not player_turn, path)
                path.pop()

                if player_can_force_win:  # If at least one winning path is found -> branch is winning
                    traversal = path+[(newx,newy)] if len(path) > len(traversal) else traversal # replace winning path if it's longer than the current one
                    # break uncomment this line to stop the search after finding the first winning path
        else:
            player_can_force_win = True
            for move in valid_moves:
                newx = x + move[0]
                newy = y + move[1]
                
                path.append((newx, newy))
                if make_graph: AddConnectedNode(graph, str((x,y)), str((newx,newy)), 'black', f"{newx},{newy}", len(path))
                player_can_force_win = player_can_force_win and will_player_win_dfs(not player_turn, path)
                path.pop()
                
                if not player_can_force_win: # If at least one losing path is found -> branch is not winning
                    traversal = [] # reset the winning path
                    # break uncomment this line to stop the search after finding the first winning path
        return player_can_force_win
    
    winner = will_player_win_dfs(player_turn, [(x, y)])

    highlightPath(graph, traversal)
    graph.show('graph.html', notebook=False)
    print("First" if winner else "Second")
    print("Winning Path:", traversal if traversal else "No winning path found")

chessboardGame(5,3, True) #checking if the player who moves first can force a win