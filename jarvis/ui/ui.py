import asyncio

import flet as ft

from jarvis.core.recorder_component import RecorderComponent


class RecordingTimer(ft.Text):

    def __init__(self, recorder: RecorderComponent):
        super().__init__()
        self.seconds = 0
        self.running = recorder.is_recording
        self.value = str(self.seconds)

    def did_mount(self):
        print("RecordingTimer did_mount")
        self.start_timer()
        return super().did_mount()

    def start_timer(self):
        self.running = True
        self.page.run_task(self.update_timer)
        self.update()

    def stop_timer(self):
        self.running = False

    def before_update(self):
        print("RecordingTimer before_update")
        if self.running:
            self.start_timer()
        else:
            self.stop_timer()

    async def update_timer(self):
        while self.seconds and self.running:
            print(self.seconds)
            mins, secs = divmod(self.seconds, 60)
            self.value = "{:02d}:{:02d}".format(mins, secs)
            self.update()
            await asyncio.sleep(1)
            self.seconds -= 1


class RecordingButton(ft.ElevatedButton):

    def __init__(self, recorder_component: RecorderComponent):
        super().__init__()
        self.recorder = recorder_component
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
        if self.recorder.is_recording:
            pass
            # self.recorder.record()


def main(page: ft.Page):
    page.title = "Jarvis AI"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    recorder: RecorderComponent = RecorderComponent(output_path="tmp/recording.wav")
    page.add(
        ft.Column(
            [
                RecordingTimer(recorder),
                ft.Text("Press the button to start recording."),
                RecordingButton(recorder_component=recorder),
            ]
        )
    )
