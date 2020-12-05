import sys
from PyQt5 import QtWidgets
from ui_class import UiMainWindow

app = QtWidgets.QApplication(sys.argv)
main_window = QtWidgets.QMainWindow()
ui = UiMainWindow()
ui.setup_ui(main_window)

main_window.show()
sys.exit(app.exec_())
