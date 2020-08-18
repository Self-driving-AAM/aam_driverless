# ORBslam2
implementation of ORBslam2 with octomap
//////////    install car Prerequisites

sudo apt-get install ros-kinetic-ackermann-msgs ros-kinetic-twist-mux ros-kinetic-joy ros-kinetic-controller-manager ros-kinetic-robotnik-msgs ros-kinetic-velodyne-simulator ros-kinetic-effort-controllers ros-kinetic-velocity-controllers ros-kinetic-joint-state-controller ros-kinetic-gazebo-ros-control ros-kinetic-robotnik-msgs

//////////   install orb slam 2 dependencies

====>    Eigen3

sudo apt install libeigen3-dev


====>    go to the workspace
====>    catkin build

//////////   source devel/setup.bash

//////////   roslaunch aamfsd_gazebo acceleration.launch

//////////   roslaunch orb_slam2_ros stereo.launch

//////////   roslaunch octomap_server octomap_mapping.launch

//////////   rosrun rviz rviz 


=======>> when rviz opens instead of inserting the topic manually 
=======>> open the cofiguration file located (/aamfsd_orbslam2_ws/src/orb_slam_2_ros/ros/config)
