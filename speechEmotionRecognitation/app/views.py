from django.shortcuts import render, redirect
import os
from .models import ParallelModel
import torch
import librosa
import numpy as np

# Create your views here.
EMOTIONS = {1:'neutral', 2:'calm', 3:'happy', 4:'sad', 5:'angry', 6:'fear', 7:'disgust', 0:'surprise'}
SAMPLE_RATE = 48000
device = 'cuda' if torch.cuda.is_available() else 'cpu'

LOAD_PATH = os.path.join(os.getcwd(),'models') # loading the model
model = ParallelModel(len(EMOTIONS))
model.load_state_dict(torch.load(os.path.join(LOAD_PATH,'cnn_transf_parallel_model.pt')))


def index(request):
    return render(request, 'index.html')

def audioSubmit(request):
    if request.method == 'POST':
        audiofile = request.POST['audiofile']
    audio, sample_rate = librosa.load(audiofile, duration=3, offset=0.5,sr=SAMPLE_RATE)
    signal = np.zeros((int(SAMPLE_RATE*3,)))
    signal[:len(audio)] = audio
    mel_spectrogram = getMELspectrogram(signal, SAMPLE_RATE)

    return render(request, 'index.html')



def addAWGN(signal, num_bits=16, augmented_num=2, snr_low=15, snr_high=30): 
    signal_len = len(signal)
    # Generate White Gaussian noise
    noise = np.random.normal(size=(augmented_num, signal_len))
    # Normalize signal and noise
    norm_constant = 2.0**(num_bits-1)
    signal_norm = signal / norm_constant
    noise_norm = noise / norm_constant
    # Compute signal and noise power
    s_power = np.sum(signal_norm ** 2) / signal_len
    n_power = np.sum(noise_norm ** 2, axis=1) / signal_len
    # Random SNR: Uniform [15, 30] in dB
    target_snr = np.random.randint(snr_low, snr_high)
    # Compute K (covariance matrix) for each noise 
    K = np.sqrt((s_power / n_power) * 10 ** (- target_snr / 10))
    K = np.ones((signal_len, augmented_num)) * K  
    # Generate noisy signal
    return signal + K.T * noise

def getMELspectrogram(audio, sample_rate):
    mel_spec = librosa.feature.melspectrogram(y=audio,
                                              sr=sample_rate,
                                              n_fft=1024,
                                              win_length = 512,
                                              window='hamming',
                                              hop_length = 256,
                                              n_mels=128,
                                              fmax=sample_rate/2
                                             )
    mel_spec_db = librosa.power_to_db(mel_spec, ref=np.max)
    return mel_spec_db

X_test_tensor = torch.tensor(X_test, device=device).float()

# If necessary, reshape or preprocess X_test_tensor according to your model's input requirements

# Call the validate function with the single audio file tensor
test_loss, test_acc, predictions = validate(X_test_tensor.unsqueeze(0), torch.tensor([your_label], device=device))





