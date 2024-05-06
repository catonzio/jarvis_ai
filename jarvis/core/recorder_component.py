from pvrecorder import PvRecorder
import struct
import wave
from wave import Wave_write


class RecorderComponent:

    device_name: str
    recorder: PvRecorder
    output_path: str
    is_recording: bool

    def __init__(self, output_path: str):
        devices = PvRecorder.get_available_devices()
        self.is_recording = False
        self.device_name = devices[-1]
        print(f"Using device {self.device_name}")

        self.recorder = PvRecorder(frame_length=512, device_index=-1)
        self.output_path = output_path

    def toggle_is_recording(self):
        self.is_recording = not self.is_recording
        print(f"Recording {'started' if self.is_recording else 'stopped'}.")

    def record(self):
        try:
            wavfile: Wave_write = None
            if self.output_path is not None:
                wavfile = wave.open(self.output_path, "w")
                wavfile.setparams(
                    (
                        1,
                        2,
                        self.recorder.sample_rate,
                        self.recorder.frame_length,
                        "NONE",
                        "NONE",
                    )
                )
            self.recorder.start()
            while self.is_recording:
                frame = self.recorder.read()
                if wavfile is not None:
                    wavfile.writeframes(struct.pack("h" * len(frame), *frame))
        except OSError as e:
            print("Error while recording: ", e)
        except KeyboardInterrupt:
            print("Stopping...")
        finally:
            self.recorder.stop()
            if wavfile is not None:
                wavfile.close()
            self.is_recording = False
