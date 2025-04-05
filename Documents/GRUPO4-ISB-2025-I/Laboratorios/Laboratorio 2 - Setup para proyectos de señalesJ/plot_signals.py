import neurokit2 as nk
import matplotlib.pyplot as plt

# Simular 2 señales EMG
emg1 = nk.emg_simulate(duration=10, sampling_rate=1000)
emg2 = nk.emg_simulate(duration=10, sampling_rate=1000)

# Simular 2 señales ECG
ecg1 = nk.ecg_simulate(duration=10, sampling_rate=1000)
ecg2 = nk.ecg_simulate(duration=10, sampling_rate=1000)

# Graficar las señales
plt.figure(figsize=(12, 8))

plt.subplot(4, 1, 1)
plt.plot(emg1)
plt.title("EMG 1")

plt.subplot(4, 1, 2)
plt.plot(emg2)
plt.title("EMG 2")

plt.subplot(4, 1, 3)
plt.plot(ecg1)
plt.title("ECG 1")

plt.subplot(4, 1, 4)
plt.plot(ecg2)
plt.title("ECG 2")

plt.tight_layout()
plt.show()
