import tkinter as tk
import Form1


def main():
    root = tk.Tk()
    root.title("motor")
    root.geometry("1024x768")
    form1 = Form1.Form1(root)
    form1.player_screen()
    form1.setting_screen()
    root.mainloop()


if __name__ in "__main__":
    main()
