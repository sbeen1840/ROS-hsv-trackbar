# my_trackbar Package

The my_trackbar package is a ROS (Robot Operating System) package that allows you to tune HSV (Hue, Saturation, Value) values using a trackbar interface. This package provides an easy way to adjust the HSV values required for image processing.

## Installation

1. Before using this package, make sure you have ROS installed on your system. For detailed instructions on installing ROS, please refer to the official ROS website at https://www.ros.org/.

2. Once ROS is installed, you can install the My_Trackbar package by following these steps. Open a terminal and execute the following commands:

```bash
$ cd ~/catkin_ws/src
$ git clone https://github.com/your_username/my_trackbar.git
$ cd ~/catkin_ws
$ catkin_make
$ source devel/setup.bash
```

## Usage

To run the My_Trackbar package, use the roslaunch command as follows:

```bash
$ roslaunch my_trackbar trackbar.launch
```

Running the above command will open a trackbar window where you can adjust the HSV values for the desired image. Move the trackbars to see the applied image.

## Package Structure

The my_trackbar package is organized as follows:

```
my_trackbar/
    ├── CMakeLists.txt
    ├── launch/
    │   └── trackbar.launch
    ├── package.xml
    ├── src/
    │   ├── trackbar.py

```


## Important Notes

- Ensure that the ROS master is running before using this package.

## Lisence
- sbeen1840
