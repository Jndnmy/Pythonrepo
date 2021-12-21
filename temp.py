

def EucliedanDist(v1, v2):
    dist = 0.0
    for i in range(len(v1)):
        dist += abs(v1[i] - v2[i])**2
    return dist**(1.0/2)

class Animal(object):
    def __init__(self, name, features):
        self.name = name
        self.features = pylab.array(features)
        
    def getName(self):
        return self.name
    
    def getFeatures(self):
        return self.features
    
    def distance(self, other):
        return EucliedanDist(self.getFeatures(), other.getFeatures())
    
import pylab

def compareAnimals(animals, precision):
    #Get labels for columns and rows
    columnLabels = []
    for a in animals:
        columnLabels.append(a.getName())
    rowLabels = columnLabels[:]
    tableVals = []
    #Get distances between pairs of animals
    #For each row
    for a1 in animals:
        row = []
        #For each column
        for a2 in animals:
            if a1 == a2:
                row.append('--')
            else:
                distance = a1.distance(a2)
                row.append(str(round(distance, precision)))
        tableVals.append(row)
    pylab.figure(figsize=(15,5))
    #Produce table
    table = pylab.table(rowLabels = rowLabels,
                        colLabels = columnLabels,
                        cellText = tableVals,
                        cellLoc = 'center',
                        loc = 'center',
                        colWidths = [0.15]*len(animals))
    
    table.scale(1, 4)
    table.set_fontsize(14)
    pylab.title('Eucliedan Distance Between Animals')
    pylab.show()
    
rattlesnake = Animal('rattlesnake', [1,1,1,1,0])
boa = Animal('boa', [0,1,0,1,0])
frog = Animal('frog', [1,0,1,0,1])

rattlesnake = Animal('rattlesnake', [1,1,1,1,0])
boa = Animal('boa', [0,1,0,1,0])
frog = Animal('frog', [1,0,1,0,1])

animals= (rattlesnake,boa,frog)

compareAnimals(animals,2)