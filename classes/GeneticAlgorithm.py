import math
import random
from .Subject import Subject
from utils.order_by_aptitude import order_by_apttitude
from utils.get_random import get_random_number

class GeneticAlgorithm:

    parents = []
    matches = []
    childrens = []
    generation = []

    generations = []

    y_best = []
    y_worst = []
    y_avg = []
    x_generation = []

    generation_y = []
    generation_x = []

    best_x = []
    best_y = []

    worst_x = []
    worst_y = []

    avg_y = []

    n_generation = 0



    def __init__(self, a, b, dx, p_cross, p_mutation, p_mutation_bit):
        self.a = a
        self.b = b
        self.dx = dx 
        self.n = self.get_n()
        self.bits = self.get_bits()
        self.dx_fit = self.get_dx_fit()
        self.max_bits = self.get_max_bits()
        self.mutation_probability = p_mutation
        self.mutation_bit_probability = p_mutation_bit
        self.cross_probability = p_cross
    
    def get_n(self):
        return int(((self.b - self.a)/self.dx) + 1)
    
    def get_bits(self):
        return math.ceil(math.log2(self.n))
    
    def get_dx_fit(self):
        return (self.b - self.a)/((math.pow(2, self.bits)) - 1)
    
    def get_max_bits(self):
        binary = ""
        for _ in range(self.bits):
            binary += "1"
        return int(binary, 2)

    def set_poblation(self):
        for i in range(1, self.max_bits + 1):
            subject = Subject(i)
            subject.set_x(self.a, self.dx_fit)
            self.parents.append(subject)
        self.parents = order_by_apttitude(self.parents)
    
    def set_matches(self):
        for i in range(len(self.parents)):
            if get_random_number() <= self.cross_probability:
                j = random.randint(0, i)
                self.matches.append((self.parents[i], self.parents[j]))
    
    def set_childrens(self):
        for match in self.matches:

            cut = random.randint(1, self.bits - 1)

            # First children
            father_part_one = match[0].binary[:cut]
            father_part_two = match[0].binary[cut:]

            # Second children
            mother_part_one = match[1].binary[:cut]
            mother_part_two = match[1].binary[cut:]

            first_children = Subject(int(father_part_one + mother_part_two, 2))
            first_children.set_x(self.a, self.dx_fit)

            second_children = Subject(int(mother_part_one + father_part_two, 2))
            second_children.set_x(self.a, self.dx_fit)

            self.childrens.append(first_children)
            self.childrens.append(second_children)
        
        # print("Chindlrens")
        # for i in range(10):
        #     print(f"i: {self.childrens[i].i} aptitude: {self.childrens[i].aptitude} binary: {self.childrens[i].binary} ")
        
    def set_mutations(self):
        for child in self.childrens:
            aux = list(child.binary)
            if get_random_number() <= self.mutation_probability:
                for j in range(len(child.binary)):
                    if random.random() <= self.mutation_bit_probability:
                        if aux[j] == '1':
                            aux[j] = '0'
                        elif aux[j] == '0':
                            aux[j] = '1'
                    child = Subject(int(''.join(aux), 2))
                    child.set_x(self.a, self.dx_fit)
    
    def set_mow(self):
        
        all_subjects = self.parents + self.childrens
        all_subjects = order_by_apttitude(all_subjects)

        unique_subjects = {subject.i: subject for subject in all_subjects}.values()
        unique_subjects = list(unique_subjects) 

        self.generation = unique_subjects

        # print("Generation")
        # for i in range(10):
        #     print(f"i: {self.generation[i].i} aptitude: {self.generation[i].aptitude} binary: {self.generation[i].binary} ")

    def set_generation(self):

        best_subject = max(self.childrens, key=lambda s: s.aptitude)
        worst_subject = min(self.childrens, key=lambda s: s.aptitude)
        average_subject = (best_subject.aptitude + worst_subject.aptitude) / 2
        
        self.generations.append({ 
            "best": best_subject, 
            "worst": worst_subject,
            "average": average_subject
        })

        for i in range(len(self.generations)):
            print(f"i: {self.generations[i]["best"].i } aptitude: {self.generations[i]["best"].aptitude }" )
            print(f"i: {self.generations[i]["worst"].i } aptitude: {self.generations[i]["worst"].aptitude }" )
            print(f"i: {self.generations[i]["average"] }" )

    def get_data_to_graphic(self):

        for i in range(len(self.generations)):
            generation = self.generations[i]
            self.y_best.append(generation["best"].aptitude)
            self.y_worst.append(generation["worst"].aptitude)
            self.y_avg.append(generation["average"])
            self.x_generation.append(i + 1)

    def get_data_for_generation(self):

        self.best_x.clear()
        self.best_y.clear()
        self.worst_x.clear()
        self.worst_y.clear()
        self.generation_x.clear()
        self.generation_y.clear()
        self.avg_y.clear()

        j = len(self.generations) - 1
        print(j)
        generation = self.generations[j]
        self.best_x.append(generation["best"].i)
        self.best_y.append(generation["best"].aptitude)

        self.worst_x.append(generation["worst"].i)
        self.worst_y.append(generation["worst"].aptitude)

        aux_childrens = sorted(self.childrens, key=lambda s: s.i, reverse=True)

        for i in range(len(aux_childrens)):
            subject = aux_childrens[i]
            self.generation_x.append(subject.i)
            self.generation_y.append(subject.aptitude)
            self.avg_y.append(generation["average"])

    def start(self):

        if not self.parents:
            print("Paso aqui")
            self.set_poblation()

        # print("Parents")
        # for i in range(10):
        #     print(f"i: {self.parents[i].i} aptitude: {self.parents[i].aptitude} binary: {self.parents[i].binary} ")

        self.set_matches()
        self.set_childrens()
        self.set_mutations()

        self.set_generation()
        self.get_data_for_generation()

        self.set_mow()
        self.parents = self.generation

        # self.get_data_to_graphic()

        # return self.y_best, self.y_worst, self.y_avg, self.x_generation

        return self.generation_x, self.generation_y, self.best_x, self.best_y, self.worst_x, self.worst_y, self.avg_y
