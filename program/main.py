import tkinter as tk
import Form1
import lib.Motor as Motor
import Form1Definition
import lib.KeyEvent as KeyEvent
from functools import partial
import configparser


# import RPi.GPIO as GPIO


class ConfigSave:
    def __init__(self, root, widget_object, config):
        self.widget_obj = widget_object
        save_data = []
        for i in list(self.widget_obj['config_setting'].values()):
            if hasattr(i, 'winfo_name'):
                if 'notebook' in i.winfo_name():
                    continue
            for j in list(i.values()):
                if "button" in j.winfo_name():
                    save_data.append(j["text"])
                elif "entry" in j.winfo_name():
                    save_data.append(j.get())
                elif "spinbox" in j.winfo_name():
                    save_data.append(j.get())
        a = 0
        for i in config.sections():
            for j in config[i]:
                if j == "Type":
                    continue
                config[i][j] = save_data[a]
                a += 1
        with open('./config/config.ini', 'w') as configfile:
            config.write(configfile)
        root.destroy()
        main()


class TestEvents:
    def __init__(self, config, motor, key_event):
        self.config_ini = config
        self.motor = motor
        self.key_event = key_event

    def servo(self, scale_value):
        value = float(scale_value)
        print(value)
        steering_duty = self.motor.convert_duty_percent_from_angle(int(value))
        self.motor.rotate_motor(0, 0, 0, 0, steering_duty, 0)

    def right_gain(self, scale_value):
        value = float(scale_value)
        print(value)
        self.motor.rotate_motor(0, self.key_event.duty * value, 0, self.key_event.duty, 0, 0)

    def left_gain(self, scale_value):
        value = float(scale_value)
        print(value)
        self.motor.rotate_motor(0, self.key_event.duty, 0, self.key_event.duty * value, 0, 0)


def main():
    # configファイルを読み込む
    config_ini = configparser.ConfigParser()
    config_ini.optionxform = str
    config_ini.read('config/config.ini')

    # tkinterのインスタンスを作成
    root = tk.Tk()
    widget_instance = Form1Definition.Form1Definition(root, config_ini)
    widget_obj = widget_instance.widgets_definition()  # widgetのインスタンスを作成

    # フォームを表示するためのインスタンスを作成
    form1 = Form1.Form1(root, widget_obj)

    # モーター制御系のインスタンスを作成
    motor = Motor.Motor(config_ini)

    # キーボードイベントが発生した時の処理をするインスタンスを作成
    move_event = KeyEvent.MoveEvent(motor, widget_obj, config_ini)
    config_event = KeyEvent.ConfigEvent()

    # formを表示
    form1.player_screen()
    form1.setting_screen()

    # 移動用のキーイベントの発生を待機
    root.bind("<KeyPress>", move_event.bind_func)
    # root.bind("<KeyRelease>", move_event.bind_func)

    # 設定タブのKEY_CONFIG欄のボタンが押されたときのイベントを設定
    for i in list(widget_obj['config_setting']['KEY_CONFIG'].values()):
        i.bind("<Button-1>", config_event.key_setting)

    # セーブボタンのが押された時に呼び出す関数を紐付ける
    widget_obj["tab_two_widgets"]["save_button"]['command'] = partial(ConfigSave, root, widget_obj, config_ini)

    # ゲイン及びサーボモーターの調整用
    test_events = TestEvents(config_ini, motor, move_event)
    widget_obj["main_canvas_widgets"]["mission_scale"]['command'] = test_events.servo
    widget_obj["main_canvas_widgets"]["right_motor_scale"]['command'] = test_events.right_gain
    widget_obj["main_canvas_widgets"]["left_motor_scale"]['command'] = test_events.left_gain

    # formを待機
    root.mainloop()


if __name__ in "__main__":
    main()
    # GPIO.cleanup()
