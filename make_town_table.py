#! python3
"""A Script to run generate_town_table.py
"""
import sys

import tools.generate_town_table as gtt

# Modify This ------------------------------
SAMPLE_DIR = "./sample_screenshots"
# ------------------------------------------

print(gtt.get_town_table(SAMPLE_DIR))