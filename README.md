# aam_driverless

## Prerequisites
<b>- Install ROS packages on Ubuntu 16:</b>
Note: Replace "kinetic" with "melodic" in all these commands if running Ubuntu 18
ros-kinetic-ackermann-msgs
ros-kinetic-twist-mux
ros-kinetic-joy
ros-kinetic-controller-manager
ros-kinetic-robotnik-msgs
ros-kinetic-velodyne-simulator
ros-kinetic-effort-controllers
ros-kinetic-velocity-controllers
ros-kinetic-joint-state-controller
ros-kinetic-gazebo-ros-control


```
sudo apt-get install ros-kinetic-ackermann-msgs ros-kinetic-twist-mux ros-kinetic-joy ros-kinetic-controller-manager ros-kinetic-robotnik-msgs ros-kinetic-velodyne-simulator ros-kinetic-effort-controllers ros-kinetic-velocity-controllers ros-kinetic-joint-state-controller ros-kinetic-gazebo-ros-control ros-kinetic-robotnik-msgs
```

<b>- Download and Install VScode from:</b> https://code.visualstudio.com/download

## Steps
1-Create a workspace for the simulation if you don't have one:
```mkdir -p ~/aamfsd_ws/src```

Note: Make sure the directory path has no spaces in it's name

2-Open the `aamfsd_ws` directory in VScode

3-Open VScode Terminal from `Terminal` menu `New Terminal`

4-Write the following commands:


```git init```

```git remote add origin https://github.com/Self-driving-AAM/aam_driverless```

```git pull origin master```


## Build on VScode
On VScode press `Ctrl + Shift + B` and from the menu select Build

## Run on VScode
On VScode press `Ctrl + Shift + B` and from the menu select Gazebo

Then select one of the race tracks to run on Gazebo

## Controlling on VScode
On VScode press `Ctrl + Shift + B` and from the menu select Control

## Build from Terminal
Write the following command


```catkin_make```


## Run from Terminal
Write the following commands


```source devel/setup.bash```


Choose one of these race tracks to run and replace the "empty" in the cmd below.
- empty
- acceleration
- skidpad
- sprint17
- small_track
- big_track


```roslaunch aamfsd_gazebo empty.launch ```


## Controlling from Terminal
To control the car open another terminal and run:


```roslaunch robot_control rqt_robot_control.launch```


## Optional
To use keyboard open another terminal and run


```sudo apt-get install ros-kinetic-teleop-twist-keyboard```

```rosrun teleop_twist_keyboard teleop_twist_keyboard.py```


## Troubleshooting
If your recieved this error while running rqt_robot_control.launch


>ERROR: cannot launch node of type [robot_control/twist_to_ackermannDrive.py]: can't locate node [twist_to_ackermannDrive.py] in package [robot_control]


Cancel the operation and run the cmds below in the same terminal


```roscd robot_control```

```chmod +x nodes/twist_to_ackermannDrive.py```


Now rerun and have fun.
