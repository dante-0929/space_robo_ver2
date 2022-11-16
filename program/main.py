import tkinter as tk
import threading
import Form1
import lib.Motor as Motor
import Form1Definition
import lib.KeyEvent as KeyEvent
import os
# import RPi.GPIO as GPIO


def canvas_sled():
    # form1.canvas_camera()
    root.after(10, canvas_sled())
    pass


def main():

    # rootの設定
    root.title("motor")
    root.geometry("1024x768")

    # formを表示
    form1.player_screen()
    form1.setting_screen()

    # playerタブの映像をサブタスクで実行
    job1 = threading.Thread(target=canvas_sled)
    job1.start()

    # KeyEventを待機
    widget_obj['note_book_widgets']['tab_one'].bind("<KeyPress>", key_event.bind_func)
    root.bind("<KeyRelease>", key_event.bind_func)
    for i in list(widget_obj['config_setting']['KEY_CONFIG'].values()):
        i.bind("<Button-1>", key_event.key_setting)
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
