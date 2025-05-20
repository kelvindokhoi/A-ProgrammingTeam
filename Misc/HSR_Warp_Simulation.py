from random import random, choices

# Honkai: Star Rail constants
pull_price = 160  # Stellar Jades per pull
five_star_base_rate = 0.006  # 0.6%
four_star_char_base_rate = 0.0255  # 2.55%
four_star_cone_base_rate = 0.0255  # 2.55%
trash_drop_rate = 0.943  # 94.3%
five_star_pity = 90
four_star_pity = 10
five_star_featured_rate = 0.5
four_star_featured_rate = 0.5
starlight_per_4star = 8
starlight_per_4star_overflow = 20
starlight_per_5star = 40
starlight_per_5star_overflow = 100
starlight_per_pull = 20
item_limit = 7  # Overflow after 7 copies

# 4-star characters
four_star_characters = [
    'Dan Heng', 'Serval', 'Moze', 'March 7th', 'Arlan', 'Asta', 'Herta', 'Natasha', 'Pela', 'Sampo',
    'Hook', 'Sushang', 'Qingque', 'Tingyun', 'Yukong', 'Luka', 'Lynx', 'Guinaifen', 'Hanya', 'Xueyi',
    'Misha', 'Gallagher'
]

# 4-star Light Cones
four_star_light_cones = [
    'Post-Op Conversation', 'Good Night and Sleep Well', 'Day One of My New Life', 'Only Silence Remains',
    'Memories of the Past', 'The Moles Welcome You', 'The Birth of the Self', 'Shared Feeling',
    'Eyes of the Prey', 'Landau\'s Choice', 'Swordplay', 'Planetary Rendezvous', 'A Secret Vow',
    'Make the World Clamor', 'Perfect Timing', 'Resolution Shines As Pearls of Sweat',
    'Trend of the Universal Market', 'Subscribe for More!', 'Dance! Dance! Dance!', 'Under the Blue Sky',
    'Genius\'s Repose', 'Indelible Promise', 'Concert for Two', 'Boundless Choreo',
    'After the Charmony Fall', 'Poised to Bloom', 'Shadowed by Night', 'Dream\'s Montage',
    'Genius\'s Greetings'
]

# Full 4-star pool
all_4_star = four_star_characters + four_star_light_cones

# Selectable non-featured 5-star characters
selectable_5_star = [
    'Fu Xuan', 'Seele', 'Blade', 'Himeko', 'Bronya', 'Gepard', 'Welt', 'Yanqing', 'Bailu', 'Clara'
]

def get_five_star_probability(pull_count):
    """Soft pity: Linear increase from pull 70 to 90"""
    if pull_count < 70:
        return five_star_base_rate
    elif pull_count >= five_star_pity:
        return 1.0
    else:
        slope = (1.0 - five_star_base_rate) / (five_star_pity - 70)
        return five_star_base_rate + slope * (pull_count - 70)

class Calculator:
    def __init__(self, featured_5_star, featured_4_stars, non_featured_5_stars):
        # Validate inputs
        if len(featured_4_stars) != 3:
            raise ValueError("featured_4_stars must contain exactly 3 characters/Light Cones")
        if not all(f in all_4_star for f in featured_4_stars):
            raise ValueError("All featured_4_stars must be valid 4-star entities")
        if len(non_featured_5_stars) != 7:
            raise ValueError("non_featured_5_stars must contain exactly 7 characters")
        if not all(f in selectable_5_star for f in non_featured_5_stars):
            raise ValueError("All non_featured_5_stars must be valid selectable 5-star characters")
        if featured_5_star in non_featured_5_stars:
            raise ValueError("featured_5_star cannot be in non_featured_5_stars")
        
        self.pity5 = 0
        self.guaranteed_featured = False
        self.pity4 = 0
        self.starlight = 0
        self.total_pull = 0
        self.paid_pull = 0
        self.five_star_copies = {char: 0 for char in non_featured_5_stars + [featured_5_star]}
        self.four_star_copies = {char: 0 for char in all_4_star}
        self.total_five_stars = 0
        self.total_featured_from_pulls = 0
        self.uprate_5_star = featured_5_star
        self.non_up_5_star = non_featured_5_stars
        self.uprate_4_star = featured_4_stars
        self.no_up_4_star = [item for item in all_4_star if item not in featured_4_stars]
        self.no_up_4_star_chars = [item for item in four_star_characters if item not in featured_4_stars]
        self.no_up_4_star_cones = [item for item in four_star_light_cones if item not in featured_4_stars]

    def random_5_star(self):
        if self.guaranteed_featured:
            self.guaranteed_featured = False
            return self.uprate_5_star, True
        if random() < five_star_featured_rate:
            self.guaranteed_featured = False
            return self.uprate_5_star, True
        else:
            self.guaranteed_featured = True
            return choices(self.non_up_5_star, [1/len(self.non_up_5_star)] * len(self.non_up_5_star))[0], False

    def random_4_star(self, is_character):
        # At 4-star pity, select from featured entities
        if self.pity4 >= four_star_pity:
            return choices(self.uprate_4_star, [1/len(self.uprate_4_star)] * len(self.uprate_4_star))[0], True
        # Otherwise, 50% chance for featured
        if random() < four_star_featured_rate:
            return choices(self.uprate_4_star, [1/len(self.uprate_4_star)] * len(self.uprate_4_star))[0], True
        # Select from non-featured characters or Light Cones
        if is_character:
            return choices(self.no_up_4_star_chars, [1/len(self.no_up_4_star_chars)] * len(self.no_up_4_star_chars))[0], False
        else:
            return choices(self.no_up_4_star_cones, [1/len(self.no_up_4_star_cones)] * len(self.no_up_4_star_cones))[0], False

    def accumulate(self, result):
        if result in self.five_star_copies:
            self.five_star_copies[result] += 1
            self.total_five_stars += 1
            if result == self.uprate_5_star:
                self.total_featured_from_pulls += 1
            # Starlight for 5-star
            if self.five_star_copies[result] > item_limit:
                self.starlight += starlight_per_5star_overflow
            else:
                self.starlight += starlight_per_5star
        elif result in self.four_star_copies:
            self.four_star_copies[result] += 1
            # Starlight for 4-star
            if result in four_star_characters and self.four_star_copies[result] > item_limit:
                self.starlight += starlight_per_4star_overflow
            else:
                self.starlight += starlight_per_4star

    def pull(self):
        # Prioritize Starlight-redeemed pulls
        if self.starlight >= starlight_per_pull:
            self.starlight -= starlight_per_pull
            self.total_pull += 1
        else:
            self.total_pull += 1
            self.paid_pull += 1
        
        self.pity5 += 1
        self.pity4 += 1

        five_star_prob = get_five_star_probability(self.pity5)
        pull_type = choices(
            [0, 1, 2, 3],
            [five_star_prob, four_star_char_base_rate, four_star_cone_base_rate, 1 - five_star_prob - four_star_char_base_rate - four_star_cone_base_rate]
        )[0]

        if pull_type == 0 or self.pity5 >= five_star_pity:
            result, uprate = self.random_5_star()
            self.pity5 = 0
            self.pity4 = 0
            self.accumulate(result)
        elif pull_type == 1 or (pull_type == 2 and self.pity4 >= four_star_pity):
            result, uprate = self.random_4_star(is_character=True)
            self.pity4 = 0
            self.accumulate(result)
        elif pull_type == 2:
            result, uprate = self.random_4_star(is_character=False)
            self.pity4 = 0
            self.accumulate(result)
        else:
            pass

    def roll_until_n_copies(self, n=7):
        while self.five_star_copies[self.uprate_5_star] < n:
            self.pull()
        total_five_star_copies = sum(self.five_star_copies.values())
        return (
            self.total_pull,
            self.paid_pull,
            self.total_five_stars,
            self.total_featured_from_pulls,
            self.five_star_copies[self.uprate_5_star],
            total_five_star_copies,
            self.starlight
        )

