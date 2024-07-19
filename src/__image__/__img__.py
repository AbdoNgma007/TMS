
import os

base_dir = os.path.dirname(os.path.abspath(__file__))


files = os.listdir(base_dir)

def get_images() -> dict:
    images = {}
    for img in files:
        if ".py" not in img:
            key = img.split(".")[0]
            path = os.path.join(base_dir, img)
            images.update({key:path})

    return images