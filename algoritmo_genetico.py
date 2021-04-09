from random import random
import matplotlib.pyplot as plt
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  6 21:20:21 2021

@author: juniorsantos
"""

class Product():
    def __init__(self, name, space, value):
        self.name = name
        self.space = space
        self.value = value
        

class Specimen():
    def __init__(self, spaces, values, limit_space, gen = 0):
        self.spaces = spaces
        self.values = values
        self.limit_space = limit_space
        self.evaluation = 0
        self.space_used = 0
        self.gen = gen
        self.chromosome = []
        
        
        for i in range (len(spaces)):
            if random() < 0.5:
                self.chromosome.append("0")
            else:
                self.chromosome.append("1")
                
        self.rating()
        
        
    def rating(self):
        sum_spaces = 0
        sum_evaluation = 0
        for i in range(len(self.chromosome)):
           if self.chromosome[i] == '1':
               sum_spaces+= self.spaces[i]
               sum_evaluation+=self.values[i]
        if sum_spaces > self.limit_space:
            sum_evaluation = 1
        self.evaluation = sum_evaluation
        self.space_used = sum_spaces
        
    def crossover(self, another_specimen):
        cut = round(random()*len(self.chromosome))
        child_chromosome1 = self.chromosome[0: cut] + another_specimen.chromosome[cut::]
        child_chromosome2 = another_specimen.chromosome[0: cut] + self.chromosome[cut::]
        
        children = [Specimen(self.spaces, self.values, self.limit_space, self.gen+1),
                    Specimen(self.spaces, self.values, self.limit_space, self.gen+1)]
        children[0].chromosome = child_chromosome1
        children[1].chromosome = child_chromosome2
        
        return children
    
    
    def mutation(self, tax_mutation):
        for i in range(len(self.chromosome)):
            if random() < tax_mutation:
                if self.chromosome[i] == '1':
                    self.chromosome[i] = '0'
                else:
                    self.chromosome[i] = '1'
        return self
        
    
    
class AlgorithmGenetic():
    def __init__(self, size_population):
        self.size_population = size_population
        self.population = []
        self.gen = 0
        self.best_solution = 0
        self.list_solutions = []
        
    def initialize_population(self, spaces, values, limit_space):
        for i in range(self.size_population):
            self.population.append(Specimen(spaces, values, limit_space))
        self.best_solution = self.population[0]
        
    def sort_population(self):
        self.population = sorted(self.population,
                                 key = lambda population: population.evaluation,
                                 reverse = True)
    def best_specimen(self, specimen):
        if specimen.evaluation > self.best_solution.evaluation:
            self.best_solution = specimen
    
    def sum_evaluation(self):
        total_sum = 0
        for specimen in self.population:
           total_sum += specimen.evaluation
        return total_sum
        
        
    def select_dad(self, sum_evaluation):
        dad = -1
        value_sorted = random() * sum_evaluation
        total_sum = 0
        i = 0
        while i < len(self.population) and total_sum < value_sorted:
            total_sum += self.population[i].evaluation
            dad += 1
            i += 1
        return dad
        
    
    
    def view_generation(self):
        best = self.population[0]
        print("G:%s -> value: %s space: %s chromosome: %s" % (best.gen, best.evaluation, best.space_used, best.chromosome))
        
    
    
    def resolver(self, tax_mutation, number_gen, spaces, values, space_limit):
        self.initialize_population(spaces, values, space_limit)
        
        self.sort_population()            
        self.best_specimen(self.population[0])
        self.list_solutions.append(self.best_solution.evaluation)
        self.view_generation()
        
        
        for gen in range(number_gen):
            sum_evaluation = self.sum_evaluation()
            new_population = []
            
            for specimen_generated in range(0, self.size_population, 2):
                dad1 = self.population[self.select_dad(sum_evaluation)]
                dad2 = self.population[self.select_dad(sum_evaluation)]
                
                children = dad1.crossover(dad2)
                
                child1 = children[0].mutation(tax_mutation)
                child2 = children[1].mutation(tax_mutation)
                
                
                new_population.append(child1)
                new_population.append(child2)
            
            self.population = list (new_population)
            
            
            for specimen in self.population:
                specimen.rating()
            
            self.sort_population()
            self.view_generation()
            
            best = self.population[0]
            
            self.best_specimen(best)
            self.list_solutions.append(best.evaluation)
        
        print("\n Best gen => %s values => %s spaces => %s chromosome => %s" % (self.best_solution.gen,  best.evaluation, best.space_used, best.chromosome))
        
        return self.best_solution.chromosome
        
    
    
    
    
    
if __name__ == "__main__":
    product_list = []    
    product_list.append(Product("Geladeira Dako", 0.751, 999.90))
    product_list.append(Product("Geladeira Dako", 0.751, 999.90))
    product_list.append(Product("Iphone 6", 0.0000899, 2911.12))
    product_list.append(Product("Iphone 6", 0.0000899, 2911.12))
    product_list.append(Product("Iphone 6", 0.0000899, 2911.12))
    product_list.append(Product("TV 55' ", 0.400, 4346.99))
    product_list.append(Product("TV 55' ", 0.400, 4346.99))
    product_list.append(Product("TV 55' ", 0.400, 4346.99))
    product_list.append(Product("TV 50' ", 0.290, 3999.90))
    product_list.append(Product("TV 50' ", 0.290, 3999.90))
    product_list.append(Product("TV 42' ", 0.200, 2999.00))
    product_list.append(Product("Notebook Dell", 0.00350, 2499.90))
    product_list.append(Product("Notebook Dell", 0.00350, 2499.90))
    product_list.append(Product("Notebook Dell", 0.00350, 2499.90))
    product_list.append(Product("Ventilador Panasonic", 0.496, 199.90))
    product_list.append(Product("Microondas Electrolux", 0.0424, 308.66))
    product_list.append(Product("Microondas Electrolux", 0.0424, 308.66))
    product_list.append(Product("Microondas LG", 0.0544, 429.90))
    product_list.append(Product("Microondas LG", 0.0544, 429.90))
    product_list.append(Product("Microondas Panasonic", 0.0319, 299.29))
    product_list.append(Product("Geladeira Brastemp", 0.635, 849.00))
    product_list.append(Product("Geladeira Consul", 0.870, 1199.89))
    product_list.append(Product("Notebook Lenovo", 0.498, 1999.90))
    product_list.append(Product("Notebook Asus", 0.527, 3999.00))

    
    spaces = []
    values = []
    product_names = []
    
    for product in product_list:
        spaces.append(product.space)
        product_names.append(product.name)
        values.append(product.value)
    
    
    space_limit = 3
    number_gen = 200
    size_population = 100
    tax_mutation = 0.1
    
    ag = AlgorithmGenetic(size_population)
    
    result = ag.resolver(tax_mutation, number_gen, spaces, values, space_limit)
    
    
    plt.plot(ag.list_solutions[50::])
    plt.title("Values")
    plt.show()
