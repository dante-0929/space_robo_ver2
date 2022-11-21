import tkinter as tk


# import RPi.GPIO as GPIO
# import matplotlib.pyplot as plt


class MoveEvent:
    direction = 0
    servo_status = 0

    def __init__(self, motor_class, widget_obj, config):
        self.config_ini = config
        self.motor = motor_class
        self.widget_obj = widget_obj
        self.duty = 0
        self.test_list = []
        self.gain = float(config['MOTOR_SETTING']['Gain'])

    def bind_func(self, event):
        key = event.keysym
        if key == self.config_ini['KEY_CONFIG']['MoveForward']:
            self.pressed_forward_key()
        elif key == self.config_ini['KEY_CONFIG']['MoveLeft']:
            self.pressed_left_key()
        elif key == self.config_ini['KEY_CONFIG']['MoveBack']:
            self.pressed_back_key()
        elif key == self.config_ini['KEY_CONFIG']['MoveRight']:
            self.pressed_right_key()
        elif key == self.config_ini['KEY_CONFIG']['AllStop']:
            self.pressed_stop_key()
        elif key == self.config_ini['KEY_CONFIG']['Deceleration']:
            self.pressed_deceleration_key()
        elif key == self.config_ini['KEY_CONFIG']['Mission']:
            self.pressed_mission_key()

    def pressed_left_key(self):
        steering_left = float(self.config_ini['STEERING']['Left'])
        if MoveEvent.direction == 0:
            self.motor.rotate_motor(self.duty*self.gain, 0, self.duty - steering_left, 0, 0, 0)
        elif MoveEvent.direction == 1:
            self.motor.rotate_motor(0, self.duty*self.gain, 0, self.duty - steering_left, 0, 0)

    def pressed_forward_key(self):
        if 100 > self.duty >= 0:
            MoveEvent.direction = 0
            self.duty = self.motor.acceleration(self.duty)
            self.test_list.append(self.duty)
            self.motor.rotate_motor(self.duty*self.gain, 0, self.duty, 0, 0, 0)

    def pressed_back_key(self):
        if 100 > self.duty >= 0:
            MoveEvent.direction = 1
            self.duty = self.motor.acceleration(self.duty)
            self.motor.rotate_motor(0, self.duty*self.gain, 0, self.duty, 0, 0)

    def pressed_right_key(self):
        steering_right = float(self.config_ini['STEERING']['Right'])
        if MoveEvent.direction == 0:
            self.motor.rotate_motor((self.duty - steering_right)*self.gain, 0, self.duty, 0, 0, 0)
        elif MoveEvent.direction == 1:
            self.motor.rotate_motor(0, (self.duty - steering_right)*self.gain, 0, self.duty, 0, 0)

    def pressed_stop_key(self):
        # GPIO.cleanup()
        self.motor.__init__(self.config_ini)
        self.duty = 0
        self.motor.rotate_motor(0, 0, 0, 0, 0, 0)

    def pressed_deceleration_key(self):
        if 100 >= self.duty > 0:
            self.duty = self.motor.deceleration(self.duty)
            if MoveEvent.direction == 0:
                self.motor.rotate_motor(self.duty*self.gain, 0, self.duty, 0, 0, 0)
            elif MoveEvent.direction == 1:
                self.motor.rotate_motor(0, self.duty*self.gain, 0, self.duty, 0, 0)

    def pressed_mission_key(self):
        # angle = self.config_ini["MISSION_STEERING"]['Angle']
        # steering_duty = self.motor.convert_duty_percent_from_angle(int(angle))
        if MoveEvent.servo_status == 0:
            MoveEvent.servo_status = 1
            if MoveEvent.direction == 0:
                self.motor.rotate_motor(self.duty * self.gain, 0, self.duty, 0, 2.5, 0)
            elif MoveEvent.direction == 1:
                self.motor.rotate_motor(0, self.duty * self.gain, 0, self.duty, 2.5, 0)
        elif MoveEvent.servo_status == 1:
            MoveEvent.servo_status = 0
            if MoveEvent.direction == 0:
                self.motor.rotate_motor(self.duty * self.gain, 0, self.duty, 0, 12.0, 0)
            elif MoveEvent.direction == 1:
                self.motor.rotate_motor(0, self.duty * self.gain, 0, self.duty, 12.0, 0)


class ConfigEvent:
    def __init__(self):
        self.sub_win = None
        self.sub_label = ''

    def key_setting(self, event):
        if self.sub_win is None or not self.sub_win.winfo_exists():
            self.sub_win = tk.Toplevel()
            self.sub_win.geometry("300x100")
            label_sub = tk.Label(self.sub_win, text="キーを入力してください")
            self.sub_label = tk.Label(self.sub_win)
            label_sub.pack()
            self.sub_label.pack()
            self.sub_label["text"] = event.widget["text"]
            self.sub_win.bind("<KeyPress>", self.sub_setting_key)
        self.sub_win.focus_set()
        self.key_setting_widget = event.widget

    def sub_setting_key(self, event):
        key = event.keysym
        self.sub_label['text'] = key
        self.key_setting_widget['text'] = key
