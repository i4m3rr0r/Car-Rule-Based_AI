#defining the rules as a list of dictionaries so I can have key:value pairings.

RULES = [
    {'name': 'R1 Unsafe', 'if': {'safety': ['low']}, 'then': 'unacc'},
    {'name': 'R2 Not enough seats', 'if': {'persons': ['2']}, 'then':'unacc'}, 
    {'name': 'R3 Very high maintenance with high or very high buying price', 'if': {'maint': ['vhigh'], 'buying': ['vhigh', 'high']}, 'then':'unacc'},
    {'name': 'R4 High maintenence with very high price', 'if': {'maint': ['high'], 'buying': ['vhigh']}, 'then':'unacc'},
    {'name': 'R5 High or very high buying cost, lug boot is too small, and safety is medium', 'if': {'buying': ['vhigh', 'high'], 'lug_boot': ['small'], 'safety': ['med']}, 'then':'unacc'},
    {'name': 'R6 Very high maintenance cost, lug boot is too small, and safety is medium', 'if': {'maint': ['vhigh'], 'lug_boot': ['small'], 'safety': ['med']}, 'then':'unacc'},
    {'name': 'R7 Vgood car', 'if': {'buying': ['med', 'low'], 'maint': ['med', 'low'], 'lug_boot': ['big'], 'safety': ['high']}, 'then': 'vgood'},
    {'name': 'R8 Cheap to buy, high maintenance, big boot and high safety', 'if': {'buying': ['low'], 'maint': ['high'], 'lug_boot': ['big'], 'safety': ['high']}, 'then': 'vgood'},
    {'name': 'R9 Low or medium costs, medium boot, high safety and 4+ doors', 'if': {'buying': ['med', 'low'], 'maint': ['med', 'low'], 'lug_boot': ['med'], 'safety': ['high'], 'doors': ['4', '5more']}, 'then': 'vgood'},
    {'name': 'R10 Low or medium costs, medium boot, 3 doors, seats more than 4, high safety', 'if': {'buying': ['med', 'low'], 'maint': ['med', 'low'], 'lug_boot': ['med'], 'safety': ['high'], 'doors': ['3'], 'persons': ['more']}, 'then': 'vgood'}
    
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

 

