import numpy as np
import matplotlib.pyplot as plt

# Time window: 0 to 10ms, 10,000 points (high temporal resolution)
t = np.linspace(0, 0.01, 10000)

# Tesla 3-6-9 Frequencies in radians/sec
omega = 2 * np.pi * 369  # Base frequency
A = 1.0   # Amplitude of 3ω component
B = 0.8   # Amplitude of 6ω component
C = 0.6   # Amplitude of 9ω component

# Harmonic waveform equation
E_harmonic = (
    A * np.sin(3 * omega * t) +
    B * np.sin(6 * omega * t) +
    C * np.sin(9 * omega * t)
)

# Plotting the waveform
plt.figure(figsize=(12, 5))
plt.plot(t * 1000, E_harmonic, label="Eₕₐᵣₘₒₙᵢ𝒸(t)", color="blue")
plt.title("IX-ThermaForge Harmonic Beam: Tesla 3-6-9 Modulation Pattern")
plt.xlabel("Time (ms)")
plt.ylabel("Amplitude (arbitrary units)")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.savefig("harmonic_beam_waveform.png", dpi=300)
plt.show()
