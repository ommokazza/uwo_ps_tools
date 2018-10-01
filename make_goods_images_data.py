#! python3
"""A Script to run convert_goods_images_to_bin.py
"""
import os

# Modify This --------------------------------------------------
INPUT_DIR = "./resources/training_data_goods"
OUTPUT_DIR = "./gen"
OUTPUT_NAME = "goods"
# --------------------------------------------------------------

cmd = "python tools/convert_goods_images_to_bin.py"
cmd += " --input_dir=" + os.path.abspath(INPUT_DIR)
cmd += " --output_dir=" + os.path.abspath(OUTPUT_DIR)
cmd += " --output_name=" + OUTPUT_NAME

os.system(cmd)