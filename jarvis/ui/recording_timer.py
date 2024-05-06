import asyncio

import flet as ft

from jarvis.core.recorder_component import RecorderComponent


class RecordingTimer(ft.Text):

    def __init__(self, recorder: RecorderComponent):
        super().__init__()
        self.seconds = 0
        self.running = recorder.is_recording
        self.value = "00:00"
        self.task: asyncio.Future | None = None

    def start_timer(self):
        self.running = True
        if not self.task:
            self.task = self.page.run_task(self.update_timer)
        self.update()

    def stop_timer(self):
        self.running = False
        if not self.task.cancelled:
            self.task.cancel()
        self.task = None
        self.seconds = 0
        self.update()

    async def update_timer(self):
        while self.running:
            mins, secs = divmod(self.seconds, 60)
            self.value = "{:02d}:{:02d}".format(mins, secs)
            self.update()
            await asyncio.sleep(1)
            self.seconds += 1
