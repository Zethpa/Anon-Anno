def normalize_coords(x, y, img_width, img_height):
    """ 像素坐标 -> 归一化坐标 """
    return x / img_width, y / img_height

def denormalize_coords(x, y, img_width, img_height):
    """ 归一化坐标 -> 像素坐标 """
    return x * img_width, y * img_height