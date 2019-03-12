from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.scatter import Scatter
from kivy.uix.floatlayout import FloatLayout


class SimpleKivy(App):
    def build(self):
        f = FloatLayout()
        s = Scatter()
        l = Label(text="Hello!", font_size = 150)
        f.add_widget(s)
        s.add_widget(l)
        return f
    

if __name__ == "__main__":
    SimpleKivy().run()