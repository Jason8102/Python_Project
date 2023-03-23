import pyaudio
import wave
import time
import threading
import tkinter as tk

class Recorder:
    def __init__(self):
        self.frames = []
        self.recording = False
        self.format = pyaudio.paInt16
        self.channels = 1
        self.rate = 44100
        self.chunk = 1024

    def start_recording(self):
        self.recording = True
        self.frames = []
        self.audio = pyaudio.PyAudio()
        self.stream = self.audio.open(format=self.format, channels=self.channels,
                                      rate=self.rate, input=True,
                                      frames_per_buffer=self.chunk)

        t = threading.Thread(target=self.record)
        t.start()

    def stop_recording(self):
        self.recording = False
        self.stream.stop_stream()
        self.stream.close()
        self.audio.terminate()

    def record(self):
        while self.recording:
            data = self.stream.read(self.chunk)
            self.frames.append(data)

    def save_to_file(self, filename):
        wf = wave.open(filename, 'wb')
        wf.setnchannels(self.channels)
        wf.setsampwidth(self.audio.get_sample_size(self.format))
        wf.setframerate(self.rate)
        wf.writeframes(b''.join(self.frames))
        wf.close()


class GUI:
    def __init__(self, recorder):
        self.recorder = recorder
        self.root = tk.Tk()
        self.root.title("Audio Recorder")

        self.start_button = tk.Button(self.root, text="Start Recording",
                                      command=self.start_recording)
        self.start_button.pack()

        self.stop_button = tk.Button(self.root, text="Stop Recording",
                                     command=self.stop_recording)
        self.stop_button.pack()
        self.stop_button.config(state="disabled")

        self.time_label = tk.Label(self.root, text="")
        self.time_label.pack()

        self.root.mainloop()

    def start_recording(self):
        self.start_button.config(state="disabled")
        self.stop_button.config(state="normal")
        self.recorder.start_recording()
        t = threading.Thread(target=self.update_time)
        t.start()

    def stop_recording(self):
        self.start_button.config(state="normal")
        self.stop_button.config(state="disabled")
        self.recorder.stop_recording()
        self.recorder.save_to_file(f"recording_{time.strftime('%Y%m%d_%H%M%S')}.wav")

    def update_time(self):
        start_time = time.time()
        while self.recorder.recording:
            elapsed_time = time.time() - start_time
            self.time_label.config(text=f"Recording time: {elapsed_time:.1f} seconds")
            time.sleep(0.1)
        self.time_label.config(text="")

recorder = Recorder()
gui = GUI(recorder)
