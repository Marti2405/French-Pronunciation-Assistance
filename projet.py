import scipy.io.wavfile as wf
import scipy
import scipy.fftpack as fftpk
import numpy as np
from matplotlib import pyplot as plt


def show_fourier_graph_compare(PATH1 , PATH2):
    plot1 = plt.figure(1)
    s_rate , signal = wf.read(PATH1)


    FFT = abs(scipy.fft.fft(signal))
    freqs = fftpk.fftfreq(len(FFT), (1.0/s_rate))

    plt.plot(freqs[range(len(FFT)//2)] , FFT[range(len(FFT)//2)])
    plt.xlabel("Frequence (Hz)")
    plt.ylabel("Amplitude")
    plt.title(PATH1)
    ############################################
    plot2 = plt.figure(2)
    s_rate , signal = wf.read(PATH2)
    

    FFT = np.abs(scipy.fft.fft(signal))
    freqs = fftpk.fftfreq(len(FFT), (1.0/s_rate))

    plt.plot(freqs[range(len(FFT)//2)] , FFT[range(len(FFT)//2)])
    plt.xlabel("Frequence (Hz)")
    plt.ylabel("Amplitude")
    plt.title(PATH2)


    plt.show()

fem1 = "C:\\Users\\marti\\Desktop\\fem1.wav"
vem1 = "C:\\Users\\marti\\Desktop\\vem1.wav"
fft1 = "C:\\Users\\marti\\Desktop\\fft1.wav"
vvt1 = "C:\\Users\\marti\\Desktop\\vvt1.wav"

show_fourier_graph_compare(fft1,vvt1)
