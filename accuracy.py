import pandas as pd
#function to check accuracy of ai

def evaluateAccuracy(actual, predicted):
    correct = 0
    
    for x in range(0, len(actual)):
        if actual[x] == predicted[x]:
            correct += 1
    
    accuracy = (correct / len(actual)) * 100
    
    return accuracy


#confusion matrix helps visualise 
def createConfusionMatrix(actual, predicted, classes):
    
    matrix = pd.crosstab(actual, predicted, rownames=['actual'], colnames=['predicted'])
    matrix = matrix.reindex(index = classes, columns = classes, fill_value=0)
    
    return matrix