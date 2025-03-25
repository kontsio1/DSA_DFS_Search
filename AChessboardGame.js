function chessboardGame(x, y) {
    //1 playing: true || 2 playing: false
    let playerTurn = true 
    let availableMoves = [
        [-2, -1], 
        [-1, -2],
        [-2, +1], 
        [+1, -2], 
    ]
    let winner = WillPlayerWinDfs(x, y, playerTurn)
    console.log(winner ? "First" : "Second")

    function WillPlayerWinDfs(x,y,playerTurn) {
        let playerCanForceWin;
        let validMoves = checkValidMoves(x, y)

        if(playerTurn){
            playerCanForceWin = false

            for (let move of validMoves) {
                let newx = x + move[0]
                let newy = y + move[1]
                playerCanForceWin = playerCanForceWin || WillPlayerWinDfs(newx, newy, !playerTurn)
                
                if (playerCanForceWin) {
                    break
                }
            }
        } else {
            playerCanForceWin = true

            for (let move of validMoves) {
                let newx = x + move[0]
                let newy = y + move[1]
                playerCanForceWin = playerCanForceWin && WillPlayerWinDfs(newx, newy, !playerTurn)
            }
        }
        return playerCanForceWin
    }
    
    function checkValidMoves(x, y) {
        let validMovesResp = []
        availableMoves.forEach((moveSet)=>{
            let newx = x
            let newy = y
            newx += moveSet[0]
            newy += moveSet[1]
            if (newx>0 && newy>0){
                validMovesResp.push(moveSet)
            }
        })
        return validMovesResp
    }
}

chessboardGame(64, 64)