import os
import traceback
import ast

# text = input('请输入两个整数，以逗号隔开...')
# x, y = eval(text)

def test_eval():
    cmd = "__import__('os').startfile(r'C:\\Windows\\notepad.exe')"
    input('eval %s...'% cmd)
    eval(cmd)
    cmd2 = "os.startfile(r'C:\\Windows\\notepad.exe')"
    input('eval %s...'% cmd2)
    eval(cmd2)
    try:
        safe_dict = {"__builtins__": {}, "os": None }
        input('eval with safe_dict...')
        eval(cmd2,safe_dict)
    except :
        traceback.print_exc()
    try:
        input('ast.literal_eval %s...' % cmd2)
        ast.literal_eval( cmd )
    except ValueError :
        traceback.print_exc()

if __name__ == '__main__':
    test_eval()
