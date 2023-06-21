import numpy as np
import matplotlib.pyplot as plt

# # Generate a sample signal
# duration = 5.0  # duration of the signal in seconds
# fs = 1000  # number of samples per second
# t = np.linspace(0.0, duration, int(duration * fs), endpoint=False)
# frequency = 50  # frequency of the signal
# amplitude = 6.0  # amplitude of the signal
# signal = amplitude * np.sin(2 * np.pi * frequency * t)
# Generate a time series
fs = 600  # Sampling frequency
t = np.arange(0, 10, 1/fs)  # Time vector
f_signal = 10  # Signal frequency
f_noise = 50  # Frequency to remove
f_noisey = 60  # Frequency to remove
signal = np.sin(2*np.pi*f_signal*t) + 0.5 * np.sin(2*np.pi*f_noise*t)+ 2 * np.sin(2*np.pi*f_noisey*t)


# Perform FFT
fft = np.fft.fft(signal)
freqs = np.fft.fftfreq(len(signal)) * fs
amplitudes = np.abs(fft) / (len(signal)*0.5)  # Normalize the amplitudes


# Identify the indices of the frequencies to remove
frequencies_to_remove = [[f_noise,f_noisey]]
indices_to_remove = np.round(np.array(frequencies_to_remove) / (fs / len(signal))).astype(int)

# Zero out the identified frequencies in the FFT
fft_denoised=fft.copy()
fft_denoised[indices_to_remove] = 0
fft_denoised[-indices_to_remove] = 0
amplitudes_denoised = np.abs(fft_denoised) / (len(signal)*0.5)  # Normalize the amplitudes

# Compute the inverse FFT
denoised_signal = np.fft.ifft(fft_denoised)



# Plot the frequency spectrum
plt.figure(figsize=(8, 4))
plt.subplot(2,1,1)
plt.stem(freqs, np.abs(amplitudes))
plt.plot(freqs, np.abs(amplitudes_denoised),linestyle='--',color='orange')
plt.title("Frequency Spectrum")
plt.xlabel("Frequency (Hz)")
plt.ylabel("Amplitude")
plt.xlim(0, fs)  # Show only positive frequencies

# Add a vertical line at the Nyquist frequency
nyquist_freq = fs / 2
plt.axvline(x=nyquist_freq, color='r', linestyle='--', label='Nyquist Frequency')

plt.legend()
plt.grid(True)
plt.subplot(2,1,2)
plt.plot(t,signal,marker='.')
plt.plot(t, denoised_signal.real,linestyle='--')  # Use the real part after the IFFT
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.show()

##################### Low Pass example#######################
# import numpy as np
# from scipy import signal
# import matplotlib.pyplot as plt

# # Generate a synthetic noisy signal with electrical noise at 50 Hz
# fs = 1000  # Sampling frequency
# t = np.arange(0, 1, 1/fs)  # Time vector
# f_signal = 10  # Signal frequency
# signal_noise = np.sin(2*np.pi*f_signal*t) + 0.5 * np.sin(2*np.pi*50*t)

# # Apply a low-pass filter to remove high-frequency noise
# cutoff_freq = 30  # Cutoff frequency of the filter
# b, a = signal.butter(4, cutoff_freq, fs=fs, btype='low')
# filtered_signal = signal.lfilter(b, a, signal_noise)

# # Plot the original signal and the filtered signal
# plt.figure(figsize=(10, 6))
# plt.subplot(2, 1, 1)
# plt.plot(t, signal_noise)
# plt.title("Noisy Signal")
# plt.xlabel("Time")
# plt.ylabel("Amplitude")

# plt.subplot(2, 1, 2)
# plt.plot(t, filtered_signal)
# plt.title("Filtered Signal (Low-Pass Filter)")
# plt.xlabel("Time")
# plt.ylabel("Amplitude")

# plt.tight_layout()
# plt.show()

################# Notched filter ######################
# import numpy as np
# from scipy import signal
# import matplotlib.pyplot as plt

# # Generate a synthetic noisy signal with electrical noise at 50 Hz
# fs = 1000  # Sampling frequency
# t = np.arange(0, 1, 1/fs)  # Time vector
# f_signal = 10  # Signal frequency
# signal_noise = np.sin(2*np.pi*f_signal*t) + 0.5 * np.sin(2*np.pi*50*t)

# # Apply notch filter to remove 50 Hz noise
# f_notch = 50  # Notch frequency
# Q = 30  # Quality factor (determines the width of the notch)
# b, a = signal.iirnotch(f_notch, Q, fs)
# filtered_signal = signal.lfilter(b, a, signal_noise)

# filter_delay = max(len(a), len(b)) - 1
# filtered_signal = filtered_signal[filter_delay:]

# # Plot the original signal and the filtered signal
# plt.figure(figsize=(10, 6))
# plt.subplot(2, 1, 1)
# plt.plot(t, signal_noise)
# plt.title("Noisy Signal")
# plt.xlabel("Time")
# plt.ylabel("Amplitude")

# plt.subplot(2, 1, 2)
# plt.plot(t[filter_delay:], filtered_signal)
# plt.title("Filtered Signal (Notch Filter at 50 Hz)")
# plt.xlabel("Time")
# plt.ylabel("Amplitude")

# plt.tight_layout()
# plt.show()
