# import tkinter
# from classes.Interface import Interface

# if __name__ == "__main__":
#     root = tkinter.Tk()
#     app = Interface(root)
#     root.mainloop()

from classes.NeuronalNetwork import NeuronalNetwork
from utils.get_dataset import get_dataset

data = get_dataset("203722.csv")
nn = NeuronalNetwork(data)
repeat = "Y"

while(repeat == "Y"):
    nn.start()
    repeat = input()

