import os
import sys
base = os.getcwd()

statesFolder = base + "/States"
assetsFolder = base + "/Assets"
configFolder = base + "/Configuration"

sys.path.insert(1, statesFolder)
sys.path.insert(1, assetsFolder)
sys.path.insert(1, configFolder)
