# eYRC 2020-21: Vitaraṇa Drone (VD)
## eYRC:VD#1993
Suryadevara Sai Aneesh  
Shubham Lohiya    
Harshit Gupta   
Jay Sonawane  
## Problem Statement
In urban streets, especially South Asian streets, clogged with automobiles, people, animals and markets, using typical modes of transport for delivery, such as cars and bikes, is slow and time consuming. Fortunately, enabled by progress in embedded systems, materials science and control systems, unmanned aerial vehicles (UAVs), have become widespread in the past couple of decades and provide a simpler and faster alternative to using terrestrial infrastructure!<br>

These UAVs are a result of improvements in semiconductor and microprocessor technology, enabling faster chips and smaller, more efficient, power electronics. Improvements in materials sciences & manufacturing have led to the creation of novel, cheap, precise & robust sensors, along with huge improvements in battery technology. There have been wide-ranging developments in the domain of control systems powering the algorithms that run onboard as well as the techniques that power these motors. All of this has created a virtuous feedback loop of improvements, driven by widespread commercialization in both hobby and industrial spheres. UAVs now range from quadcopters smaller than a child’s palm, to large airplanes that can fly for days, while being commanded from thousands of kilometres away.<br>

This project works on concepts of <b>control systems, path planning, image processing and algorithm development.</b><br>

Tools such as the <b>Robot Operating System, robotics simulator Gazebo, the Python programming language</b> and many of its libraries are used.<br>

The competition consists of series of tasks, the final problem statement for the drone is to deliver various packages to their destinations, optimizing for time and quantity.<br>

# TASK 0
## Problem Statement
The objective of the task is to move the turtle inside the turtlesim window in a circle and stop at its initial location.
Teams are supposed to do this by creating a nodes name, /node_turtle_revolve within a python script, node_turtle_revolve.py.<br>

To run use:

```python
roslaunch pkg_task0 task0.launch record:=true rec_name:=my_turtle.bag

```
# TASK 1
## Problem Statement
The aim of this task is to design controllers which will control the eDrone's orientation as well as position in Gazebo environment.<br>
The Task 1 is divided into 2 sub tasks<br>
- Task 1A - Designing attitude controller for the eDrone<br>
- Task 1B - Designing position controller for the eDrone<br>

## Position Controller
The main task of position controller is to give the required drone orientation to reach to the required setpoint. The required orientation is calculated using a PID controlled algorithm.The orientation is published in quaternion format which ranges from 1000 to 2000. 1000 corresponds to -10 degrees and 2000 corresponds to 10 degress and all the angles between -10 and 10 degrees can be found accordingly.



## Attitude Controller
The main task of attitude controller is to keep the drone in the required orientation which is given by position controller. This is done by another PID controlled algorithm. After calculating the required PID values throttle is given to each motor of the drone so that it flies in the required orientation.These values are then converted to required PWM format that could be given to motors.<br>


To run use:

```python
roslaunch vitarana_drone task_1.launch record:=true rec_name:=task_1.bag 

```
# Task 2
## Problem Statement
The aim of this task is to pick a parcel and deliver it to its destination<br>
The Task 2 is divided into 3 sub tasks<br>
- Task 2A - Scanning the QR code and finding out the destination GPS co-ordinates.
- Task 2B - Pick/Drop the parcel box
- Task 2C - Avoiding dynamic obstacles and planing the path

To run use:

```python
roslaunch vitarana_drone task_2.launch record:=true rec_name:=task_2.bag   
```
