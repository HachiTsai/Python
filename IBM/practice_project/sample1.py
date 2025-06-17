"""sample1.py - 簡單的加法函式範例，示範 Python 變數、常數與函式用法。"""

def add(number1, number2):
    """回傳兩個數字的和。"""
    return number1 + number2

NUM1 = 4
NUM2 = 5
TOTAL = add(NUM1, NUM2)

print(f"The sum of {NUM1} and {NUM2} is {TOTAL}")
