# プログラミングテスト自動採点システム

## 概要
このシステムは、授業のプログラミングテストにおいて、ソースコードの提出・採点や問題一覧の表示を行います。  
問題一覧は、フォルダ内のファイル名から「1-1」などの問題名を抽出し、AtCoder風のUIで表示します。

## インストールと起動方法
1. GitHubから本リポジトリをクローンしてください。
   ```bash
   git clone https://github.com/yudai-4/mipro_easy_test
   cd programming_test_system
   python3 app.py
## 使い方
まず、http://127.0.0.1:5000/
にアクセスします。
sharepointから"公開"フォルダをダウンロードして、解凍し、そのフォルダのパスを取得してください。
それを貼り付けたらあとはUIに従うとできます。

## About this repository
This system facilitates the submission and grading of source code for programming tests in classes, as well as the display of a list of problems.
The problem list is extracted from file names within a folder (e.g., “1-1”) and is presented in a relatively user-friendly UI. There are plans to improve the UI in the future.
## Install and Open
1. Clone this repository from Github
   ```bash
   git clone https://github.com/yudai-4/mipro_easy_test
   cd programming_test_system
   python3 app.py
## Usage
First, access http://127.0.0.1:5000/
Download the “公開” folder from SharePoint, extract it, and obtain the folder path.
Paste the path into the system, then follow the UI instructions to proceed.
