import re

# ## Problem 1: Match a specific string

# **Task**: Write a regex pattern that matches the exact string "python".

# **Example**:
# - "I love python programming" ➡ Should match "python"
# - "Python is fun" ➡ Should not match (case sensitive)
# - "typhoon" ➡ Should not match

text1 = "I love python programming"
text2 = "Python is fun"
text3 =  "typhoon"
alltxt = [text1,text2,text3]

pattern = r'python'
for text in alltxt:
    print(re.findall(pattern,text))