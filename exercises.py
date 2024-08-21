class Game():
    def __init__(self, turn='X', tie=False, winner=None, board={}):
        self.turn = turn
        self.tie = tie
        self.winner = winner
        self.board = {
            'a1': None, 'b1': None, 'c1': None,
            'a2': None, 'b2': None, 'c2': None,
            'a3': None, 'b3': None, 'c3': None,
            }
    
    def print_board(self):
        b = self.board
        print(f"""
                A   B   C
            1)  {b['a1'] or ' '} | {b['b1'] or ' '} | {b['c1'] or ' '}
                ----------
            2)  {b['a2'] or ' '} | {b['b2'] or ' '} | {b['c2'] or ' '}
                ----------
            3)  {b['a3'] or ' '} | {b['b3'] or ' '} | {b['c3'] or ' '}
        """)

    def print_message(self):
        ## If there is a tie: print("Tie game!")
        if self.tie:
            print('Tie Game')
        elif self.winner:
            print(f'{self.winner} wins!')
        else:
            print(f"It's player {self.turn}'s turn!")
        ## If there is a winner: print(f"{self.winner} wins the game!")
        ## Otherwise: print(f"It's player {self.turn}'s turn!")

    def render(self):
        self.print_board()
        self.print_message()
        
    def get_move(self):
        while True:
             
            move = input(f"Enter a valid move (example: A1: ").lower()

            if move in self.board and self.board[move] is None:
                self.board[move] = self.turn

                break
            else:
                print('Invalid move. Try again')

    def check_for_winner(self):
        winning_combos = [
            ['a1', 'b1', 'c1'], 
            ['a2', 'b2', 'c2'], 
            ['a3', 'b3', 'c3'],
            ['a1', 'a2', 'a3'], 
            ['b1', 'b2', 'b3'], 
            ['c1', 'c2', 'c3'],  
            ['a1', 'b2', 'c3'], 
            ['c1', 'b2', 'a3'] 
        ]

        for winner in winning_combos:
            if self.board[winner[0]] == self.board[winner[1]] == self.board[winner[2]] != None:
                self.winner = self.turn
                return

    def check_tie(self):

        if all(self.board[positions] is not None for positions in self.board) and not self.winner:
            self.tie=True
    
    def switch(self):
        self.turn = 'O' if self.turn == 'X' else 'X'

    def play_game(self):
        print("Let's Play!")

        while not self.winner and not self.tie:
            self.render()
            self.get_move()
            self.check_for_winner()
            self.check_tie()

            if not self.winner and not self.tie:
                self.switch()
        self.render()


game = Game()
game.play_game()