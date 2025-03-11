import re

# ## Problem 2: Match digits

# **Task**: Write a regex pattern that matches any single digit.

# **Example**:
# - "There are 365 days in a year" ➡ Should match "3", "6", "5"
# - "No numbers here" ➡ Should not match anything

alltxt = ["There are 365 days in a year","No numbers here"]
pattern = r'[0-9]'
for tx in alltxt:
    print(re.findall(pattern,tx))