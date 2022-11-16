import tkinter as tk
import cv2
from PIL import Image, ImageTk, ImageOps
from lib import conversion as con


class Form1:
    def __init__(self, root_instance, widget_obj):
        self.root = root_instance

        # ウィジェットのインスタンスを定義ファイルから持ってくる
        self.wgl = widget_obj

        # 画面のサイズを取得
        try:
            self.display_height = self.wgl["tab_one_widgets"]['main_canvas'].winfo_height()
            self.display_width = self.wgl["tab_one_widgets"]['main_canvas'].winfo_width()
        except AttributeError as e:
            print('\033[96m' + 'Not Tkinter.Tk Object' + '\033[0m')
            print('\033[96m' + str(e) + '\033[0m')

        # OpenCVのインスタンス及びカメラオープン
        # self.capture = cv2.VideoCapture(0000)

    def player_screen(self):

        # タブをnotebookオブジェクトに追加して表示
        self.wgl["root_widgets"]["notebook"].add(self.wgl["note_book_widgets"]["tab_one"], text="player")
        self.wgl["root_widgets"]["notebook"].add(self.wgl["note_book_widgets"]["tab_two"], text="setting")
        self.wgl["root_widgets"]["notebook"].pack(expand=True, fill='both')

        # playerタブのウィジェットを表示
        for i in list(self.wgl["tab_one_widgets"].values()):
            i.pack(expand=True, fill=tk.BOTH)
        self.wgl["tab_one_widgets"]["main_canvas"].create_text(10, 10, anchor='nw', text='p1 duty:0.0')
        self.wgl["tab_one_widgets"]["main_canvas"].create_text(10, 20, anchor='nw', text='p2 duty:0.0')
        self.wgl["tab_one_widgets"]["main_canvas"].create_text(10, 30, anchor='nw', text='p3 duty:0.0')
        self.wgl["tab_one_widgets"]["main_canvas"].create_text(10, 40, anchor='nw', text='p4 duty:0.0')
        self.wgl["tab_one_widgets"]["main_canvas"].create_text(10, 50, anchor='nw', text='p5 duty:0.0')
        self.wgl["tab_one_widgets"]["main_canvas"].create_text(10, 60, anchor='nw', text='p6 duty:0.0')

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
        pass
