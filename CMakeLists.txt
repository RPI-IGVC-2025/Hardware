cmake_minimum_required(VERSION 3.16)
project(hardware)

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
    add_compile_options(-Wall -Wextra -Wpedantic)
endif()

# find dependencies
find_package(ament_cmake REQUIRED)

find_package(controller_manager REQUIRED)
find_package(hardware_interface REQUIRED)
find_package(pluginlib REQUIRED)
find_package(rclcpp REQUIRED)
find_package(rclcpp_lifecycle REQUIRED)

# Define the library target
add_library(
    ${PROJECT_NAME}_library
    SHARED
        src/bot_system.cpp
)

target_compile_features(${PROJECT_NAME}_library PUBLIC cxx_std_17)

target_include_directories(
    ${PROJECT_NAME}_library
    PUBLIC
        $<BUILD_INTERFACE:${PROJECT_SOURCE_DIR}/src/include>
        $<INSTALL_INTERFACE:include/${PROJECT_NAME}>
)

target_link_libraries(
    ${PROJECT_NAME}_library 
    PUBLIC
        hardware_interface::hardware_interface
        pluginlib::pluginlib
        rclcpp::rclcpp
        rclcpp_lifecycle::rclcpp_lifecycle
)

install(
    DIRECTORY src/include/
    DESTINATION include
    FILES_MATCHING PATTERN "*.hpp"
)

install(
    FILES bot.xml
    DESTINATION share/${PROJECT_NAME}
)

install(
    DIRECTORY description launch
    DESTINATION share/${PROJECT_NAME}
)

install(TARGETS ${PROJECT_NAME}_library
  EXPORT export_${PROJECT_NAME}_library
  ARCHIVE DESTINATION lib
  LIBRARY DESTINATION lib
  RUNTIME DESTINATION bin
)

# Plugin Export
pluginlib_export_plugin_description_file(hardware_interface bot.xml)

ament_export_targets(export_${PROJECT_NAME}_library HAS_LIBRARY_TARGET)
ament_export_dependencies(
    controller_manager
    hardware_interface
    rclcpp
    pluginlib
    rclcpp_lifecycle
)

if(BUILD_TESTING)
    find_package(ament_lint_auto REQUIRED)
    # the following line skips the linter which checks for copyrights
    # comment the line when a copyright and license is added to all source files
    set(ament_cmake_copyright_FOUND TRUE)
    # the following line skips cpplint (only works in a git repo)
    # comment the line when this package is in a git repo and when
    # a copyright and license is added to all source files
    set(ament_cmake_cpplint_FOUND TRUE)
    ament_lint_auto_find_test_dependencies()
endif()

ament_package()
