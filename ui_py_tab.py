# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'py_tab.ui'
##
## Created by: Qt User Interface Compiler version 6.5.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialog, QDialogButtonBox,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(452, 300)
        self.run_task = QDialogButtonBox(Dialog)
        self.run_task.setObjectName(u"run_task")
        self.run_task.setGeometry(QRect(40, 240, 341, 32))
        self.run_task.setOrientation(Qt.Horizontal)
        self.run_task.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 50, 61, 16))
        self.select_file_btn = QPushButton(Dialog)
        self.select_file_btn.setObjectName(u"select_file_btn")
        self.select_file_btn.setGeometry(QRect(270, 40, 75, 24))
        self.select_dir_src_btn = QPushButton(Dialog)
        self.select_dir_src_btn.setObjectName(u"select_dir_src_btn")
        self.select_dir_src_btn.setGeometry(QRect(350, 40, 75, 24))
        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 120, 81, 20))
        self.select_dir_res_btn = QPushButton(Dialog)
        self.select_dir_res_btn.setObjectName(u"select_dir_res_btn")
        self.select_dir_res_btn.setGeometry(QRect(280, 110, 75, 24))
        self.source_code_path_edt = QLineEdit(Dialog)
        self.source_code_path_edt.setObjectName(u"source_code_path_edt")
        self.source_code_path_edt.setGeometry(QRect(90, 39, 171, 31))
        self.result_path_edt = QLineEdit(Dialog)
        self.result_path_edt.setObjectName(u"result_path_edt")
        self.result_path_edt.setGeometry(QRect(100, 109, 171, 31))

        self.retranslateUi(Dialog)
        self.run_task.accepted.connect(Dialog.accept)
        self.run_task.rejected.connect(Dialog.reject)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"\u6e90\u4ee3\u7801\u8def\u5f84", None))
        self.select_file_btn.setText(QCoreApplication.translate("Dialog", u"\u9009\u62e9\u6587\u4ef6", None))
        self.select_dir_src_btn.setText(QCoreApplication.translate("Dialog", u"\u9009\u62e9\u6587\u4ef6\u5939", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"\u7ed3\u679c\u5b58\u50a8\u8def\u5f84", None))
        self.select_dir_res_btn.setText(QCoreApplication.translate("Dialog", u"\u9009\u62e9\u6587\u4ef6\u5939", None))
    # retranslateUi

