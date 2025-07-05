from random import random, choices
from typing import List, Tuple, Dict
import math

# Game configuration constants
CONFIG = {
    'pull_price': 160,
    'five_star_base_rate': 0.008,
    'four_star_base_rate': 0.06,
    'trash_drop_rate': 0.932,
    'five_star_pity': 80,
    'four_star_pity': 10,
    'five_star_featured_rate': 0.5,
    'four_star_featured_rate': 0.5,
    'five_star_reward': 15,
    'enhanced_five_star_reward': 40,
    'four_star_reward': 3,
    'enhanced_four_star_reward': 8,
    'trash_reward': 1,
    'redemption_cost': 360,
    'redemption_limit': 2,
    'item_limit': 7,
    'all_4_stars': [
        'Yuanwu', 'Lumi', 'Taoqi', 'Chixia', 'Youhu', 'Morfeti', 'Baizhi', 'Danjin',
        'Sanhua', 'Yangyang', 'Aalto', 'Dauntless Evernight', 'Commando of Conviction',
        'Undying Flame', 'Amilty Accord', 'Jinzhou Keeper', 'Discord', 'Overture',
        'Cadenza', 'Marcato', 'Variation', 'Helios Cleaver', 'Lunar Cutter',
        'Novaburst', 'Hollow Mirage', 'Comet Flare', 'Waning Redshift',
        'Endless Colapse', 'Relativistic Jet', 'Celestial Spiral', 'Fusion Accretion'
    ],
    'default_5_stars': ['Verina', 'Encore', 'Calcharo', 'Lingyang', 'Jianxin']
}

def get_five_star_probability(pull_count: int, config: Dict) -> float:
    """Calculate 5-star probability with soft pity model."""
    if pull_count < 65:
        return config['five_star_base_rate']
    if pull_count >= config['five_star_pity']:
        return 1.0
    return config['five_star_base_rate'] + (
        (pull_count - 65) / (config['five_star_pity'] - 65)
    ) * (1.0 - config['five_star_base_rate'])

class GachaSimulator:
    def __init__(
        self,
        featured_5_star: str,
        featured_4_stars: List[str],
        max_pulls: int,
        initial_coral: int,
        initial_5_star_pity: int,
        config: Dict
    ):
        """Initialize gacha simulator with game state."""
        if len(featured_4_stars) != 3:
            raise ValueError("Exactly 3 featured 4-star characters/weapons required")
        if not all(f in config['all_4_stars'] for f in featured_4_stars):
            raise ValueError("Invalid featured 4-star characters/weapons")

        self.config = config
        self.max_pulls = max_pulls
        self.pity5 = initial_5_star_pity
        self.pity4 = 0
        self.last_5_star_non_featured = False
        self.last_4_star_non_featured = False
        self.coral = initial_coral
        self.redeemed = 0
        self.total_pulls = 0

        # 5-star setup
        self.featured_5_star = featured_5_star
        self.non_featured_5_stars = [
            char for char in config['default_5_stars'] if char != featured_5_star
        ]
        self.all_5_stars = [featured_5_star] + self.non_featured_5_stars

        # 4-star setup
        self.featured_4_stars = set(featured_4_stars)
        self.non_featured_4_stars = [item for item in config['all_4_stars'] if item not in self.featured_4_stars]

        # Track copies
        self.five_star_copies = {char: 0 for char in self.all_5_stars}
        self.four_star_copies = {char: 0 for char in config['all_4_stars']}
        self.total_five_stars = 0
        self.featured_5_star_pulls = 0

    def _random_5_star(self) -> Tuple[str, bool]:
        """Select a random 5-star with featured rate mechanics."""
        if self.pity5 >= self.config['five_star_pity'] or self.last_5_star_non_featured:
            return self.featured_5_star, True
        if random() < self.config['five_star_featured_rate']:
            return self.featured_5_star, True
        return choices(self.non_featured_5_stars, k=1)[0], False

    def _random_4_star(self) -> Tuple[str, bool]:
        """Select a random 4-star with featured rate mechanics."""
        if self.pity4 >= self.config['four_star_pity'] or self.last_4_star_non_featured:
            return choices(list(self.featured_4_stars), k=1)[0], True
        if random() < self.config['four_star_featured_rate']:
            return choices(list(self.featured_4_stars), k=1)[0], True
        return choices(self.non_featured_4_stars, k=1)[0], False

    def _accumulate(self, result: str | None):
        """Update rewards and counters based on pull result."""
        if result in self.five_star_copies:
            self.five_star_copies[result] += 1
            self.total_five_stars += 1
            if result == self.featured_5_star:
                self.featured_5_star_pulls += 1
            reward = (
                self.config['enhanced_five_star_reward']
                if self.five_star_copies[result] > self.config['item_limit']
                else self.config['five_star_reward']
            )
        elif result in self.four_star_copies:
            self.four_star_copies[result] += 1
            reward = (
                self.config['enhanced_four_star_reward']
                if self.four_star_copies[result] > self.config['item_limit']
                else self.config['four_star_reward']
            )
        else:
            reward = self.config['trash_reward']
        self.coral += reward

    def pull(self) -> bool:
        """Simulate a single pull."""
        if self.total_pulls >= self.max_pulls:
            return False
        self.total_pulls += 1
        self.pity5 += 1
        self.pity4 += 1

        five_star_prob = get_five_star_probability(self.pity5, self.config)
        pull_type = choices(
            [0, 1, 2],
            [five_star_prob, self.config['four_star_base_rate'], 1 - five_star_prob - self.config['four_star_base_rate']],
            k=1
        )[0]

        if pull_type == 0 or self.pity5 >= self.config['five_star_pity']:
            result, is_featured = self._random_5_star()
            self.pity5 = 0
            self.pity4 = 0
            self.last_5_star_non_featured = not is_featured
        elif pull_type == 1 or self.pity4 >= self.config['four_star_pity']:
            result, is_featured = self._random_4_star()
            self.pity4 = 0
            self.last_4_star_non_featured = not is_featured
        else:
            result = None

        self._accumulate(result)

        # Handle redemption
        if (
            self.coral >= self.config['redemption_cost']
            and self.redeemed < self.config['redemption_limit']
            and self.five_star_copies[self.featured_5_star] < self.config['item_limit']
        ):
            self.coral -= self.config['redemption_cost']
            self.redeemed += 1
            self.five_star_copies[self.featured_5_star] += 1

        return True

    def simulate_until_target_or_limit(self, target_copies: int = 7) -> Tuple[int, int, int, int, int, int, int]:
        """Simulate pulls until target copies or pull limit is reached."""
        while (
            self.five_star_copies[self.featured_5_star] < target_copies
            and self.total_pulls < self.max_pulls
        ):
            if not self.pull():
                break
        return (
            self.total_pulls,
            self.total_five_stars,
            self.featured_5_star_pulls,
            self.redeemed,
            self.five_star_copies[self.featured_5_star],
            sum(self.five_star_copies.values()),
            self.coral
        )

