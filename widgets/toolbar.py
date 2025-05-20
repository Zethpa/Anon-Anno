from PyQt5.QtWidgets import QToolBar, QPushButton, QFileDialog

class ControlToolBar(QToolBar):
    def __init__(self, parent):
        super().__init__("Tools", parent)
        self.parent = parent
        
        self.btn_open = QPushButton("打开文件夹")
        self.btn_prev = QPushButton("上一张")
        self.btn_next = QPushButton("下一张")
        self.btn_save = QPushButton("保存")
        
        self._setup_ui()
        
    def _setup_ui(self):
        self.addWidget(self.btn_open)
        self.addWidget(self.btn_prev)
        self.addWidget(self.btn_next)
        self.addWidget(self.btn_save)
        
        # 信号连接
        self.btn_open.clicked.connect(self._open_folder)
        self.btn_prev.clicked.connect(lambda: self.parent.canvas.load_prev_image())
        # ...其他信号连接
        
    def _open_folder(self):
        folder = QFileDialog.getExistingDirectory(self, "选择图片文件夹")
        if folder:
            self.parent.load_folder(folder)