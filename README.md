# aamfsd_localization


# core/eigen error
cd /usr/include
sudo ln -sf eigen3/Eigen Eigen
sudo ln -sf eigen3/unsupported unsupported

# QVariantMap DBusMenuExporterDBus::getProperties(int, const QStringList&) const: Condition failed: action

sudo apt-get install ros-kinetic-find-object-2d

#error this file requires compiler and library support for the iso c++ 2011 standard ubuntu

Put this line :

set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=c++14")

after the first line of CMakeLists.txt located in src directory

# missing libraries

sudo apt-get update
sudo apt-get install -y \
    cmake \
    g++ \
    git \
    google-mock \
    libboost-all-dev \
    libcairo2-dev \
    libeigen3-dev \
    libgflags-dev \
    libgoogle-glog-dev \
    liblua5.2-dev \
    libsuitesparse-dev \
    ninja-build \
    python-sphinx \
    stow

# suite sparse missing from ceres

sudo apt-get install libsuitesparse-dev


# syntax error in library not found in 'std' (gcc & g++)
# only gcc5 and g++5 can compile it

sudo add-apt-repository ppa:ubuntu-toolchain-r/test
sudo apt-get update
sudo apt-get install gcc-5 g++-5
sudo update-alternatives --install /usr/bin/gcc gcc /usr/bin/gcc-5 60 --slave /usr/bin/g++ g++ /usr/bin/g++-5


sudo apt-get update
sudo apt-get install gcc-5sudo apt-get update
sudo apt-get install gcc-5

# ceres solver missing lib

sudo apt-get install libatlas-base-dev


# install gazebo problem 

sudo sh -c 'echo "deb http://packages.osrfoundation.org/gazebo/ubuntu-stable `lsb_release -cs` main" > /etc/apt/sources.list.d/gazebo-stable.list'

wget http://packages.osrfoundation.org/gazebo.key -O - | sudo apt-key add -

sudo apt-get update

sudo apt-get install gazebo7

