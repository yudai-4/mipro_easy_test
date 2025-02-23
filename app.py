# app.py
from flask import Flask, request, render_template, redirect, url_for, session
import os
from test_case_scanner import scan_test_cases_by_problem
from wandbox_client import compile_and_run
from grader import compare_outputs

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'  # セッション利用のためのシークレットキー

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        assignment_dir = request.form.get('assignment_dir')
        if not assignment_dir:
            return "課題ディレクトリパスは必須です", 400
        session['assignment_dir'] = assignment_dir
        return redirect(url_for('problems'))
    return render_template("index.html")

@app.route('/problems')
def problems():
    assignment_dir = session.get('assignment_dir')
    if not assignment_dir:
        return redirect(url_for('index'))
    test_cases = scan_test_cases_by_problem(assignment_dir)
    return render_template("problems.html", test_cases=test_cases, assignment_dir=assignment_dir)

@app.route('/problem/<problem_id>', methods=['GET', 'POST'])
def problem(problem_id):
    assignment_dir = session.get('assignment_dir')
    if not assignment_dir:
        return redirect(url_for('index'))
    test_cases_dict = scan_test_cases_by_problem(assignment_dir)
    if problem_id not in test_cases_dict:
        return f"問題 {problem_id} が見つかりません。", 400

    if request.method == 'POST':
        source_file = request.files.get('source_code')
        if not source_file:
            return "ソースコードファイルは必須です", 400
        code = source_file.read().decode("utf-8")
        problem_results = []
        for in_file in test_cases_dict[problem_id]:
            with open(in_file, 'r', encoding="utf-8") as f:
                test_input = f.read()
            out_file = in_file.replace("in", "out")
            if os.path.exists(out_file):
                with open(out_file, 'r', encoding="utf-8") as f:
                    expected_output = f.read()
            else:
                continue
            execution_result = compile_and_run(code, test_input)
            if "error" in execution_result:
                result_detail = {
                    "input": test_input,
                    "expected": expected_output,
                    "actual": "",
                    "error": execution_result["error"],
                    "grade": "Error"
                }
            else:
                actual_output = execution_result.get("program_output", "")
                is_correct, detail = compare_outputs(expected_output, actual_output)
                result_detail = {
                    "input": test_input,
                    "expected": expected_output,
                    "actual": actual_output,
                    "error": execution_result.get("compiler_error", ""),
                    "grade": "AC" if is_correct else "WA",
                    "details": detail
                }
            problem_results.append(result_detail)
        return render_template("results.html", problem_id=problem_id, results=problem_results)
    else:
        return render_template("problem.html", problem_id=problem_id)

if __name__ == '__main__':
    app.run(debug=True)