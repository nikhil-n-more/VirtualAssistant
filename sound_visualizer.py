import matplotlib.pyplot as plt
import numpy as np
import wave
import sys

# Function to visualize sound waves
def visualize_sound_wave(path_to_wav):
    # Open the WAV file
    with wave.open(path_to_wav, 'rb') as wav_file:
        # Extract Raw Audio from Wav File
        signal = wav_file.readframes(-1)
        # Convert Binary Data to Numpy Array
        signal = np.frombuffer(signal, dtype='int16')
        # Get the Frame Rate
        frame_rate = wav_file.getframerate()
        # Calculate Time Axis in Seconds
        time_axis = np.linspace(0, len(signal) / frame_rate, num=len(signal))

        # Plotting the Sound Wave
        plt.figure(1)
        plt.title('Sound Wave')
        plt.xlabel('Time (seconds)')
        plt.ylabel('Amplitude')
        plt.plot(time_axis, signal)
        plt.show()

# Replace 'path_to_file.wav' with the path to your WAV file
visualize_sound_wave('path_to_file.wav')
