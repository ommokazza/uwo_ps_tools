"""Converting goods images to single binary and label files.
"""
import argparse
import os

from PIL import Image

def main(input_dir, output_dir, output_name):
    files = sorted(get_image_paths(input_dir, "png"))

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    label_file = open(os.path.join(output_dir, output_name + ".labels"), "wt")

    im = Image.open(files[0])
    height = im.height
    out_img = Image.new("RGB", (im.width, height * len(files)))

    index = 0
    for f in files:
        name, _ = os.path.splitext(os.path.basename(f))
        label_file.write(name + os.linesep)

        im = Image.open(f)
        out_img.paste(im, (0, index * height))
        index += 1

    label_file.close()
    out_img.save(os.path.join(output_dir, output_name + ".png"))

def get_image_paths(directory, ext):
    """Get full paths with given extenstion

    Arguments:
        directory (str): Image directory path
        ext (str): Extenstion filter to add to list

    Return:
        full paths (list)
    """
    image_files = []
    for (dirpath, _, filenames) in os.walk(directory):
        for filename in filenames:
            if filename.lower().endswith(ext):
                image_files.append(os.sep.join([dirpath, filename]))
    return image_files

def __verify(goods_name):
    label_file = open("./gen/goods.labels", "rt")
    labels = label_file.read().splitlines()
    label_file.close()

    im = Image.open("./gen/goods.png")
    height = int(im.height / len(labels))

    index = labels.index(goods_name)
    print(labels[index])
    im.crop([0, index * height, im.width, index * height + height]).show()

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input_dir")
    parser.add_argument("-od", "--output_dir")
    parser.add_argument("-on", "--output_name")
    args = parser.parse_args()

    main(args.input_dir, args.output_dir, args.output_name)
