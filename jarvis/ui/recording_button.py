import flet as ft

from jarvis.core.recorder_component import RecorderComponent


class RecordingButton(ft.ElevatedButton):

    def __init__(
        self, recorder: RecorderComponent, start_callback=None, end_callback=None
    ):
        super().__init__()
        self.recorder = recorder
        self.start_callback = start_callback
        self.end_callback = end_callback
        self.text = (
            "Stop Recording" if self.recorder.is_recording else "Start Recording"
        )
        self.on_click = self.click

    def click(self, e):
        self.recorder.toggle_is_recording()
        self.text = (
            "Stop Recording" if self.recorder.is_recording else "Start Recording"
        )
        self.update()
        if self.start_callback and self.recorder.is_recording:
            self.start_callback()
        elif self.end_callback and not self.recorder.is_recording:
            self.end_callback()

        if self.recorder.is_recording:
            self.recorder.record()
