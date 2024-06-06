import numpy as np
import networkx as nx
from scipy.sparse import dia_matrix, kron
import scipy
from scipy import sparse
from apgl.graph.VertexList import VertexList
from apgl.graph.SparseGraph import SparseGraph
from apgl.generator.KroneckerGenerator import KroneckerGenerator
import unittest

# Basic sparse kronecker product
A = sparse.csr_matrix(np.array([[0, 2], [5, 0]]))
B = sparse.csr_matrix(np.array([[1, 2], [3, 4]]))
sparse.kron(A, B).toarray() 
sparse.kron(A, B).todense() 

# Construct a 1000x1000 lil_matrix 
from scipy.sparse import lil_matrix
from numpy.random import rand
A1 = lil_matrix((100, 100))
A1[0, :10] = rand(10)
A1[1, 10:20] = A1[0, :10]
A1.setdiag(rand(100))
# converting in CSR format
A1 = A1.tocsr()
 
 # Construct anther matrix  
B1 = lil_matrix((100, 100))
B1[0, :10] = rand(10)
B1[1, 10:20] = B1[0, :10]
B1.setdiag(rand(100))
# converting in CSR forma
B1 = B1.tocsr()
 
 # Sparse kronecker product
C1 = sparse.kron(A1, B1).toarray() 

#sparse kronecker sum 
C2 = sparse.kronsum(A1,B1).toarray()

# Sparse Kronecker product diagonal matrix
def populatematrix1(dim):
    return dia_matrix( (np.array( [np.array([2]*5),np.array([1]*5), np.array([1]*5)] ),np.array([0,1,-1]) ),shape=(5,5))
def populatematrix2(dim):
    return dia_matrix( (np.array( [np.array([2]*5),np.array([1]*5), np.array([1]*5)] ),np.array([0,1,-1]) ),shape=(5,5))

dx = np.linspace(0,1,5)
x = populatematrix1(len(dx))
print (x.shape, type(x))
y = populatematrix2(len(dx))
print (y.shape, type(y))
z = kron(x,y)
print (z.shape)

# Generating simple graph

numVertices = 5000

weightMatrix = scipy.sparse.lil_matrix((numVertices, numVertices))
graph = SparseGraph(numVertices, W=weightMatrix)
graph[0, 1] = 1
graph[0, 2] = 1

#Output the number of vertices
print(graph.size)

# PLotting Graph
a = np.reshape(np.random.random_integers(0,1,size=100),(10,10))
G= nx.DiGraph(a)
#nx.draw(G)

# Computing Matrix Exponetaial 

Mat_Exp = scipy.linalg.expm(a, q=None)
print('debug')
# Outputsum of all elements

Sum = np.sum(Mat_Exp)
Cul_Sum = np.cumsum(Mat_Exp)



# Other Know method from different authors.
# generating graph

class KroneckerGenerator(object):
    '''
    A class which generates graphs according to the Kronecker method.
    '''
    def __init__(self, initialGraph, k):
        """
        Initialise with a starting graph, and number of iterations k. Note that
        the starting graph must have self edges on every vertex. Only the
        adjacency matrix of the starting graph is used. 
 
        :param initialGraph: The intial graph to use.
        :type initialGraph: :class:`apgl.graph.AbstractMatrixGraph`
 
        :param k: The number of iterations.
        :type k: :class:`int`
        """
        Parameter.checkInt(k, 1, float('inf'))
        
        W = initialGraph.getWeightMatrix()
        if (np.diag(W)==np.zeros(W.shape[0])).any():
            raise ValueError("Initial graph must have all self-edges")
 
        self.initialGraph = initialGraph
        self.k = k
 
    def setK(self, k):
        """
        Set the number of iterations k.
 
        :param k: The number of iterations.
        :type k: :class:`int`
        """
        Parameter.checkInt(k, 1, float('inf'))
        self.k = k 
 
    def generate(self):
        """
        Generate a Kronecker graph using the adjacency matrix of the input graph.
 
        :returns: The generate graph as a SparseGraph object.
        """
        W = self.initialGraph.adjacencyMatrix()
        Wi = W
 
        for i in range(1, self.k):
            Wi = np.kron(Wi, W)
 
        vList = VertexList(Wi.shape[0], 0)
        graph = SparseGraph(vList, self.initialGraph.isUndirected())
        graph.setWeightMatrix(Wi)
 
        return graph
        
class KroneckerGeneratorTest(unittest.TestCase):
    def setUp(self):
        pass
  
    def testGenerate(self):
        k = 2
        numVertices = 1000
        numFeatures = 0
  
        vList = VertexList(numVertices, numFeatures)
        initialGraph = SparseGraph(vList)
        initialGraph.addEdge(0, 1)
        initialGraph.addEdge(1, 2)
  
        for i in range(numVertices):
            initialGraph.addEdge(i, i)
  
        generator = KroneckerGenerator(initialGraph, k)
  
        graph = generator.generate()
        print (graph.size)
