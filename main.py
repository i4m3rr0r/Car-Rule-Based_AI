#Loads the car evaluation dataset, and creates a summary
import pandas as pd


#Data file has no headers, so here we load the file and initialise column names ourselves
def loadData(path):
    #Read car data into pandas
    
    return pd.read_csv(path, header = None, names=['buying', 'maint', 'doors', 'persons', 'lug_boot', 'safety', 'classification'])

if __name__ == '__main__':
    cars = loadData("data/car.data")
    
    #rows + columns count
    print("Shape: ", cars.shape)
    
    #print first five
    print(cars.head())
    
    #how many in each class
    print(cars["classification"].value_counts())
    
    #check how class corresponds to safety (as one example)
    print(pd.crosstab(cars["safety"], cars["classification"]))
    
    