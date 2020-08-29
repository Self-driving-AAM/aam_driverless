;; Auto-generated. Do not edit!


(when (boundp 'orb_slam2_ros::ORBState)
  (if (not (find-package "ORB_SLAM2_ROS"))
    (make-package "ORB_SLAM2_ROS"))
  (shadow 'ORBState (find-package "ORB_SLAM2_ROS")))
(unless (find-package "ORB_SLAM2_ROS::ORBSTATE")
  (make-package "ORB_SLAM2_ROS::ORBSTATE"))

(in-package "ROS")
;;//! \htmlinclude ORBState.msg.html
(if (not (find-package "STD_MSGS"))
  (ros::roseus-add-msgs "std_msgs"))


(intern "*UNKNOWN*" (find-package "ORB_SLAM2_ROS::ORBSTATE"))
(shadow '*UNKNOWN* (find-package "ORB_SLAM2_ROS::ORBSTATE"))
(defconstant orb_slam2_ros::ORBState::*UNKNOWN* 0)
(intern "*SYSTEM_NOT_READY*" (find-package "ORB_SLAM2_ROS::ORBSTATE"))
(shadow '*SYSTEM_NOT_READY* (find-package "ORB_SLAM2_ROS::ORBSTATE"))
(defconstant orb_slam2_ros::ORBState::*SYSTEM_NOT_READY* 1)
(intern "*NO_IMAGES_YET*" (find-package "ORB_SLAM2_ROS::ORBSTATE"))
(shadow '*NO_IMAGES_YET* (find-package "ORB_SLAM2_ROS::ORBSTATE"))
(defconstant orb_slam2_ros::ORBState::*NO_IMAGES_YET* 2)
(intern "*NOT_INITIALIZED*" (find-package "ORB_SLAM2_ROS::ORBSTATE"))
(shadow '*NOT_INITIALIZED* (find-package "ORB_SLAM2_ROS::ORBSTATE"))
(defconstant orb_slam2_ros::ORBState::*NOT_INITIALIZED* 3)
(intern "*MAPPING*" (find-package "ORB_SLAM2_ROS::ORBSTATE"))
(shadow '*MAPPING* (find-package "ORB_SLAM2_ROS::ORBSTATE"))
(defconstant orb_slam2_ros::ORBState::*MAPPING* 4)
(intern "*LOCALIZING*" (find-package "ORB_SLAM2_ROS::ORBSTATE"))
(shadow '*LOCALIZING* (find-package "ORB_SLAM2_ROS::ORBSTATE"))
(defconstant orb_slam2_ros::ORBState::*LOCALIZING* 5)
(intern "*LOST*" (find-package "ORB_SLAM2_ROS::ORBSTATE"))
(shadow '*LOST* (find-package "ORB_SLAM2_ROS::ORBSTATE"))
(defconstant orb_slam2_ros::ORBState::*LOST* 6)
(defclass orb_slam2_ros::ORBState
  :super ros::object
  :slots (_header _state _num_closes ))

(defmethod orb_slam2_ros::ORBState
  (:init
   (&key
    ((:header __header) (instance std_msgs::Header :init))
    ((:state __state) 0)
    ((:num_closes __num_closes) 0)
    )
   (send-super :init)
   (setq _header __header)
   (setq _state (round __state))
   (setq _num_closes (round __num_closes))
   self)
  (:header
   (&rest __header)
   (if (keywordp (car __header))
       (send* _header __header)
     (progn
       (if __header (setq _header (car __header)))
       _header)))
  (:state
   (&optional __state)
   (if __state (setq _state __state)) _state)
  (:num_closes
   (&optional __num_closes)
   (if __num_closes (setq _num_closes __num_closes)) _num_closes)
  (:serialization-length
   ()
   (+
    ;; std_msgs/Header _header
    (send _header :serialization-length)
    ;; uint16 _state
    2
    ;; uint16 _num_closes
    2
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; std_msgs/Header _header
       (send _header :serialize s)
     ;; uint16 _state
       (write-word _state s)
     ;; uint16 _num_closes
       (write-word _num_closes s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; std_msgs/Header _header
     (send _header :deserialize buf ptr-) (incf ptr- (send _header :serialization-length))
   ;; uint16 _state
     (setq _state (sys::peek buf ptr- :short)) (incf ptr- 2)
   ;; uint16 _num_closes
     (setq _num_closes (sys::peek buf ptr- :short)) (incf ptr- 2)
   ;;
   self)
  )

(setf (get orb_slam2_ros::ORBState :md5sum-) "0a1b35f9b2e5df4fa8c6909051734938")
(setf (get orb_slam2_ros::ORBState :datatype-) "orb_slam2_ros/ORBState")
(setf (get orb_slam2_ros::ORBState :definition-)
      "Header header
uint16 state # State from Tracking.h
uint16 num_closes  # number of loop closure occured

# constants for enum-like access
uint16 UNKNOWN=0
uint16 SYSTEM_NOT_READY=1
uint16 NO_IMAGES_YET=2
uint16 NOT_INITIALIZED=3
uint16 MAPPING=4
uint16 LOCALIZING=5
uint16 LOST=6


================================================================================
MSG: std_msgs/Header
# Standard metadata for higher-level stamped data types.
# This is generally used to communicate timestamped data 
# in a particular coordinate frame.
# 
# sequence ID: consecutively increasing ID 
uint32 seq
#Two-integer timestamp that is expressed as:
# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')
# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')
# time-handling sugar is provided by the client library
time stamp
#Frame this data is associated with
# 0: no frame
# 1: global frame
string frame_id

")



(provide :orb_slam2_ros/ORBState "0a1b35f9b2e5df4fa8c6909051734938")


