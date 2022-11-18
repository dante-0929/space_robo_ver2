import tkinter as tk
import threading
import Form1
import lib.Motor as Motor
import Form1Definition
import lib.KeyEvent as KeyEvent
import os
from functools import partial


# import RPi.GPIO as GPIO


def canvas_sled():
    # form1.canvas_camera()
    root.after(10, canvas_sled())
    pass


class ConfigSave:
    def __init__(self, widget_object):
        self.widget_obj = widget_object
        # print(self.widget_obj['config_setting']['STEERING']['Rightinput'].winfo_name())
        for i in list(self.widget_obj['config_setting'].values()):
            for j in list(i.values()):
                # print(j.winfo_name())
                save_data = []
                if "button" in j.winfo_name():
                    save_data = j["text"]
                elif "entry" in j.winfo_name():
                    save_data = j.get()
                elif "spinbox" in j.winfo_name():
                    save_data = j.get()
                print(save_data)


def main():
    # rootの設定
    root.title("motor")
    root.geometry("1024x768")

    # formを表示
    form1.player_screen()
    form1.setting_screen()

    # playerタブの映像をサブタスクで実行
    job1 = threading.Thread(target=canvas_sled)
    # job1.start()

    # KeyEventを待機
    root.bind("<KeyPress>", key_event.bind_func)
    root.bind("<KeyRelease>", key_event.bind_func)
    for i in list(widget_obj['config_setting']['KEY_CONFIG'].values()):
        i.bind("<Button-1>", key_event.key_setting)
    widget_obj["tab_two_widgets"]["save_button"]['command'] = partial(ConfigSave, widget_obj)
    # formを待機
    root.mainloop()


if __name__ in "__main__":
    path = os.getcwd()
    print(path)
    root = tk.Tk()
    widget_instance = Form1Definition.Form1Definition(root)
    widget_obj = widget_instance.widgets_definition()
    form1 = Form1.Form1(root, widget_obj)
    motor = Motor.Motor()
    key_event = KeyEvent.KeyEvent(motor, widget_obj)
    main()
    # GPIO.cleanup()
