
# -*- coding: UTF-8 -*-
import web
import pyautogui
import time
urls = (
    '/(.*)', 'hello'
)

app = web.application(urls, globals())


class hello:
    def GET(self, name):

        pyautogui.keyDown('win')
        pyautogui.keyDown('d')
        pyautogui.keyUp('d')
        pyautogui.keyUp('win')
        print("执行")
        return "go"

if __name__ == "__main__":
    app.run()