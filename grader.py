# grader.py
import re

def normalize_whitespace(s):
    """余分な空白１つのスペースに置換"""
    return " ".join(s.split())

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

def compare_outputs(expected, actual, tolerance=1e-6):
    """
    expected と actual の出力文字列をトークン毎に比較する。
    数値トークンは相対誤差 tolerance を許容
    文字列は正規化後に完全一致で比較する。
    """
    expected_norm = normalize_whitespace(expected)
    actual_norm = normalize_whitespace(actual)
    
    exp_tokens = expected_norm.split()
    act_tokens = actual_norm.split()
    
    if len(exp_tokens) != len(act_tokens):
        return False, f"トークン数が一致しません（expected: {len(exp_tokens)}, actual: {len(act_tokens)}）"
    
    details = []
    for i, (e_token, a_token) in enumerate(zip(exp_tokens, act_tokens)):
        if is_number(e_token) and is_number(a_token):
            e_val = float(e_token)
            a_val = float(a_token)
            if e_val == 0:
                if abs(a_val - e_val) > tolerance:
                    details.append(f"Token {i}: expected {e_val}, got {a_val}")
            else:
                if abs(a_val - e_val) / abs(e_val) > tolerance:
                    details.append(f"Token {i}: expected {e_val}, got {a_val}")
        else:
            if e_token != a_token:
                details.append(f"Token {i}: expected '{e_token}', got '{a_token}'")
    
    if details:
        return False, "; ".join(details)
    return True, "出力が一致しました。"