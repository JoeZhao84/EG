
class RejSampling(object):
    """
    """
    def __init__(self):
        self.variables = []
        
    def get_variables(self,variables):
        self.variables = variables
        
    def get_list(self,df):
        n_var = len(self.variables)
        unique_list = [None] * len(self.variables)
        for i in range(n_var):
            t = df[self.variables[i]].unique()
            unique_list[i] = t[~pd.isnull(t)]
        return unique_list
           
    def get_ratio(self,df):
        ratios = []
        import itertools
        unique_pair_list = []
        for element in itertools.product(*unique_list):
            unique_pair_list.append(element)
            
        for i in unique_pair_list:
            temp_df = df[(df[self.variables[0]] == i[0])]
            j = 1
            while j < len(self.variables):
                temp_df = temp_df[(temp_df[self.variables[j]] == i[j])]
                j = j + 1
            male_count = temp_df[temp_df['flavor'] == 'Base']['flavor'].count()
            female_count = temp_df[temp_df['flavor'] == 'PreferredModel']['flavor'].count()
            ratio = female_count / male_count
            ratios.append(ratio)
            nonnan_ratios = [x for x in ratios if str(x) != 'nan']
            nonnan_nonzero_ratios = [x for x in nonnan_ratios if x != 0.0]
            min_ratio = np.min(nonnan_nonzero_ratios)
            #print(nonnan_ratios)
        return min_ratio
    
    
#        for i in unique_pair_list:
#            male_count = df[(df[self.variables[0]] == i[0]) & (df[self.variables[1]] == i[1]) & (df['Sex'] == 'male')]['Sex'].count()
#            female_count = df[(df[self.variables[0]] == i[0]) & (df[self.variables[1]] == i[1]) & (df['Sex'] == 'female')]['Sex'].count()
#            ratio = female_count / male_count
#            ratios.append(ratio)
#            min_ratio = min(ratios)
#        return min_ratio
    
    def get_sample(self,df):
        newDF = pd.DataFrame()
        import itertools
        unique_pair_list = []
        for element in itertools.product(*unique_list):
            unique_pair_list.append(element)
            
        for i in unique_pair_list:
            temp_df = df[(df[self.variables[0]] == i[0])]
            j = 1
            while j < len(self.variables):
                temp_df = temp_df[(temp_df[self.variables[j]] == i[j])]
                j = j + 1
            male_count = temp_df[temp_df['flavor'] == 'Base']['flavor'].count()
            female_count_e = int(round(male_count * ratio))
            if female_count_e == 0:
                pass  
            elif temp_df[temp_df['flavor'] == 'PreferredModel']['flavor'].count() == 0:
                pass
            else:
                acc_sample =  temp_df[temp_df['flavor'] == 'PreferredModel'].sample(n=female_count_e,replace=True)
            #print(acc_sample)
                newDF = newDF.append(acc_sample, ignore_index=True)
        return newDF
