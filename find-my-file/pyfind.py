import os
import sys

currDir = os.getcwd()
if len(sys.argv) == 1:
    print("No arguments provided")
    sys.exit(1)
fileName = sys.argv[1]
newDir = os.path.join(currDir, fileName)


for root, dirs, files in os.walk(newDir):
    for file in files:
        if file.startswith("._"):
            continue
        print(os.path.join(root, file))