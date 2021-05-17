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

    def add_number(self, instance):
        self.formula += str(instance.text)
        self.label_input.text = self.formula

    def calc_result(self, instance):
        self.label_info.text = self.formula
        self.label_input.text = str(eval(self.formula))
        self.formula = ''


class CalculatorApp(App):
    title = "Калькулятор"
    def build(self):
        return Container()


if __name__ == '__main__':
    CalculatorApp().run()