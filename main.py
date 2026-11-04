#Loads the car evaluation dataset, and creates a summary
import pandas as pd

from baseline import baselineClassify 

from accuracy import *

from rules import *

#Defining columns as a constant
COLUMNS = ['buying', 'maint', 'doors', 'persons', 'lug_boot', 'safety', 'classification']

#Class values as constants for the confusion matrix
CLASSIFICATION_VALUES = ['unacc', 'acc', 'good', 'vgood']

#Data file has no headers, so here we load the file and initialise column names ourselves
def loadData(path):
    #Read car data into pandas
    
    return pd.read_csv(path, header = None, names=COLUMNS)

def carsSummary(cars):
    #rows + columns count
    print("Shape: ", cars.shape)
        
    #print first five
    print(cars.head())
        
    #how many in each class
    print(cars["classification"].value_counts())
        
    #check how class corresponds to safety (as one example)
    print(pd.crosstab(cars["safety"], cars["classification"]))
    

if __name__ == '__main__':
    
    cars = loadData("data/car.data")
    
    #carsSummary(cars)
    
    #two lists, one to hold the ai's predictions, one to be the actual classes
    rulePredictions = []
    rulesMatched = []   
    actualClassifications = []
    
    for _, carRow in cars.iterrows():  
        
        # Append actual classifications to list
        actualClassifications.append(carRow['classification'])
        
        #append the Ais classifications to a new list
        classification, ruleName = classify(carRow)
        
        rulePredictions.append(classification)
        
        rulesMatched.append(ruleName)
    
    accuracy = evaluateAccuracy(actualClassifications, rulePredictions)
    
    print(f'The accuracy of this test is {accuracy:.1f}%')
    
    matrix = createConfusionMatrix(actualClassifications, rulePredictions, CLASSIFICATION_VALUES)
    
    print(matrix)
    
    