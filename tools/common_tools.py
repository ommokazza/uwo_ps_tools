import os

from PIL import Image

from uwo_ps_utils import common
from uwo_ps_utils import cropper

TH = 200    #Threshhold

def generate_chat_messages(in_dir, out_dir):
    """Generate chatting messages from the screenshots in in_dir to out_dir.
    """
    files = sorted(common.get_image_paths(in_dir, "bmp"))

    if not os.path.exists(out_dir):
        os.makedirs(out_dir)

    mk_bytes = Image.open("resources/chat_imgs/marketkeeper.png")\
                    .point(__clear_bg)\
                    .tobytes()
    count = 0
    for f in files:
        print(f)
        im = Image.open(os.path.join(in_dir, f))
        chats = cropper.get_chat_msg(im)
        for chat in chats:
            teller_bytes = cropper.get_teller(chat).point(__clear_bg).tobytes()
            if mk_bytes == teller_bytes:
                name, _ = os.path.splitext(os.path.basename(f))
                chat.save(os.path.join(out_dir, name + "_" + str(count) + ".png"))
                count = count + 1

def generate_tokens(in_dir, out_dir):
    """Generate token images from the chat images in_dir to out_dir.

    Remark! the category names are same in plummeted and flooded.
    So, only 1 set is enough.
    """
    files = sorted(common.get_image_paths(in_dir, "png"))

    if not os.path.exists(out_dir):
        os.makedirs(out_dir)

    for f in files:
        print(f)
        name, _ = os.path.splitext(os.path.basename(f))
        im = Image.open(f)
        t1 = cropper.get_first_token(im)
        t1.save(os.path.join(out_dir, "t1_" + name + ".png"))
        pm = cropper.get_plummet_second_token(im)
        pm.save(os.path.join(out_dir, "pm_" + name + ".png"))
        fl = cropper.get_flooded_second_token(im)
        fl.save(os.path.join(out_dir, "fl_" + name + ".png"))

def compare_token(im1, im2):
    bytes1 = im1.point(__clear_bg).tobytes()
    bytes2 = im2.point(__clear_bg).tobytes()
    return bytes1 == bytes2

def __clear_bg(c):
    return int(c / TH) * 255

# generate_chat_messages({in_dir}, "gen/chats")
# generate_tokens("gen/chats", "gen/tokens")
