from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput


class MainApp(App):
    def build(self):
        main_layout = BoxLayout(orientation="vertical", padding=10, spacing=15)
        self.solution = TextInput(multiline=False, readonly=False, halign="center", font_size=130)
        self.colution = TextInput(multiline=False, readonly=False, halign="center", font_size=130)
        self.holution = TextInput(multiline=False, readonly=True, halign="center", font_size=100)
        self.holution1 = TextInput(multiline=False, readonly=True, halign="center", font_size=100, text = 'Введите свой рост:')
        self.holution2 = TextInput(multiline=False, readonly=True, halign="center", font_size=100, text = 'Введите свой вес:')
        self.holution3 = TextInput(multiline=False, readonly=True, halign="center", font_size=100, text = 'Имт вашего тела:')
        main_layout.add_widget(self.holution1)
        main_layout.add_widget(self.solution)
        main_layout.add_widget(self.holution2)
        main_layout.add_widget(self.colution)
        main_layout.add_widget(self.holution3)
        main_layout.add_widget(self.holution)
        buttons = [
        ['Очистить']
        ]
        for row in buttons:
            h_layout = BoxLayout()
            for label in row:
                button = Button(text=label, pos_hint={"center_x": 0.5, "center_y": 0.5}, font_size=100)
                button.bind(on_press=self.on_button_press)
                h_layout.add_widget(button)
            main_layout.add_widget(h_layout)

        equals_button = Button(text="Рассчитать ИМТ", pos_hint={"center_x": 0.5, "center_y": 0.5}, font_size=100)
        equals_button.bind(on_press=self.on_solution)
        main_layout.add_widget(equals_button)
       

        # return a Button() as a root widget
        return main_layout
        

    def on_button_press(self, instance):
        if instance.text == "Очистить":
            self.solution.text = ""
            self.colution.text = ""
            self.holution.text = ""
        else:
            self.solution.text += instance.text

    def on_solution(self, instance):
        a = int(self.solution.text)
        b = int(self.colution.text)
        self.holution.text = str(b/((a/100)*(a/100)))
                
                
if __name__ == '__main__':
    MainApp().run()
