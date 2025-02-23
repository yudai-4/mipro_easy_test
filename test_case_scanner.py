# test_case_scanner.py
import os

def scan_test_cases_by_problem(root_dir):
    """
    課題ディレクトリ内の各トップレベルの数字フォルダについて、
    「テストケース」フォルダ内の数字サブディレクトリ（あれば）をそれぞれ問題として扱い、
    それ以外の場合はテストケースフォルダ直下の入力ファイルをひとまとめにして問題として扱います。

    ※ 対応する出力ファイル（入力ファイル名中の "in" を "out" に置換）が存在しない場合は無視します。

    戻り値は dict 形式:
      { "1-1": [ "path/to/input1.txt", "path/to/input2.txt", ... ],
        "1-2": [ "path/to/mipro012-1.in.txt", ... ],
        "2-1": [ "path/to/input1.txt", ... ], ... }
    """
    test_cases_by_problem = {}
    
    # 課題ディレクトリ直下の各数字フォルダ（例: "1", "2", …）を対象
    for top in os.listdir(root_dir):
        top_path = os.path.join(root_dir, top)
        if os.path.isdir(top_path) and top.isdigit():
            # 「テストケース」フォルダを探す
            test_cases_dir = os.path.join(top_path, "テストケース")
            if os.path.exists(test_cases_dir) and os.path.isdir(test_cases_dir):
                # サブディレクトリがあるかチェック
                subdirs = [d for d in os.listdir(test_cases_dir)
                           if os.path.isdir(os.path.join(test_cases_dir, d))]
                if subdirs:
                    # サブディレクトリがある場合、各数字フォルダを問題として扱う
                    for sub in subdirs:
                        if sub.isdigit():
                            problem_id = f"{top}-{sub}"
                            sub_path = os.path.join(test_cases_dir, sub)
                            input_files = []
                            for f in os.listdir(sub_path):
                                if "in" in f.lower():
                                    out_file = f.replace("in", "out")
                                    if os.path.exists(os.path.join(sub_path, out_file)):
                                        input_files.append(os.path.join(sub_path, f))
                            if input_files:
                                test_cases_by_problem[problem_id] = input_files
                else:
                    # サブディレクトリがなければ、test_cases_dir直下の入力ファイルをひとまとめにする
                    problem_id = f"{top}-1"
                    input_files = []
                    for f in os.listdir(test_cases_dir):
                        if "in" in f.lower():
                            out_file = f.replace("in", "out")
                            if os.path.exists(os.path.join(test_cases_dir, out_file)):
                                input_files.append(os.path.join(test_cases_dir, f))
                    if input_files:
                        test_cases_by_problem[problem_id] = input_files
    test_cases_by_problem = dict(sorted(test_cases_by_problem.items(), key=lambda x: x[0]))
    return test_cases_by_problem