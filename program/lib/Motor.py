# import RPi.GPIO as GPIO
from functools import wraps


class Motor:
    def __init__(self, config):
        # configファイルからデータを持ってくる
        self.config_ini = config

        # TODO 変数aの名前を変える
        # 加速度の初期値
        self.a = 0

        self.difference = 0
        rightmotor1 = self.config_ini['GPIO_PIN']['RightMotor1']
        rightmotor2 = self.config_ini['GPIO_PIN']['RightMotor2']
        leftmotor1 = self.config_ini['GPIO_PIN']['LeftMotor1']
        leftmotor2 = self.config_ini['GPIO_PIN']['LeftMotor2']
        missionservo = self.config_ini['GPIO_PIN']['MissionServo']
        """
        # GPIO初期設定
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(rightmotor1, GPIO.OUT)
        GPIO.setup(rightmotor2, GPIO.OUT)
        GPIO.setup(leftmotor1, GPIO.OUT)
        GPIO.setup(leftmotor2, GPIO.OUT)
        GPIO.setup(missionservo, GPIO.OUT)

        self.p1 = GPIO.PWM(rightmotor1, 50)  # 50Hz
        self.p2 = GPIO.PWM(rightmotor2, 50)  # 50Hz
        self.p3 = GPIO.PWM(leftmotor1, 50)  # 50Hz
        self.p4 = GPIO.PWM(leftmotor2, 50)  # 50Hz
        self.p5 = GPIO.PWM(missionservo, 50)  # 50Hz

        self.p1.start(0)
        self.p2.start(0)
        self.p3.start(0)
        self.p4.start(0)
        self.p5.start(0)
        """
    def __safe_calculation(status: str):
        def safe_calculation_wrapper(func):
            @wraps(func)
            def wrapper(self, *args, **kwargs):
                print(status)
                now = func(self, *args, **kwargs)
                if status == "+" and now < self.difference:
                    self.difference = now
                    return 99.9
                if status == "-" and self.difference < now:
                    self.difference = now
                    return 0
                self.difference = now
                return now
            return wrapper
        return safe_calculation_wrapper

    # ====================================================================
    # 台形加速
    # ====================================================================
    # TODO 変数aの名前を変える
    @__safe_calculation(status='+')
    def acceleration(self, input_duty):
        if self.a < 0:
            self.a = self.a * -1
        if 18 > input_duty >= 0:
            self.a += 0.05
        elif 82 <= input_duty < 99.9:
            self.a -= 0.05
        elif input_duty >= 99.9:
            self.a = 0
            input_duty = 99.9
        input_duty += round(self.a, 2)
        input_duty = round(input_duty, 2)
        return input_duty

    # ==================================================================
    # 台形減速
    # ==================================================================
    # TODO 変数aの名前を変える
    @__safe_calculation(status='-')
    def deceleration(self, input_duty):
        if self.a > 0:
            self.a = self.a * -1
        if 18 > input_duty:
            self.a += 0.05
        elif 82 <= input_duty:
            self.a -= 0.05
        input_duty += round(self.a, 2)
        input_duty = round(input_duty, 2)
        if input_duty <= 0.0:
            self.a = 0
            input_duty = 0
        return input_duty

    # ============================================================
    # 角度からduty比の計算
    # ============================================================
    def convert_duty_percent_from_angle(self, angle):
        minimum_pulse = float(self.config_ini['SERVO_MOTOR']['MinimumPulse'])
        max_pulse = float(self.config_ini['SERVO_MOTOR']['MaxPulse'])
        behavior_range = float(self.config_ini['SERVO_MOTOR']['BehaviorRange'])
        max_duty_percent = self.convert_duty_percent_from_pulse(max_pulse)
        minimum_duty_percent = self.convert_duty_percent_from_pulse(minimum_pulse)
        rs = (minimum_duty_percent
              + (max_duty_percent - minimum_duty_percent)
              / behavior_range
              * (angle + behavior_range))
        return rs

    # ============================================================
    # パルス幅からduty比のパーセントを計算
    # ============================================================
    def convert_duty_percent_from_pulse(self, pulse):
        pulse_cycle = pulse * 50 / 10
        return pulse_cycle

    def rotate_motor(self, right_motor_a, right_motor_b, left_motor_a, left_motor_b, steering_servo, mission_servo):

        # 使用不可能な値を使用可能な値へ変換
        if 0 > right_motor_a or right_motor_a > 100:
            if right_motor_a < 0:
                right_motor_a = 0
            elif right_motor_a > 100:
                right_motor_a = 99.9
        elif 0 > right_motor_b or right_motor_b > 100:
            if right_motor_b < 0:
                right_motor_b = 0
            elif right_motor_b > 100:
                right_motor_b = 99.9
        elif 0 > left_motor_a or left_motor_a > 100:
            if left_motor_a < 0:
                left_motor_a = 0
            elif left_motor_a > 100:
                left_motor_a = 99.9
        elif 0 > left_motor_b or left_motor_b > 100:
            if left_motor_b < 0:
                left_motor_b = 0
            elif left_motor_b > 100:
                left_motor_b = 99.9

        # duty比を出力
        print(f"{right_motor_a},{right_motor_b},{left_motor_a},{left_motor_b},{steering_servo},{mission_servo}")

        # duty比を変更
        """
        self.p1.ChangeDutyCycle(right_motor_a)
        self.p2.ChangeDutyCycle(right_motor_b)
        self.p3.ChangeDutyCycle(left_motor_a)
        self.p4.ChangeDutyCycle(left_motor_b)
        self.p5.ChangeDutyCycle(steering_servo)
        time.sleep(0.4)
        self.p5.ChangeDutyCycle(0.0)
        """
