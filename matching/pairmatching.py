import pandas as pd

class NaivePairMatching():
    """
    Class that performs naive pair matching

    Unless the number of covariates is small, this method is NOT expected to work well

    It has been developed for illustrative purposes
    """

    def __init__(self, df_treatment, df_control, y_treatment, y_control):
        self.df_treatment = df_treatment.copy()
        self.df_control = df_control.copy()
        self.df_paired_control = pd.DataFrame(columns=df_control.columns)
        self.df_paired_outcomes = pd.DataFrame(columns=['treatment', 'control'])
        self.y_treatment = y_treatment.copy()
        self.y_control = y_control.copy()
        self.discarded = []


    def find_pair(self, element, element_index):
        """
        Finds an element in the control group with the same covariates
        """
        pair = self.df_control.loc[self.df_control.eq(element).all(1)]
        if len(pair) == 0:
            self.discarded.append(element_index)
            return 'NOPAIR'
        return pair.iloc[[0]]


    def add_outcomes_to_df(self, treatment_index, control_index):
        """
        Adds outcomes of paired treatment and control elements
        """
        series = pd.DataFrame({
            'treatment' : [self.y_treatment.loc[treatment_index]],
            'control' : [self.y_control.loc[control_index]]
        })

        self.df_paired_outcomes = pd.concat(
            [self.df_paired_outcomes,
            series], ignore_index=True
        )


    def add_pair_to_paired_control(self, pair):
        """
        Add paired outcomes to df_paired_outcomes dataframe
        """
        self.df_paired_control = pd.concat(
            [self.df_paired_control,
            pair]
        )


    def pair_matching(self):
        """
        Main function. It is the only function that is supposed to be called by the user
        """
        for treat in self.df_treatment.itertuples(index=False):

            treat_index = self.df_treatment.loc[self.df_treatment.eq(treat).all(1)].index[0]
            pair = self.find_pair(treat, treat_index)
            if not isinstance(pair, pd.DataFrame):
                continue
            pair_index = pair.index[0]
            self.df_control = self.df_control.drop([pair_index])
            self.add_outcomes_to_df(
                treat_index,
                pair_index
            )
            self.add_pair_to_paired_control(pair)
