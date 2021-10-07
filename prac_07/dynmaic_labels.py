from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label


class DynamicLabels(App):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.names = ["Jordan", "Bob"]

    def build(self):
        self.title = "Dynamic labels"
        self.root = Builder.load_file('dynamic_labels.kv')
        self.create_widgets()
        return self.root

    def create_widgets(self):
        for name in self.names:
            temp_label = Label(text=name)
            self.root.ids.entries_label.add_widget(temp_label)


DynamicLabels().run()
