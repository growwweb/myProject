from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout


class MyBtns(App):
    def build(self):
        gl = GridLayout(cols=5, rows=3)

        test = 100

        while test != 10:
            test -= 10

            btn = Button(text=str(test))

            gl.add_widget(btn)

        return gl


if __name__ == "__main__":
    MyBtns().run()
