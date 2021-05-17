from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
# from kivy.core.window import Window

# Window.size = (1080,1920)
# Window.size = (270,480)

# from calculator.config import Config
# Config.set('graphics', 'resizable', 0)
# Config.set('graphics', 'width', 270)
# Config.set('graphics', 'height', 480)

class Container(BoxLayout):

    label_info = ObjectProperty()
    label_input = ObjectProperty()
    formula = ''

    def add_in_formula(self, instance):
        if self.label_info.text == 'Error':
            self.label_info.color = 'yellow'
            self.label_info.text = ''

        self.formula += str(instance.text)
        self.label_input.text = self.formula

    def set_sign(self, instance):
        if self.formula[0] == '-':
            self.formula = self.formula[1:]
        else:
            self.formula = '-' + self.formula

        self.label_input.text = self.formula

    def clear_formula(self, instance):
        self.formula = ''
        self.label_input.text = ''
        self.label_info.text = ''

    def calc_result(self, instance):
        if self.formula == '':
            return

        try:
            calc = str(eval(self.formula.replace('x', '*')))
        except:
            self.label_info.color = 'red'
            self.label_info.text = 'Error'
            calc = False

        if calc:
            if len(calc) > 2 and calc[-2:] == '.0':
                calc = calc[:-2]

            self.label_input.text = calc
            self.label_info.text = self.formula + ' ='
            self.formula = calc


class CalculatorApp(App):
    title = "Калькулятор"
    icon = "logo512.png"

    def build(self):
        return Container()


CalculatorApp().run()