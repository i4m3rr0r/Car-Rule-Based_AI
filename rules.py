#defining the rules as a list of dictionaries so I can have key:value pairings.

RULES = [
    {'name': 'R1 Unsafe', 'if': {'safety': ['low']}, 'then': 'unacc'},
    {'name': 'R2 Not enough seats', 'if': {'persons': ['2']}, 'then':'unacc'} 
]

#Matching the rules to the car
def ruleMatches(car, conditions):
    for feature, allowed in conditions.items():
        if car[feature] not in allowed:
            return False
    
    return True


testCar = {"buying": "low", "maint": "low", "doors": "4",
            "persons": "4", "lug_boot": "big", "safety": "low"}


print(ruleMatches(testCar, RULES[0]['if']))
print(ruleMatches(testCar, RULES[1]['if']))
