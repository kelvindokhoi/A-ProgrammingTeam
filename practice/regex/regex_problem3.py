

import re
pattern = r"\w+"
text = "user123_admin"
matches = re.findall(pattern, text)
print(matches) 

text ="user@example.com"
matches = re.findall(pattern, text)
print(matches) 