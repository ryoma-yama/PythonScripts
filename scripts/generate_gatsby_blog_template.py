import datetime
import os

import inflection
from translate import Translator


# ユーザーからタイトルを入力として受け取る関数
def get_title_input():
    while True:  # タイトルが入力されるまでループ
        title = input("記事のタイトルを入力してください: ").strip()
        if title:  # タイトルが入力された場合
            return title


# タイトルを英語のkebab-caseに変換する関数
def title_to_slug(title):
    print("Translating the title...")  # デバッグ用のprint文
    try:
        # Memo: 翻訳前の言語は自動判別らしいがjaはfromで指定しないと翻訳されなかった
        translator = Translator(from_lang="ja", to_lang="en")
        translated_title = translator.translate(title)

        print(f"Translated title: {translated_title}")  # 翻訳後のタイトルを表示

        slug = inflection.parameterize(translated_title, separator="-").lower()  # kebab-caseで小文字にする
        print(f"Generated slug: {slug}")  # 生成されたスラッグを表示
        return slug
    except Exception as e:
        print(f"翻訳に失敗しました: {e}")
        return None


# メインの処理
def main():
    title = get_title_input()
    slug = title_to_slug(title)

    if not slug:  # 翻訳が失敗した場合は終了
        return

    today = datetime.datetime.now().strftime("%Y-%m-%d")

    # 保存先のパスを生成（WindowsとMacでの対応）
    user_home = os.path.expanduser("~")
    target_dir = os.path.join(user_home, "ryomazone.dev", "blog", f"{today}_{slug}")
    print(f"Directory path: {target_dir}")  # 作成予定のディレクトリパスを表示

    # ディレクトリが存在しない場合は作成
    if not os.path.exists(target_dir):
        os.makedirs(target_dir)

    # MDXファイルの内容を生成
    mdx_content = f"""---
title: {title}
date: "{today}"
slug: {slug}
hero_image: "./hero_image.jpg"
hero_image_alt: hero_image
tags: 
  - 
---

## はじめに



## おわりに



"""

    # MDXファイルを保存
    with open(os.path.join(target_dir, "index.mdx"), "w", encoding="utf-8") as file:
        file.write(mdx_content)

    print(f"MDXファイルが {target_dir}/index.mdx に保存されました。")


# スクリプトを実行
if __name__ == "__main__":
    main()