def n_tries(
    n_sims=10000,
    target_copies=7,
    featured_5_star='Dan Heng Imbibitor Lunae',
    featured_4_stars=['March 7th', 'Pela', 'Sampo'],
    non_featured_5_stars=['Fu Xuan', 'Seele', 'Blade', 'Himeko', 'Bronya', 'Gepard', 'Welt']
):
    list_total_pulls = []
    list_paid_pulls = []
    total_five_stars = 0
    total_featured_from_pulls = 0
    total_featured_copies = 0
    total_all_five_star_copies = 0
    total_starlight = 0
    for _ in range(n_sims):
        calc = Calculator(featured_5_star, featured_4_stars, non_featured_5_stars)
        total_pulls, paid_pulls, five_stars, featured_pulls, featured_copies, all_five_star_copies, starlight = (
            calc.roll_until_n_copies(target_copies)
        )
        list_total_pulls.append(total_pulls)
        list_paid_pulls.append(paid_pulls)
        total_five_stars += five_stars
        total_featured_from_pulls += featured_pulls
        total_featured_copies += featured_copies
        total_all_five_star_copies += all_five_star_copies
        total_starlight += starlight
    avg_total_pulls = sum(list_total_pulls) / n_sims
    avg_paid_pulls = sum(list_paid_pulls) / n_sims
    avg_stellar_jades = avg_paid_pulls * pull_price
    avg_pulls_per_five_star = sum(list_total_pulls) / total_five_stars if total_five_stars > 0 else 0
    avg_pulls_per_featured = sum(list_total_pulls) / total_featured_from_pulls if total_featured_from_pulls > 0 else 0
    avg_featured_copies = total_featured_copies / n_sims
    avg_all_five_star_copies = total_all_five_star_copies / n_sims
    avg_starlight = total_starlight / n_sims
    print(f'Average total pulls for {target_copies} {featured_5_star}: {avg_total_pulls:.2f}')
    print(f'Average paid pulls (excluding Starlight pulls): {avg_paid_pulls:.2f}, requires {avg_stellar_jades:.2f} Stellar Jades')
    print(f'Average pulls per 5-star (simulated): {avg_pulls_per_five_star:.2f}')
    print(f'Average pulls per {featured_5_star} from pulls (simulated): {avg_pulls_per_featured:.2f}')
    print(f'Average redemptions per simulation: 0.00 (no redemption in Honkai: Star Rail)')
    print(f'Average copies of {featured_5_star} per simulation: {avg_featured_copies:.2f}')
    print(f'Average total 5-star copies per simulation: {avg_all_five_star_copies:.2f}')
    print(f'Average unused Undying Starlights per simulation: {avg_starlight:.2f}')
    print(f'Featured 4-stars: {featured_4_stars}')
    print(f'Non-featured 5-stars: {non_featured_5_stars}')

if __name__ == "__main__":
    n_tries(
        target_copies=7,
        featured_5_star='Lệnh sứ Animation: Castorice',
        featured_4_stars=['March 7th', 'Pela', 'Sampo'],
        non_featured_5_stars=['Fu Xuan', 'Seele', 'Blade', 'Himeko', 'Bronya', 'Gepard', 'Welt']
    )