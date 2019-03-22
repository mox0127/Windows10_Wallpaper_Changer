
# Created by: Pycharm
# Auther: MoGyver
# Date: 11/25/2018
# Time: 11:49 AM

import ctypes
import os
from datetime import datetime
from PIL import Image
#win10_img_path = "%userprofile%\AppData\Local\Packages\Microsoft.Windows.ContentDeliveryManager_cw5n1h2txyewy\LocalState\Assets"
#ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
#local_images_path = os.path.join(ROOT_DIR, 'windows_images')


# def rename_images():
#     #img_files = os.listdir(local_images_path)
#
#     for f in os.listdir(local_images_path):
#         print('old file name: ', f)
#         old_name = os.path.join(local_images_path, f)
#         new_name = os.path.join(local_images_path,f) + '.jpg'
#         os.rename(old_name, new_name)
#         im = Image.open(new_name)
#         print(im.size)


read_only_path = 'C:\ProgramData\Microsoft\Windows\SystemData\S-1-5-21-4069847384-3223734922-1025951441-1001\ReadOnly\LockScreen_O'

def read_sys_images():
    win10_img_path = "%userprofile%\AppData\Local\Packages\Microsoft.Windows.ContentDeliveryManager_cw5n1h2txyewy\LocalState\Assets"
    ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
    local_images_path = os.path.join(ROOT_DIR, 'windows_images')

    wallpapers = []
    img_system_path = os.path.expandvars(win10_img_path)
    max_create_time = datetime.now().strftime("%Y-%m-%d")

    for i in os.listdir(img_system_path):
        t = os.path.getctime(os.path.join(img_system_path, i))
        if max_create_time == datetime.fromtimestamp(t).strftime('%Y-%m-%d'):
            wallpapers.append(i)
            print(i)
            change_desktop_background(os.path.join(img_system_path, i))
        else:
            continue

    ready_img=''
    for x in wallpapers:
        z = os.path.join(img_system_path, x)
        im = Image.open(z)
        width, height = im.size
        if width < 1920 or height < 1080:
            continue
        else:
            ready_img = z
            print(ready_img, im.size)  # , datetime.fromtimestamp(max_create_time).strftime('%Y-%m-%d'))

    #change_desktop_background(os.path.join(img_system_path, z))


    # find image with large size of images with the same date/time stamp

    if len(wallpapers) > 1:
         size = 0
         for y in wallpapers:
             img_full_path = os.path.join(img_system_path, y)
             sz = os.path.getsize(img_full_path)
             if size < sz:
                 size = sz
                 ready_img = y
             else:
                 continue

         print('the cadidate image: ', ready_img)

    change_desktop_background(os.path.join(img_system_path, ready_img))

    # print(datetime.now().strftime("%Y-%m-%d"))


def change_desktop_background(image_url):
    SPI_SETDESKWALLPAPER = 20
    ctypes.windll.user32.SystemParametersInfoA(SPI_SETDESKWALLPAPER, 0, image_url, 0)



def main():
    read_sys_images()

if __name__ == "__main__":
    main()
