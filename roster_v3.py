import pandas as pd

roster = ["Cadeau", "Davis", "Tyson", "Trimble", "Powell", "Jackson", "Washington", "Withers", "Claude", "Brown"]
player = {"Last Name": roster}
data = pd.DataFrame(player)
print(data)