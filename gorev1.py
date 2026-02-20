import numpy as np
import matplotlib.pyplot as plt

# --- PARAMETRELER ---
f0 = 135  
f1 = f0          # 135 Hz
f2 = f0 / 2      # 67.5 Hz
f3 = 10 * f0     # 1350 Hz

# Nyquist Kriteri: fs en az 2 * f3 (2700 Hz) olmalı.
# Pürüzsüz görüntü için 44100 Hz (standart ses hızı) seçiyoruz.
fs = 44100 

def signal_gen(f, periods=3):
    T = 1/f
    t = np.linspace(0, periods*T, int(fs * periods * T))
    return t, np.sin(2 * np.pi * f * t)

# Sinyalleri Üret
t1, s1 = signal_gen(f1)
t2, s2 = signal_gen(f2)
t3, s3 = signal_gen(f3)

# Toplam Sinyal (En düşük frekansın 1 periyodu kadar süre)
t_sum, _ = signal_gen(f2, periods=1)
s_sum = (np.sin(2*np.pi*f1*t_sum) + 
         np.sin(2*np.pi*f2*t_sum) + 
         np.sin(2*np.pi*f3*t_sum))

# --- GRAFİK ÇİZİMİ ---
fig, axs = plt.subplots(4, 1, figsize=(10, 12))
axs[0].plot(t1, s1, 'b'); axs[0].set_title(f'f1 = {f1}Hz')
axs[1].plot(t2, s2, 'g'); axs[1].set_title(f'f2 = {f2}Hz')
axs[2].plot(t3, s3, 'r'); axs[2].set_title(f'f3 = {f3}Hz')
axs[3].plot(t_sum, s_sum, 'm'); axs[3].set_title('Sinyallerin Toplamı')

for ax in axs: ax.grid(True)
plt.tight_layout()
plt.show() # Bu komut grafiği ekrana getirir