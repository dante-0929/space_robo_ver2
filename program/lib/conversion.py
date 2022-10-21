from PIL import Image, ImageTk, ImageOps
import cv2


def create_canvas_image(fct, width: int, height: int, wgl: dict) -> ImageTk.PhotoImage:
    ret, frame = fct.read()
    # BGR→RGB変換
    cv_image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    # NumPyのndarrayからPillowのImageへ変換
    pil_image = Image.fromarray(cv_image)

    # 画像のアスペクト比（縦横比）を崩さずに指定したサイズ（キャンバスのサイズ）全体に画像をリサイズする
    pil_image = ImageOps.pad(pil_image, (width, height))

    # PIL.ImageからPhotoImageへ変換する
    photo_image = ImageTk.PhotoImage(image=pil_image)
    wgl["tab_one_widgets"]['main_canvas'].create_image(
        width / 2,  # 画像表示位置(Canvasの中心)
        height / 2,
        image=photo_image  # 表示画像データ
    )

    return photo_image


