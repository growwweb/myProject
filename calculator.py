from kivy.app import App

from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout

from kivy.config import Config
Config.set('graphics', 'resizable', 0)
Config.set('graphics', 'width', 500)
Config.set('graphics', 'height', 800)

class calculatorApp(App):
    def update_label(self):
        self.lbl.text = self.formula

    def add_number(self, instance):
        if (self.formula == '0'):
            self.formula = ''

        self.formula += str(instance.text)
        self.update_label()

    def add_operation(self, instance):
        if( str(instance.text).lower() == 'x'):
            self.formula += '*'
        elif (str(instance.text).lower() == 'st'):
            self.formula += '**'
        else:
            self.formula += str(instance.text)
        self.update_label()

    def calc_result(self, instance):
        self.error = Label(text = 'none')

        try:
            self.lbl.text = str(eval(self.lbl.text))
            self.formula = self.lbl.text
        except ZeroDivisionError:
            self.lbl.text = self.error.text
            self.formula = '0'
        except SyntaxError:
            self.lbl.text = self.error.text
            self.formula = '0'

    def backspace (self, instance):
        self.lbl.text = self.lbl.text[:-1]
        self.formula = self.lbl.text

    def restart(self, instance):
        self.lbl.text = '0'
        self.formula = '0'

    def build(self):
        self.formula = '0'
        gl = GridLayout(cols = 4, spacing = 3)
        bl = BoxLayout(orientation = "vertical", padding = 25)

        self.lbl = Label(text="0", halign="right", valign="center", font_size = 40, size_hint = (1,.4), text_size=(400 - 50, 500 * .4 - 50))
        bl.add_widget(self.lbl)

        for x in range(1):

            gl.add_widget(Button(text='/', on_press=self.add_operation))
            gl.add_widget(Button(text='ST', on_press=self.add_operation))
            gl.add_widget(Button(text='del', on_press=self.backspace))
            gl.add_widget(Button(text='CE', on_press = self.restart))
            for n1 in range(7, 10):
                gl.add_widget(Button(text=str(n1), on_press = self.add_number))
            gl.add_widget(Button(text='x', on_press = self.add_operation))
            for n2 in range(4, 7):
                gl.add_widget(Button(text=str(n2), on_press = self.add_number))
            gl.add_widget(Button(text='-', on_press = self.add_operation))
            for n3 in range(1, 4):
                gl.add_widget(Button(text=str(n3), on_press = self.add_number))
            gl.add_widget(Button(text='+', on_press = self.add_operation))
            gl.add_widget(Button(text='CE', on_press = self.restart))
            gl.add_widget(Button(text='0', on_press = self.add_number))
            gl.add_widget(Button(text='.', on_press = self.add_operation))
            gl.add_widget(Button(text='=', on_press = self.calc_result))

        bl.add_widget(gl)

        self.mytext = Label(text='Калькулятор разработан 10.10.2022 by spinch', font_size='12', halign="left", valign="center", size_hint = (1,.1))
        bl.add_widget(self.mytext)
        
        return bl

if __name__ == "__main__":
    calculatorApp().run()