import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from explorer_widget import Explorer


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        explorer = Explorer(self)
        self.setCentralWidget(explorer)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    screen_rect = app.desktop().screenGeometry()
    main_window = MainWindow()
    main_window.resize(int(screen_rect.width()/2), int(screen_rect.height()/2))
    main_window.show()
    sys.exit(app.exec())