import os
import sys

from PIL import Image


def convert_png_to_jpg(directory, quality=70):
    # 指定されたディレクトリ内およびサブディレクトリ内のファイルを一つずつ処理する
    for foldername, _, filenames in os.walk(directory):
        for filename in filenames:
            if filename.endswith(".png"):
                filepath = os.path.join(foldername, filename)
                # 変換後の.jpgが存在する場合はスキップ
                jpg_filepath = os.path.join(foldername, "hero_image.jpg")
                if os.path.exists(jpg_filepath):
                    continue
                # 画像を開く
                img = Image.open(filepath)
                # アルファチャンネル（透明度）がある場合は、白背景に合成
                if img.mode in ("RGBA", "LA"):
                    background = Image.new(img.mode[:-1], img.size, (255, 255, 255))
                    background.paste(img, img.split()[-1])
                    img = background
                # JPGとして保存
                img.save(jpg_filepath, "JPEG", quality=quality)


# 実行部分
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("使用方法: python convert_png_to_jpg.py [target_directory_path]")
        sys.exit(1)

    target_directory = sys.argv[1]
    convert_png_to_jpg(target_directory)
    print("変換が完了しました。")
