import tkinter as tk
import tkinter.ttk as ttk
from lib.WidgetCreatorForConfig import WidgetTextCreator
import sys


class OutCreateWidget:
    def __init__(self, config, parent_factor):
        # configファイルからデータを読み込み
        self.config_ini = dict(config)
        self.root = parent_factor
        self.wct = WidgetTextCreator.TextCreator(self.config_ini)
        self.note = ttk.Notebook(self.root, height=650)
        self.frame_list = []

    def bunch_create(self) -> dict:

        reply = {'title': {},
                 'note': self.note}
        for i, j in enumerate(list(self.config_ini)):
            self.frame_list.append(tk.Frame(self.note))
            self.note.add(self.frame_list[i], text=j)
            if 'Type' in self.config_ini[j]:
                if self.config_ini[j]['Type'] == "Spinbox":
                    reply[j] = self.type_spinbox(j, i)
                elif self.config_ini[j]['Type'] == 'Entry':
                    reply[j] = self.type_entry(j, i)
                elif self.config_ini[j]['Type'] == 'Button':
                    reply[j] = self.type_button(j, i)
                else:
                    print('TypeError:widgetのタイプが間違っています', file=sys.stderr)
                    sys.exit(1)
        return reply

    def type_spinbox(self, title: str, index: int) -> dict:
        reply = {}
        for i in list(self.config_ini[title]):
            if i == 'Type':
                pass
            else:
                var = tk.DoubleVar(self.frame_list[index])
                var.set(float(self.config_ini[title][i]))
                reply[i + "label"] = tk.Label(self.frame_list[index], text=self.wct.uppercase_before_spacer_put(i))
                reply[i + "input"] = tk.Spinbox(self.frame_list[index], from_=-10000, to=10000, increment=0.01,
                                                textvariable=var)
        return reply

    def type_entry(self, title: str, index: int) -> dict:
        reply = {}
        for i in list(self.config_ini[title]):
            if i == 'Type':
                pass
            else:
                reply[i + "label"] = tk.Label(self.frame_list[index], text=self.wct.uppercase_before_spacer_put(i))
                reply[i + "input"] = tk.Entry(self.frame_list[index])
                reply[i + "input"].insert(0, self.config_ini[title][i])
        return reply

    def type_button(self, title: str, index: int) -> dict:
        reply = {}
        for i in list(self.config_ini[title]):
            if i == 'Type':
                pass
            else:
                reply[i + "label"] = tk.Label(self.frame_list[index], text=self.wct.uppercase_before_spacer_put(i))
                reply[i + "input"] = tk.Button(self.frame_list[index], text=self.config_ini[title][i])
        return reply
