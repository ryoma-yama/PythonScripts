#!/bin/bash

# 実行時のコマンドの実行パスやexit;の表示をクリアして非表示
clear

# カレントディレクトリをこのスクリプトの場所に設定
DIR="$( cd "$( dirname "$0" )" && pwd )"
cd "$DIR"

# 'scripts' ディレクトリ内のPythonスクリプトを検索
for PYTHON_SCRIPT_PATH in "$DIR/scripts/"*.py; do
    PYTHON_SCRIPT_FILENAME=$(basename "$PYTHON_SCRIPT_PATH" .py)
    COMMAND_NAME="$DIR/commands/$PYTHON_SCRIPT_FILENAME.command"
    
    # .commandファイルが存在しない場合にのみ、新たに作成する
    if [ ! -f "$COMMAND_NAME" ]; then
        # .command ファイルを生成
        # ''はLiteralとしてそのまま、\"\"は変数として展開してから、追記
        echo '#!/bin/bash' > "$COMMAND_NAME"
        echo 'clear' >> "$COMMAND_NAME"
        echo 'DIR="$( cd "$( dirname "$0" )" && pwd )"' >> "$COMMAND_NAME"
        echo 'cd "$DIR/../scripts"' >> "$COMMAND_NAME"
        echo "python3 \"$PYTHON_SCRIPT_FILENAME.py\"" >> "$COMMAND_NAME"
        echo 'echo' >> "$COMMAND_NAME"
        echo 'read -n 1 -p "Press any key to continue ..."' >> "$COMMAND_NAME"

        # ユーザーへの実行権限を設定
        chmod u+x "$COMMAND_NAME"

        echo "$COMMAND_NAME file created and executable!"
    fi
done

# 空白行を挿入
echo
# n: 字数制限, p: 入力を求める前にプロンプトを表示
read -n 1 -p "Press any key to continue ..."
