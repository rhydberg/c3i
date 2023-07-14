import numpy as np
from gnuradio import gr


class blk(gr.sync_block):
    """Embedded Python Block example - a simple multiply const"""

    def __init__(self, example_param=1.0):  # only default arguments here
        """arguments to this function show up as parameters in GRC"""
        gr.sync_block.__init__(
            self,
            name='Embedded Python Block',   # will show up in GRC
            in_sig=[(np.float32, 1024)],
            out_sig=[(np.float32, 1)]
        )
        # if an attribute with the same name as a parameter is found,
        # a callback is registered (properties work, too).
        self.example_param = example_param

    def work(self, input_items, output_items):
        """example: multiply with constant"""
        fft_output = input_items[0]  # Assuming the input is the FFT output

        magnitudes = np.abs(fft_output)
        max_index = np.argmax(magnitudes)

        # sample_rate = 32000
        # fft_size = len(fft_output)

        # max_frequency = magnitudes[max_index]

        output_items[0][:] = len(magnitudes)

        return len(output_items)
