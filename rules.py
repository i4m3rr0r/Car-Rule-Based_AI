''' Defining the rules as a list of dictionaries so I can have key:value pairings '''

''' List of rules, started with the highest priority one, going to more specific '''
RULES = [
    {'name': 'R1 Unsafe', 'if': {'safety': ['low']}, 'then': 'unacc'},
    
    {'name': 'R2 Not enough seats', 'if': {'persons': ['2']}, 'then':'unacc'}, 
    
    {'name': 'R3 Very high maintenance cost, high or very high buying price', 'if': {'maint': ['vhigh'], 'buying': ['vhigh', 'high']}, 'then':'unacc'},
    
    {'name': 'R4 High maintenance cost, very high price', 'if': {'maint': ['high'], 'buying': ['vhigh']}, 'then':'unacc'},
    
    {'name': 'R5 High or very high buying cost, small boot, medium safety', 'if': {'buying': ['vhigh', 'high'], 'lug_boot': ['small'], 'safety': ['med']}, 'then':'unacc'},
    
    {'name': 'R6 Very high maintenance cost, small boot, medium safety', 'if': {'maint': ['vhigh'], 'lug_boot': ['small'], 'safety': ['med']}, 'then':'unacc'},
    
    {'name': 'R7 Low or medium Costs, big boot, high safety', 'if': {'buying': ['med', 'low'], 'maint': ['med', 'low'], 'lug_boot': ['big'], 'safety': ['high']}, 'then': 'vgood'},
    
    {'name': 'R8 Low buying price, high maintenance, big boot and high safety', 'if': {'buying': ['low'], 'maint': ['high'], 'lug_boot': ['big'], 'safety': ['high']}, 'then': 'vgood'},
    
    {'name': 'R9 Low or medium costs, medium boot, high safety and 4+ doors', 'if': {'buying': ['med', 'low'], 'maint': ['med', 'low'], 'lug_boot': ['med'], 'safety': ['high'], 'doors': ['4', '5more']}, 'then': 'vgood'},
    
    {'name': 'R10 Low or medium costs, medium boot, 3 doors, seats more than 4, high safety', 'if': {'buying': ['med', 'low'], 'maint': ['med', 'low'], 'lug_boot': ['med'], 'safety': ['high'], 'doors': ['3'], 'persons': ['more']}, 'then': 'vgood'},
    
    {'name': 'R11 Medium costs', 'if': {'buying': ['med'], 'maint': ['med']}, 'then': 'acc'},
    
    {'name': 'R12 Low or medium costs, big boot, medium safety', 'if': {'buying': ['med', 'low'], 'maint': ['med', 'low'], 'lug_boot': ['big'], 'safety': ['med']}, 'then': 'good'},
    
    {'name': 'R13 Low or medium costs, medium boot, high safety', 'if': {'buying': ['med', 'low'], 'maint':['med', 'low'], 'lug_boot': ['med'], 'safety': ['high']}, 'then': 'good'},
    
    {'name': 'R14 2 doors, seats more than 4, small boot', 'if': {'doors': ['2'], 'persons': ['more'], 'lug_boot': ['small']}, 'then': 'unacc'},
    
    {'name': 'R15 Low or medium costs, small boot, high safety', 'if': {'buying': ['med', 'low'], 'maint': ['med', 'low'], 'lug_boot': ['small'], 'safety': ['high']}, 'then': 'good'},
    
    {'name': 'R16 Low or medium costs, medium boot, medium safety, 4+ doors', 'if': {'buying': ['med', 'low'], 'maint': ['med', 'low'], 'lug_boot': ['med'], 'safety': ['med'], 'doors': ['4', '5more']}, 'then': 'good'},
    
    {'name': 'R17 Low or medium costs, medium boot, medium safety, 3 doors, seats more than 4', 'if': {'buying': ['med', 'low'], 'maint': ['med', 'low'], 'lug_boot': ['med'], 'safety': ['med'], 'doors': ['3'], 'persons': ['more']}, 'then': 'good'}
    
]

DEFAULT = 'acc'

''' Matching the rules to the car '''
def ruleMatches(car, conditions):
    for feature, allowed in conditions.items():
        if car[feature] not in allowed:
            return False
    
    return True

''' Iterate through rules to classify '''
def classify(car):
    for rule in RULES:
        if ruleMatches(car, rule['if']):
            return rule['then'], rule['name']
    return DEFAULT, 'default'

 

