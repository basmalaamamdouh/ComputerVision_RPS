import random

# --- Constants ---
MOVES = ['rock', 'paper', 'scissors']

# --- Basic Computer Strategy ---
def get_random_move():
    """Generates a move using a uniformly random distribution."""
    return random.choice(MOVES)

# --- Core Game Logic ---
def play_round(player_move, computer_move):
    """
    Determines the winner of a single round based on standard RPS rules.
    Returns: 'player', 'computer', or 'draw'.
    """
    player_move = player_move.lower()
    computer_move = computer_move.lower()

    if player_move == computer_move:
        return 'draw'

    # Winning conditions: Rock > Scissors, Paper > Rock, Scissors > Paper
    if (player_move == 'rock' and computer_move == 'scissors') or \
       (player_move == 'paper' and computer_move == 'rock') or \
       (player_move == 'scissors' and computer_move == 'paper'):
        return 'player'
    else:
        # If the player didn't win or draw, the computer won.
        return 'computer'

# --- Advanced Computer Strategy (Smarter Opponent) ---
def get_smarter_move(player_history):
    """
    A frequency-based strategy: predicts the player's most frequent 
    recent move and chooses the counter-move. Falls back to random if history is short.
    """
    # Use 5 rounds of history before attempting a prediction
    if len(player_history) < 5:
        return get_random_move()

    # Analyze the last 10 moves for responsiveness
    recent_history = player_history[-10:]
    counts = {move: recent_history.count(move) for move in MOVES}

    # Find the move the player has used most frequently
    most_frequent_move = max(counts, key=counts.get)
    
    # Determine the counter move
    if most_frequent_move == 'rock':
        return 'paper'       # Paper beats Rock
    elif most_frequent_move == 'paper':
        return 'scissors'    # Scissors beats Paper
    else: # most_frequent_move == 'scissors'
        return 'rock'        # Rock beats Scissors