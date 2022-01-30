import scipy.io.wavfile as wf
import scipy
import scipy.fftpack as fftpk
import numpy as np


# this function creates a matrice of 40000 lines from a .wav file. Used as input for the Neural Network.
# in->PATH(file.wav) ; out->mat(40000,1)
def create_nn_input(PATH):
    
    # fast fourier transform of the input signal
    s_rate , signal = wf.read(PATH)
    FFT = np.abs(fftpk.fft(signal))
    freqs = fftpk.fftfreq(len(FFT), (1.0/s_rate))


    # doing an average of the values between the frequences n and n+0.5
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
    

    # new frequences for res, you can use them to visualise the graph of the output with matplotlib
    freqs = np.arange(0.0,20000,0.5)

    # return res with 40000 values 
    
    while len(res) < 40000:
        res.append(0)

    return res[:40000]

fem1 = "C:\\Users\\marti\\Desktop\\fem1.wav"
vem1 = "C:\\Users\\marti\\Desktop\\vem1.wav"
fft1 = "C:\\Users\\marti\\Desktop\\fft1.wav"
vvt1 = "C:\\Users\\marti\\Desktop\\vvt1.wav"

print(create_nn_input(vvt1))

