from pvrecorder import PvRecorder
import struct
import wave

devices = PvRecorder.get_available_devices()
print(devices)
recorder = PvRecorder(frame_length=512, device_index=-1)

output_path = "tmp/output.wav"

try:
    if output_path is not None:
        wavfile = wave.open(output_path, "w")
        # noinspection PyTypeChecker
        wavfile.setparams(
            (1, 2, recorder.sample_rate, recorder.frame_length, "NONE", "NONE")
        )
    recorder.start()
    print("Recording", end="", flush=True)
    while True:
        frame = recorder.read()
        if wavfile is not None:
            wavfile.writeframes(struct.pack("h" * len(frame), *frame))
            print(".", end="", flush=True)

except KeyboardInterrupt:
    print("Stopping...")
finally:
    recorder.delete()
    if wavfile is not None:
        wavfile.close()
