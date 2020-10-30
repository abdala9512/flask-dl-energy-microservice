"""Deep Learning Univariate Modeling Class"""

from tensorflow.keras.layers import LSTM, Dense
from tensorflow.keras.models import Sequential
import numpy as np

class DeepLearningUTSModel:
    """LSTM model Pipeline Class"""
    
    def __init__(self, LSTM_layer_depth=50, epochs=10):
        
        #self.data = data
        self.LSTM_layer_depth = LSTM_layer_depth
        self.epochs = epochs
        self.model = None
    
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
        
        model = Sequential()
        model.add(LSTM(self.LSTM_layer_depth, activation='relu', input_shape=(lags, n_features)))
        model.add(Dense(1))
        model.compile(optimizer='adam', loss='mse')
                
        model.fit(X, y, epochs=self.epochs, verbose=0)
        
        self.model = model

        return model

    
    def predict(self, x):
          
        if self.model is not None:
            predictions = [y[0] for y in self.model.predict(x)]
        else:
            raise ValueError("Model haven't fitted.")
        
        return predictions
        