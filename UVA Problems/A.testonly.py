# Read input
elephants = []
with open('.\sample_in.txt', 'r') as file:
    for line in file:
        weight, iq = map(int, line.strip().split())
        elephants.append({'id': len(elephants) + 1, 'weight': weight, 'iq': iq})

# Sort by weight in descending order
elephants.sort(key=lambda x: (-x['weight'], x['iq']))

# Apply LIS on IQ
n = len(elephants)
dp = [1] * n
sequence = [[] for _ in range(n)]

for i in range(n):
    sequence[i] = [elephants[i]['id']]
    for j in range(i):
        if elephants[j]['iq'] < elephants[i]['iq'] and elephants[j]['weight'] > elephants[i]['weight']:
            if dp[j] + 1 > dp[i]:
                dp[i] = dp[j] + 1
                sequence[i] = sequence[j] + [elephants[i]['id']]

# Find the maximum length and corresponding sequence
max_length = max(dp)
max_index = dp.index(max_length)
longest_sequence = sequence[max_index]

# Output the result
print(max_length)
for elephant_id in longest_sequence:
    print(elephant_id)