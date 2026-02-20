import numpy as np
import sounddevice as sd
import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt

class DTMFApp:
    def __init__(self, master):
        self.master = master
        master.title("DTMF Sinyal Sentezleyici")
        master.geometry("800x500")

        # DTMF Frekans Tablosu
        self.dtmf_map = {
            '1': (697, 1209), '2': (697, 1336), '3': (697, 1477), 'A': (697, 1633),
            '4': (770, 1209), '5': (770, 1336), '6': (770, 1477), 'B': (770, 1633),
            '7': (852, 1209), '8': (852, 1336), '9': (852, 1477), 'C': (852, 1633),
            '*': (941, 1209), '0': (941, 1336), '#': (941, 1477), 'D': (941, 1633)
        }
        
        self.fs = 8000  # Standart telefon örnekleme hızı
        self.duration = 0.3 # saniye
        
        self.create_widgets()

    def create_widgets(self):
        # Sol taraf: Tuş Takımı
        key_frame = tk.Frame(self.master)
        key_frame.pack(side=tk.LEFT, padx=20)

        keys = [
            ['1', '2', '3', 'A'],
            ['4', '5', '6', 'B'],
            ['7', '8', '9', 'C'],
            ['*', '0', '#', 'D']
        ]

        for r, row in enumerate(keys):
            for c, key in enumerate(row):
                btn = tk.Button(key_frame, text=key, width=5, height=2,
                                command=lambda k=key: self.play_dtmf(k))
                btn.grid(row=r, column=c, padx=5, pady=5)

        # Sağ taraf: Grafik
        self.fig, self.ax = plt.subplots(figsize=(5, 4))
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.master)
        self.canvas.get_tk_widget().pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

    def play_dtmf(self, key):
        f_low, f_high = self.dtmf_map[key]
        t = np.linspace(0, self.duration, int(self.fs * self.duration))
        
        # Sinyal Sentezi (Normalizasyon için 0.5 ile çarpıldı)
        signal = 0.5 * (np.sin(2 * np.pi * f_low * t) + np.sin(2 * np.pi * f_high * t))
        
        # Sesi Çal
        sd.play(signal, self.fs)
        
        # Grafiği Güncelle (İlk 50ms'yi göstererek dalga formunu netleştir)
        self.ax.clear()
        self.ax.plot(t[:400], signal[:400]) 
        self.ax.set_title(f"Tuş: {key} ({f_low}Hz + {f_high}Hz)")
        self.ax.grid(True)
        self.canvas.draw()

if __name__ == "__main__":
    root = tk.Tk()
    app = DTMFApp(root)
    root.mainloop()