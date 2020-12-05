from PyQt5 import QtCore, QtGui, QtWidgets
from search_job import SearchJob


class UiMainWindow():
    def setup_ui(self, main_window):
        main_window.setWindowTitle('Phone-number-tracker')
        size = {
            'width': {
                'default': 600,
                'minimum': 100,
                'maximum': 10000
            },
            'height': {
                'default': 400,
                'minimum': 100,
                'maximum': 10000
            }
        }
        main_window.resize(size['width']['default'],
                           size['height']['default'])
        main_window.setMinimumSize(size['width']['minimum'],
                                   size['height']['minimum'])
        main_window.setMaximumSize(size['width']['maximum'],
                                   size['height']['maximum'])

        self.centralwidget = QtWidgets.QWidget(main_window)
        self.centralwidget.setStyleSheet('background-color: #eaeaea;')
        
        # stackedwidget
        self.stackedwidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedwidget.setGeometry(100, 100, 
                                       size['width']['default'] - 200,
                                       size['height']['default'] - 200)

        # stackedwidget main_page
        self.main_page = QtWidgets.QWidget()
        self.main_page.setGeometry(100, 100, 
                                   size['width']['default'] - 200,
                                   size['height']['default'] - 200)
        self.main_page_layout = QtWidgets.QVBoxLayout(self.main_page)

        self.main_page_title = QtWidgets.QLabel(self.main_page)
        self.setup_qlabel(self.main_page_title, 'The phone number tracker', 24, '#ea5506')
        self.main_page_title.setFixedHeight(100)

        self.main_page_note = QtWidgets.QLabel(self.main_page)
        self.setup_qlabel(self.main_page_note, "Note: No '-' needed", 12, '#3e3e3e')

        self.main_page_phone_number = QtWidgets.QLineEdit(self.main_page)
        self.main_page_phone_number.setFont(self.setup_font(14))
        self.main_page_phone_number.setMaxLength(34)
        self.main_page_phone_number.setStyleSheet('color: #2e2e2e; border: 2px solid #7fbfff; border-radius: 4px; padding: 2px')

        self.main_page_track_btn = QtWidgets.QPushButton(self.main_page)
        self.main_page_track_btn.setText('Track')
        self.main_page_track_btn.setFont(self.setup_font(14))
        self.main_page_track_btn.setStyleSheet('color: #2e2e2e;')
        self.main_page_track_btn.clicked.connect(self.clicked_track)

        self.main_page_layout.addWidget(self.main_page_title)
        self.main_page_layout.addWidget(self.main_page_note)
        self.main_page_layout.addWidget(self.main_page_phone_number)
        self.main_page_layout.addWidget(self.main_page_track_btn)
        self.stackedwidget.addWidget(self.main_page)

        # stackedwidget result_page
        self.result_page = QtWidgets.QWidget()
        self.result_page.setGeometry(100, 100,
                                     size['width']['default'] - 200,
                                     size['height']['default'] - 200)
        self.result_page_layout = QtWidgets.QVBoxLayout(self.result_page)
        self.result_page_layout.setContentsMargins(0, 0, 0, 0)

        self.result_page_title = QtWidgets.QLabel(self.result_page)
        self.setup_qlabel(self.result_page_title, '', 16)
        self.result_page_title.setFixedHeight(26)

        self.result_page_detail = QtWidgets.QPlainTextEdit(self.result_page)
        self.result_page_detail.setFont(self.setup_font(12))
        self.result_page_detail.setStyleSheet('border: 2px solid #7fbfff; border-radius: 4px')
        self.result_page_detail.verticalScrollBar().setStyleSheet('border: none')
        self.result_page_detail.setReadOnly(True)

        self.result_page_layout.addWidget(self.result_page_title)
        self.result_page_layout.addWidget(self.result_page_detail)
        self.stackedwidget.addWidget(self.result_page)

        self.stackedwidget.setCurrentIndex(0)
        main_window.setCentralWidget(self.centralwidget)

    def setup_qlabel(self, label, text, size, color='#2e2e2e'):
            label.setText(text)
            label.setFont(self.setup_font(size))
            label.setAlignment(QtCore.Qt.AlignHCenter)
            label.setStyleSheet('color: {}'.format(color))
        
    def setup_font(self, size):
        font = QtGui.QFont()
        font.setPointSize(size)
        return font

    def clicked_track(self):
        number = self.main_page_phone_number.text()
        job = SearchJob(number)
        try:
            job.search()
            result = job.finish()
            self.show_result(number, result)
        except ValueError as err:
            result = str(err)
            self.show_result(number, result)
            
    def show_result(self, number, result):
        self.result_page_title.setText(f'Result: {number}')
        self.result_page_detail.setPlainText(result)
        self.stackedwidget.setCurrentIndex(1)
