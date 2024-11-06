#https://goheels.com/sports/mens-basketball/roster

import pandas as pd

player = {"Last Name":["Cadeau", "Davis", "Tyson", "Trimble", "Powell", "Jackson", "Washington", "Withers", "Claude", "Brown"],
          "First Name": ["Elliot", "RJ", "Cade", "Seth", "Drake", "Ian", "Jalen", "Jae'lyn", "Ty", "James"],
          "height": [73, 70, 79, 75, 78, 76, 82, 81, 79, 82],
          "weight": [180, 180, 200, 195, 195, 190, 235, 220, 230, 215]}
data = pd.DataFrame(player)

# bmi = weight in kg/height in meters squared
data["bmi"] = ((data["weight"]/2.205)/((data["height"]/39.37)**2)).round(2)

print(data)

data.to_csv("bmi.csv")