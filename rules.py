#defining the rules as a list of dictionaries so I can have key:value pairings.

RULES = [
    {'name': 'R1 Unsafe', 'if': {'safety': ['low']}, 'then': 'unacc'},
    {'name': 'R2 Not enough seats', 'if': {'persons': ['2']}, 'then':'unacc'} 
]

DEFAULT = 'acc'

#Matching the rules to the car
def ruleMatches(car, conditions):
    for feature, allowed in conditions.items():
        if car[feature] not in allowed:
            return False
    
    return True


def classify(car):
    for rule in RULES:
        if ruleMatches(car, rule['if']):
            return rule['then'], rule['name']
    return DEFAULT, 'default'

 
testCar = {"buying": "low", "maint": "low", "doors": "4",
            "persons": "2", "lug_boot": "big", "safety": "high"}


print(classify(testCar))

