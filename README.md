# AddSatsueibi
写真に撮影した日時を書き込む

カメラで撮影した写真に日時を書き込むソースコード
写真撮影日時を読み込み、写真の左下に書き込む

- add_satsueibi.py: 主軸となるPythonファイル

Linux
```
$python3 add_satsueibi.py <写真のパス>
```


### Python OpenCVで画像に文字を入れる
#### OpenCVのputText()メソッドを用いた方法

写真の撮影日時を写真の左下へ追記するソースコードのサンプルを使って説明する

```python
import PIL
from PIL import Image
from PIL import ExifTags
import cv2 as cv
import sys

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

def write_text(image_path):
    captured_datetime = get_exif(image_path)
    
    print(captured_datetime)
    
    img = cv.imread(image_path)
    
    h, w, c = img.shape
    
    cv.putText(img, captured_datetime, (10, h),
               cv.FONT_HERSHEY_PLAIN, 14,
               (0, 128, 255), 1, cv.LINE_AA)
    cv.imwrite(image_path + '.new.jpg', img)
    

if __name__ == '__main__':
    args = sys.argv
    image_path = args[1]
    write_text(image_path)

```

実際に写真にテキストを入力しているのは、上記ソースコードの"write_text()"関数内にある、"cv.putText()"の部分。

**putText()"の引数は以下の通り**

| 順位 | 引数      |                                                              |
| ---- | --------- | ------------------------------------------------------------ |
| 1    | img       | `cv.imread` で開いた画像オブジェクト。                       |
| 2    | text      | 書き込む文字列。                                             |
| 3    | org       | 書き込む位置。文字列の左下の角が指定の位置に配置される。     |
| 4    | fontFace  | フォントスタイル。`CV_FONT_HERSHEY_PLAIN`、`CV_FONT_HERSHEY_SCRIPT_SIMPLEX` などを指定できる。 |
| 5    | fontScale | フォントサイズ。                                             |
| 6    | color     | フォントの色。                                               |
| 7    | thickness | フォントの太さ。                                             |
| 8    | lineType  | `4`、`8`、`cv.LINE_AA` のいずれかを指定できる。              |
