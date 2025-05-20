from random import random, choices
import math

# Input variables
astrites = 0
forging_tides = 345
afterglow_coral = 0
featured_5_star = 'Blazing Justice'
featured_4_stars = ['Hollow Mirage', 'Overture', 'Dauntless Evernight']
n_sims = 10000

# Game constants
pull_price = 160
five_star_base_rate = 0.008
four_star_base_rate = 0.06
trash_drop_rate = 0.932
five_star_pity = 80
four_star_pity = 10
four_star_featured_rate = 0.5
five_star_reward = 15
enhanced_five_star_reward = 40
four_star_reward = 3
enhanced_four_star_reward = 8
trash_reward = 1
item_limit = 5

# Full list of 4-star characters and weapons
all_4_star = [
    'Yuanwu', 'Lumi', 'Taoqi', 'Chixia', 'Youhu', 'Morfeti', 'Baizhi', 'Danjin', 'Sanhua', 'Yangyang', 'Aalto',
    'Dauntless Evernight', 'Commando of Conviction', 'Undying Flame', 'Amilty Accord', 'Jinzhou Keeper', 'Discord',
    'Overture', 'Cadenza', 'Marcato', 'Variation', 'Helios Cleaver', 'Lunar Cutter', 'Novaburst', 'Hollow Mirage',
    'Comet Flare', 'Waning Redshift', 'Endless Colapse', 'Relativistic Jet', 'Celestial Spiral', 'Fusion Accretion'
]

def get_five_star_probability(pull_count):
    """Soft pity model: Linear increase from pull 65 to 80."""
    if pull_count < 65:
        return five_star_base_rate
    elif pull_count >= five_star_pity:
        return 1.0
    else:
        return 0.008 + ((pull_count - 65) / (five_star_pity - 65)) * (1.0 - 0.008)

class Calculator:
    def __init__(self, featured_5_star, featured_4_stars, max_pulls):
        # Validate featured 4-stars
        if len(featured_4_stars) != 3:
            raise ValueError("featured_4_stars must contain exactly 3 characters/weapons")
        if not all(f in all_4_star for f in featured_4_stars):
            raise ValueError("All featured_4_stars must be valid 4-star characters/weapons")
        
        self.pity5 = 0
        self.pity4 = 0
        self.last_4_star_non_featured = False
        self.reward = 0
        self.max_pulls = max_pulls
        # 5-star weapon setup
        self.uprate_5_star = featured_5_star
        self.all_5_star = [featured_5_star]  # Only featured weapon
        # 4-star setup
        self.uprate_4_star = featured_4_stars
        self.no_up_4_star = [item for item in all_4_star if item not in featured_4_stars]
        self.five_star_copies = {weapon: 0 for weapon in self.all_5_star}
        self.four_star_copies = {item: 0 for item in all_4_star}
        self.total_pull = 0
        self.total_five_stars = 0
        self.total_featured_from_pulls = 0

    def random_5_star(self):
        # Always return featured 5-star weapon
        return self.uprate_5_star, True

    def random_4_star(self):
        if self.pity4 >= four_star_pity or self.last_4_star_non_featured:
            return choices(self.uprate_4_star, [1/len(self.uprate_4_star)] * len(self.uprate_4_star))[0], True
        if random() < four_star_featured_rate:
            return choices(self.uprate_4_star, [1/len(self.uprate_4_star)] * len(self.uprate_4_star))[0], True
        return choices(self.no_up_4_star, [1/len(self.no_up_4_star)] * len(self.no_up_4_star))[0], False

    def accumulate(self, result):
        if result in self.five_star_copies:
            self.five_star_copies[result] += 1
            self.total_five_stars += 1
            self.total_featured_from_pulls += 1  # All 5-stars are featured
            self.reward += enhanced_five_star_reward if self.five_star_copies[result] > item_limit else five_star_reward
        elif result in self.four_star_copies:
            self.four_star_copies[result] += 1
            self.reward += enhanced_four_star_reward if self.four_star_copies[result] > item_limit else four_star_reward
        else:
            self.reward += trash_reward

    def pull(self):
        if self.total_pull >= self.max_pulls:
            return False
        self.total_pull += 1
        self.pity5 += 1
        self.pity4 += 1

        five_star_prob = get_five_star_probability(self.pity5)
        pull_type = choices([0, 1, 2], [five_star_prob, four_star_base_rate, 1 - five_star_prob - four_star_base_rate])[0]

        if pull_type == 0 or self.pity5 >= five_star_pity:
            result, uprate = self.random_5_star()
            self.pity5 = 0
            self.pity4 = 0
            self.accumulate(result)
        elif pull_type == 1 or self.pity4 >= four_star_pity:
            result, uprate = self.random_4_star()
            self.pity4 = 0
            self.last_4_star_non_featured = not uprate
            self.accumulate(result)
        else:
            self.accumulate(None)
        return True

    def roll_until_n_copies_or_limit(self, n=5):
        while self.five_star_copies[self.uprate_5_star] < n and self.total_pull < self.max_pulls:
            if not self.pull():
                break
        total_five_star_copies = sum(self.five_star_copies.values())
        return self.total_pull, self.total_five_stars, self.total_featured_from_pulls, self.five_star_copies[self.uprate_5_star], total_five_star_copies, self.reward

