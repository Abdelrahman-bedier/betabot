# Betabot Obstacle avoider

- [Betabot Obstacle avoider](#betabot-obstacle-avoider)
  - [Project Description](#project-description)
  - [After you implement the pkg state your reflection below](#after-you-implement-the-pkg-state-your-reflection-below)
    - [How did you plan the task?](#how-did-you-plan-the-task)
    - [what is your logic?](#what-is-your-logic)
    - [What ROS REPs did you used?](#what-ros-reps-did-you-used)
    - [How we could increase the overall performance?](#how-we-could-increase-the-overall-performance)
    - [List the most time consuming problems you faced](#list-the-most-time-consuming-problems-you-faced)
    - [Demo](#demo)
    - [Screenshot](#screenshot)
      - [NAME:](#name)
      - [ID:](#id)

## Project Description 

Create a ROS package with custom nodes c++/python to move the
betabot randomly in gazebo, the movement should be triggered then the robot
moves randomly while avoid objects based on laser scans reading based on the laser
scans.


>NOTE: DON'T process one ray of the laser scans array or it will be considered ultrasonic/IR sensor.try to come up with approach thats use the laser full potential. 

>To make you project standout try not to visit any place twice.

---

## After you implement the pkg state your reflection below

### How did you plan the task?
building the package , then configuring how to read laser scan topic then writing the python code and make it executable and testing the package on gazebo.

### what is your logic?
first get random angle to move the robot by it. then moving forward always till it faces an obstacle by 2 m then it changes the angle of the robot till no obstacle ahead and keep moving forward.

### What ROS REPs did you used?
geometry_msgs , rospy and std_msgs

### How we could increase the overall performance?
I made the betabot to check only the angles ahead of it. these angels are 0(straight ahead ),-20 (20 degrees twoards right) , -25 (25 degrees twoards right),-10 (10 degrees twoards right) and 10 (10 degrees twoards left) as i made the robot to avoid obstacles by always moving left.
so by generalizing the betabot to check all the angles around his area will improve the overall performance.


### List the most time consuming problems you faced
reading laser scan didn't take much time but manipulating angles takes much time to get it right.

---

### Demo
Add unlisted youtube/drive video

[Demo](yourlinkhere)
https://drive.google.com/file/d/14RcGMFqTy9YSqnAb7PSiB07Hf0xELH1t/view?usp=sharing

### Screenshot

[image](yourscreenshot)


---

#### NAME:Abdelrahman Aly Bedier
#### ID:201400473

---
