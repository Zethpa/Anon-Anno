import os

def load_image_folder(folder_path):
    """ 返回文件夹内所有图片路径列表 """
    valid_ext = ['.jpg', '.png', '.jpeg']
    return [
        os.path.join(folder_path, f) 
        for f in os.listdir(folder_path) 
        if os.path.splitext(f)[1].lower() in valid_ext
    ]

def save_annotation(txt_path, points):
    """ 保存标注到TXT文件 """
    with open(txt_path, 'w') as f:
        flat_coords = ' '.join([f"{x:.5f} {y:.5f}" for x, y in points])
        f.write(f"0 {flat_coords}")