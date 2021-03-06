class AdjacentMatrix:
    UNIDIRECTIONAL = 0
    BIODIRECTIONAL = 1
    def __init__(self, numberOfEdges, type=UNIDIRECTIONAL):
        '''

        :param numberOfEdges: is the number of the matrix.
        :param type: whether AdjacentMatrix.UNIDIRECTIONAL or AdjacentMatrix.BIODIRECTIONAL which are expressive enough.
        '''
        self._Matrix = [[0 for x in range(numberOfEdges)] for y in range(numberOfEdges)]
        self._type = type

    def getMatrix(self):
        '''
        this function is responsible for printing the whole matrix in a readable way.
        :return: void
        '''
        for i, item in enumerate(self._Matrix):
            print(self._Matrix[i])

    def setPath(self, fromNode, toNode, weight=1):
        '''

        :param fromNode: from node
        :param toNode: to node
        :param weight: weight of the edge
        :return: void
        '''
        if self._type == AdjacentMatrix.UNIDIRECTIONAL:
            if fromNode != toNode:
                self._Matrix[fromNode][toNode] = weight
            else:
                raise ValueError("UniDirectional Adjacent Matrix should have different <FROM> <TO> node values")

        elif self._type == AdjacentMatrix.BIODIRECTIONAL:
            self._Matrix[fromNode][toNode] = weight
            self._Matrix[toNode][fromNode] = weight

if __name__ == '__main__':
    adjMat = AdjacentMatrix(5, AdjacentMatrix.UNIDIRECTIONAL)
    # adjMat.setPath(1, 1)
    adjMat.setPath(2, 4, weight=2)
    adjMat.getMatrix()
