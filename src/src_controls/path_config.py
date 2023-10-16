import os
import sys


PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))[:-17]
print("project dir",PROJECT_DIR)

CONFIG_DIR = os.path.join(PROJECT_DIR,"config")
DATA_DIR = os.path.join(PROJECT_DIR,"data")
OUTPUT_DIR = os.path.join(PROJECT_DIR,"outputs")