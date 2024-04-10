from pynput.mouse import Listener
import keyboard
import pyautogui
import pyperclip
import time
SAFETY_WAIT =0.3
pyautogui.PAUSE = SAFETY_WAIT



def get_click_position():
    coordinates = []

    def on_click(x, y, button, pressed):
        if pressed:
            coordinates.append((x, y))
            return False  # リスナーを停止

    # マウスリスナーをスレッドで開始
    listener = Listener(on_click=on_click)
    listener.start()
    listener.join()  # リスナーが停止するのを待つ
    if coordinates:
        return coordinates[0]  # 最初に記録された座標を返す


def wait_for_gosign():
    print("Ctrl+1を押すまで待機します。")
    keyboard.wait('ctrl+1')


def input_positions(tgt, positions):
    print(f"{tgt} に設定する座標をクリックしてください")
    positions[tgt] = get_click_position()
    # print(positions)
    # return positions


def type_and_select(phrase):
    # クリップボードにテキストをコピー
    pyperclip.copy(phrase)
    pyautogui.hotkey('ctrl', 'v', interval=0.15)
    
    time.sleep(SAFETY_WAIT)  # 少し待つ
    pyautogui.press('down')  # 下矢印キーを押す
    time.sleep(SAFETY_WAIT)  # 少し待つ
    pyautogui.press('enter')  # エンターキーを押す


def click_at_position(position):
    # 指定された座標にマウスカーソルを移動
    pyautogui.moveTo(position[0], position[1])

    # マウスをクリック
    pyautogui.click()


# メイン関数を実行
if __name__ == "__main__":

    # 決まり事
    loop_list = []
    for header in [f"C{n}" for n in range(1, 17, 1)]:
        for what in ["最終考課者コメント", "一次考課者コメント", "二次考課者", "一次考課者"]:
            loop_list.append(f"{header}{what}")
    print(loop_list)
    # 操作の準備ができるまで待機
    wait_for_gosign()

    positions = {}
    for loop_num, x in enumerate(loop_list):

        print(positions)
        if loop_num == 0:
            # 座標を覚える
            print("初回だけ座標を覚えさせるためにクリックを求められます。メッセージに従ってクリックしてください。")
            input_positions("追加", positions)
            input_positions("検索窓", positions)
            type_and_select(x)
            input_positions("名前入力窓", positions)
            type_and_select("佐藤")
            type_and_select("田中")
            type_and_select("高橋")
            input_positions("編集外し", positions)
            input_positions("閲覧外し", positions)
        else:
            click_at_position(positions["追加"])
            click_at_position(positions["検索窓"])
            type_and_select(x)
            click_at_position(positions["名前入力窓"])
            type_and_select("佐藤")
            type_and_select("田中")
            type_and_select("高橋")
            click_at_position(positions["編集外し"])
            click_at_position(positions["閲覧外し"])
