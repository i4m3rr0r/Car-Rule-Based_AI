# Car Evaluation: Rule-Based AI - CPU5006 Artificial Intelligence, Assessment S1.

A rule-based system that rates how acceptable a car is to a buyer (**unacc**, **acc**, **good** or **vgood**) from six attributes: buying price, maintenance cost, number of doors, passenger capacity, boot size and safety.

Every decision is made by an explicit IF–THEN rule, so the system can always say why a car got its rating.


## How to run

Requires Python 3.10 or later.

```
pip install -r requirements.txt
python main.py
```

This prints the results for the baseline and for the rule-based system: accuracy, a confusion matrix, precision/recall/F1 for each class, and macro-F1. It then prints the rule coverage; how many cars each rule handled.

## Dataset

The UCI Car Evaluation dataset, which I've included in `data/` in its original format.

- 1,728 cars: every possible combination of the six attributes, appearing once each

`car.data` has no header row, so it is loaded with `header=None` and the column names are supplied from `car.names`.

## How it works

The system is split into a **knowledge base** and an **inference engine**:

- **knowledge base** (`RULES` in `rules.py`): 17 rules stored as data. Each rule has a name, its conditions and its result.
  - Conditions on different attributes must all be true (AND).
  - Several values listed for one attribute means any of them is fine (OR).
- **Inference engine** (`ruleMatches` and `classify` in `rules.py`): checks the rules in order and the **first rule that matches decides the class**. If no rule matches, the car is rated **acc**.

The rules are structured as follows:

1. **R1–R6:** deal-breakers (unacc)
2. **R7–R10:** very good cars (vgood)
3. **R11:** both costs medium (acc)
4. **R12–R17:** good cars (good), with one further deal-breaker (R14) placed before the rule it protects

## Results

**Baseline** (always unacc) :
- Accuracy: 70%
- Macro-F1: 0.21

**Rule-based System** :
- Accuracy: 97.8%
- Macro-F1: 0.97

**Individual F1s**:
unacc: 0.99
acc: 0.95
good: 1.00
vgood: 0.96

All remaining mistakes are cars rated **acc** (the default) that are really unacc (33) or vgood (5). The system never rejects an acceptable car, never rates a car good or vgood when it isn't, and never confuses the extremes: no unacceptable car is rated good or vgood, and no good or vgood car is rejected.

## Files

**main.py** Loads the data, runs the baseline and the rule-based system, prints the results 
**rules.py** The knowledge base (rules) and inference engine 
**baseline.py** Baseline classifier: always predicts the most common class 
**accuracy.py** Accuracy, confusion matrix, and precision/recall/F1 
**data/** The original dataset files 
**notes.md** Development notes: version history and how each rules were found 

