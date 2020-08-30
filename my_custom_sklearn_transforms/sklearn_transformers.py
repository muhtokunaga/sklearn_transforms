from sklearn.base import BaseEstimator, TransformerMixin


# All sklearn Transforms must have the `transform` and `fit` methods
class DropColumns(BaseEstimator, TransformerMixin):
    def __init__(self, columns):
        self.columns = columns

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        # Primeiro realizamos a cópia do dataframe 'X' de entrada
        data = X.copy()
        # Retornamos um novo dataframe sem as colunas indesejadas
        return data.drop(labels=self.columns, axis='columns')

    
class FillNotaGo(BaseEstimator, TransformerMixin):
    def __init__(self):
        pass

    def fit(self, X, y=None):
        return self
    
    def transform(self, X):
        data = X.copy()
        data['NOTA_GO'] = np.where(data['REPROVACOES_GO'] > 0, data['NOTA_GO'].fillna(0), data['NOTA_GO'])
        data['NOTA_GO'].fillna(data['NOTA_GO'].median(), inplace = True)
        return data

    
class FillIngles(BaseEstimator, TransformerMixin):
    def __init__(self):
        pass

    def fit(self, X, y=None):
        return self
    
    def transform(self, X):
        data = X.copy()
        data['INGLES'].fillna(0, inplace = True)
        return data

    
class PerfilTransform(BaseEstimator, TransformerMixin):
    def __init__(self):
        pass

    def fit(self, X, y=None):
        return self
    
    def transform(self, X):
        data = X.copy()#Aplicando tranform no perfil
        data['PERFIL'] = data['PERFIL'].map( {'EXATAS': 0, 'HUMANAS': 1, 'DIFICULDADE': 2, 'MUITO_BOM': 3, 'EXCELENTE': 4} )
        return data
