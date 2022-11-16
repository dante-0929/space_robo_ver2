import configparser
import tkinter as tk
# import matplotlib.pyplot as plt


class KeyEvent:
    def __init__(self, motor_class, widget_obj):
        self.config_ini = configparser.ConfigParser()
        self.config_ini.optionxform = str
        self.config_ini.read('config/config.ini')
        self.motor = motor_class
        self.widget_obj = widget_obj
        self.sub_label = ''
        self.duty = 0
        self.test_list = []

    def bind_func(self, event):
        key = event.keysym
        if key == self.config_ini['KEY_CONFIG']['MoveForward']:
            self.pressed_w()
        elif key == self.config_ini['KEY_CONFIG']['MoveLeft']:
            self.pressed_a()
        elif key == self.config_ini['KEY_CONFIG']['MoveBack']:
            self.pressed_s()
        elif key == self.config_ini['KEY_CONFIG']['MoveRight']:
            self.pressed_d()
        elif key == "e":
            self.pressed_e()
        elif key == self.config_ini['KEY_CONFIG']['AllStop']:
            self.pressed_q()
        elif key == self.config_ini['KEY_CONFIG']['Deceleration']:
            self.pressed_shift()

    def key_setting(self, event):
        sub_win = tk.Toplevel()
        sub_win.geometry("300x100")
        label_sub = tk.Label(sub_win, text="キーを入力してください")
        self.sub_label = tk.Label(sub_win)
        label_sub.pack()
        self.sub_label.pack()
        self.sub_label["text"] = event.widget["text"]
        sub_win.bind("<KeyPress>", self.sub_setting_key)
        self.key_setting_widget = event.widget

    def sub_setting_key(self, event):
        key = event.keysym
        self.sub_label['text'] = key
        self.key_setting_widget['text'] = key

    def pressed_a(self):
        steering_left = float(self.config_ini['STEERING']['Left'])
        steering_duty = self.motor.convert_duty_percent_from_angle(steering_left)
        self.motor.rotate_motor(0, 0, 0, 0, steering_duty, 0)

    def pressed_w(self):
        if 100 > self.duty >= 0:
            self.duty = self.motor.acceleration(self.duty)
            self.test_list.append(self.duty)
            self.motor.rotate_motor(self.duty, 0, self.duty, 0, 0, 0)

    def pressed_s(self):
        if 100 > self.duty >= 0:
            self.duty = self.motor.acceleration(self.duty)
            self.motor.rotate_motor(0, self.duty, 0, self.duty, 0, 0)

    def pressed_d(self):
        steering_right = float(self.config_ini['STEERING']['Right'])
        steering_duty = self.motor.convert_duty_percent_from_angle(steering_right)
        self.motor.rotate_motor(0, 0, 0, 0, steering_duty, 0)

    def pressed_q(self):
        self.motor.__init__()
        self.duty = 0
        self.motor.rotate_motor(0, 0, 0, 0, 0, 0)

    def pressed_p(self):
        if 100 > self.duty >= 0:
            self.duty += 10
            self.motor.rotate_motor(self.duty, 0, self.duty, 0, 0, 0)

    def pressed_m(self):
        if 100 >= self.duty > 0:
            self.duty -= 10
            self.motor.rotate_motor(self.duty, 0, self.duty, 0, 0, 0)

    def pressed_e(self):
        plt.plot(self.test_list, marker="o")
        plt.grid(True)
        plt.show()

    def pressed_shift(self):
        if 100 >= self.duty > 0:
            self.duty = self.motor.deceleration(self.duty)
            self.test_list.append(self.duty)
            self.motor.rotate_motor(self.duty, 0, self.duty, 0, 0, 0)

