# ds_dataset_exploration

## What is it?
Python package providing data science exploration tools for relational datasets. It aims to be a fundamental research block for doing efficient and practical dataset exploration.

## Current Exploration Features
Here are just a few of the things that this package contains:

  - Ground Truth representation validation.

## Where to get it
The source code is currently hosted on GitHub at:
https://github.com/amitBotzer/ds_dataset_exploration

## Main Dependencies
- [scikit-learn](https://github.com/scikit-learn/scikit-learn)
- [pandas](https://github.com/pandas-dev/pandas)
- [pyspark](https://github.com/apache/spark/tree/master/python/pyspark)

## Discussion and Development
Most development discussion is taking place on github in this repo.

## Project Building Blocks

### DS Dataset
This is an encapsulating object for datasets. It defines conventions for datasets scheme and consequently allows us to apply many useful actions on it. There's a main interface from which different types of DSDataSets can inherit.

### Exploration Concepts
For each exploration concept (such as features correlation, clustering, etc) there's a different directory. Each directory contains a module for each possible method, and a factory class that allows other modules to create exploration insatnces more easily.

### Reports
A report is simply a module that takes DS dataset as a parameter, perform several explorations on it and returns the results. The reports directory is the place to define different reports. We might like to run different explorations given different kinds of datasets, so new report modules can be added easily.

### Tests
Each and every computational module (exploration methods, reports, dataset implementations) should have a corresponding test module. The tests modules are based on the python built-in unittest module.

## Contributing

All contributions, bug reports, bug fixes, documentation improvements, enhancements and ideas are welcome.

### There are few ways to contribute:

#### Documentation
The best way to start is documenting code. There's always code which is ill-documented and it is the best way to understand the project structure. Documentation should also be done on dedicated branch and not on the master branch directly.

#### Fixing Bugs
Facing new bug in the library, first thing to do is to write corresponding test case (if there isn't already) that is failing. Proper bug fixing will make the new test case run correctly while all other test cases stay OK. Bug fixes should be done on a dedicated branch with the name format "bug/<name>".

#### Adding novel methods for old exploration concepts
Say you read about a novel visualization algorithm and you would like to make it a standard or at least an option for other researchers. First you should git checkout a new branch such as "feature/X_new_visulaization_algorithm". Then, on the corresponding exploration concept directory, create a new implementation for the existing interface. Add the new option to the factory module in the same directory and make sure you cover yourself with proper test module. Lastly, update or create reports modules so the new method will be part of your whole exploration.

#### Adding novel exploration concepts
Say you find a new whole concpet of dataset analysis. First you should git checkout a new branch such as "feature/X".
Then you create a new directory that will represent the new concept. Adding an interface, the specific implementation and a factory module will turn this new concept usable in the future. Create a corresponding "test_X" directory under the main tests directory and add test cases that cover your new code. Lastly, update or create reports modules so the new concept will be part of your whole exploration.
