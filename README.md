## Factory Demo

This repo illustrates two creational design patterns from the Gang of Four patterns: Factory and Singleton. 
The example is based on [https://refactoring.guru/design-patterns/creational-patterns](https://refactoring.guru/design-patterns/creational-patterns).

## Factory Pattern

Please read [https://refactoring.guru/design-patterns/factory-method](https://refactoring.guru/design-patterns/factory-method) for the problem context. You basically have a logistics app that used trucks to transport goods. Now, you want to also add sea ships as a method of transportation. 

## What's in this demo

- The [main branch](https://github.com/snadi-teaching/StructuralPatterns-Python) has the base code without applying any design pattern
- The [snadi/uglycode branch](https://github.com/snadi-teaching/StructuralPatterns-Python/tree/snadi/uglycode) shows an example of patching in the extra ship logic without thinking of commonalities and design patterns. For this small example, it might not be that obvious that this is ugly/not extensible but imagine you have more shipping methods and each has its own complicated logic etc.
- The [snadi/factory branch](https://github.com/snadi-teaching/StructuralPatterns-Python/tree/snadi/factory) has an example of changing this code to use factory pattern


Before looking at the other branches, we advise you to first look at the base code and try to think of how you can redesign this code to be more extensible. For example, what if there's sea shipping and air shipping in the future?

You can switch between the branches by using `git checkout <name of the branch>`

## How to run the code

### Requirements

- Python 3.9+ recommended

### To run the code

```
cd logistics
python main.py
```

