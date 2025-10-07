from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.core.window import Window

class HelloApp(App):
    def build(self):
        Window.clearcolor = (1, 1, 1, 1)  # sfondo bianco
        root = BoxLayout(orientation='vertical', padding=20, spacing=10)
        self.lbl = Label(text='Hello, world!', font_size='24sp')
        btn = Button(text='Verde!', size_hint=(1, None), height='48dp')
        btn.bind(on_release=self.make_green)
        root.add_widget(self.lbl)
        root.add_widget(btn)
        return root

    def make_green(self, *_):
        Window.clearcolor = (0, 1, 0, 1)  # sfondo verde

if __name__ == "__main__":
    HelloApp().run()
