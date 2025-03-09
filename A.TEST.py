def solve_spiderman_workout(moves):
    total_sum = sum(moves)
    
    # dp[i][h] = minimum maximum height if we're at move i and height h
    # Initialize with float('inf') (unreachable states)
    dp = [[float('inf') for _ in range(total_sum + 1)] for _ in range(len(moves) + 1)]
    
    # choice[i][h] = 'U' if we went up at move i to reach height h, 'D' if down
    choice = [['' for _ in range(total_sum + 1)] for _ in range(len(moves) + 1)]
    
    # Base case: at move 0, height is 0, and max height so far is 0
    dp[0][0] = 0
    
    for i in range(1, len(moves) + 1):
        dist = moves[i-1]  # Current move distance
        
        for h in range(total_sum + 1):
            # Try going up
            if h >= dist:  # We can only go up if we were at height h-dist before
                new_max = max(dp[i-1][h-dist], h)  # Max height is either previous max or current height
                if new_max < dp[i][h]:
                    dp[i][h] = new_max
                    choice[i][h] = 'U'
            
            # Try going down
            if h + dist <= total_sum:  # Make sure we don't go out of bounds
                new_max = max(dp[i-1][h+dist], h+dist)  # Max height includes h+dist
                if new_max < dp[i][h]:
                    dp[i][h] = new_max
                    choice[i][h] = 'D'
    
    # Check if there's a solution that ends at height 0
    if dp[len(moves)][0] == float('inf'):
        return "IMPOSSIBLE"
    
    # Reconstruct the path
    path = []
    h = 0
    for i in range(len(moves), 0, -1):
        path.append(choice[i][h])
        if choice[i][h] == 'U':
            h -= moves[i-1]
        else:
            h += moves[i-1]
    
    return ''.join(reversed(path))

def main():
    n = int(input())
    for _ in range(n):
        m = int(input())
        moves = list(map(int, input().split()))
        print(solve_spiderman_workout(moves))

if __name__ == "__main__":
    main()