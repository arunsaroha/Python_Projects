import pandas

squirrel = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
color = squirrel["Primary Fur Color"]
gray = 0
cinnamon = 0
white = 0
for c in color:
    if c == "Gray":
        gray += 1
    if c == "Cinnamon":
        cinnamon += 1
    else:
        white += 1

count = {
    "Fur Color": ["Gray", "Cinnamon", "White"],
    "Count": [gray, cinnamon, white],
}

final = pandas.DataFrame(count)
final.to_csv("fur_color_count.csv")
