from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty


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

    def power(self, instance):
        if self.formula == '':
            return

        self.formula += '^'
        self.label_input.text = self.formula

    def clear_formula(self, instance):
        self.formula = ''
        self.label_input.text = ''
        self.label_info.text = ''

    def delete_char(self, instance):
        if self.formula == '':
            return

        self.formula = self.formula[:-1]
        self.label_input.text = self.formula

    def calc_result(self, instance):
        if self.formula == '':
            return

        formula = self.formula.replace('x', '*').replace('÷', '/').replace('^', '**')

        try:
            calc = str(eval(formula))
        except:
            self.label_info.color = 'red'
            self.label_info.text = 'Error'
            return

        self.label_info.text = self.formula + '='
        self.formula = calc[:-2] if len(calc) > 2 and calc[-2:] == '.0' else calc
        self.label_input.text = self.formula


class CalculatorApp(App):
    title = "Калькулятор"
    icon = "logo512.png"

    def build(self):
        return Container()


CalculatorApp().run()
