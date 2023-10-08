import os
import re
import sys


def replace_cloze_format(file_path, output_dir):
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
        # 正規表現を使って、指定されたフォーマットをCloze形式に置換
        content = re.sub(r"\{([^}]+)\}", r"{{c1::\1}}", content)

    # 出力ディレクトリに同じ名前のファイルとして保存
    output_path = os.path.join(output_dir, os.path.basename(file_path))
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(content)


def main():
    if len(sys.argv) != 2:
        print("Usage: python script_name.py <directory_path>")
        return

    dir_path = sys.argv[1]
    parent_dir = os.path.dirname(os.path.abspath(dir_path))
    # 出力ディレクトリの作成
    output_dir = os.path.join(parent_dir, "output")
    os.makedirs(output_dir, exist_ok=True)

    # 指定されたディレクトリ内のすべての.txtファイルを走査
    for root, _, files in os.walk(dir_path):
        for file in files:
            if file.endswith(".txt"):
                replace_cloze_format(os.path.join(root, file), output_dir)


if __name__ == "__main__":
    main()
