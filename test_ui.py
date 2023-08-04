"""
作者:周乐天
日期:2023年08月03日
"""
import ctypes
import sys

from PySide6.QtWidgets import QMainWindow, QFileDialog, QApplication
from ctypes import *
import os

from ui_py_tab import Ui_Dialog

source_code_path: str = ''
dest_code_path: str = ''
dll_name = "C_dll.dll"
dll_path = './C_dll.dll'
my_dll = windll.LoadLibrary(dll_path)
func = my_dll.task_on
func.restype = None  # set function return type to None
func.argtypes = [ctypes.c_char_p, ctypes.c_char_p]


def python_str_to_c_char_p(source: str) -> c_char_p:
    src_encode = source.encode('UTF-8')
    return c_char_p(src_encode)


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent=parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        # 设置槽函数
        self.ui.select_file_btn.clicked.connect(self.select_file)
        self.ui.select_dir_src_btn.clicked.connect(self.select_dir_src)
        self.ui.select_dir_res_btn.clicked.connect(self.select_dir_dst)

        # 显示客户端
        self.show()

    def reject(self):
        self.close()

    def accept(self):
        self.read_parameters()
        wait_trans_files = self.search_files_in_dir()
        self.convert_task(wait_trans_files)

    def search_files_in_dir(self):
        wait_trans_files = []
        if os.path.isfile(source_code_path) and source_code_path.lower().endswith(
                ".c") or source_code_path.lower().endswith(".cpp") \
                and os.path.getsize(source_code_path) > 0:
            wait_trans_files.append(source_code_path)
            return wait_trans_files
        for file in os.listdir(source_code_path):
            remote_file_path = os.path.join(source_code_path, file)
            if file.lower().endswith('.c') or file.lower().endswith('.cpp'):
                wait_trans_files.append(remote_file_path)

        return wait_trans_files

    def convert_task(self, wait_trans_files: list):

        for file_path_str in wait_trans_files:
            file_name = os.path.basename(file_path_str)
            dst_file_name = 'rm_comments_' + file_name
            dest_code_file_path = os.path.join(dest_code_path,dst_file_name)
            source_code_path_p_char = python_str_to_c_char_p(file_path_str)
            dest_code_file_path_p_char = python_str_to_c_char_p(dest_code_file_path)
            my_dll.task_on(source_code_path_p_char, dest_code_file_path_p_char)
        print('ok')

    def select_file(self):
        options = QFileDialog.Options()
        options |= QFileDialog.Option.DontUseNativeDialog
        file_dialog = QFileDialog(self)
        file_dialog.setOptions(options)

        file_dialog.setWindowTitle("选择C或CPP文件")
        file_dialog.setFileMode(QFileDialog.FileMode.ExistingFile)
        file_dialog.setNameFilters(["(*.cpp *.c)"])
        file_dialog.setDirectory(self.ui.source_code_path_edt.text())

        if file_dialog.exec_() == QFileDialog.Accepted:
            selected_files = file_dialog.selectedFiles()
            for file in selected_files:
                self.ui.source_code_path_edt.setText(file)

    def select_dir_dst(self):
        options = QFileDialog.Options()
        options |= QFileDialog.Option.DontUseNativeDialog
        file_dialog = QFileDialog(self)
        file_dialog.setOptions(options)

        file_dialog.setWindowTitle("选择文件夹")
        file_dialog.setFileMode(QFileDialog.FileMode.Directory)
        file_dialog.setDirectory(self.ui.result_path_edt.text())

        if file_dialog.exec_() == QFileDialog.Accepted:
            selected_files = file_dialog.selectedFiles()
            for file in selected_files:
                self.ui.result_path_edt.setText(file)

    def select_dir_src(self):
        options = QFileDialog.Options()
        options |= QFileDialog.Option.DontUseNativeDialog
        file_dialog = QFileDialog(self)
        file_dialog.setOptions(options)

        file_dialog.setWindowTitle("选择文件夹")
        file_dialog.setFileMode(QFileDialog.FileMode.Directory)
        file_dialog.setDirectory(self.ui.source_code_path_edt.text())

        if file_dialog.exec_() == QFileDialog.Accepted:
            selected_files = file_dialog.selectedFiles()
            for file in selected_files:
                # if file.lower().endswith('.cpp') or file.lower().endswith('.c'):
                self.ui.source_code_path_edt.setText(file)

    def read_parameters(self):
        global source_code_path, dest_code_path
        source_code_path = self.ui.source_code_path_edt.text()
        dest_code_path = self.ui.result_path_edt.text()


if __name__ == '__main__':
    app = QApplication.instance()
    if not app:
        app = QApplication(sys.argv)
        w = MainWindow()
        sys.exit(app.exec_())
