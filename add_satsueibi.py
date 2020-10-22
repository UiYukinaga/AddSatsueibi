import PIL
from PIL import Image
from PIL import ExifTags
import cv2 as cv
import sys
import os

def get_exif(image_path):
    captured_datetime = None
    with Image.open(image_path) as imgfh:
        try:
            exif = imgfh._getexif()
            for attr, val in exif.items():
                tag = ExifTags.TAGS.get(attr, attr)
                if tag == 'DateTimeOriginal':
                    captured_datetime = val
        except AttributeError:
            pass
    return captured_datetime

def add_satsueibi(image_path):
    captured_datetime = get_exif(image_path)
    img = cv.imread(image_path)
    h, w, c = img.shape
    cv.putText(img, captured_datetime, (10, h-10),
               cv.FONT_HERSHEY_PLAIN, 12,
               (0, 128, 255), 3, cv.LINE_AA)
    
    '''
    # 以下2行をコメントアウトすると上書き保存モード
    raw_path = os.path.os.path.splitext(os.path.basename(image_path))[0]
    image_path = raw_path + "_with_date.jpg"
    '''
    cv.imwrite(image_path, img)
    
    b_name = os.path.basename(image_path)
    print(b_name + "に撮影日を書き込みました")
    
if __name__ == '__main__':
    args = sys.argv
    image_path = args[1]
    add_satsueibi(image_path)