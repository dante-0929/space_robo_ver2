import Form1Definition
import tkinter as tk
import cv2
from PIL import Image, ImageTk, ImageOps
from lib import conversion as con


class Form1:
    def __init__(self, root_instance):
        self.root = root_instance

        # ウィジェットのインスタンスを定義ファイルから持ってくる
        self.widget_obj = Form1Definition.Form1Definition(self.root)
        self.wgl = self.widget_obj.widgets_definition()

        # 画面のサイズを取得
        try:
            self.display_height = self.wgl["tab_one_widgets"]['main_canvas'].winfo_height()
            self.display_width = self.wgl["tab_one_widgets"]['main_canvas'].winfo_width()
        except AttributeError as e:
            print('\033[96m' + 'Not Tkinter.Tk Object' + '\033[0m')
            print('\033[96m' + str(e) + '\033[0m')

        self.capture = cv2.VideoCapture(0000)

    def player_screen(self):

        # タブをnotebookオブジェクトに追加して表示
        self.wgl["root_widgets"]["notebook"].add(self.wgl["note_book_widgets"]["tab_one"], text="player")
        self.wgl["root_widgets"]["notebook"].add(self.wgl["note_book_widgets"]["tab_two"], text="setting")
        self.wgl["root_widgets"]["notebook"].pack(expand=True, fill='both')

        # playerタブのウィジェットを表示
        for i in list(self.wgl["tab_one_widgets"].values()):
            i.pack(expand=True, fill=tk.BOTH)
        """
        for i in list(self.wgl["main_canvas_widgets"].values()):
            i.pack(anchor=tk.W)
        """

    def setting_screen(self):
        print(self.wgl['config_setting'])
        # settingタブのウィジェットを表示
        """
        for i in list(self.wgl["tab_two_forms"].values()):
            i.pack(anchor=tk.W)
        for i in list(self.wgl["tab_two_widgets"].values()):
            i.pack(anchor=tk.W)
        """
        for i in list(self.wgl['config_setting'].values()):
            for j in list(i.values()):
                j.pack(anchor=tk.W)

    def canvas_camera(self):
        con.create_canvas_image(self.capture, self.display_width, self.display_height, self.wgl)

