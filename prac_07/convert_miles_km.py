from kivy.app import App
from kivy.lang import Builder
from kivy.app import StringProperty

MILES_TO_KILOMETERS_CONVERSION_RATE = 1.61


class ConvertMilesKms(App):
    message = StringProperty()

    def build(self):
        self.title = "Convert miles to kms"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_calculate(self, text):
        """ handle calculation (could be button press or other call), output result to label widget """
        try:
            number = float(text)
        except ValueError:
            number = 0.0
        result = number * MILES_TO_KILOMETERS_CONVERSION_RATE
        self.message = str(result)

    def handle_increment(self, text, increment):
        try:
            number = float(text)
        except ValueError:
            number = 0
        result = number + increment
        self.root.ids.input_number.text = str(result)


ConvertMilesKms().run()
