import numpy as np


class Problem:
    def __init__(self):
        self.mesh = np.array([
            [1, 1,  2, 3],
            [1, 0.5,0, 4],
            [2, 0,  0, 5],
            [3, 4,  5, 5]
        ])
        self.tol = 1.0e-9
        self.maxIts = 50
    def FDM(self):
        sol = self.mesh
        prev = self.mesh.copy()
        
        row, col = self.mesh.shape
        
        relativeError = 5
        for its in range(self.maxIts):
            if (relativeError > self.tol):
                for i in range(row):
                    for j in range(col):
                        if (i == 0 or i == 3):
                            if (j == 0 or j == 3):
                                pass
                        elif (j == 0 or j == 3):
                            if (i ==0 or i == 3):
                                pass
                        else:
                            sol[i,j] = 0.25*(sol[i+1, j] + sol[i-1,j] + sol[i,j+1] + sol[i,j-1])
                            relativeError = ( sol[i,j] - prev[i,j] ) / sol[i,j]
                            print (its, sol[i,j], prev[i,j], relativeError)
                            prev[i,j] = sol[i,j]
            else:
                break
        return sol

def main():
    laplace = Problem()
    solution = laplace.FDM()
    print (solution)


if __name__ == "__main__": main()

