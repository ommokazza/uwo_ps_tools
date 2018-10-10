import os
import urllib

from imgurpython import ImgurClient

CLIENT_ID = '077727de8f6f20d'
ALBUM_ID = 'A5bsWH2'

DOWNLOAD_PATH = "downloads"

def main(is_all):
    client = ImgurClient(CLIENT_ID, None)

    images = client.get_album_images(ALBUM_ID)
    for image in images:
        print(image.title, image.id, image.description)
        path = os.path.join(DOWNLOAD_PATH, image.title)
        if not os.path.exists(path):
            os.makedirs(path)

        descs = image.description.splitlines()
        name = image.id + "_" + descs[0] + ".png"
        if need_to_download(is_all, descs):
            urllib.request.urlretrieve(image.link, os.path.join(path, name))

def need_to_download(is_all, descs):
    if is_all or len(descs) == 1:
        return True
    
    if descs[1] == '(Closed)':
        return False

    return True

if __name__ == "__main__":
    print("Manage Suggestions:")
    print("  1. Download not closed suggestions")
    print("  2. Download all suggestions")
    print("")

    while True:
        choice = input("Select: ")
        if choice == "1":
            main(False)
            break
        elif choice == "2":
            main(True)
            break
        else:
            continue