def calculate_probability(
    astrites=astrites,
    forging_tides=forging_tides,
    n_sims=n_sims,
    target_copies=5,
    featured_5_star='Blazing Justice',
    featured_4_stars=['Hollow Mirage', 'Overture', 'Dauntless Evernight']
):
    max_pulls = forging_tides + math.floor(astrites / pull_price)
    remaining_astrites = astrites % pull_price
    successes = 0
    total_pulls_used = 0
    total_five_stars = 0
    total_featured_from_pulls = 0
    total_featured_copies = 0
    total_all_five_star_copies = 0
    total_coral = 0
    total_remaining_forging_tides = 0

    for _ in range(n_sims):
        calc = Calculator(featured_5_star, featured_4_stars, max_pulls)
        pulls, five_stars, featured_pulls, featured_copies, all_five_star_copies, coral = calc.roll_until_n_copies_or_limit(target_copies)
        remaining_forging_tides = max_pulls - pulls
        if featured_copies >= target_copies:
            successes += 1
        total_pulls_used += pulls
        total_five_stars += five_stars
        total_featured_from_pulls += featured_pulls
        total_featured_copies += featured_copies
        total_all_five_star_copies += all_five_star_copies
        total_coral += coral
        total_remaining_forging_tides += remaining_forging_tides

    probability = successes / n_sims * 100
    avg_pulls = total_pulls_used / n_sims
    avg_astrites = avg_pulls * pull_price
    avg_pulls_per_five_star = total_pulls_used / total_five_stars if total_five_stars > 0 else 0
    avg_featured_copies = total_featured_copies / n_sims
    avg_all_five_star_copies = total_all_five_star_copies / n_sims
    avg_coral = total_coral / n_sims
    avg_remaining_forging_tides = total_remaining_forging_tides / n_sims

    print(f'Probability of getting {target_copies} {featured_5_star}: {probability:.2f}%')
    print(f'Average pulls used: {avg_pulls:.2f}, equivalent to {avg_astrites:.2f} Astrites')
    print(f'Average pulls per 5-star (simulated): {avg_pulls_per_five_star:.2f}')
    print(f'Average copies of {featured_5_star} per simulation: {avg_featured_copies:.2f}')
    print(f'Average total 5-star copies per simulation: {avg_all_five_star_copies:.2f}')
    print(f'Average remaining Afterglow Coral: {avg_coral:.2f}')
    print(f'Remaining Astrites (not used for pulls): {remaining_astrites:.2f}')
    print(f'Average remaining Forging Tides: {avg_remaining_forging_tides:.2f}')
    print(f'Featured 4-stars: {featured_4_stars}')
    print(f'Expected pulls per 5-star (empirical): 53.44')

if __name__ == "__main__":
    calculate_probability()