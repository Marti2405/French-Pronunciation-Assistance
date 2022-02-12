import os

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))


fichiers = []
for fichier in os.listdir("C:\\Users\\marti\\Desktop\\Dossiers\\Coding\\Projet 2MIC_S2\\audio_samples"):
    fichiers.append(fichier.split(".")[0])

def audio (nom):
    __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
    return os.path.join(__location__, f'audio_samples\\{nom}.wav')

fft1 = os.path.join(__location__, 'audio_samples\\fft1.wav')
vvt1 = os.path.join(__location__, 'audio_samples\\vvt1.wav')
fem1 = os.path.join(__location__, 'audio_samples\\fem1.wav')
vem1 = os.path.join(__location__, 'audio_samples\\vem1.wav')
f1 = os.path.join(__location__, 'audio_samples\\f1.wav')
f2 = os.path.join(__location__, 'audio_samples\\f2.wav')
f3 = os.path.join(__location__, 'audio_samples\\f3.wav')
v1 = os.path.join(__location__, 'audio_samples\\v1.wav')
v2 = os.path.join(__location__, 'audio_samples\\v2.wav')
v3 = os.path.join(__location__, 'audio_samples\\v3.wav')

