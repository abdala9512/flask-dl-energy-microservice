"""Deep Learning Univariate Modeling Class"""

from fbprohet import Prophet
from tensorflow.keras.layers import LSTM, Dense
from tensorflow.keras.models import Sequential
from tensorflow.keras.callbacks import EarlyStopping
import numpy as np

class DeepLearningUTSModel:
    """
    Univariate Time Series Deep Learning Model pipeline Class
    """
    
    def __init__(self, data=None, LSTM_layer_depth=50, epochs=10):
        
        self.data = data
        self.LSTM_layer_depth = LSTM_layer_depth
        self.epochs = epochs
        self.model = None
        self.prophet_ = False
    
    @classmethod
    def create_ts_sequences(cls, series, lag):
        """Create vectors along a time series with
        an specified number of lags"""
        
        X, y = [], []
        
        for t in range(len(series)):
            
            # Index + defined_lag t = [t-1, t-2, ..., t-lag]
            t_plus_lag = t + lag
            
            if t_plus_lag > len(series)-1:
                break
            
            X_seq, y_seq = series[t:t_plus_lag], series[t_plus_lag]
            
            # Append arrays to the 
            X.append(X_seq)
            y.append(y_seq)
            
        # Reshape and transformation to array
        
        X = np.array(X)
        y = np.array(y)
        
        X = np.reshape(X, (X.shape[0], X.shape[1], 1))
        
        return X, y
        
    def vanillaLSTM(self, X, y, lags, n_features=1):
        """Minimalist LSTM model
            
           n_features=1 for univariate time series
        """
        callback = EarlyStopping(monitor='loss', patience=10)
        model = Sequential()
        model.add(LSTM(self.LSTM_layer_depth, activation='relu', input_shape=(lags, n_features)))
        model.add(Dense(1))
        model.compile(optimizer='adam', loss='mse')
                
        model.fit(X, y, epochs=self.epochs, verbose=0, callbacks=[callback])
        
        self.model = model

        return model
    
    def prophet(self, ds, ts):
        """Facebook Prophet estimation
            df: dataframe
            ds: datatime column
            ts: time series
        """
        
        if self.data is None:
            raise TypeError("""
            DataFrame is a None value, initialize 
            the DeepLearningUTSModel with an appropiate dataframe
            """)
            
        columns = ['ds', 'y']
        
        df = self.data[[ds, ts]]
        df.columns = columns
        
        model = Prophet()
        model.fit(df)
        
        self.model = model
        self.prophet_ = True
        future = model.make_future_dataframe(periods=500)
        
        return model, future
    
    def stackedLSTM(self):
        pass

    def bdLSTM(self):
        pass

    def cnnLSTM(self):
        pass

    def convLSTM(self):
        pass

    
    def predict(self, x):
          
        if self.model is not None:
            if self.prophet_ == False:
                predictions = [y[0] for y in self.model.predict(x)]
            else:
                predictions = model.predict(x)
        else:
            raise ValueError("Model haven't fitted.")
        
        return predictions
    

    def predict_future(self, series, lag, n_ahead):
        """Preditions n moments ahead"""
        
        X, _ = DeepLearningUTSModel.create_ts_sequences(series=series, lag=lag)
        
        yhat = []
        for _ in range(n_ahead):
            
            if self.model is not None:
                forecast = self.model.predict(X)
            else:
                raise ValueError("Model haven't fitted.")   
            
            yhat.append(forecast)
                        
            X = np.append(X, forecast)
            # Ommiting the first variable
            X = np.delete(X, 0)
            X = np.reshape(X, (1, len(X), 1))
            
        return yhat
          