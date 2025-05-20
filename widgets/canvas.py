from PyQt5.QtWidgets import QGraphicsView, QGraphicsScene
from PyQt5.QtGui import QPixmap, QPen, QBrush, QMouseEvent
from PyQt5.QtCore import Qt
from utils.coord_utils import normalize_coords, denormalize_coords

class AnnotationCanvas(QGraphicsView):
    def __init__(self, parent):
        super().__init__(parent)
        self.scene = QGraphicsScene()
        self.setScene(self.scene)
        self.current_points = []
        self.current_image_size = (0, 0)  # 记录当前图片尺寸

    def load_image(self, img_path):
        """ 加载图片和对应标注 """
        self.scene.clear()
        pixmap = QPixmap(img_path)
        self.scene.addPixmap(pixmap)
        self.current_image_size = (pixmap.width(), pixmap.height())
        
        # 加载标注文件（示例逻辑）
        txt_path = img_path.replace('.jpg', '.txt')
        self.current_points = self._load_annotation(txt_path)
        self._draw_points()
        
    def _load_annotation(self, txt_path):
        """ 从TXT文件加载坐标点 """
        with open(txt_path, 'r') as f:
            line = f.readline().strip()
            data = list(map(float, line.split()[1:]))
            points = [(data[i*2], data[i*2+1]) for i in range(4)]  # 转换为(x,y)元组
        return points
    
    def _draw_points(self):
        """ 绘制所有点（不同颜色表示顺序） """
        self.scene.clear()  # 清空后重新绘制
        # 重新添加图片（否则会被清空）
        pixmap = QPixmap(self.current_image_path)  # 需要提前保存current_image_path
        self.scene.addPixmap(pixmap)
        
        # 绘制点
        for i, (x, y) in enumerate(self.current_points):
            px, py = denormalize_coords(
                x, y, 
                self.current_image_size[0], 
                self.current_image_size[1]
            )
            color = QBrush(Qt.red if i == 0 else Qt.blue)
            self.scene.addEllipse(px-5, py-5, 10, 10, QPen(color), color)

    def mousePressEvent(self, event: QMouseEvent):
        """ 鼠标点击事件：添加或移动点 """
        if event.button() == Qt.LeftButton:
            # 获取点击位置（转换为归一化坐标）
            click_x = event.pos().x()
            click_y = event.pos().y()
            norm_x, norm_y = normalize_coords(
                click_x, click_y, 
                self.current_image_size[0], 
                self.current_image_size[1]
            )
            
            # 添加新点（插入到首位）
            self.current_points.insert(0, (norm_x, norm_y))
            self._draw_points()  # 重绘