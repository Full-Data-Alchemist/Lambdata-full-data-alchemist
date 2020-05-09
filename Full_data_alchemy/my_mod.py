# Full_data_alchemymy_mod.py

# import shap
from sklearn.model_selection import train_test_split

def enlarge(n):
    '''
    Function ellarges a nember
    '''
    return n * 100
class splitter:
    '''
    TODO
    '''
    def __inti__(self, df, trn_size:float, tst_size:float, target:str):
        

        pass


    def splitter(self, df, trn_size:float, tst_size:float, target:str):
        '''
        function automaticaly creates a train and tests split
        '''
        train, test = train_test_split(df, 
                                        train_size = trn_size,
                                        test_size = tst_size,
                                        stratify = target)
        X = train
        y = test
        return X, y


# def shap_val(row, model, encoder):
#     row = X_test.loc[[row]]
#     row

#     explainer = shap.TreeExplainer(model)
#     encoder = encoder
#     row_processed = encoder.transform(row)
#     shap_values = explainer.shap_values(row_processed)

#     shap.initjs()
#     return shap.force_plot(
#         base_value=explainer.expected_value,
#         shap_values=shap_values,
#         features=row,
#         link='logit'

# x = 5 
# print(enlarge(x))


if __name__ == '__main__':
    # only run the code below ix exe code from cmd line
    #otherwise don;t run it()



    y = int(input('please choose a number like 3:'))

    print(enlarge(y))