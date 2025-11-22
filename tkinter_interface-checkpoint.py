import tkinter as tk
from functools import partial
from game_logic import get_random_move, get_smarter_move, play_round, MOVES

# --- Configuration ---
# Set the desired computer strategy for the interactive game
# Change this to get_random_move if you want a simpler opponent.
COMP_STRATEGY = get_smarter_move 

class RPS_GUI:
    def __init__(self, master):
        self.master = master
        master.title("Rock-Paper-Scissors Project")
        
        # --- Game State ---
        self.score = {'player': 0, 'computer': 0, 'draw': 0}
        self.player_history = []
        
        # --- Labels and Displays ---
        self.result_text = tk.StringVar()
        self.result_text.set("Select your move to start the game!")
        
        self.score_text = tk.StringVar()
        self._update_score_display()
        
        tk.Label(master, textvariable=self.result_text, font=('Arial', 16, 'bold')).pack(pady=15)
        tk.Label(master, textvariable=self.score_text, font=('Arial', 12)).pack(pady=5)
        
        # --- Move Buttons ---
        button_frame = tk.Frame(master)
        button_frame.pack(pady=20)
        
        for move in MOVES:
            button = tk.Button(
                button_frame, 
                text=move.upper(), 
                command=partial(self.play_handler, move), 
                width=12, 
                height=2,
                font=('Arial', 10)
            )
            button.pack(side=tk.LEFT, padx=10)
        
        # --- Reset Button ---
        tk.Button(master, text="Reset Score", command=self.reset_score).pack(pady=10)

    def _update_score_display(self):
        """Updates the score label text."""
        self.score_text.set(
            f"SCORE | Player: {self.score['player']} | Computer: {self.score['computer']} | Draws: {self.score['draw']}"
        )
    
    def reset_score(self):
        """Resets the score and the player history."""
        self.score = {'player': 0, 'computer': 0, 'draw': 0}
        self.player_history = []
        self.result_text.set("Score has been reset. Play again!")
        self._update_score_display()

    def play_handler(self, player_choice):
        """Handles a move made by the player via button click."""
        
        # 1. Get Computer's Move 
        if COMP_STRATEGY.__name__ == 'get_smarter_move':
            # Pass history to the smart strategy
            computer_choice = COMP_STRATEGY(self.player_history)
        else:
            # Random strategy needs no history
            computer_choice = COMP_STRATEGY()
        
        # 2. Determine Winner
        winner = play_round(player_choice, computer_choice)
        
        # 3. Update Score and History
        self.score[winner] += 1
        self.player_history.append(player_choice)
        
        # 4. Update Display
        self._update_score_display()
        
        p_move = player_choice.upper()
        c_move = computer_choice.upper()

        if winner == 'player':
            result_msg = f"You chose {p_move}. Computer chose {c_move}. You WIN!"
        elif winner == 'computer':
            result_msg = f"You chose {p_move}. Computer chose {c_move}. Computer WINS!"
        else:
            result_msg = f"You both chose {p_move}. It's a DRAW!"
            
        self.result_text.set(result_msg)