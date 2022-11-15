import tkinter as tk
import threading
import Form1
import lib.Motor as motor
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
    root.bind("<KeyPress>", key_event.bind_func)
    root.bind("<KeyRelease>", key_event.bind_func)

    # formを待機
    root.mainloop()


if __name__ in "__main__":
    path = os.getcwd()
    print(path)
    root = tk.Tk()
    widget_obj = Form1Definition.Form1Definition(root)
    form1 = Form1.Form1(root, widget_obj)
    motor = motor.Motor()
    key_event = KeyEvent.KeyEvent(motor)
    main()
    # GPIO.cleanup()
