# Runs the baseline and rule-based system on the car dataset and prints the results

import pandas as pd

from baseline import baselineClassify 

from accuracy import evaluateAccuracy, createConfusionMatrix, classMetrics

from rules import classify

# Defining columns as a constant
COLUMNS = ['buying', 'maint', 'doors', 'persons', 'lug_boot', 'safety', 'classification']

# Class values as constants for the confusion matrix
CLASSIFICATION_VALUES = ['unacc', 'acc', 'good', 'vgood']

# Data file has no headers, so here we load the file and initialise column names ourselves
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
    

def printResults(name, actual, predicted):
    """Print accuracy, confusion matrix and per-class metrics for one system."""
    print(f'\n===== {name} =====')
    accuracy = evaluateAccuracy(actual, predicted)
    print(f'Accuracy: {accuracy:.1f}%')
    matrix = createConfusionMatrix(actual, predicted, CLASSIFICATION_VALUES)
    print(matrix)
    metrics = classMetrics(matrix, CLASSIFICATION_VALUES)
    print(metrics.round(2))
    print(f"Macro-F1: {metrics['f1'].mean():.2f}")

def analyseMistakes(cars, predictions, actualClass, predictedClass='acc'):
    # Improved with help from Claude (Anthropic)
    # Prompt: Help me with creating function that shows what the incorrect classifications have in common. 
    
    """Show what the cars the system gets wrong have in common.
    Example: actualClass='vgood' looks at vgood cars that were wrongly predicted as acc."""
    mistakes = cars[(cars['classification'] == actualClass) & (pd.Series(predictions) == predictedClass)]

    print(f'\n===== {len(mistakes)} {actualClass} cars predicted as {predictedClass} =====')
    for feature in COLUMNS[:-1]:          # every column except 'classification'
        print()
        print(mistakes[feature].value_counts().to_string())

if __name__ == '__main__':
    
    cars = loadData("data/car.data")
    
    #carsSummary(cars)
    
    #four lists, one to hold baseline prediction,  one for the ai's predictions, one for the name of the rule triggered, and one to be the actual classes
    baselinePredictions = []
    rulePredictions = []
    rulesMatched = []   
    actualClassifications = []
    
    for _, carRow in cars.iterrows():  
        
        # Append actual classifications to list
        actualClassifications.append(carRow['classification'])
        
        # Make baseline predictions
        baselinePredictions.append(baselineClassify(carRow))
        
        #append the Ais classifications to a new list
        classification, ruleName = classify(carRow)
        
        rulePredictions.append(classification)
        
        rulesMatched.append(ruleName)
    
    
    printResults('Baseline (always unacc)', actualClassifications, baselinePredictions)
    printResults('Rule-based system', actualClassifications, rulePredictions)
    
    # Used during development to find new rules, e.g 5 vgood cars still missed:
    # analyseMistakes(cars, rulePredictions, 'vgood')
    
    
    #Developed with help from Clause (Anthropic).
    # Prompt: how do I see how many cars each rule handles
    # Rule coverage: how many cars each rule handled, and their real classes
     
    print('\n===== Rule coverage =====')
    print(pd.crosstab(pd.Series(rulesMatched, name='rule'),
                      pd.Series(actualClassifications, name='actual')))
    
    
    
    