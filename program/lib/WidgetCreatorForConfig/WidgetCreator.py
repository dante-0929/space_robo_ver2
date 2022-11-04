import tkinter as tk
from program.lib.WidgetCreatorForConfig import WidgetTextCreator
import sys


class OutCreateWidget:
    def __init__(self, config, parent_factor):
        # configファイルからデータを読み込み
        self.config_ini = dict(config)
        self.root = parent_factor
        self.wct = WidgetTextCreator.TextCreator(self.config_ini)
        print(self.config_ini)

    def bunch_create(self) -> dict:
        reply = {}
        for i in list(self.config_ini):
            if 'Type' in self.config_ini[i]:
                if self.config_ini[i]['Type'] == "Spinbox":
                    reply[i] = self.type_spinbox(i)
                elif self.config_ini[i]['Type'] == 'Entry':
                    reply[i] = self.type_entry(i)
                else:
                    print('TypeError:widgetのタイプが間違っています', file=sys.stderr)
                    sys.exit(1)
        print(reply)
        return reply

    def type_spinbox(self, title: str) -> dict:
        reply = {}
        for i in list(self.config_ini[title]):
            if i == 'Type':
                pass
            else:
                var = tk.DoubleVar(self.root)
                var.set(float(self.config_ini[title][i]))
                reply[i + "label"] = tk.Label(self.root, text=self.wct.uppercase_before_spacer_put(i))
                reply[i + "input"] = tk.Spinbox(self.root, from_=-10000, to=10000, increment=0.01, textvariable=var)
                print(reply[i + "input"].get())
        return reply

    def type_entry(self, title: str) -> dict:
        reply = {}
        for i in list(self.config_ini[title]):
            if i == 'Type':
                pass
            else:
                reply[i + "label"] = tk.Label(self.root, text=self.wct.uppercase_before_spacer_put(i))
                reply[i + "input"] = tk.Entry(self.root)
                reply[i + "input"].insert(0, self.config_ini[title][i])
        return reply
