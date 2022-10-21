# space_robo_ver2
宇宙探求部のバージョン２

## はじめに
このソースコードは`.net framework`と`Django`を参考に作られている。


## 目次
- [ファイルツリー](#ファイルツリー)
- [config.ini](#configini)
- [Form1.py](#form1py)
- [Form1Definition.py](#form1definitionpy)
- [main.py](#mainpy)
- [Motor.py](#motorpy)

## ファイルツリー
<pre>
program
   │  config.ini          // 設定
   │  Form1.py            // tkinterの表示/非表示の切り替え
   │  Form1Definition.py  // tkinterのウィジェットの定義
   │  main.py             // 全体の大まかな制御
   │  Motor.py            // モータを制御するための計算など
   └─ README.md          
</pre>

## config.ini
settingタブに入力されたデータがここに保存される。
### [SERVO_MOTOR]　サーボモータの設定
<pre>
MinimumPulse  ・・・・ 制御パルスの最低値  
MaxPulse      ・・・・ 制御パルスの最大値  
BehaviorRange ・・・・ モーターの可動域  
</pre>
### [STEERING]　ステアリングの設定
<pre>
Right ・・・ ステアリングが右に傾く角度
Left  ・・・ ステアリングが左に傾く角度
</pre>
### [KEY_CONFIG]　キーコンフィグ
<pre>
MoveForward  ・・・・ 前進キー
MoveBack     ・・・・ 後進キー
MoveLeft     ・・・・ 左移動キー
MoveRight    ・・・・ 右移動キー
AllStop      ・・・・ 急に止まるキー
Deceleration ・・・・ ゆっくり止まるキー
</pre>

## Form1.py  
フォームのシーンを定義します
- `player_screen`  
playerタブのウィジェットを表示する。
- `setting_screen`  
settingタブのウィンジェットを表示する。

## Form1Definition.py  
Form1で表示するウィジェットを定義する。
ウィジェットを追加したいときはここに追加する。
```python
wgl = FormDefinition.widgets_definition()
```
上記のコードを実行すると以下のデータデータを取得することができる。
```python
{
    "root_widgets": {
            "widget1": Widget1.Instance,
            "widget2": Widget2.Instance,
            "widget3": Widget3.Instance,
            ...
            ...
            ...
        },
    "note_book_widgets": {
            "widget1": Widget1.Instance,
            "widget2": Widget2.Instance,
            "widget3": Widget3.Instance,
            ...
            ...
            ...
        },
    ...
    ...
    ...
}
```
ウィジェットを追加するときは、
辞書型オブジェクトにウィジェットインスタンスを作成して、
その辞書型オブジェクトを返り値用の辞書型オブジェクト(widgets)に登録すればいい。
### 活用法
活用方法を説明する。
まず下のコードを見てほしい
```python
wgl = Form1Definition.widgets_definition()

wgl["dictionary_key"]["widgets_key1"].pack()
wgl["dictionary_key"]["widgets_key2"].pack()
...
...
...
```
このコードは1つのウィジェットごとにコードを書いている。
この書き方はウィジェットのスタイルが1つずつ違う時に使うのには適しているが、複数のウィジェットが同じスタイルの時には適していない。  
複数のウィジェットが同じスタイルの時は下のコードを使うといいだろう
```python
wgl = Form1Definition.widgets_definition()

for i in list(wgl["dictionary_key"].values()):
    i.pack()
```
このコードにするメリットは２つある。  
1つ目はコードを簡潔に書ける事だ。コードを簡潔に書くことで読みやすくなる。  
2つ目はウィジェットの追加が簡単になる。  
このfor文は辞書の要素数ループするようになっている。なので、辞書にウィジェットを追加するだけで他にコードを書くことなく表示してくれる。

## main.py
ウィジェットのシーンなどの制御を行う

## Motor.py  
モータを制御するために必要な計算をする。
### Motor
- `acceleration(duty)`  
台形加速の計算
- `deceleration(duty)`  
台形減速の計算
- `convert_duty_percent_from_angle(angle)`  
角度を受け取ってサーボモーターを回転させるduty比を計算
- `convert_duty_percent_from_pulse(pulse)`  
パルス幅からdutyのパーセントを計算

  
