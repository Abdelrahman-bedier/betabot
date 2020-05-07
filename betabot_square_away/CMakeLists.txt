cmake_minimum_required(VERSION 2.8.3)
project(betabot_square_away)


find_package(catkin REQUIRED COMPONENTS
  geometry_msgs
  nav_msgs
  rospy
)





catkin_python_setup()


catkin_package(
   CATKIN_DEPENDS geometry_msgs nav_msgs rospy
)

catkin_install_python(PROGRAMS
  scripts/square_run.py
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)

install(DIRECTORY launch
  DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}
)