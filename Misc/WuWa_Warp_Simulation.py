from random import random, choices

# Game constants
pull_price = 160
five_star_base_rate = 0.008
four_star_base_rate = 0.06
trash_drop_rate = 0.932
five_star_pity = 80
four_star_pity = 10
five_star_featured_rate = 0.5
four_star_featured_rate = 0.5
five_star_reward = 15
enhanced_five_star_reward = 40
four_star_reward = 3
enhanced_four_star_reward = 8
trash_reward = 1
redemption = 360
redemption_limit = 2
item_limit = 7

# Full list of 4-star characters and weapons
all_4_star = [
    'Yuanwu', 'Lumi', 'Taoqi', 'Chixia', 'Youhu', 'Morfeti', 'Baizhi', 'Danjin', 'Sanhua', 'Yangyang', 'Aalto',
    'Dauntless Evernight', 'Commando of Conviction', 'Undying Flame', 'Amilty Accord', 'Jinzhou Keeper', 'Discord',
    'Overture', 'Cadenza', 'Marcato', 'Variation', 'Helios Cleaver', 'Lunar Cutter', 'Novaburst', 'Hollow Mirage',
    'Comet Flare', 'Waning Redshift', 'Endless Colapse', 'Relativistic Jet', 'Celestial Spiral', 'Fusion Accretion'
]

# Default non-featured 5-star characters
default_no_up_5_star = ['Verina', 'Encore', 'Calcharo', 'Lingyang', 'Jianxin']

def get_five_star_probability(pull_count):
    """Original soft pity model."""
    if pull_count < 65:
        return five_star_base_rate
    elif pull_count >= five_star_pity:
        return 1.0
    else:
        return 0.008 + ((pull_count - 65) / (five_star_pity - 65)) * (1.0 - 0.008)

class Calculator:
    def __init__(self, featured_5_star, featured_4_stars):
        # Validate featured 4-stars
        if len(featured_4_stars) != 3:
            raise ValueError("featured_4_stars must contain exactly 3 characters/weapons")
        if not all(f in all_4_star for f in featured_4_stars):
            raise ValueError("All featured_4_stars must be valid 4-star characters/weapons")
        
        self.pity5 = 0
        self.last_5_star_non_featured = False
        self.pity4 = 0
        self.last_4_star_non_featured = False
        self.reward = 0
        self.redeemed = 0
        # 5-star character setup
        self.uprate_5_star = featured_5_star
        self.no_up_5_star = default_no_up_5_star.copy()
        if featured_5_star in self.no_up_5_star:
            self.no_up_5_star.remove(featured_5_star)
        self.all_5_star_char = [featured_5_star] + self.no_up_5_star
        # 4-star character setup
        self.uprate_4_star = featured_4_stars
        self.no_up_4_star = [item for item in all_4_star if item not in featured_4_stars]
        self.five_star_copies = {char: 0 for char in self.all_5_star_char}
        self.four_star_copies = {char: 0 for char in all_4_star}
        self.total_pull = 0
        self.total_five_stars = 0
        self.total_featured_from_pulls = 0

    def random_5_star(self):
        if self.pity5 >= five_star_pity or self.last_5_star_non_featured:
            return self.uprate_5_star, True
        if random() < five_star_featured_rate:
            return self.uprate_5_star, True
        return choices(self.no_up_5_star, [1/len(self.no_up_5_star)] * len(self.no_up_5_star))[0], False

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
            if result == self.uprate_5_star:
                self.total_featured_from_pulls += 1
            self.reward += enhanced_five_star_reward if self.five_star_copies[result] > item_limit else five_star_reward
        elif result in self.four_star_copies:
            self.four_star_copies[result] += 1
            self.reward += enhanced_four_star_reward if self.four_star_copies[result] > item_limit else four_star_reward
        else:
            self.reward += trash_reward

    def pull(self):
        self.total_pull += 1
        self.pity5 += 1
        self.pity4 += 1

        five_star_prob = get_five_star_probability(self.pity5)
        pull_type = choices([0, 1, 2], [five_star_prob, four_star_base_rate, 1 - five_star_prob - four_star_base_rate])[0]

        if pull_type == 0 or self.pity5 >= five_star_pity:
            result, uprate = self.random_5_star()
            self.pity5 = 0
            self.pity4 = 0
            self.last_5_star_non_featured = not uprate
            self.accumulate(result)
        elif pull_type == 1 or self.pity4 >= four_star_pity:
            result, uprate = self.random_4_star()
            self.pity4 = 0
            self.last_4_star_non_featured = not uprate
            self.accumulate(result)
        else:
            self.accumulate(None)

        # Immediate redemption, but only once per pull
        if self.reward >= redemption and self.redeemed < redemption_limit and self.five_star_copies[self.uprate_5_star] < item_limit:
            self.reward -= redemption
            self.redeemed += 1
            self.five_star_copies[self.uprate_5_star] += 1

    def roll_until_n_copies(self, n=7):
        while self.five_star_copies[self.uprate_5_star] < n:
            self.pull()
        # Compute total 5-star copies
        total_five_star_copies = sum(self.five_star_copies.values())
        return self.total_pull, self.total_five_stars, self.total_featured_from_pulls, self.redeemed, self.five_star_copies[ self.uprate_5_star], total_five_star_copies

