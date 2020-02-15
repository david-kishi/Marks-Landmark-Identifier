# Imports
import os, shutil

# Mars Landmark Classes
class_names = [
    "other",
    "crater",
    "dark dune",
    "slope streak",
    "bright dune",
    "impact ejecta",
    "swiss cheese",
    "spider",
]

# Dictionary to hold file counts for each class
labels_dict = {"0": 0, "1": 0, "2": 0, "3": 0, "4": 0, "5": 0, "6": 0, "7": 0}

# Open txt that holds all file names and labels
labels = open("hirise-map-proj-v3/labels-map-proj-v3.txt", "r")

# Sort file names into lists
for line in labels:
    temp = line.strip().split(" ")
    if temp[1] == "0":
        labels_dict["0"] += 1
    elif temp[1] == "1":
        labels_dict["1"] += 1
    elif temp[1] == "2":
        labels_dict["2"] += 1
    elif temp[1] == "3":
        labels_dict["3"] += 1
    elif temp[1] == "4":
        labels_dict["4"] += 1
    elif temp[1] == "5":
        labels_dict["5"] += 1
    elif temp[1] == "6":
        labels_dict["6"] += 1
    elif temp[1] == "7":
        labels_dict["7"] += 1

# Validate count
print(
    "---- SUMMARY ----",
    f"\n{class_names[0]}: ",
    labels_dict["0"],
    f"\n{class_names[1]}: ",
    labels_dict["1"],
    f"\n{class_names[2]}: ",
    labels_dict["2"],
    f"\n{class_names[3]}: ",
    labels_dict["3"],
    f"\n{class_names[4]}: ",
    labels_dict["4"],
    f"\n{class_names[5]}: ",
    labels_dict["5"],
    f"\n{class_names[6]}: ",
    labels_dict["6"],
    f"\n{class_names[7]}: ",
    labels_dict["7"],
    "\nTotal: ",
    sum(
        [
            labels_dict["0"],
            labels_dict["1"],
            labels_dict["2"],
            labels_dict["3"],
            labels_dict["4"],
            labels_dict["5"],
            labels_dict["6"],
            labels_dict["7"],
        ]
    ),
)
