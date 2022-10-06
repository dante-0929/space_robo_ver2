import Form1Definition
import tkinter as tk


class Form1:
    def __init__(self, root_instance):
        self.root = root_instance

        # ウィジェットのインスタンスを定義ファイルから持ってくる
        self.widget_obj = Form1Definition.Form1Definition(self.root)
        self.wgl = self.widget_obj.widgets_definition()

    def first_screen(self):

        # タブをnotebookオブジェクトに追加して表示
        self.wgl["root_widgets"]["notebook"].add(self.wgl["note_book_widgets"]["tab_one"], text="player")
        self.wgl["root_widgets"]["notebook"].add(self.wgl["note_book_widgets"]["tab_two"], text="setting")
        self.wgl["root_widgets"]["notebook"].pack(expand=True, fill='both')

        # playerタブのウィジェットを表示
        for i in list(self.wgl["tab_one_widgets"].values()):
            i.pack(anchor=tk.W)

    def setting_screen(self):

        # settingタブのウィジェットを表示
        for i in list(self.wgl["tab_two_forms"].values()):
            i.pack(anchor=tk.W)
        for i in list(self.wgl["tab_two_widgets"].values()):
            i.pack(anchor=tk.W)
