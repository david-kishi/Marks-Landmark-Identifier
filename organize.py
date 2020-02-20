# Imports
import os, shutil
from random import randint

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
training_dict = {"0": [], "1": [], "2": [], "3": [], "4": [], "5": [], "6": [], "7": []}
test_dict = {"0": [], "1": [], "2": [], "3": [], "4": [], "5": [], "6": [], "7": []}


# Open txt that holds all file names and labels
labels = open("hirise-map-proj-v3/labels-map-proj-v3.txt", "r")

# Sort all filenames into training_dict
for line in labels:
    temp = line.strip().split(" ")
    if temp[1] == "0":
        training_dict["0"].append(temp[0])
    elif temp[1] == "1":
        training_dict["1"].append(temp[0])
    elif temp[1] == "2":
        training_dict["2"].append(temp[0])
    elif temp[1] == "3":
        training_dict["3"].append(temp[0])
    elif temp[1] == "4":
        training_dict["4"].append(temp[0])
    elif temp[1] == "5":
        training_dict["5"].append(temp[0])
    elif temp[1] == "6":
        training_dict["6"].append(temp[0])
    elif temp[1] == "7":
        training_dict["7"].append(temp[0])

# Use random to pop 50 images from each class into test_dict
for key in training_dict:
    while len(test_dict[key]) < 50:
        try:
            test_dict[key].append(
                training_dict[key].pop(randint(0, len(training_dict[key])))
            )
        except:
            pass

# Create training and testing directory
try:
    path = f"hirise-map-proj-v3/training/"
    if not os.path.isdir(path):
        os.mkdir(path)
    path = f"hirise-map-proj-v3/testing/"
    if not os.path.isdir(path):
        os.mkdir(path)
except OSError:
    print("Creation of the directory %s failed" % path)
else:
    print("Successfully created the directory %s" % path)

# Copy files into training folder
for key, val in training_dict.items():
    # Create directory
    try:
        path = f"hirise-map-proj-v3/training/{class_names[int(key)]}"
        if not os.path.isdir(path):
            os.mkdir(path)
    except OSError:
        print("Creation of the directory %s failed" % path)
    else:
        print("Successfully created the directory %s" % path)

    for item in val:
        try:
            source = f"hirise-map-proj-v3/map-proj-v3/{item}"
            destination = f"hirise-map-proj-v3/training/{class_names[int(key)]}/{item}"
            dest = shutil.copyfile(source, destination)
            print(f"Copied '{source}' to '{dest}'")
        except Exception as e:
            print(e)

# Copy files into testing folder
for key, val in test_dict.items():
    # Create directory
    try:
        path = f"hirise-map-proj-v3/testing/{class_names[int(key)]}"
        if not os.path.isdir(path):
            os.mkdir(path)
    except OSError:
        print("Creation of the directory %s failed" % path)
    else:
        print("Successfully created the directory %s" % path)

    for item in val:
        try:
            source = f"hirise-map-proj-v3/map-proj-v3/{item}"
            destination = f"hirise-map-proj-v3/training/{class_names[int(key)]}/{item}"
            dest = shutil.copyfile(source, destination)
            print(f"Copied '{source}' to '{dest}'")
        except Exception as e:
            print(e)

# Validate count
print(
    "\n" + ("-" * 40),
    "\n\t\t COUNT",
    "\n" + ("-" * 40) + "\n",
    "CLASS\t\tTRAINING\tTESTING",
    "\n" + ("-" * 40),
    f"\n{class_names[0]}\t\t{len(training_dict['0'])}\t\t{len(test_dict['0'])}",
    f"\n{class_names[1]}\t\t{len(training_dict['1'])}\t\t{len(test_dict['1'])}",
    f"\n{class_names[2]}\t{len(training_dict['2'])}\t\t{len(test_dict['2'])}",
    f"\n{class_names[3]}\t{len(training_dict['3'])}\t\t{len(test_dict['3'])}",
    f"\n{class_names[4]}\t{len(training_dict['4'])}\t\t{len(test_dict['4'])}",
    f"\n{class_names[5]}\t{len(training_dict['5'])}\t\t{len(test_dict['5'])}",
    f"\n{class_names[6]}\t{len(training_dict['6'])}\t\t{len(test_dict['6'])}",
    f"\n{class_names[7]}\t\t{len(training_dict['7'])}\t\t{len(test_dict['7'])}",
    "\n" + ("-" * 40),
    "\nTotal\t\t",
    sum(
        [
            len(training_dict["0"]),
            len(training_dict["1"]),
            len(training_dict["2"]),
            len(training_dict["3"]),
            len(training_dict["4"]),
            len(training_dict["5"]),
            len(training_dict["6"]),
            len(training_dict["7"]),
        ]
    ),
    "\t\t",
    sum(
        [
            len(test_dict["0"]),
            len(test_dict["1"]),
            len(test_dict["2"]),
            len(test_dict["3"]),
            len(test_dict["4"]),
            len(test_dict["5"]),
            len(test_dict["6"]),
            len(test_dict["7"]),
        ]
    ),
    "\n",
)
