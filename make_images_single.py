#! python3
"""A Script to run convert_images_to_bin.py
"""
import os

# Goods Images --------------------------------------------------
INPUT_DIR = "./resources/training_data_goods"
OUTPUT_DIR = "./gen"
OUTPUT_NAME = "goods"
# --------------------------------------------------------------

cmd = "python tools/convert_images_to_bin.py"
cmd += " --input_dir=" + os.path.abspath(INPUT_DIR)
cmd += " --output_dir=" + os.path.abspath(OUTPUT_DIR)
cmd += " --output_name=" + OUTPUT_NAME

os.system(cmd)

# Towns Images --------------------------------------------------
INPUT_DIR = "./resources/training_data_towns_set"
OUTPUT_DIR = "./gen"
OUTPUT_NAME = "towns"
# --------------------------------------------------------------

cmd = "python tools/convert_images_to_bin.py"
cmd += " --input_dir=" + os.path.abspath(INPUT_DIR)
cmd += " --output_dir=" + os.path.abspath(OUTPUT_DIR)
cmd += " --output_name=" + OUTPUT_NAME

os.system(cmd)