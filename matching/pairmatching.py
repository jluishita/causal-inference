import pandas as pd
import numpy as np

class NaivePairMatching():

    def __init__(self, df_treatment, df_control, y_treatment, y_control):
        self.df_treatment = df_treatment.copy()
        self.df_control = df_control.copy()
        self.df_paired_control = pd.DataFrame(columns=df_control.columns)
        self.df_paired_outcomes = pd.DataFrame(columns=['treated', 'control'])
        self.y_treatment = y_treatment.copy()
        self.y_control = y_control.copy()

    def find_pair(self, element):
        pair = self.df_control_copy.loc[self.df_control.eq(element).all(1)]
        if pair == None:
            raise ValueError("ERROR: No se ha encontrado pareja para todos los casos")
        return pair

    def add_outcomes_to_df(self, treatment_index, control_index):
        series = pd.Series({
            'treatment' : self.y_tratment.loc[treatment_index],
            'control' : self.y_tratment.loc[treatment_index]
        })
        
        self.df_paired_outcomes = pd.concat(
            [self.df_paired_outcomes,
            series]
        )

    def add_pair_to_paired_control(self, pair):
        self.df_paired_control = pd.concat(
            [self.df_paired_control,
            pair]
        )

    def pair_matching(self):
        for treat in self.df_treatment.itertuples():
            pair = self.find_pair(treat)
            pair_index = pair.index[0]
            self.df_control = self.df_control.drop([pair_index])
            self.add_outcomes_to_df(
                treat.index[0], 
                pair_index
            )
            self.add_pair_to_paired_control(pair)


        
        