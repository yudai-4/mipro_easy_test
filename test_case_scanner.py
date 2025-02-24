# test_case_scanner.py
import os

def scan_test_cases_by_problem(root_dir):
    """
    DFS Retrieval of test cases and problem IDs.
      { "1-1": [ "path/to/input1.txt", "path/to/input2.txt", ... ],
        "1-2": [ "path/to/mipro012-1.in.txt", ... ],
        "2-1": [ "path/to/input1.txt", ... ], ... }
    """
    test_cases_by_problem = {}
    for top in os.listdir(root_dir):
        top_path = os.path.join(root_dir, top)
        if os.path.isdir(top_path) and top.isdigit():
            test_cases_dir = os.path.join(top_path, "テストケース")
            if os.path.exists(test_cases_dir) and os.path.isdir(test_cases_dir):
                subdirs = [d for d in os.listdir(test_cases_dir)
                           if os.path.isdir(os.path.join(test_cases_dir, d))]
                if subdirs:
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