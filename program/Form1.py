import tkinter as tk
from lib import conversion as con


class Form1:
    def __init__(self, root_instance, widget_obj):
        self.root = root_instance
        self.root.title("space")
        self.root.geometry("1024x768")
        # ウィジェットのインスタンスを定義ファイルから持ってくる
        self.wgl = widget_obj

        # 画面のサイズを取得
        try:
            self.display_height = self.wgl["tab_one_widgets"]['main_canvas'].winfo_height()
            self.display_width = self.wgl["tab_one_widgets"]['main_canvas'].winfo_width()
        except AttributeError as e:
            print('\033[96m' + 'Not Tkinter.Tk Object' + '\033[0m')
            print('\033[96m' + str(e) + '\033[0m')

    def player_screen(self):

        # タブをnotebookオブジェクトに追加して表示
        self.wgl["root_widgets"]["notebook"].add(self.wgl["note_book_widgets"]["tab_one"], text="player")
        self.wgl["root_widgets"]["notebook"].add(self.wgl["note_book_widgets"]["tab_two"], text="setting")
        self.wgl["root_widgets"]["notebook"].pack(expand=True, fill='both')

        # playerタブのウィジェットを表示
        for i in list(self.wgl["main_canvas_widgets"].values()):
            i.pack()
        self.wgl["main_canvas_widgets"]["right_motor_scale"].set(1)
        self.wgl["main_canvas_widgets"]["left_motor_scale"].set(1)

    def setting_screen(self):
        # settingタブのウィジェットを表示
        self.wgl['config_setting']['note'].pack(fill='both')
        for i in list(self.wgl['config_setting'].values()):
            if hasattr(i, 'winfo_name'):
                if 'notebook' in i.winfo_name():
                    continue
            for j in list(i.values()):
                j.pack(anchor=tk.W)
        self.wgl["tab_two_widgets"]["save_button"].place(x=920, y=680)
