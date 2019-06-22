This is a project I have started as a hobby. Mostly to apply what I have learned through online courses and other resources. If you have any suggestions feel free to contact me at ozgeyoluk_at_proteinart.net.

** Current status : ** Creating the structure of the code and deciding on what parameters should be supplied, what test cases should be written before writing the code. The first steps.

# GOAL
Being able to plot motions of animals through line graphs in a GUI. The idea is that features of an animal will be chosen and a series of simple line graphs will be generated to display a motion based on those features. While the graphs are animated, equations will be displayed next to the lines. Extra equations could be entered to add details to the animal. 
The functions will also be available as a python package (if it provides an advantage some functionality might be written as a C, C++ library). This project could be modifed and used in teaching kids equations as well as a tutorial for PyQT, cython, python.

# MILESTONES
The following steps are defined to highligh the challanges and checkpoints. At each checkpoint a code review will take place to ensure that the written code is at the optimum level for the next point. Doing the job is not enough, the job must be well done. The steps might be modified is at any point an improvement is identified.

## CORE FUNCTIONS
- Test cases to compare the results of the functions.
- Function to handle polynomials. Use Horner's method.
- Function to plot the polynomial and return a graph image.
- There should be an efficient way to get points from these functions, so that they can used to connect the lines from user added extra functions.
- Identification of parameters:
  - Classification of animal features (wings, number of legs, tail , etc.).
  - Determine the best function to plot each feature (this will be hard coded) and create a class to accept parameters for the functions.
  - Pick the easisest and the hardest feature for moving futher.

### 1. Code review: 
Go through the functions, thinking about the structure of the GUI as well. Add/remove/modify according to what will be the user input, how do we make a tail appear connected to the body line?. At this stage, I assume one feature selection by the user, however for creativiy multiple selections could be allowed. A winged cat would be fun to see. Altough I may not make this work, modify to code to handle multiple feature selections as much as possible. This way we don't need to rewrite the program entirely. 

## PLOTTING AN ANIMATED GRAPH
- Decide on the library to create the graphs. Identify the allowed plotting area for early tests, use (0,0) as the origin (This could be scaled up or down later on, origin for features could be flexible.)
- Using the easiest feature, plot a single graph. If correct, plot multiple graphs.
- Turn the graph into a gif. 
- Repeat the above process with the hardest feature.

### 2. Code review:
This code review process will be done while creating a tutorial for the code. Create a jupyter notebook. Explain the input and output at each step, how to use it.

## CREATE THE GUI
- Create a simple GUI with PyQt that accepts a feature, and displays the gif created. As of 2019.06.22 I am thinking this should work as a standalone GUI. However I should consider whether I want to host this on a server. If I am to host this, I cannot work with PyQt. Javascript will be the way to go. 

### 3. Code review:
- Optimize the code for GUI to accept multiple features. Create a user manual. 

## EXTRA FUNCTIONS GUI SUPPORT
Add the support for extra functions from GUI. User will have to select to which feature they want those function to be connected to. Having a tail at the head is not beyond imagination. 

# TEST RELEASE
Alpha release in a foreseeable future. 



