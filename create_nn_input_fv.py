import scipy.io.wavfile as wf
import scipy.fftpack as fftpk
import numpy as np
import os
from supress_output import suppress_output


# this function creates a matrice of 40000 lines from a .wav file. Used as input for the Neural Network.
# in->PATH(file.wav) ; out->mat(40000,1)
def create_nn_input_fv(PATH):
    
    # fast fourier transform of the input signal
    with suppress_output(suppress_stdout=True, suppress_stderr=True):
        #we don't print the output message of this function
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
            try :
                sum += FFT[i][0]
            except:
                sum += FFT[i]
            den+=1
        else:
            if den == 0:
                res.append(0)
            else:
                res.append(sum/den)
            
            if f <= a + 0.5 :
                try :
                    sum = FFT[i][0]
                except:
                    sum = FFT[i]
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
    
    # Output values between 0 and 1
    t = res[:1000]
    t = t/max(t)

    return t


# test with some audio samples
__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

fft1 = os.path.join(__location__, 'audio_samples\\fft1.wav')
vvt1 = os.path.join(__location__, 'audio_samples\\vvt1.wav')
fem1 = os.path.join(__location__, 'audio_samples\\fem1.wav')
vem1 = os.path.join(__location__, 'audio_samples\\vem1.wav')
