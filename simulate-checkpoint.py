import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from game_logic import MOVES, get_random_move, get_smarter_move, play_round

# --- Simulation Function ---
def simulate_n_rounds(n_rounds, player_strategy=get_random_move, comp_strategy=get_random_move):
    """
    Simulates N rounds of Rock-Paper-Scissors using specified strategies.
    
    Returns: A dictionary of simulation statistics.
    """
    results = {'player': 0, 'computer': 0, 'draw': 0}
    player_moves = {move: 0 for move in MOVES}
    comp_moves = {move: 0 for move in MOVES}
    player_history = []
    
    for _ in range(n_rounds):
        p_move = player_strategy() 
        
        # Check if the computer strategy needs history (i.e., if it's the smarter move)
        if comp_strategy.__name__ == 'get_smarter_move':
            c_move = comp_strategy(player_history)
        else:
            c_move = comp_strategy()
            
        result = play_round(p_move, c_move)
        
        # Tally results and update history
        results[result] += 1
        player_moves[p_move] += 1
        comp_moves[c_move] += 1
        player_history.append(p_move)

    # Calculate percentages
    total_rounds = n_rounds
    percentages = {
        'player_win_pct': (results['player'] / total_rounds) * 100,
        'computer_win_pct': (results['computer'] / total_rounds) * 100,
        'draw_pct': (results['draw'] / total_rounds) * 100
    }
    
    player_move_pct = {k: (v / total_rounds) * 100 for k, v in player_moves.items()}
    comp_move_pct = {k: (v / total_rounds) * 100 for k, v in comp_moves.items()}

    return {
        'rounds': n_rounds,
        'results': results,
        'player_moves': player_moves,
        'comp_moves': comp_moves,
        'percentages': percentages,
        'player_move_pct': player_move_pct,
        'comp_move_pct': comp_move_pct
    }

# --- Plotting Function ---
def plot_stats(stats_dict):
    """Creates a two-part plot for Win/Loss/Draw percentages and Move Distributions."""
    
    sns.set_theme(style="whitegrid")
    
    fig, axes = plt.subplots(1, 2, figsize=(14, 6))
    
    # --- Plot 1: Win/Loss/Draw Percentages ---
    results_data = {
        'Outcome': ['Player Win', 'Computer Win', 'Draw'],
        'Percentage': [
            stats_dict['percentages']['player_win_pct'],
            stats_dict['percentages']['computer_win_pct'],
            stats_dict['percentages']['draw_pct']
        ]
    }
    df_results = pd.DataFrame(results_data)
    
    sns.barplot(
        x='Outcome', 
        y='Percentage', 
        data=df_results, 
        palette=['#4c72b0', '#c44e52', '#55a868'], 
        ax=axes[0]
    )
    axes[0].set_title(f'Win/Loss/Draw Distribution ({stats_dict["rounds"]} Rounds)')
    axes[0].set_ylim(0, 100)
    axes[0].set_ylabel('Percentage (%)')
    
    # --- Plot 2: Move Distribution ---
    move_data = {
        'Move': MOVES * 2,
        'Percentage': list(stats_dict['player_move_pct'].values()) + list(stats_dict['comp_move_pct'].values()),
        'Entity': ['Player'] * len(MOVES) + ['Computer'] * len(MOVES)
    }
    df_moves = pd.DataFrame(move_data)
    
    sns.barplot(
        x='Move', 
        y='Percentage', 
        hue='Entity', 
        data=df_moves, 
        palette='tab10', 
        ax=axes[1]
    )
    axes[1].set_title(f'Move Distribution by Entity ({stats_dict["rounds"]} Rounds)')
    axes[1].set_ylim(0, 100)
    axes[1].legend(title='Player/Comp')
    
    plt.tight_layout()
    plt.show()