def calculate_gacha_probability(
    astrites: int,
    radiant_tides: int,
    afterglow_coral: int,
    n_sims: int = 10000,
    target_copies: int = 7,
    featured_5_star: str = 'Camellya',
    featured_4_stars: List[str] = ['Chixia', 'Sanhua', 'Danjin'],
    config: Dict = CONFIG
) -> None:
    """Calculate probability and statistics for obtaining target 5-star copies."""
    max_pulls = radiant_tides + math.floor(astrites / config['pull_price'])
    remaining_astrites = astrites % config['pull_price']
    
    stats = {
        'successes': 0,
        'total_pulls': 0,
        'total_five_stars': 0,
        'total_featured_pulls': 0,
        'total_redemptions': 0,
        'total_featured_copies': 0,
        'total_all_five_star_copies': 0,
        'total_coral': 0,
        'total_remaining_tides': 0
    }

    for _ in range(n_sims):
        sim = GachaSimulator(featured_5_star, featured_4_stars, max_pulls, afterglow_coral, 48, config)
        pulls, five_stars, featured_pulls, redemptions, featured_copies, all_five_star_copies, coral = (
            sim.simulate_until_target_or_limit(target_copies)
        )
        stats['successes'] += 1 if featured_copies >= target_copies else 0
        stats['total_pulls'] += pulls
        stats['total_five_stars'] += five_stars
        stats['total_featured_pulls'] += featured_pulls
        stats['total_redemptions'] += redemptions
        stats['total_featured_copies'] += featured_copies
        stats['total_all_five_star_copies'] += all_five_star_copies
        stats['total_coral'] += coral
        stats['total_remaining_tides'] += max_pulls - pulls

    # Calculate averages
    probability = (stats['successes'] / n_sims) * 100
    avg_pulls = stats['total_pulls'] / n_sims
    avg_astrites = avg_pulls * config['pull_price']
    avg_pulls_per_five_star = stats['total_pulls'] / stats['total_five_stars'] if stats['total_five_stars'] > 0 else 0
    avg_pulls_per_featured = (
        stats['total_pulls'] / stats['total_featured_pulls'] if stats['total_featured_pulls'] > 0 else 0
    )
    avg_redemptions = stats['total_redemptions'] / n_sims
    avg_featured_copies = stats['total_featured_copies'] / n_sims
    avg_all_five_star_copies = stats['total_all_five_star_copies'] / n_sims
    avg_coral = stats['total_coral'] / n_sims
    avg_remaining_tides = stats['total_remaining_tides'] / n_sims

    # Output results
    print(f"\nWith {astrites} Astrite{'s' * (astrites > 1)}, "
          f"{radiant_tides} Radiant Tide{'s' * (radiant_tides > 1)}, "
          f"and {afterglow_coral} Afterglow Coral{'s' * (afterglow_coral > 1)}")
    print(f"Probability of getting {target_copies} {featured_5_star}: {probability:.2f}%")
    print(f"Average pulls used: {avg_pulls:.2f} (~{avg_astrites:.2f} Astrites)")
    print(f"Average pulls per 5-star: {avg_pulls_per_five_star:.2f}")
    print(f"Average pulls per {featured_5_star} from pulls: {avg_pulls_per_featured:.2f}")
    print(f"Average redemptions: {avg_redemptions:.2f}")
    print(f"Average {featured_5_star} copies: {avg_featured_copies:.2f}")
    print(f"Average total 5-star copies: {avg_all_five_star_copies:.2f}")
    print(f"Average remaining Afterglow Coral: {avg_coral:.2f}")
    print(f"Remaining Astrites (not used): {remaining_astrites:.2f}")
    print(f"Average remaining Radiant Tides: {avg_remaining_tides:.2f}")

if __name__ == "__main__":
    calculate_gacha_probability(
        astrites=64030,
        radiant_tides=85,
        afterglow_coral=173,
        n_sims=10000,
        target_copies=7,
        featured_5_star='Camellya',
        featured_4_stars=['Chixia', 'Sanhua', 'Danjin']
    )