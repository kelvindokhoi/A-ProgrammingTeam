import random
from collections import defaultdict

# Game parameters
CHARACTERS = ['Jinsi', 'Calcharo', 'Camellya', 'Carlotta']
UNDERDOG_ODDS = {'Jinsi': 1.25, 'Calcharo': 1.25, 'Camellya': 1.25, 'Carlotta': 1.25}
TRACK_LENGTH = 36
SUPPORT_PERCENTAGES = [0, 0.25, 0.5, 0.75, 1.0]
NUM_SIMULATIONS = 10000
NUM_WINNERS = 1
INITIAL_POPULARITY = 5452

def roll_dice(character):
    return random.randint(1, 3)

def simulate_game(supported_character, support_percentage):
    # Initialize positions and stacks, including TRACK_LENGTH
    positions = {char: 0 for char in CHARACTERS}
    stacks = {i: [] for i in range(TRACK_LENGTH + 1)}  # Include position 36
    for char in CHARACTERS:
        stacks[0].append(char)
    
    turn = 0
    while True:
        turn += 1
        # Determine move order
        move_order = CHARACTERS.copy()
        random.shuffle(move_order)
        
        for char in move_order:
            current_pos = positions[char]
            if current_pos >= TRACK_LENGTH:
                continue
                
            # Roll dice and move
            steps = roll_dice(char)
            
            # Carlotta's ability: 28% chance to move twice
            if char == 'Carlotta' and random.random() < 0.28:
                steps *= 2
                
            # Camellya's ability: 50% chance to move extra per other cube on same pad
            if char == 'Camellya' and random.random() < 0.5:
                others = len(stacks[current_pos]) - 1
                steps += others
            
            # Move character and those stacked above
            stack_index = stacks[current_pos].index(char)
            moving_chars = stacks[current_pos][stack_index:]
            stacks[current_pos] = stacks[current_pos][:stack_index]
            
            new_pos = min(current_pos + steps, TRACK_LENGTH)
            for moving_char in moving_chars:
                positions[moving_char] = new_pos
                stacks[new_pos].append(moving_char)
            
            # Jinsi's ability: 40% chance to move to top of stack
            if char == 'Jinsi' and new_pos < TRACK_LENGTH and len(stacks[new_pos]) > 1:
                if random.random() < 0.4:
                    stacks[new_pos].remove('Jinsi')
                    stacks[new_pos].append('Jinsi')
            
            # Calcharo's ability: +3 pads if last to move
            if char == 'Calcharo' and char == move_order[-1] and new_pos < TRACK_LENGTH:
                stacks[new_pos].remove('Calcharo')
                new_pos = min(new_pos + 3, TRACK_LENGTH)
                positions['Calcharo'] = new_pos
                stacks[new_pos].append('Calcharo')
        
        # Check for winners
        winners = []
        if len(stacks[TRACK_LENGTH]) >= NUM_WINNERS:
            winners = stacks[TRACK_LENGTH][::-1][:NUM_WINNERS]  # Top NUM_WINNERS in reverse order (highest rank first)
            # Calculate popularity reward
            popularity_spent = INITIAL_POPULARITY * support_percentage
            if supported_character in winners:
                reward = popularity_spent * UNDERDOG_ODDS[supported_character]
            else:
                reward = popularity_spent * 0.8
            return winners, reward, turn
    
    return [], 0, turn

def run_simulations():
    win_counts = defaultdict(int)
    reward_sums = defaultdict(float)
    turns = []
    
    # Simulate for each support percentage and character
    for support_percentage in SUPPORT_PERCENTAGES:
        for supported_char in CHARACTERS:
            for _ in range(NUM_SIMULATIONS):
                winners, reward, turn = simulate_game(supported_char, support_percentage)
                for winner in winners:
                    win_counts[winner] += 1
                reward_sums[(supported_char, support_percentage)] += reward
                turns.append(turn)
    
    # Calculate win probabilities (probability of being in top NUM_WINNERS)
    total_games = NUM_SIMULATIONS * len(SUPPORT_PERCENTAGES) * len(CHARACTERS)
    win_probs = {char: win_counts[char] / total_games for char in CHARACTERS}
    
    # Calculate average ROI and absolute gain
    avg_rewards = {}
    for char in CHARACTERS:
        for percentage in SUPPORT_PERCENTAGES:
            popularity_spent = INITIAL_POPULARITY * percentage
            if popularity_spent > 0:
                avg_reward = reward_sums[(supported_char, percentage)] / NUM_SIMULATIONS
                roi = (avg_reward - popularity_spent) / popularity_spent if popularity_spent > 0 else 0
                absolute_gain = avg_reward - popularity_spent
                avg_rewards[(char, percentage)] = (avg_reward, roi, absolute_gain)
    
    return win_probs, avg_rewards, sum(turns) / len(turns)

def main():
    win_probs, avg_rewards, avg_turns = run_simulations()
    
    print(f"Probabilities of Being in Top {NUM_WINNERS}:")
    for char, prob in sorted(win_probs.items(), key=lambda x: x[1], reverse=True):
        print(f"{char}: {prob:.4f} ({prob*100:.2f}%)")
    
    print("\nAverage Reward, ROI, and Absolute Gain:")
    # Sort by character and percentage for consistent output
    for char in sorted(CHARACTERS):
        for percentage in sorted(SUPPORT_PERCENTAGES):
            if percentage > 0 and (char, percentage) in avg_rewards:
                avg_reward, roi, absolute_gain = avg_rewards[(char, percentage)]
                print(f"Supporting {char} with {percentage*100}% popularity: Avg Reward = {avg_reward:.2f}, ROI = {roi:.4f}, Absolute Gain = {absolute_gain:.2f}")
    
    # Find best strategy for absolute gain
    best_gain = -float('inf')
    best_strategy = None
    for (char, percentage), (avg_reward, roi, absolute_gain) in avg_rewards.items():
        if absolute_gain > best_gain:
            best_gain = absolute_gain
            best_strategy = (char, percentage)
    
    print(f"\nBest Strategy for Absolute Gain: Support {best_strategy[0]} with {best_strategy[1]*100}% popularity (Absolute Gain = {best_gain:.2f})")
    print(f"Average number of turns per game: {avg_turns:.2f}")

if __name__ == "__main__":
    main()