from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout


class MyApp(App):
    def build(self):
        bl = BoxLayout(orientation='horizontal')

        mylist = ['hello', 'bye']

        for i in mylist:
            lbl = Label(text=str(i))

            bl.add_widget(lbl)

        return bl


if __name__ == "__main__":
    MyApp().run()
