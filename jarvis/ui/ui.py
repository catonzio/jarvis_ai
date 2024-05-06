import asyncio

import flet as ft

from jarvis.core.recorder_component import RecorderComponent
from jarvis.core.stt_component import SttComponent
from jarvis.ui.recording_button import RecordingButton
from jarvis.ui.recording_timer import RecordingTimer

PAGE_WIDTH = 1080 / 2
PAGE_HEIGHT = 1920 / 2


class JarvisApp(ft.Stack):

    def __init__(self):
        super().__init__()
        self.transcription: str = ""
        self.audio_output_path: str = "tmp/recording.wav"
        self.recorder: RecorderComponent = RecorderComponent(
            output_path=self.audio_output_path
        )
        self.stt = SttComponent()

    def make_transcription(self) -> None:
        self.transcription = self.stt.transcribe(self.audio_output_path)["text"]
        print("Transcription: ", self.transcription)

    def build(self):
        recording_timer = RecordingTimer(self.recorder)
        record_transcription = ft.Text(
            "",
            size=20,
            no_wrap=False,
            width=PAGE_WIDTH * 0.8,
            height=PAGE_HEIGHT * 0.2,
            color="white",
        )

        def on_recording_end():
            recording_timer.stop_timer()
            self.make_transcription()
            record_transcription.value = self.transcription
            self.update()

        recording_button = RecordingButton(
            recorder=self.recorder,
            start_callback=recording_timer.start_timer,
            end_callback=on_recording_end,
        )

        return ft.Column(
            [
                ft.Container(
                    record_transcription,
                    bgcolor="black",
                ),
                recording_timer,
                ft.Text("Press the button to start recording."),
                recording_button,
                # recording_button(page, recorder),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        )


def main(page: ft.Page):
    page.window_width = PAGE_WIDTH
    page.window_height = PAGE_HEIGHT
    page.title = "Jarvis AI"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.update()

    jarvis_app = JarvisApp()
    page.add(jarvis_app)
