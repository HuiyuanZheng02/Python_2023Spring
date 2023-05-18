'''
2023-05-18
@HuiyuanZheng02
'''
import os

def main(file_name):
    '''
    @description: 装饰文本
    @param {str} file_name 文件名
    '''
    # Check if the input file exists
    if not os.path.exists(file_name):
        print(f"{file_name} does not exist.")
        return
    # Open the input file and read the text
    with open(file_name, "r") as f:
        text = f.readlines()

    # Find the length of the longest line in the text
    max_len = max([len(line.rstrip()) for line in text])

    # Add the top and bottom borders to the text
    decorated_text = ["+" + "-" * (max_len + 2) + "+\n"]
    for line in text:
        # Remove any trailing whitespace from the line
        line = line.rstrip()
        # Add the left border and the line to the decorated text
        decorated_text.append("| " + line + " " * (max_len - len(line)) + " |\n")
    decorated_text.append("+" + "-" * (max_len + 2) + "+\n")

    # Write the decorated text to the output file
    with open("decorate.txt", "w") as f:
        f.writelines(decorated_text)

if __name__ == '__main__':
    main('project10.txt')