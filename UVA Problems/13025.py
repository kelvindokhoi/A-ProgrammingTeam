# 13025 - Back to the Past

from datetime import date

data = date(2013,5,29)
print(data.strftime("%B %d, %Y ") + data.strftime('%A'))

