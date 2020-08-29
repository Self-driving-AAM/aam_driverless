// Generated by gencpp from file cartographer_ros_msgs/LandmarkList.msg
// DO NOT EDIT!


#ifndef CARTOGRAPHER_ROS_MSGS_MESSAGE_LANDMARKLIST_H
#define CARTOGRAPHER_ROS_MSGS_MESSAGE_LANDMARKLIST_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>

#include <std_msgs/Header.h>
#include <cartographer_ros_msgs/LandmarkEntry.h>

namespace cartographer_ros_msgs
{
template <class ContainerAllocator>
struct LandmarkList_
{
  typedef LandmarkList_<ContainerAllocator> Type;

  LandmarkList_()
    : header()
    , landmark()  {
    }
  LandmarkList_(const ContainerAllocator& _alloc)
    : header(_alloc)
    , landmark(_alloc)  {
  (void)_alloc;
    }



   typedef  ::std_msgs::Header_<ContainerAllocator>  _header_type;
  _header_type header;

   typedef std::vector< ::cartographer_ros_msgs::LandmarkEntry_<ContainerAllocator> , typename ContainerAllocator::template rebind< ::cartographer_ros_msgs::LandmarkEntry_<ContainerAllocator> >::other >  _landmark_type;
  _landmark_type landmark;





  typedef boost::shared_ptr< ::cartographer_ros_msgs::LandmarkList_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::cartographer_ros_msgs::LandmarkList_<ContainerAllocator> const> ConstPtr;

}; // struct LandmarkList_

typedef ::cartographer_ros_msgs::LandmarkList_<std::allocator<void> > LandmarkList;

typedef boost::shared_ptr< ::cartographer_ros_msgs::LandmarkList > LandmarkListPtr;
typedef boost::shared_ptr< ::cartographer_ros_msgs::LandmarkList const> LandmarkListConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::cartographer_ros_msgs::LandmarkList_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::cartographer_ros_msgs::LandmarkList_<ContainerAllocator> >::stream(s, "", v);
return s;
}

} // namespace cartographer_ros_msgs

