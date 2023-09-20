import numpy as np



class Perceptron():
    def __init__(self, n_input, learning_rate): #inicializamos los valores
        self.w= -1 + 2 * np.random.rand(n_input)
        self.b=-1 + 2 * np.random.rand()
        self.eta = learning_rate
    
    def predict(self, X):#predict hace una predicción de los Y que podrian ser respuesta para los valores dados
        p=X.shape[1]
        y_est=np.zeros(p)
        for i in range (p):
            y_est[i]=np.dot(self.w, X[:,i])+self.b
            if y_est[i]>=0:
                y_est[i]=1
            else:
                y_est[i]=0
        return y_est
    
    def fit(self, X, Y, epochs=50):
        p=X.shape[1]
        for _ in range (epochs):
            for i in range(p):
                y_est=self.predict(X[:,i].reshape(-1,1))
                self.w += self.eta * (Y[i]-y_est) *  X[:,i]
                self.b += self.eta * (Y[i]-y_est) * 1

