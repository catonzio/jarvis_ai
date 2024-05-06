from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout


class Recorder:
    def __init__(self):
        self.is_recording = False

    def toggle_is_recording(self):
        self.is_recording = not self.is_recording


class MyApp(App):
    def build(self):
        self.recorder = Recorder()
        self.layout = BoxLayout()
        self.button = Button(text="Start Recording", on_press=self.toggle_recording)
        self.layout.add_widget(self.button)
        return self.layout

    def toggle_recording(self, instance):
        print("Toggling recording")
        self.recorder.toggle_is_recording()
        new_text = "Stop Recording" if self.recorder.is_recording else "Start Recording"
        self.button.text = new_text


if __name__ == "__main__":
    MyApp().run()
