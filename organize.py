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

# Dictionary to hold file names for each class
labels_dict = {"0": [], "1": [], "2": [], "3": [], "4": [], "5": [], "6": [], "7": []}

# Open txt that holds all file names and labels
labels = open("hirise-map-proj-v3/labels-map-proj-v3.txt", "r")

# Sort file names into lists
for line in labels:
    temp = line.strip().split(" ")
    if temp[1] == "0":
        labels_dict["0"].append(temp[0])
    elif temp[1] == "1":
        labels_dict["1"].append(temp[0])
    elif temp[1] == "2":
        labels_dict["2"].append(temp[0])
    elif temp[1] == "3":
        labels_dict["3"].append(temp[0])
    elif temp[1] == "4":
        labels_dict["4"].append(temp[0])
    elif temp[1] == "5":
        labels_dict["5"].append(temp[0])
    elif temp[1] == "6":
        labels_dict["6"].append(temp[0])
    elif temp[1] == "7":
        labels_dict["7"].append(temp[0])

# Validate count
print(
    "---- SUMMARY ----",
    f"\n{class_names[0]}: ",
    len(labels_dict["0"]),
    f"\n{class_names[1]}: ",
    len(labels_dict["1"]),
    f"\n{class_names[2]}: ",
    len(labels_dict["2"]),
    f"\n{class_names[3]}: ",
    len(labels_dict["3"]),
    f"\n{class_names[4]}: ",
    len(labels_dict["4"]),
    f"\n{class_names[5]}: ",
    len(labels_dict["5"]),
    f"\n{class_names[6]}: ",
    len(labels_dict["6"]),
    f"\n{class_names[7]}: ",
    len(labels_dict["7"]),
    "\nTotal: ",
    sum(
        [
            len(labels_dict["0"]),
            len(labels_dict["1"]),
            len(labels_dict["2"]),
            len(labels_dict["3"]),
            len(labels_dict["4"]),
            len(labels_dict["5"]),
            len(labels_dict["6"]),
            len(labels_dict["7"]),
        ]
    ),
)

# Create datasets directory
try:
    path = f"hirise-map-proj-v3/datasets/"
    if not os.path.isdir(path):
        os.mkdir(path)
except OSError:
    print("Creation of the directory %s failed" % path)
else:
    print("Successfully created the directory %s" % path)

# Copy files into categorized folders
for key, val in labels_dict.items():
    # Create directory
    try:
        path = f"hirise-map-proj-v3/datasets/{class_names[int(key)]}"
        if not os.path.isdir(path):
            os.mkdir(path)
    except OSError:
        print("Creation of the directory %s failed" % path)
    else:
        print("Successfully created the directory %s" % path)

    for item in val:
        try:
            source = f"hirise-map-proj-v3/map-proj-v3/{item}"
            destination = f"hirise-map-proj-v3/datasets/{class_names[int(key)]}/{item}"
            dest = shutil.copyfile(source, destination)
            print(f"Copied '{source}' to '{dest}'")
        except Exception as e:
            print(e)
