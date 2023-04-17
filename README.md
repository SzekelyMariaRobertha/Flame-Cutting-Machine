# Flame Cutting Machine
This project simulates the movement of the cutting head on the computer screen.


## Requirements
PyCharm

## Usage
Simulating a flame cutting machine can be useful for various reasons. For example, by simulating a flame cutting machine, you can validate the design and functionality of the machine before investing in building a physical prototype. More than that, you can use the simulation to test the safety features of the machine and identify potential hazards and risks. However, the most importanta reason is that the simulation can also help you optimize the machine's performance. 
The program reads a file that contains the cutting trajectory (sequence of segments and arcs of a circle - coordinates) and generates commands for moving the cutting head in two directions (X and Y).

The user can enter different coordinates into the input file to create different models (their outline) and view the result on the screen. 
A segment will be determined by four parameters: two for the start point and two for the end point. Thus, a circular arc will be determined by two coordinates that represent the starting point of the circular arc, by two other coordinates that represent the final point of the circular arc, a value that constitutes the radius of the circular arc and the last value that represents the opening of the circular arc.

The application uses the OpenCV and Turtle libraries to reproduce the cutting process as realistically as possible.

## Visuals
![Picture1](https://user-images.githubusercontent.com/93877610/232517077-3e242402-9784-4f14-93ae-c96a4d298575.png)
![Picture2](https://user-images.githubusercontent.com/93877610/232517088-60f69471-1a72-40b3-a88d-67db86356e08.png)
