from kivy.app import App
from kivy.uix.widget import Widget
from kivy.core.window import Window
from kivy.lang.builder import Builder

Builder.load_file('./gerador.kv')
Window.size = (350, 550)

class GeradorWidget(Widget):
    pass

class GeradorApp(App):
    def build(self):
        return GeradorWidget()

if __name__ == "__main__":
    GeradorApp().run()