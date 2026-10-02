from random import choice


class RPS:

    WIN_SCORE = 10
    EXIT_COMMAND = "exit"

    emoji = {
        "rock": "🪨",
        "paper": "🗞️",
        "scissors": "✂️",
    }
    valid_moves = list(emoji.keys())
    lookup_table = {
        "rock": "paper",
        "paper": "scissors",
        "scissors": "rock",
    }

    def __init__(self):
        print("Welcome to the game RPS 7400!\n")
        self.player_name = input("Enter your name: ").title()
        print("**Note: type  \"exit\" to quit the game!")
        self.player_point = 0
        self.ai_point = 0
        self.running = True

    def play_game(self):
        player_move = self.get_player_move()

        if player_move == self.EXIT_COMMAND:
            self.running = False
            return

        ai_move = choice(self.valid_moves)
        self.display_moves(player_move, ai_move)
        self.check_move(player_move, ai_move)

    def get_player_move(self):
        while True:
            move = input("rock/paper/scissors: ").strip().lower()
            if move in self.valid_moves or move == self.EXIT_COMMAND:
                return move
            print("Enter a valid move!")

    def display_moves(self, player_move, ai_move):
        print("-"*20)
        print(f"{self.player_name}: {self.emoji[player_move]}")
        print(f"AI:  {self.emoji[ai_move]}")
        print("-"*20)

    def check_move(self, player_move, ai_move):
        if player_move == ai_move:
            print("\tTie!")
        elif player_move == self.lookup_table[ai_move]:
            self.player_point += 1
            print(f"\tBooyah!")
        else:
            self.ai_point += 1
            print("\tDefeat :(")

        print("-"*20)
        print("Point:")
        print(f"{self.player_name}: {self.player_point}")
        print(f"AI: {self.ai_point}")
        print("-"*20)

        self.check_winner()

    def check_winner(self):
        if self.player_point >= self.WIN_SCORE:
            print(f"🎉 {self.player_name} won the game!")
            self.running = False
        elif self.ai_point >= self.WIN_SCORE:
            print("🤖 AI won the game!")
            self.running = False


if __name__ == "__main__":
    rps = RPS()
    while rps.running:
        rps.play_game()
    print(f"Thanks for playing the game, {rps.player_name}!")
