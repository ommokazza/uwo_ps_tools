#! python3
"""A Script to run generate_label_ml.py
"""
import sys

import tools.generate_label_ml as glt

# Modify This ------------------------------
SCREENSHOT_DIR = "C:\\Users\\ommok\\Documents\\src\\raw_data\\screenshots_no_label"
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
    # labels[3] = 'Lisbon'
    # labels[6] = 'Porto'
    # labels[9] = 'Gijon'
    # labels[12] = 'Seville'
    # labels[15] = 'Bilbao '
    return labels

glt.main(SCREENSHOT_DIR,
         MODEL_DIRS,
         LABEL_PATHS,
         "!LowRank",    #filter string
         __manual_fix)
