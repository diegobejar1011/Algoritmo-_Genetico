from utils.get_random import get_random_number
import numpy as np

class NeuronalNetwork:

    x = []
    y = []
    w = []

    y_calculate = []
    error = []
    dw = []

    w_iterations = []

    time = 0

    errors = []

    def __init__(self, data):
        self.data = data
        self.n = 0.1
    
    def get_parameters(self):
        for i in range(len(self.data)):
            self.x.append([ 1, self.data[i]["X1"], self.data[i]["X2"], self.data[i]["X3"]])
            self.y.append(self.data[i]["Y"])
    
        n_w = len(self.x[0])
        for i in range(n_w):
            number = round(get_random_number(), 1)
            self.w.append(number)
        
        #print("Peso:")
        #print(self.w)

    def get_y_calculate(self):
        aux_x = np.array(self.x)
        aux_w = np.array(self.w)
        self.y_calculate =  np.dot(aux_x, aux_w).tolist()
    
    def get_error(self):
        pass
        aux_y = np.array(self.y)
        aux_y_c = np.array(self.y_calculate)

        self.error = (aux_y - aux_y_c).tolist()

        # print("Error:")
        # print(self.error[:10])

    def set_dw(self):
        aux_dw = np.array(self.x)
        aux_dw_t = -aux_dw.T

        self.dw = (aux_dw_t @ self.error).tolist()

    def set_w(self):
        aux_dw = np.array(self.dw)

        dw = (self.n * aux_dw).tolist()

        aux_w = np.array(self.w)

        self.w = (aux_w + dw).tolist()

        self.w_iterations.append(sorted(self.w, reverse=True))

        # print("Peso:")
        # print(self.w)
    
    def set_error(self):
        self.errors.append(np.linalg.norm(self.error))
        return self.errors

    def set_w_iterations(self):
            return list(map(list, zip(*self.w_iterations)))

    def start(self):

        if not self.w:
            # Obtención de matriz x, y los vectores y y w 
            self.get_parameters()

        # Obtención de Y calculada
        self.get_y_calculate()

        # Obtener los errores
        self.get_error()

        # Obtener delta W
        self.set_dw()

        # Dar una nueva w
        self.set_w()

        aux_error = self.set_error()
        aux_w_iterations = self.set_w_iterations()

        self.time +=1

        return aux_error, aux_w_iterations, self.time, self.y, self.y_calculate
    