from matplotlib.pyplot import plot, show
import numpy as np

t = np.arange(256)
sp = np.fft.fft(np.sin(t))
freq = np.fft.fftfreq(t.shape[-1])
plot(freq, sp.real, freq, sp.imag)
# [<matplotlib.lines.Line2D object at 0x...>, <matplotlib.lines.Line2D object at 0x...>]
show()