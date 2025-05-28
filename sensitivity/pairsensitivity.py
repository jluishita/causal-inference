import pandas as pd
import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt


class RosenbaumPValue():
    """
    """

    def __init__(self, paired_data, q_statistic='t-statistic'):
        self.paired_data = paired_data
        self.q_statistic = q_statistic


    def get_q_statistic(self):
        """
        """
        if self.q_statistic == 't-statistic':
            result = np.abs(self.paired_data)
        return result


    def get_sum_q_statistic(self):
        """
        """
        result = np.sum(self.get_q_statistic())
        return result


    def get_sum_q_statistic_squared(self):
        """
        """
        result = np.sum(self.get_q_statistic()**2)
        return result


    def get_T_value(self):
        """
        """
        return (self.get_q_statistic()[self.paired_data>0]).sum()


    def get_approximate_pvalue(self, Gamma=1):
        """
        """
        mean = (Gamma/(1 + Gamma)) * self.get_sum_q_statistic()
        variance = (Gamma/((1 + Gamma)**2)) * self.get_sum_q_statistic_squared()
        T_value = self.get_T_value()
        p_value = 1 - norm.cdf(T_value, loc=mean, scale=np.sqrt(variance))
        return p_value

    def plot_sensitivity_analysis(self, Gamma_i=1, Gamma_f=10, n_points=50):
        """
        """
        gamma_array = np.linspace(Gamma_i, Gamma_f, n_points)
        pvalue_array = []
        for gamma in gamma_array:
            pvalue_array.append(self.get_approximate_pvalue(gamma))

        plt.figure()
        plt.plot(gamma_array, [0.05]*len(gamma_array), '--')
        plt.plot(gamma_array, pvalue_array, '-', label='p-value')
        plt.xlabel('Gamma')
        plt.ylabel('p-value')
        plt.legend()
        plt.show()