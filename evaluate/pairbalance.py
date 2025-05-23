import pandas as pd
import numpy as np

class StandarizedDifferences():
    """
    """
    def __init__(self, pairing, data=None):
        self.pairing = pairing
        self.data = data

    def differences(self):
        """
        """
        mean_treatment = self.pairing.df_treatment.mean()
        mean_control = self.pairing.df_control.mean()
        mean_paired_control = self.pairing.df_paired_control.mean()

        var_treatment = self.pairing.df_treatment.var()
        var_control = self.pairing.df_control.var()
        var_paired_control = self.pairing.df_paired_control.var()

        std_diff_original = (mean_treatment - mean_control) / np.sqrt((var_treatment + var_control)/2)
        std_diff_paired = (mean_treatment - mean_paired_control) / np.sqrt((var_treatment + var_paired_control)/2)

        df = pd.DataFrame({'Original': std_diff_original, 'Paired': std_diff_paired})

        return df
        