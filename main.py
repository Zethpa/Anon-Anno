from PyQt5.QtWidgets import QApplication, QMainWindow
from widgets.canvas import AnnotationCanvas
from widgets.toolbar import ControlToolBar
from utils.file_loader import load_image_folder

class AnnotationApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("四点标注编辑器")
        self.setGeometry(100, 100, 1200, 800)
        
        # 初始化核心组件
        self.image_paths = []
        self.current_index = 0
        self.canvas = AnnotationCanvas(self)
        self.toolbar = ControlToolBar(self)
        
        # 布局设置
        self.setCentralWidget(self.canvas)
        self.addToolBar(self.toolbar)
        
    def load_folder(self, folder_path):
        """ 由工具栏调用 """
        self.image_paths = load_image_folder(folder_path)
        if self.image_paths:
            self.canvas.load_image(self.image_paths[0])

if __name__ == "__main__":
    app = QApplication([])
    window = AnnotationApp()
    window.show()
    app.exec_()