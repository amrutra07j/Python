# import csv
# temp_list = []
# with open("weather_data.csv") as we_data:
#     data = csv.reader(we_data)
#     for row in data:
#         if row[1] != "temp":
#             temp_list.append(int(row[1]))
#
# print(f"mean = {sum(temp_list)/len(temp_list)}")

# import pandas
# data = pandas.read_csv("weather_data.csv")
# se = data["temp"]
# data_dict = data.to_dict()
# temp_list = data["temp"].mean()
# print(data_dict)
# print(temp_list)
# print(data[data.day == "Monday"])
# print(data[data.temp == data.temp.max()])
import pandas

data = pandas.read_csv("Central_Park_Squirrel_Census.csv")
sq_color = list(set(data["Primary Fur Color"]))[1:]
count = data["Primary Fur Color"].value_counts().to_list()
dict1 = {"Fur Color": sq_color, "count": count}
# db = col.to_list()
print(sq_color)
print(count)
final = pandas.DataFrame(dict1)
final.to_csv("color_squirrel.csv")