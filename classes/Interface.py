import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import os
import cv2

from classes.GeneticAlgorithm import GeneticAlgorithm

class Interface:

    frame_number = 0
    folder = "captures"

    def __init__(self, root):
        self.ag = None

        self.root = root
        self.root.title("Algoritmo Genetico")
        self.root.geometry("900x500")

        # Columns
        self.root.columnconfigure(0, weight=1)
        self.root.columnconfigure(1, weight=1) 
        self.root.grid_rowconfigure(0, weight=0)
        self.root.grid_columnconfigure(1, weight=1)  
        self.root.grid_rowconfigure(1, weight=1)

        # Frames
        self.frame_inputs = tk.Frame(self.root)
        self.frame_inputs.grid(row=0, column=0, sticky="n", padx=10, pady=10)

        # Title
        self.title = tk.Label(self.frame_inputs, text="Llene todos los campos")
        self.title.grid(row=0, column=0, sticky="w", pady=5)

        # Input A
        self.label_a = tk.Label(self.frame_inputs, text="Ingrese el valor de A:")
        self.label_a.grid(row=1, column=0, pady=5)
        self.input_a = tk.Entry(self.frame_inputs)
        self.input_a.grid(row=2, column=0, pady=5)

        # Input B
        self.label_b = tk.Label(self.frame_inputs, text="Valor de B:")
        self.label_b.grid(row=3, column=0, pady=5)
        self.input_b = tk.Entry(self.frame_inputs)
        self.input_b.grid(row=4, column=0, pady=5)

        # Input Dx
        self.label_dx = tk.Label(self.frame_inputs, text="Valor de Dx:")
        self.label_dx.grid(row=5, column=0, pady=5)
        self.input_dx = tk.Entry(self.frame_inputs)
        self.input_dx.grid(row=6, column=0, pady=5)

        
        # Input Probabily Cross
        self.label_cross = tk.Label(self.frame_inputs, text="Valor de la probabilidad de cruza:")
        self.label_cross.grid(row=7, column=0, pady=5)
        self.input_cross = tk.Entry(self.frame_inputs)
        self.input_cross.grid(row=8, column=0, pady=5)

        # Input Probabily Mutation
        self.label_mutation = tk.Label(self.frame_inputs, text="Valor de la probabilidad de mutacion:")
        self.label_mutation.grid(row=9, column=0, pady=5)
        self.input_mutation = tk.Entry(self.frame_inputs)
        self.input_mutation.grid(row=10, column=0, pady=5)

        # Input Probabily Mutation Bit
        self.label_mutation_bit = tk.Label(self.frame_inputs, text="Valor de la probabilidad de mutacion de bit:")
        self.label_mutation_bit.grid(row=11, column=0, pady=5)
        self.input_mutation_bit = tk.Entry(self.frame_inputs)
        self.input_mutation_bit.grid(row=12, column=0, pady=5)

        # Button Run
        self.button = tk.Button(self.frame_inputs, text="Iterar", command=self.run)
        self.button.grid(row=13, column=0, pady=5)

        # Button Save Video
        self.button_save_video = tk.Button(self.frame_inputs, text="Guardar video", command=self.save_video)
        self.button_save_video.grid(row=14, column=0, pady=10)
        
        # Graphic
        self.frame = tk.Frame(self.root)
        self.fig, self.ax = plt.subplots()
        
        self.ax.grid(True)
        self.ax.set_title("Generación")
        self.ax.set_xlabel("Tiempo")
        self.ax.set_ylabel("Aptitud")

        self.canvas = FigureCanvasTkAgg(self.fig, master = self.frame)
        self.canvas.get_tk_widget().grid()
        self.frame.grid(row=0, column=1, sticky="nsew", padx=10, pady=10)

    
    def run(self):
        if not self.ag:
            a = int(self.input_a.get())
            b = int(self.input_b.get())
            dx = float(self.input_dx.get())
            p_cross = float(self.input_cross.get())
            p_mutation = float(self.input_mutation.get())
            p_mutation_bit = float(self.input_mutation_bit.get())
            self.ag = GeneticAlgorithm(a, b, dx, p_cross, p_mutation, p_mutation_bit)
        self.generation_x, self.generation_y, self.best_x, self.best_y, self.worst_x, self.worst_y, self.avg_y, self.n_generation = self.ag.start()

        self.update_graph()

    def update_graph(self):

        self.ax.clear()
        self.ax.set_title(f"Generación #{self.n_generation}")
        self.ax.set_xlabel("Tiempo")
        self.ax.set_ylabel("Aptitud")
        self.ax.grid(True)

        self.ax.plot(self.generation_x, self.avg_y, label="Promedio", color="blue", zorder=1, linestyle='--')
        self.ax.plot(self.generation_x, self.generation_y, label="F(x)", color="orange", zorder=2)

        self.ax.scatter(self.generation_x, self.generation_y, label="Individuo", color="purple", zorder=3)
        self.ax.scatter(self.best_x, self.best_y, label="Mejor", c="green", zorder=4)
        self.ax.scatter(self.worst_x, self.worst_y, label="Peor", c="red", zorder=5)

        self.ax.legend()

        self.set_capture()

        self.canvas.draw()

    def set_capture(self):
        
        self.frame_number += 1
        file_path = os.path.join(self.folder, f"grafica_{self.frame_number}.png")
        self.fig.savefig(file_path)
        print(f"Imagen guardada: {file_path}")
    
    def save_video(self):
        fps = 1
        video_name="graficas_video.avi"

        images = [f for f in os.listdir(self.folder) if f.endswith(".png")]
        if not images:
            print("No se encontraron imágenes en la carpeta para crear el video.")
            return

        images.sort(key=lambda x: int(x.split('_')[1].split('.')[0]))

        first_image_path = os.path.join(self.folder, images[0])
        frame = cv2.imread(first_image_path)
        if frame is None:
            print(f"Error al leer la imagen: {first_image_path}")
            return

        height, width, layers = frame.shape

        video = cv2.VideoWriter(video_name, cv2.VideoWriter_fourcc(*'DIVX'), fps, (width, height))
        print(f"Creando video: {video_name}")

        for image in images:
            img_path = os.path.join(self.folder, image)
            img = cv2.imread(img_path)
            if img is None:
                print(f"Error al leer la imagen: {img_path}")
                continue

            if img.shape[:2] != (height, width):
                img = cv2.resize(img, (width, height))

            video.write(img)

        video.release()
        print(f"Video guardado exitosamente en: {video_name}")

        print("Eliminando imágenes...")
        for image in images:
            img_path = os.path.join(self.folder, image)
            try:
                os.remove(img_path)
            except OSError as e:
                print(f"Error al eliminar {img_path}: {e}")

        print("Todas las imágenes han sido eliminadas.")
