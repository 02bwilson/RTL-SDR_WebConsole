from rtlsdr import *


class SDRController:
    _VERSION_ = "1.0"

    def __init__(self, sample_rate=2e6, center_freq=95e6, freq_correction=45, gain='auto'):

        # Instantiate sdr object
        self.sdr_obj = RtlSdr()

        # Set params
        self.set_sample_rate(sample_rate)
        self.set_center_freq(center_freq)
        self.set_freq_correction(freq_correction)
        self.set_gain(gain)

        # Set some defaults
        self.read_size = 1024

    def read_samples(self):
        return self.sdr_obj.read_samples(self.read_size)

    def set_read_size(self, size):
        self.read_size = size

    def close(self):
        self.sdr_obj.close()

    def set_sample_rate(self, rate):
        try:
            self.sdr_obj.sample_rate = rate
        except:
            raise Exception("Invalid Sample Rate!")

    def set_center_freq(self, freq):
        try:
            self.sdr_obj.center_freq = freq
        except:
            raise Exception("Invalid Center Freq!")

    def set_freq_correction(self, rate):
        try:
            self.sdr_obj.freq_correction = rate
        except:
            raise Exception("Invalid Freq Correction!")

    def set_gain(self, gain):
        try:
            self.sdr_obj.gain = gain
        except:
            raise Exception("Invalid Gain!")