namespace ros
{
namespace message_traits
{



// BOOLTRAITS {'IsFixedSize': False, 'IsMessage': True, 'HasHeader': True}
// {'std_msgs': ['/opt/ros/kinetic/share/std_msgs/cmake/../msg'], 'cartographer_ros_msgs': ['/home/fayoumi/aam_carto_ws/src/cartographer_ros/cartographer_ros_msgs/msg'], 'geometry_msgs': ['/opt/ros/kinetic/share/geometry_msgs/cmake/../msg']}

// !!!!!!!!!!! ['__class__', '__delattr__', '__dict__', '__doc__', '__eq__', '__format__', '__getattribute__', '__hash__', '__init__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_parsed_fields', 'constants', 'fields', 'full_name', 'has_header', 'header_present', 'names', 'package', 'parsed_fields', 'short_name', 'text', 'types']




template <class ContainerAllocator>
struct IsFixedSize< ::cartographer_ros_msgs::LandmarkList_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::cartographer_ros_msgs::LandmarkList_<ContainerAllocator> const>
  : FalseType
  { };

template <class ContainerAllocator>
struct IsMessage< ::cartographer_ros_msgs::LandmarkList_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::cartographer_ros_msgs::LandmarkList_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::cartographer_ros_msgs::LandmarkList_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::cartographer_ros_msgs::LandmarkList_<ContainerAllocator> const>
  : TrueType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::cartographer_ros_msgs::LandmarkList_<ContainerAllocator> >
{
  static const char* value()
  {
    return "301d0343edf9ac469d5bbb0142518bf8";
  }

  static const char* value(const ::cartographer_ros_msgs::LandmarkList_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0x301d0343edf9ac46ULL;
  static const uint64_t static_value2 = 0x9d5bbb0142518bf8ULL;
};

template<class ContainerAllocator>
struct DataType< ::cartographer_ros_msgs::LandmarkList_<ContainerAllocator> >
{
  static const char* value()
  {
    return "cartographer_ros_msgs/LandmarkList";
  }

  static const char* value(const ::cartographer_ros_msgs::LandmarkList_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::cartographer_ros_msgs::LandmarkList_<ContainerAllocator> >
{
  static const char* value()
  {
    return "# Copyright 2018 The Cartographer Authors\n\
#\n\
# Licensed under the Apache License, Version 2.0 (the \"License\");\n\
# you may not use this file except in compliance with the License.\n\
# You may obtain a copy of the License at\n\
#\n\
#      http://www.apache.org/licenses/LICENSE-2.0\n\
#\n\
# Unless required by applicable law or agreed to in writing, software\n\
# distributed under the License is distributed on an \"AS IS\" BASIS,\n\
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.\n\
# See the License for the specific language governing permissions and\n\
# limitations under the License.\n\
\n\
std_msgs/Header header\n\
cartographer_ros_msgs/LandmarkEntry[] landmark\n\
\n\
================================================================================\n\
MSG: std_msgs/Header\n\
# Standard metadata for higher-level stamped data types.\n\
# This is generally used to communicate timestamped data \n\
# in a particular coordinate frame.\n\
# \n\
# sequence ID: consecutively increasing ID \n\
uint32 seq\n\
#Two-integer timestamp that is expressed as:\n\
# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')\n\
# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')\n\
# time-handling sugar is provided by the client library\n\
time stamp\n\
#Frame this data is associated with\n\
# 0: no frame\n\
# 1: global frame\n\
string frame_id\n\
\n\
================================================================================\n\
MSG: cartographer_ros_msgs/LandmarkEntry\n\
# 2018 The Cartographer Authors\n\
#\n\
# Licensed under the Apache License, Version 2.0 (the \"License\");\n\
# you may not use this file except in compliance with the License.\n\
# You may obtain a copy of the License at\n\
#\n\
#      http://www.apache.org/licenses/LICENSE-2.0\n\
#\n\
# Unless required by applicable law or agreed to in writing, software\n\
# distributed under the License is distributed on an \"AS IS\" BASIS,\n\
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.\n\
# See the License for the specific language governing permissions and\n\
# limitations under the License.\n\
\n\
string id\n\
geometry_msgs/Pose tracking_from_landmark_transform\n\
float64 translation_weight\n\
float64 rotation_weight\n\
\n\
================================================================================\n\
MSG: geometry_msgs/Pose\n\
# A representation of pose in free space, composed of position and orientation. \n\
Point position\n\
Quaternion orientation\n\
\n\
================================================================================\n\
MSG: geometry_msgs/Point\n\
# This contains the position of a point in free space\n\
float64 x\n\
float64 y\n\
float64 z\n\
\n\
================================================================================\n\
MSG: geometry_msgs/Quaternion\n\
# This represents an orientation in free space in quaternion form.\n\
\n\
float64 x\n\
float64 y\n\
float64 z\n\
float64 w\n\
";
  }

  static const char* value(const ::cartographer_ros_msgs::LandmarkList_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::cartographer_ros_msgs::LandmarkList_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.header);
      stream.next(m.landmark);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct LandmarkList_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::cartographer_ros_msgs::LandmarkList_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::cartographer_ros_msgs::LandmarkList_<ContainerAllocator>& v)
  {
    s << indent << "header: ";
    s << std::endl;
    Printer< ::std_msgs::Header_<ContainerAllocator> >::stream(s, indent + "  ", v.header);
    s << indent << "landmark[]" << std::endl;
    for (size_t i = 0; i < v.landmark.size(); ++i)
    {
      s << indent << "  landmark[" << i << "]: ";
      s << std::endl;
      s << indent;
      Printer< ::cartographer_ros_msgs::LandmarkEntry_<ContainerAllocator> >::stream(s, indent + "    ", v.landmark[i]);
    }
  }
};

} // namespace message_operations
} // namespace ros

#endif // CARTOGRAPHER_ROS_MSGS_MESSAGE_LANDMARKLIST_H
