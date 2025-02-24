class BoggleSolver:
    def __init__(self):
        # All 8 directions, matching C++ implementation
        self.dirs = [(0,1), (1,0), (-1,0), (0,-1), (-1,-1), (-1,1), (1,-1), (1,1)]
        
    def dfs(self, x, y, word, idx, grid, visited):
        # Base cases
        if idx == len(word):
            return True
        if (x < 0 or x >=  4 or y < 0 or y >=  4 or 
            visited[x][y] or grid[x][y] != word[idx]):
            return False
        visited[x][y] = True
        for dx, dy in self.dirs:
            next_x, next_y = x + dx, y + dy
            if self.dfs(next_x, next_y, word, idx + 1, grid, visited):
                visited[x][y] = False
                return True
                
        visited[x][y] = False
        return False
    
    def calculate_score(self, word_len):
        if word_len <= 4:
            return 1
        elif word_len == 5:
            return 2
        elif word_len == 6:
            return 3
        elif word_len == 7:
            return 5
        return 11
    
    def solve(self):
        test_cases = int(input())
        for tc in range(1, test_cases + 1):
            input()  # blank line
            
            # Read grid
            grid = [list(input().strip()) for _ in range( 4)]
            
            # Process words
            words_count = int(input())
            total_score = 0
            
            for _ in range(words_count):
                word = input().strip()
                found = False
                
                # Try each starting position
                visited = [[False] *  4 for _ in range( 4)]
                
                for i in range( 4):
                    if found:
                        break
                    for j in range( 4):
                        if grid[i][j] == word[0] and self.dfs(i, j, word, 0, grid, visited):
                            found = True
                            total_score += self.calculate_score(len(word))
                            break
            
            print(f"Score for Boggle game #{tc}: {total_score}")

if __name__ == "__main__":
    solver = BoggleSolver()
    solver.solve()