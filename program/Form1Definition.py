# このファイルではwidgetの定義をしています。
# widgets_definitionメソッドのようにwidgetのインスタンスを辞書型オブジェクトに格納することでwidgetインスタンスのやり取りを簡単にしています。
# 悪い例: change_display = ChangeDisplay(インスタンス1,インスタンス2,インスタンス3...) ･･･ インスタンスの数だけ引数が必要だしタプル型でわかりにくい
# 良い例: change_display = ChangeDisplay(widgets) ･･･ 引数が1つで済んでなおかつkeyでインスタンスを指定できるのでわかりやすい
import tkinter as tk
import tkinter.ttk as ttk
import tkinter.font as tkfont


class Form1Definition:
    def __init__(self, root_instance):
        self.root = root_instance

    def widgets_definition(self):
        # TODO root_widgetsなどの変数名だとrootを定義していると解釈されてしまうため変更が必要
        root_widgets = {
            "notebook": ttk.Notebook(self.root),
            "text_font": tkfont.Font(size=10),
        }

        note_book_widgets = {
            "tab_one": tk.Frame(root_widgets["notebook"]),
            "tab_two": tk.Frame(root_widgets["notebook"]),
        }

        tab_one_widgets = {
            "duty_frame": tk.Frame(note_book_widgets["tab_one"]),
            "duty_speed_p1": tk.Label(note_book_widgets["tab_one"], text="p1 duty:0.0", font=root_widgets["text_font"]),
            "duty_speed_p2": tk.Label(note_book_widgets["tab_one"], text="p2 duty:0.0", font=root_widgets["text_font"]),
            "duty_speed_p3": tk.Label(note_book_widgets["tab_one"], text="p3 duty:0.0", font=root_widgets["text_font"]),
            "duty_speed_p4": tk.Label(note_book_widgets["tab_one"], text="p4 duty:0.0", font=root_widgets["text_font"]),
            "duty_speed_p5": tk.Label(note_book_widgets["tab_one"], text="p5 duty:0.0", font=root_widgets["text_font"]),
            "duty_speed_p6": tk.Label(note_book_widgets["tab_one"], text="p6 duty:0.0", font=root_widgets["text_font"]),
        }

        tab_two_forms = {
            "minimum_pulse_form": tk.Frame(note_book_widgets["tab_two"]),
            "max_pulse_form": tk.Frame(note_book_widgets["tab_two"]),
            "behavior_range_form": tk.Frame(note_book_widgets["tab_two"])
        }

        tab_two_widgets = {
            "minimum_pulse_label": tk.Label(tab_two_forms["minimum_pulse_form"], text="パルスの最小値", font=root_widgets["text_font"]),
            "minimum_pulse_entry": tk.Entry(tab_two_forms["minimum_pulse_form"]),
            "max_pulse_label": tk.Label(tab_two_forms["max_pulse_form"], text="パルスの最大値", font=root_widgets["text_font"]),
            "max_pulse_entry": tk.Entry(tab_two_forms["max_pulse_form"]),
            "behavior_range_label": tk.Label(tab_two_forms["behavior_range_form"], text='モーターの回転幅', font=root_widgets["text_font"]),
            "behavior_range_entry": tk.Entry(tab_two_forms["behavior_range_form"]),
        }

        widgets = {
            "root_widgets": root_widgets,
            "note_book_widgets": note_book_widgets,
            "tab_two_forms": tab_two_forms,
            "tab_two_widgets": tab_two_widgets,
            "tab_one_widgets": tab_one_widgets,
        }
        return widgets
        key_event = KeyEvent.KeyEvent(self.duty_speed_p1)