def n_tries(n_sims=10000, target_copies=7, featured_5_star='Zani', featured_4_stars=['Yuanwu', 'Lumi', 'Taoqi']):
    list_res = []
    total_five_stars = 0
    total_featured_from_pulls = 0
    total_redemptions = 0
    total_featured_copies = 0
    total_all_five_star_copies = 0
    for _ in range(n_sims):
        calc = Calculator(featured_5_star, featured_4_stars)
        pulls, five_stars, featured_pulls, redemptions, featured_copies, all_five_star_copies = calc.roll_until_n_copies(target_copies)
        list_res.append(pulls)
        total_five_stars += five_stars
        total_featured_from_pulls += featured_pulls
        total_redemptions += redemptions
        total_featured_copies += featured_copies
        total_all_five_star_copies += all_five_star_copies
    avg_pulls = sum(list_res) / n_sims
    avg_astrites = avg_pulls * pull_price
    avg_pulls_per_five_star = sum(list_res) / total_five_stars if total_five_stars > 0 else 0
    avg_pulls_per_featured = sum(list_res) / total_featured_from_pulls if total_featured_from_pulls > 0 else 0
    avg_redemptions = total_redemptions / n_sims
    avg_featured_copies = total_featured_copies / n_sims
    avg_all_five_star_copies = total_all_five_star_copies / n_sims
    print(f'Average pulls for {target_copies} {featured_5_star}: {avg_pulls:.2f}, requires {avg_astrites:.2f} Astrites')
    print(f'Average pulls per 5-star (simulated): {avg_pulls_per_five_star:.2f}')
    print(f'Average pulls per {featured_5_star} from pulls (simulated): {avg_pulls_per_featured:.2f}')
    print(f'Average redemptions per simulation: {avg_redemptions:.2f}')
    print(f'Average copies of {featured_5_star} per simulation: {avg_featured_copies:.2f}')
    print(f'Average total 5-star copies per simulation: {avg_all_five_star_copies:.2f}')
    print(f'Featured 4-stars: {featured_4_stars}')
    print(f'Expected pulls per 5-star (empirical): 53.44')
    print(f'Expected pulls per featured 5-star (empirical): 79.75')

if __name__ == "__main__":
    n_tries(featured_5_star='Jiyan', featured_4_stars=['Chixia', 'Sanhua', 'Danjin'])


# Average pulls for 7 Jiyan: 430.30, requires 68847.81 Astrites
# Average pulls per 5-star (simulated): 54.30
# Average pulls per Jiyan from pulls (simulated): 82.03
# Average redemptions per simulation: 1.75
# Average copies of Jiyan per simulation: 7.00
# Average total 5-star copies per simulation: 9.68
# Featured 4-stars: ['Chixia', 'Sanhua', 'Danjin']
# Expected pulls per 5-star (empirical): 53.44
# Expected pulls per featured 5-star (empirical): 79.75

#FOR 95% rate: save 554 pull, then buy 2 cons
#430 pulls: 60.28% chance