import pandas as pd

# Function to check accuracy of ai

def evaluateAccuracy(actual, predicted):
    correct = 0
    
    for x in range(0, len(actual)):
        if actual[x] == predicted[x]:
            correct += 1
    
    accuracy = (correct / len(actual)) * 100
    
    return accuracy


# Confusion matrix helps visualise 
def createConfusionMatrix(actual, predicted, classes):
    
    matrix = pd.crosstab(actual, predicted, rownames=['actual'], colnames=['predicted'])
    matrix = matrix.reindex(index = classes, columns = classes, fill_value=0)
    
    return matrix


# Developed with help from Claude {Anthropic}.
# Prompt: 'help me write a function to calculate precision, recall and F1 for each class from the confusion matrix

def classMetrics(matrix, classes):
    """Work out precision, recall and F1 for each class from the confusion matrix."""
    results = []

    for cls in classes:
        correct = matrix.loc[cls, cls]       # diagonal: said cls and was right
        saidIt = matrix[cls].sum()           # column total: every time the system said cls
        reallyIs = matrix.loc[cls].sum()     # row total: every car that really is cls

        # Check for zero first, so classes that are never predicted don't crash it
        precision = correct / saidIt if saidIt > 0 else 0
        recall = correct / reallyIs if reallyIs > 0 else 0

        if precision + recall > 0:
            f1 = 2 * precision * recall / (precision + recall)
        else:
            f1 = 0

        results.append({'class': cls, 'precision': precision, 'recall': recall, 'f1': f1})

    return pd.DataFrame(results).set_index('class')