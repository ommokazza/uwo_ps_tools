#! python3
"""A Script to run generate_label_ml.py
"""
import sys

import tools.generate_label_ml as glt

# Modify This ------------------------------
SCREENSHOT_DIR = "./screenshots_no_label"
MODEL_DIRS = [
    "./resources/model_goods",
    "./resources/model_towns",
    "./resources/model_rates",
    "./resources/model_arrows"]
LABEL_PATHS = [
    "./resources/goods.labels",
    "./resources/towns.labels",
    "./resources/rates.labels",
    "./resources/arrows.labels"]
# ------------------------------------------

def __manual_fix(labels):
    # labels[3] = 'Madeira'
    # labels[6] = 'Madeira'
    # labels[9] = 'Arguin'
    # labels[12] = 'Cattaro'
    # labels[15] = 'Venice'
    return labels

glt.main(SCREENSHOT_DIR,
         MODEL_DIRS,
         LABEL_PATHS,
         "",    #filter string
         __manual_fix)
