import scipy.io.wavfile as wf
import scipy
import scipy.fftpack as fftpk
import numpy as np
from matplotlib import pyplot as plt


def show_fourier_graph_compare(PATH1 , PATH2):
    
    #calcul fft figure 2
    s_rate , signal = wf.read(PATH1)
    FFT = np.abs(fftpk.fft(signal))
    freqs = fftpk.fftfreq(len(FFT), (1.0/s_rate))
    
    # plot de la figure 1
    _ = plt.figure(1)
    plt.plot(freqs[range(len(FFT)//2)] , FFT[range(len(FFT)//2)])
    plt.xlabel("Frequence (Hz)")
    plt.ylabel("Amplitude")
    plt.xlim([0,20000])
    plt.ylim(bottom=0)
    plt.title(PATH1)
    

    #calcul fft figure 2
    s_rate , signal = wf.read(PATH2)
    FFT = np.abs(fftpk.fft(signal))
    freqs = fftpk.fftfreq(len(FFT), (1.0/s_rate))


    print("Freq:" , freqs[:20])
    print("FFT :" , FFT[:20])

    a = 0.5
    res = []
    sum = 0
    den = 0
    for i,f in enumerate(freqs[range(len(FFT)//2)]):
        if f <= a:
            sum += FFT[i][0]
            den+=1
        else:
            if den == 0:
                res.append(0)
            else:
                res.append(sum/den)
            
            if f <= a + 0.5 :
                sum = FFT[i][0]
                den = 1
                a +=0.5
            else :
                res.append(0)
                sum = 0
                den = 0
                a +=1
    
    freqs = np.arange(0.0,20000,0.5)
    print("frequences: " , freqs[:20])
    print("res: " ,res[:20])
    
    




    # plot de la figure 2
    _ = plt.figure(2)
    
    while len(res) < 40000:
        res.append(0)

    plt.plot(freqs, res[:40000])
    
    #plt.plot(freqs[range(len(FFT)//2)] , FFT[range(len(FFT)//2)])
    plt.xlabel("Frequence (Hz)")
    plt.ylabel("Amplitude")
    plt.xlim([0,20000])
    plt.ylim(bottom=0)
    #plt.title(PATH2)
    plt.title("Moyennage a 0.5")




    #afficher les figures
    plt.show()

fem1 = "C:\\Users\\marti\\Desktop\\fem1.wav"
vem1 = "C:\\Users\\marti\\Desktop\\vem1.wav"
fft1 = "C:\\Users\\marti\\Desktop\\fft1.wav"
vvt1 = "C:\\Users\\marti\\Desktop\\vvt1.wav"

show_fourier_graph_compare(fft1,fft1)
show_fourier_graph_compare(vvt1,vvt1)
show_fourier_graph_compare(fem1,fem1)
show_fourier_graph_compare(vem1,vem1)
