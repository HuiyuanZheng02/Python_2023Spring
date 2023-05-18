import os

def visit_tree(path): 
    if not os.path.isdir(path):
        print('Error:"',path,'" is not a directory or does not exist.')
        return
    for lists in os.listdir(path): 
        sub_path = os.path.join(path, lists) 
        print(sub_path) 
        if os.path.isdir(sub_path):  
            visit_tree(sub_path)

def visit_tree2(path):
    if not os.path.isdir(path):
        print('Error:"',path,'" is not a directory or does not exist.')
        return
    # os.walk返回的对象的每个元素为3个元素的元组：目录、该目录下子目录列表表、该目录下文件列表
    list_dirs = os.walk(path)   
    # 遍历该元组的目录和文件信息
    for root, dirs, files in list_dirs:  
        for d in dirs: 
            # 获取完整路径
            print(os.path.join(root, d))  
        for f in files: 
            #获取文件绝对路径
            print(os.path.join(root, f))  

if __name__ == '__main__':
    visit_tree('..')

    print()
    visit_tree2('..')