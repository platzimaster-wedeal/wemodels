"""This file have the graph model """

import math
from utils import Utils

utils  = Utils()

class Graph:
    """Graph class"""   
    def __init__(self, name, version):
        self.name = name
        self.version = version
        self.verteces = []


class Vertex:
    """Vertex class"""
    max_edge_length_km = 100
    
    def __init__(self, value, latitude, length):
        self.value = value 
        self.latitude = latitude
        self.length = length 
        self.neighbours = [] 
        self.weights = []


    def search_neighbours(self, graph):
        """ Search all self vertex neighbours  and determine  
            weight between self vertex and rest of vertices. 
            Weight is equal to  distance between two users. 
            If  distance between two user is less or equal
            to max edge length in kilometres, edge does not exist in other 
            words, conexion between two user not exist."""

        for vertex in graph.verteces: #O(V)
            if vertex.value == self.value:
                print('A vertex must not be its own neighbor')
            else:
                weight = self.calculate_weight(vertex)
                self.weights.append((vertex.value, weight))
                vertex.weights.append((self.value, weight))
                if weight <= self.max_edge_length_km:
                    self.neighbours.append(vertex)



    def calculate_weight(self, vertex):
        """Calculate the distance between two users 
           and establish as weight"""
        lat1 = float(self.latitude)
        lon1 = float(self.length)
        lat2 = float(vertex.latitude)
        lon2 = float(vertex.length)
        return utils.haversine(lat1,lon1,lat2,lon2)


    def update_graph(self):
        """When a new vertex is created, all its neighbours
           have to update its adjacency list"""
        for element in self.neighbours:
            element.neighbours.append(self)
            print('Graph update  successful')