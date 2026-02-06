# Nav2 Configuration Parameters Reference

*Generated: 2026-02-06*
*Source: https://docs.nav2.org/configuration/*

This document contains all tunable parameters for the Nav2 navigation stack.
Use Ctrl+F / Cmd+F to search for specific parameters.

---


## Table of Contents

- [Amcl](#amcl)
- [Appendgoalposetogoals](#appendgoalposetogoals)
- [Areerrorcodespresent](#areerrorcodespresent)
- [Areposesnear](#areposesnear)
- [Assistedteleop](#assistedteleop)
- [Axis_Goal_Checker](#axis_goal_checker)
- [Backup](#backup)
- [Base_Obstacle](#base_obstacle)
- [Behavior Server](#behavior-server)
- [Binary_Filter](#binary_filter)
- [Bt Navigator](#bt-navigator)
- [Cancelassistedteleop](#cancelassistedteleop)
- [Cancelbackup](#cancelbackup)
- [Cancelcomputeandtrackroute](#cancelcomputeandtrackroute)
- [Cancelcontrol](#cancelcontrol)
- [Cancelcoverage](#cancelcoverage)
- [Canceldriveonheading](#canceldriveonheading)
- [Cancelfollowobject](#cancelfollowobject)
- [Cancelspin](#cancelspin)
- [Cancelwait](#cancelwait)
- [Clearcostmaparoundpose](#clearcostmaparoundpose)
- [Clearcostmaparoundrobot](#clearcostmaparoundrobot)
- [Clearcostmapexceptregion](#clearcostmapexceptregion)
- [Clearentirecostmap](#clearentirecostmap)
- [Collision Detector Node](#collision-detector-node)
- [Collision Monitor Node](#collision-monitor-node)
- [Computeandtrackroute](#computeandtrackroute)
- [Computecoveragepath](#computecoveragepath)
- [Computepaththroughposes](#computepaththroughposes)
- [Computepathtopose](#computepathtopose)
- [Computeroute](#computeroute)
- [Concatenatepaths](#concatenatepaths)
- [Constrained Smoother](#constrained-smoother)
- [Controller](#controller)
- [Controller Server](#controller-server)
- [Controllerselector](#controllerselector)
- [Costmap Filter Info Server](#costmap-filter-info-server)
- [Costmaps](#costmaps)
- [Coverage Server](#coverage-server)
- [Denoise](#denoise)
- [Distancecontroller](#distancecontroller)
- [Distancetraveled](#distancetraveled)
- [Docking Server](#docking-server)
- [Dockrobot](#dockrobot)
- [Driveonheading](#driveonheading)
- [Extractroutenodesasgoals](#extractroutenodesasgoals)
- [Feasible_Path_Handler](#feasible_path_handler)
- [Following Server](#following-server)
- [Followobject](#followobject)
- [Followpath](#followpath)
- [General](#general)
- [Getcurrentpose](#getcurrentpose)
- [Getnextfewgoals](#getnextfewgoals)
- [Getposefrompath](#getposefrompath)
- [Globalupdatedgoal](#globalupdatedgoal)
- [Goal_Align](#goal_align)
- [Goal_Dist](#goal_dist)
- [Goalcheckerselector](#goalcheckerselector)
- [Goalreached](#goalreached)
- [Goalupdated](#goalupdated)
- [Goalupdatedcontroller](#goalupdatedcontroller)
- [Goalupdater](#goalupdater)
- [Graceful Motion Controller](#graceful-motion-controller)
- [Inflation](#inflation)
- [Initialposereceived](#initialposereceived)
- [Input_At_Waypoint](#input_at_waypoint)
- [Isbatterycharging](#isbatterycharging)
- [Isbatterylow](#isbatterylow)
- [Isgoalnearby](#isgoalnearby)
- [Ispathvalid](#ispathvalid)
- [Isposeoccupied](#isposeoccupied)
- [Isstopped](#isstopped)
- [Iterator](#iterator)
- [Keepout_Filter](#keepout_filter)
- [Kinematic](#kinematic)
- [Lifecycle](#lifecycle)
- [Limited_Accel_Generator](#limited_accel_generator)
- [Loopback Sim](#loopback-sim)
- [Map Saver](#map-saver)
- [Map Server](#map-server)
- [Mppic](#mppic)
- [Navfn](#navfn)
- [Navigatethroughposes](#navigatethroughposes)
- [Navigatetopose](#navigatetopose)
- [Obstacle](#obstacle)
- [Obstacle_Footprint](#obstacle_footprint)
- [Oscillation](#oscillation)
- [Path_Align](#path_align)
- [Path_Dist](#path_dist)
- [Pathexpiringtimer](#pathexpiringtimer)
- [Pathhandlerselector](#pathhandlerselector)
- [Pathlongeronapproach](#pathlongeronapproach)
- [Pauseresumecontroller](#pauseresumecontroller)
- [Photo_At_Waypoint](#photo_at_waypoint)
- [Planner Server](#planner-server)
- [Plannerselector](#plannerselector)
- [Plugin_Container](#plugin_container)
- [Pose_Progress_Checker](#pose_progress_checker)
- [Position_Goal_Checker](#position_goal_checker)
- [Prefer_Forward](#prefer_forward)
- [Progresscheckerselector](#progresscheckerselector)
- [Range](#range)
- [Ratecontroller](#ratecontroller)
- [Recoverynode](#recoverynode)
- [Regulated Pp](#regulated-pp)
- [Reinitializegloballocalization](#reinitializegloballocalization)
- [Removeincollisiongoals](#removeincollisiongoals)
- [Removepassedgoals](#removepassedgoals)
- [Rotate_To_Goal](#rotate_to_goal)
- [Rotation Shim Controller](#rotation-shim-controller)
- [Roundrobin](#roundrobin)
- [Route Server](#route-server)
- [Savitzky Golay Smoother](#savitzky-golay-smoother)
- [Simple Smoother](#simple-smoother)
- [Simple_Goal_Checker](#simple_goal_checker)
- [Simple_Progress_Checker](#simple_progress_checker)
- [Smac 2D](#smac-2d)
- [Smac Hybrid](#smac-hybrid)
- [Smac Lattice](#smac-lattice)
- [Smac Planner](#smac-planner)
- [Smooth](#smooth)
- [Smoother Server](#smoother-server)
- [Smootherselector](#smootherselector)
- [Speed_Filter](#speed_filter)
- [Speedcontroller](#speedcontroller)
- [Spin](#spin)
- [Standard_Traj_Generator](#standard_traj_generator)
- [Static](#static)
- [Stopped_Goal_Checker](#stopped_goal_checker)
- [Thetastar](#thetastar)
- [Timeexpired](#timeexpired)
- [Togglecollisionmonitor](#togglecollisionmonitor)
- [Transformavailable](#transformavailable)
- [Truncatepath](#truncatepath)
- [Truncatepathlocal](#truncatepathlocal)
- [Twirling](#twirling)
- [Undockrobot](#undockrobot)
- [Vector Object Server](#vector-object-server)
- [Velocity Smoother](#velocity-smoother)
- [Visualization](#visualization)
- [Voxel](#voxel)
- [Wait](#wait)
- [Wait_At_Waypoint](#wait_at_waypoint)
- [Waypoint Follower](#waypoint-follower)
- [Wouldacontrollerrecoveryhelp](#wouldacontrollerrecoveryhelp)
- [Wouldaplannerrecoveryhelp](#wouldaplannerrecoveryhelp)
- [Wouldarouterecoveryhelp](#wouldarouterecoveryhelp)
- [Wouldasmootherrecoveryhelp](#wouldasmootherrecoveryhelp)

---

**Total: 148 components, 1297 parameters**

---

## Amcl

### AMCL
*Source: https://docs.nav2.org/configuration/packages/configuring-amcl.html*

- **`allow_parameter_qos_overrides`**
  - Type: `bool`
  - Default: `true`
  - Whether to allow QoS profiles to be overwritten with parameterized values.

- **`alpha1`**
  - Type: `double`
  - Default: `0.2`
  - Expected process noise in odometry’s rotation estimate from rotation.

- **`alpha2`**
  - Type: `double`
  - Default: `0.2`
  - Expected process noise in odometry’s rotation estimate from translation.

- **`alpha3`**
  - Type: `double`
  - Default: `0.2`
  - Expected process noise in odometry’s translation estimate from translation.

- **`alpha4`**
  - Type: `double`
  - Default: `0.2`
  - Expected process noise in odometry’s translation estimate from rotation.

- **`alpha5`**
  - Type: `double`
  - Default: `0.2`
  - For Omni models only: translation noise.

- **`always_reset_initial_pose`**
  - Type: `bool`
  - Default: `False`
  - Requires that AMCL is provided an initial pose either via topic or initial_pose* parameter (with parameter set_initial_pose: true) when reset. Otherwise, by default AMCL will use the last known pos...

- **`base_frame_id`**
  - Type: `string`
  - Default: `“base_footprint”`
  - Robot base frame.

- **`beam_skip_distance`**
  - Type: `double`
  - Default: `0.5`
  - Ignore beams that most particles disagree with in Likelihood field model. Maximum distance to consider skipping for (m).

- **`beam_skip_error_threshold`**
  - Type: `double`
  - Default: `0.9`
  - Percentage of beams after not matching map to force full update due to bad convergence.

- **`beam_skip_threshold`**
  - Type: `double`
  - Default: `0.3`
  - Percentage of beams required to skip.

- **`bond_heartbeat_period`**
  - Type: `double`
  - Default: `0.25`
  - The lifecycle node bond mechanism publishing period (on the /bond topic). Disabled if inferior or equal to 0.0.

- **`do_beamskip`**
  - Type: `bool`
  - Default: `False`
  - Whether to do beam skipping in Likelihood field model.

- **`first_map_only`**
  - Type: `bool`
  - Default: `False`
  - Allows AMCL to accept maps more than once on the map_topic. This is especially useful when you’re using theLoadMapservice inmap_server. Prior to Humble, this isfirst_map_only_.

- **`global_frame_id`**
  - Type: `string`
  - Default: `“map”`
  - The name of the coordinate frame published by the localization system.

- **`initial_pose`**
  - Type: `Pose2D`
  - Default: `{x: 0.0, y: 0.0, z: 0.0, yaw: 0.0}`
  - X, Y, Z, and yaw coordinates of initial pose (meters and radians) of robot base frame in global frame.

- **`introspection_mode`**
  - Type: `string`
  - Default: `“disabled”`
  - The introspection mode for services and actions. Options are “disabled”, “metadata”, “contents”.

- **`lambda_short`**
  - Type: `double`
  - Default: `0.1`
  - Exponential decay parameter for z_short part of model.

- **`laser_likelihood_max_dist`**
  - Type: `double`
  - Default: `2.0`
  - Maximum distance to do obstacle inflation on map, for use in likelihood_field model.

- **`laser_max_range`**
  - Type: `double`
  - Default: `100.0`
  - Maximum scan range to be considered, -1.0 will cause the laser’s reported maximum range to be used.

- **`laser_min_range`**
  - Type: `double`
  - Default: `-1.0`
  - Minimum scan range to be considered, -1.0 will cause the laser’s reported minimum range to be used.

- **`laser_model_type`**
  - Type: `string`
  - Default: `“likelihood_field”`
  - Which model to use, either beam, likelihood_field, or likelihood_field_prob. Same as likelihood_field but incorporates the beamskip feature, if enabled.

- **`map_topic`**
  - Type: `string`
  - Default: `map`
  - Map topic to subscribe to.

- **`max_beams`**
  - Type: `int`
  - Default: `60`
  - How many evenly-spaced beams in each scan to be used when updating the filter.

- **`max_particles`**
  - Type: `int`
  - Default: `2000`
  - Maximum allowed number of particles.

- **`min_particles`**
  - Type: `int`
  - Default: `500`
  - Minimum allowed number of particles.

- **`odom_frame_id`**
  - Type: `string`
  - Default: `“odom”`
  - Which frame to use for odometry.

- **`pf_err`**
  - Type: `double`
  - Default: `0.05`
  - Particle Filter population error.

- **`pf_z`**
  - Type: `double`
  - Default: `0.99`
  - Particle filter population density. 2.33 is the 99% percentile.

- **`random_seed`**
  - Type: `int`
  - Default: `-1`
  - Seed for the particle filter RNG.random_seed>=0: seed the RNG with the provided value (repeatable runs).random_seed<0(default): seed the RNG from time (preserves historical behavior).

- **`recovery_alpha_fast`**
  - Type: `double`
  - Default: `0.0`
  - Exponential decay rate for the fast average weight filter, used in deciding when to recover by adding random poses. A good value might be 0.1.

- **`recovery_alpha_slow`**
  - Type: `double`
  - Default: `0.0`
  - Exponential decay rate for the slow average weight filter, used in deciding when to recover by adding random poses. A good value might be 0.001.

- **`resample_interval`**
  - Type: `int`
  - Default: `1`
  - Number of filter updates required before resampling.

- **`robot_model_type`**
  - Type: `string`
  - Default: `“nav2_amcl::DifferentialMotionModel”`
  - The fully-qualified type of the plugin class. Options are “nav2_amcl::DifferentialMotionModel” and “nav2_amcl::OmniMotionModel”. Users can also provide their own custom motion model plugin type.

- **`save_pose_rate`**
  - Type: `double`
  - Default: `0.5`
  - Maximum rate (Hz) at which to store the last estimated pose and covariance to the parameter server, in the variables ~initial_pose_* and ~initial_cov_*. This saved pose will be used on subsequent r...

- **`scan_topic`**
  - Type: `string`
  - Default: `scan`
  - Laser scan topic to subscribe to.

- **`set_initial_pose`**
  - Type: `bool`
  - Default: `False`
  - Causes AMCL to set initial pose from the initial_pose* parameters instead of waiting for the initial_pose message.

- **`sigma_hit`**
  - Type: `double`
  - Default: `0.2`
  - Standard deviation for Gaussian model used in z_hit part of the model.

- **`tf_broadcast`**
  - Type: `bool`
  - Default: `True`
  - Set this to false to prevent amcl from publishing the transform between the global frame and the odometry frame.

- **`transform_tolerance`**
  - Type: `double`
  - Default: `1.0`
  - Time with which to post-date the transform that is published, to indicate that this transform is valid into the future.

- **`update_min_a`**
  - Type: `double`
  - Default: `0.2`
  - Rotational movement required before performing a filter update.

- **`update_min_d`**
  - Type: `double`
  - Default: `0.25`
  - Translational movement required before performing a filter update.

- **`z_hit`**
  - Type: `double`
  - Default: `0.5`
  - Mixture weight for z_hit part of model, sum of all used z weight must be 1. Beam uses all 4, likelihood model uses z_hit and z_rand..

- **`z_max`**
  - Type: `double`
  - Default: `0.05`
  - Mixture weight for z_max part of model, sum of all used z weight must be 1. Beam uses all 4, likelihood model uses z_hit and z_rand.

- **`z_rand`**
  - Type: `double`
  - Default: `0.5`
  - Mixture weight for z_rand part of model, sum of all used z weight must be 1. Beam uses all 4, likelihood model uses z_hit and z_rand..

- **`z_short`**
  - Type: `double`
  - Default: `0.005`
  - Mixture weight for z_short part of model, sum of all used z weight must be 1. Beam uses all 4, likelihood model uses z_hit and z_rand.

---

## Appendgoalposetogoals

### AppendGoalPoseToGoals
*Source: https://docs.nav2.org/configuration/packages/bt-plugins/actions/AppendGoalPoseToGoals.html*

- **`goal_pose`**
  - Type: `geometry_msgs/PoseStamped`
  - Default: `N/A`
  - Goal pose to append to thegoalsvector.

- **`input_goals`**
  - Type: `nav_msgs/Goals`
  - Default: `N/A`
  - Input goals vector to append to.

- **`output_goals`**
  - Type: `nav_msgs/Goals`
  - Default: `N/A`
  - Output goals vector appended to.

---

## Areerrorcodespresent

### AreErrorCodesPresent
*Source: https://docs.nav2.org/configuration/packages/bt-plugins/conditions/AreErrorCodesPresent.html*

- **`error_code`**
  - Type: `unsigned short`
  - Default: `N/A`
  - The active error code to compare against.

- **`error_codes_to_check`**
  - Type: `std::set<unsigned short>`
  - Default: `N/A`
  - The set of error codes you wish to compare against the active error code.

---

## Areposesnear

### ArePosesNear
*Source: https://docs.nav2.org/configuration/packages/bt-plugins/conditions/ArePosesNear.html*

- **`global_frame`**
  - Type: `string`
  - Default: `N/A`
  - Global frame to transform poses to if not given in the same frame. If not provided, uses the BT Navigator’sglobal_framesetting automatically.

- **`ref_pose`**
  - Type: `geometry_msgs::msg::PoseStamped`
  - Default: `N/A`
  - Takes in a blackboard variable containing the initial pose to check.

- **`target_pose`**
  - Type: `geometry_msgs::msg::PoseStamped`
  - Default: `N/A`
  - Takes in a blackboard variable containing the other pose to check against.

- **`tolerance`**
  - Type: `double`
  - Default: `0.50`
  - Tolerance to check poses if nearby with respect to.

---

## Assistedteleop

### AssistedTeleop
*Source: https://docs.nav2.org/configuration/packages/bt-plugins/actions/AssistedTeleop.html*

- **`error_code_id`**
  - Type: `uint16`
  - Default: `N/A`
  - Assisted teleop error code. SeeAssistedTeleopaction message for the enumerated set of error codes.

- **`error_msg`**
  - Type: `uint16`
  - Default: `N/A`
  - Assisted teleop error message. SeeAssistedTeleopaction message for the enumerated set of error codes.

- **`is_recovery`**
  - Type: `double`
  - Default: `false`
  - If true increment the recovery counter.

- **`server_name`**
  - Type: `string`
  - Default: `N/A`
  - Action server name.

- **`server_timeout`**
  - Type: `double`
  - Default: `10`
  - Action server timeout (ms).

- **`time_allowance`**
  - Type: `double`
  - Default: `10.0`
  - Time to invoke behavior for, if exceeds considers it a stuck condition or failure case (seconds).

---

## Axis_Goal_Checker

### AxisGoalChecker
*Source: https://docs.nav2.org/configuration/packages/nav2_controller-plugins/axis_goal_checker.html*

- **`<nav2_controllerplugin>.along_path_tolerance`**
  - Type: `double`
  - Default: `0.25`
  - Tolerance for the projected distance along the path direction (m). This checks how far ahead or behind the goal the robot is when projected onto the path axis.

- **`<nav2_controllerplugin>.cross_track_tolerance`**
  - Type: `double`
  - Default: `0.25`
  - Tolerance for the perpendicular distance from the path direction (m). This checks how far to the left or right of the path axis the robot is.

- **`<nav2_controllerplugin>.is_overshoot_valid`**
  - Type: `bool`
  - Default: `false`
  - Whether to allow overshooting past the goal along the path direction. When false (default), usesfabs(projected_distance)<along_path_tolerancefor symmetric tolerance. When true, usesprojected_distan...

- **`<nav2_controllerplugin>.path_length_tolerance`**
  - Type: `double`
  - Default: `1.0`
  - Maximum path length to consider for goal checking (m). If the remaining path length exceeds this value, the goal check is skipped. This prevents premature goal acceptance when far from the goal.

---

## Backup

### BackUp
*Source: https://docs.nav2.org/configuration/packages/bt-plugins/actions/BackUp.html*

- **`backup_dist`**
  - Type: `double`
  - Default: `-0.15`
  - Total distance to backup (m).

- **`backup_speed`**
  - Type: `double`
  - Default: `0.025`
  - Backup speed (m/s).

- **`disable_collision_checks`**
  - Type: `bool`
  - Default: `false`
  - Disable collision checking.

- **`error_code_id`**
  - Type: `uint16`
  - Default: `N/A`
  - Backup error code. SeeBackUpaction message for the enumerated set of error codes.

- **`error_msg`**
  - Type: `string`
  - Default: `N/A`
  - Backup error message. SeeBackUpaction message for the enumerated set of error codes.

- **`server_name`**
  - Type: `string`
  - Default: `N/A`
  - Action server name.

- **`server_timeout`**
  - Type: `double`
  - Default: `10`
  - Action server timeout (ms).

- **`time_allowance`**
  - Type: `double`
  - Default: `10.0`
  - Time to invoke behavior for, if exceeds considers it a stuck condition or failure case (seconds).

---

## Base_Obstacle

### BaseObstacleCritic
*Source: https://docs.nav2.org/configuration/packages/trajectory_critics/base_obstacle.html*

- **`<dwbplugin>.<name>.scale`**
  - Type: `double`
  - Default: `1.0`
  - Weighed scale for critic.

- **`<dwbplugin>.<name>.sum_scores`**
  - Type: `bool`
  - Default: `false`
  - Whether to allow for scores to be summed up.

---

## Behavior Server

### Behavior Server
*Source: https://docs.nav2.org/configuration/packages/configuring-behavior-server.html*

- **`allow_parameter_qos_overrides`**
  - Type: `bool`
  - Default: `true`
  - Whether to allow QoS profiles to be overwritten with parameterized values.

- **`backup.acceleration_limit`**
  - Type: `double`
  - Default: `2.5`
  - Maximum acceleration limit (m/s^2). This parameter limits the rate at which speed increases when moving backward.

- **`backup.deceleration_limit`**
  - Type: `double`
  - Default: `-2.5`
  - Maximum deceleration limit (m/s^2). Negative value. This parameter limits the rate at which speed decreases when moving backward.

- **`backup.minimum_speed`**
  - Type: `double`
  - Default: `0.10`
  - Minimum speed to move, the deadband velocity of the robot behavior (m/s). Positive value.

- **`behavior_plugins`**
  - Type: `vector<string>`
  - Default: `{“spin”, “back_up”, “drive_on_heading”, “wait”}`
  - List of plugin names to use, also matches action server names.

- **`bond_heartbeat_period`**
  - Type: `double`
  - Default: `0.25`
  - The lifecycle node bond mechanism publishing period (on the /bond topic). Disabled if inferior or equal to 0.0.

- **`cmd_vel_teleop`**
  - Type: `string`
  - Default: `cmd_vel_teleop`
  - Topic to listen for teleop messages.

- **`cycle_frequency`**
  - Type: `double`
  - Default: `10.0`
  - Frequency to run behavior plugins.

- **`drive_on_heading.acceleration_limit`**
  - Type: `double`
  - Default: `2.5`
  - Maximum acceleration limit (m/s^2).

- **`drive_on_heading.deceleration_limit`**
  - Type: `double`
  - Default: `-2.5`
  - Maximum deceleration limit (m/s^2). Negative value.

- **`drive_on_heading.minimum_speed`**
  - Type: `double`
  - Default: `0.10`
  - Minimum speed to move, the deadband velocity of the robot behavior (m/s). Positive value.

- **`enable_stamped_cmd_vel`**
  - Type: `bool`
  - Default: `true`
  - Whether to use geometry_msgs::msg::Twist or geometry_msgs::msg::TwistStamped velocity data. True uses TwistStamped, false uses Twist. Note: This parameter is defaultfalsein Jazzy or older! Kilted o...

- **`global_costmap_topic`**
  - Type: `string`
  - Default: `“global_costmap/costmap_raw”`
  - Raw costmap topic for collision checking on the global costmap.

- **`global_footprint_topic`**
  - Type: `string`
  - Default: `“global_costmap/published_footprint”`
  - Topic for footprint in the global costmap frame.

- **`global_frame`**
  - Type: `string`
  - Default: `“map”`
  - Global reference frame.

- **`introspection_mode`**
  - Type: `string`
  - Default: `“disabled”`
  - The introspection mode for services and actions. Options are “disabled”, “metadata”, “contents”.

- **`local_costmap_topic`**
  - Type: `string`
  - Default: `“local_costmap/costmap_raw”`
  - Raw costmap topic for collision checking on the local costmap.

- **`local_footprint_topic`**
  - Type: `string`
  - Default: `“local_costmap/published_footprint”`
  - Topic for footprint in the local costmap frame.

- **`local_frame`**
  - Type: `string`
  - Default: `“odom”`
  - Local reference frame.

- **`max_rotational_vel`**
  - Type: `double`
  - Default: `1.0`
  - Maximum rotational velocity (rad/s).

- **`min_rotational_vel`**
  - Type: `double`
  - Default: `0.4`
  - Minimum rotational velocity (rad/s).

- **`projection_time`**
  - Type: `double`
  - Default: `1.0`
  - Time to look ahead for collisions (s).

- **`robot_base_frame`**
  - Type: `string`
  - Default: `“base_link”`
  - Robot base frame.

- **`rotational_acc_lim`**
  - Type: `double`
  - Default: `3.2`
  - maximum rotational acceleration (rad/s^2).

- **`simulate_ahead_time`**
  - Type: `double`
  - Default: `2.0`
  - Time to look ahead for collisions (s).

- **`simulation_time_step`**
  - Type: `double`
  - Default: `0.1`
  - Time step for projections (s).

- **`transform_tolerance`**
  - Type: `double`
  - Default: `0.1`
  - TF transform tolerance.

- **`“backup”`**

- **`“drive_on_heading”`**

- **`“spin”`**

- **`“wait”`**

---

## Binary_Filter

### Binary Filter Parameters
*Source: https://docs.nav2.org/configuration/packages/costmap-plugins/binary_filter.html*

- **`<filtername>.binary_state_topic`**
  - Type: `string`
  - Default: `“binary_state”`
  - Topic ofstd_msgs::msg::Booltype to publish binary filter state to.

- **`<filtername>.default_state`**
  - Type: `bool`
  - Default: `false`
  - Default state of binary filter.

- **`<filtername>.enabled`**
  - Type: `bool`
  - Default: `True`
  - Whether it is enabled.

- **`<filtername>.filter_info_topic`**
  - Type: `string`
  - Default: `N/A`
  - Name of the incomingCostmapFilterInfotopic having filter-related information. Published by Costmap Filter Info Server along with filter mask topic. For more details about Map and Costmap Filter Inf...

- **`<filtername>.flip_threshold`**
  - Type: `double`
  - Default: `50.0`
  - Threshold for binary state flipping. Filter values higher than this threshold, will set binary state to non-default.

- **`<filtername>.transform_tolerance`**
  - Type: `double`
  - Default: `0.1`
  - Time with which to post-date the transform that is published, to indicate that this transform is valid into the future. Used when filter mask and current costmap layer are in different frames.

- **`Descrioption`**
  - Threshold for binary state flipping. Filter values higher than this threshold, will set binary state to non-default.

---

## Bt Navigator

### Behavior-Tree Navigator
*Source: https://docs.nav2.org/configuration/packages/configuring-bt-navigator.html*

- **`<navigate_through_poses>.enable_groot_monitoring`**
  - Type: `bool`
  - Default: `False`
  - Whether to enable Groot2 monitoring for this navigator.

- **`<navigate_through_poses>.goals_blackboard_id`**
  - Type: `string`
  - Default: `“goals”`
  - Blackboard variable to use to supply the goals to the behavior tree forNavigateThroughPoses. Should match ports of BT XML file.

- **`<navigate_through_poses>.groot_server_port`**
  - Type: `int`
  - Default: `1669`
  - The port number for the Groot2 server. Note: In Groot2, you only need to specify the server port value, not the publisher port, as it is always the server port +1. Therefore, in this case, to use a...

- **`<navigate_through_poses>.path_blackboard_id`**
  - Type: `string`
  - Default: `“path”`
  - Blackboard variable to get the path from the behavior tree forNavigateThroughPosesfeedback. Should match port names of BT XML file.

- **`<navigate_through_poses>.search_window`**
  - Type: `double`
  - Default: `2.0`
  - How far (in meters) along the path the searching algorithm will look for the closest point.

- **`<navigate_through_poses>.tracking_feedback_blackboard_id`**
  - Type: `string`
  - Default: `“tracking_feedback”`
  - Blackboard variable to get the tracking feedback from the behavior tree forNavigateThroughPosesfeedback. Should match port names of BT XML file.

- **`<navigate_through_poses>.waypoint_statuses_blackboard_id`**
  - Type: `string`
  - Default: `“waypoint_statuses”`
  - Blackboard variable to get the statuses of waypoints from the behavior tree forNavigateThroughPosesfeedback/result. Should match ports of BT XML file.

- **`<navigate_to_pose_name>.enable_groot_monitoring`**
  - Type: `bool`
  - Default: `False`
  - Whether to enable Groot2 monitoring for this navigator.

- **`<navigate_to_pose_name>.goal_blackboard_id`**
  - Type: `string`
  - Default: `“goal”`
  - Blackboard variable to use to supply the goal to the behavior tree forNavigateToPose. Should match ports of BT XML file.

- **`<navigate_to_pose_name>.groot_server_port`**
  - Type: `int`
  - Default: `1667`
  - The port number for the Groot2 server. Note: In Groot2, you only need to specify the server port value, not the publisher port, as it is always the server port +1. Therefore, in this case, to use a...

- **`<navigate_to_pose_name>.path_blackboard_id`**
  - Type: `string`
  - Default: `“path”`
  - Blackboard variable to get the path from the behavior tree forNavigateToPosefeedback. Should match port names of BT XML file.

- **`<navigate_to_pose_name>.search_window`**
  - Type: `double`
  - Default: `2.0`
  - How far (in meters) along the path the searching algorithm will look for the closest point.

- **`<navigate_to_pose_name>.tracking_feedback_blackboard_id`**
  - Type: `string`
  - Default: `“tracking_feedback”`
  - Blackboard variable to get the tracking feedback from the behavior tree forNavigateToPosefeedback. Should match port names of BT XML file.

- **`[“assisted_teleop”,`**
  - “backup”, “compute_path”, “dock_robot”, “drive_on_heading”, “follow_path”, “nav_thru_poses”, “nav_to_pose”, “spin”, “route”, “undock_robot”, “wait”]

- **`[“compute_path_error_code”,`**
  - “follow_path_error_code”]

- **`allow_parameter_qos_overrides`**
  - Type: `bool`
  - Default: `true`
  - Whether to allow QoS profiles to be overwritten with parameterized values.

- **`always_reload_bt_xml`**
  - Type: `bool`
  - Default: `false`
  - Always load the requested behavior tree XML description, regardless of the name of the currently active XML.

- **`bond_heartbeat_period`**
  - Type: `double`
  - Default: `0.25`
  - The lifecycle node bond mechanism publishing period (on the /bond topic). Disabled if inferior or equal to 0.0.

- **`bt_loop_duration`**
  - Type: `int`
  - Default: `10`
  - Duration (in milliseconds) for each iteration of BT execution.

- **`bt_search_directories`**
  - Type: `vector<string>`
  - Default: `$(find-pkg-share nav2_bt_navigator)/behavior_trees`
  - List of directories that hosts behavior trees XML files. It is needed to register all behavior trees as well as subtrees.

- **`default_cancel_timeout`**
  - Type: `int`
  - Default: `50`
  - Default timeout (in seconds) for BT action node cancellation requests during node halt. This value will be overwritten for a BT node if the input port “cancel_timeout” is provided.

- **`default_nav_through_poses_bt_xml`**
  - Type: `string`
  - Default: `N/A`
  - Path to the default behavior tree XML description forNavigateThroughPoses, seeBehavior Tree XML Nodesfor details on this file. New to Galactic afterNavigateThroughPoseswas added. You can use substi...

- **`default_nav_to_pose_bt_xml`**
  - Type: `string`
  - Default: `N/A`
  - Path to the default behavior tree XML description forNavigateToPose, seeBehavior Tree XML Nodesfor details on this file. This parameter used to bedefault_bt_xml_filenamepre-Galactic. You can use su...

- **`default_server_timeout`**
  - Type: `int`
  - Default: `20`
  - Default timeout value (in milliseconds) while a BT action node is waiting for acknowledgement from an action server. This value will be overwritten for a BT node if the input port “server_timeout” ...

- **`error_code_name_prefixes`**
  - Type: `vector<string>`
  - Default: `“backup”,
“compute_path”,
“dock_robot”,
“drive_on_heading”,
“follow_path”,
“nav_thru_poses”,
“nav_to_pose”,
“spin”,
“route”,
“undock_robot”,
“wait”]`
  - “backup”, “compute_path”, “dock_robot”, “drive_on_heading”, “follow_path”, “nav_thru_poses”, “nav_to_pose”, “spin”, “route”, “undock_robot”, “wait”]

- **`error_code_names`**
  - Type: `vector<string>`
  - Default: `“follow_path_error_code”]`
  - “follow_path_error_code”]

- **`filter_duration`**
  - Type: `double`
  - Default: `0.3`
  - Duration (secs) over which robot velocity should be smoothed.

- **`global_frame`**
  - Type: `string`
  - Default: `map`
  - Reference frame.

- **`introspection_mode`**
  - Type: `string`
  - Default: `“disabled”`
  - The introspection mode for services and actions. Options are “disabled”, “metadata”, “contents”.

- **`navigators`**
  - Type: `vector<string>`
  - Default: `{‘navigate_to_pose’, ‘navigate_through_poses’}`
  - New to Iron: Plugins for navigator types implementing thenav2_core::BehaviorTreeNavigatorinterface. They implement custom action servers with custom interface definitions and use that data to popul...

- **`odom_topic`**
  - Type: `string`
  - Default: `odom`
  - Topic on which odometry is published

- **`plugin_lib_names`**
  - Type: `vector<string>`
  - Default: `[“”]`
  - List of behavior tree node shared libraries. All Nav2 BT libraries are automatically included for you, so this only needs to include your new custom plugins (new to Jazzy).

- **`robot_base_frame`**
  - Type: `string`
  - Default: `base_link`
  - Robot base frame.

- **`transform_tolerance`**
  - Type: `double`
  - Default: `0.1`
  - TF transform tolerance.

- **`wait_for_service_timeout`**
  - Type: `int`
  - Default: `1000`
  - Default timeout value (in milliseconds) while Action or Service BT nodes will waiting for acknowledgement from an service or action server on BT initialization (e.g.wait_for_action_server(timeout))...

---

## Cancelassistedteleop

### CancelAssistedTeleop
*Source: https://docs.nav2.org/configuration/packages/bt-plugins/actions/CancelAssistedTeleop.html*

- **`server_timeout`**
  - Type: `double`
  - Default: `10`
  - Server timeout (ms).

- **`service_name`**
  - Type: `string`
  - Default: `N/A`
  - Service name, if not using default ofassisted_teleopdue to remapping.

---

## Cancelbackup

### CancelBackUp
*Source: https://docs.nav2.org/configuration/packages/bt-plugins/actions/CancelBackUp.html*

- **`server_timeout`**
  - Type: `double`
  - Default: `10`
  - Server timeout (ms).

- **`service_name`**
  - Type: `string`
  - Default: `N/A`
  - Service name, if not using default ofbackupdue to remapping.

---

## Cancelcomputeandtrackroute

### CancelComputeAndTrackRoute
*Source: https://docs.nav2.org/configuration/packages/bt-plugins/actions/CancelComputeAndTrackRoute.html*

- **`server_timeout`**
  - Type: `double`
  - Default: `10`
  - Server timeout (ms).

- **`service_name`**
  - Type: `string`
  - Default: `N/A`
  - Service name, if not using default ofcompute_and_track_routedue to remapping.

---

## Cancelcontrol

### CancelControl
*Source: https://docs.nav2.org/configuration/packages/bt-plugins/actions/CancelControl.html*

- **`server_timeout`**
  - Type: `double`
  - Default: `10`
  - Server timeout (ms).

- **`service_name`**
  - Type: `string`
  - Default: `N/A`
  - Service name.

---

## Cancelcoverage

### CancelCoverage
*Source: https://docs.nav2.org/configuration/packages/bt-plugins/actions/CancelCoverage.html*

- **`server_timeout`**
  - Type: `double`
  - Default: `10`
  - Server timeout (ms).

- **`service_name`**
  - Type: `string`
  - Default: `N/A`
  - Service name.

---

## Canceldriveonheading

### CancelDriveOnHeading
*Source: https://docs.nav2.org/configuration/packages/bt-plugins/actions/CancelDriveOnHeading.html*

- **`server_timeout`**
  - Type: `double`
  - Default: `10`
  - Server timeout (ms).

- **`service_name`**
  - Type: `string`
  - Default: `N/A`
  - Service name, if not using default ofdrive_on_headingdue to remapping.

---

## Cancelfollowobject

### CancelFollowObject
*Source: https://docs.nav2.org/configuration/packages/bt-plugins/actions/CancelFollowObject.html*

- **`server_timeout`**
  - Type: `double`
  - Default: `10`
  - Server timeout (ms).

- **`service_name`**
  - Type: `string`
  - Default: `N/A`
  - Service name.

---

## Cancelspin

### CancelSpin
*Source: https://docs.nav2.org/configuration/packages/bt-plugins/actions/CancelSpin.html*

- **`server_timeout`**
  - Type: `double`
  - Default: `10`
  - Server timeout (ms).

- **`service_name`**
  - Type: `string`
  - Default: `N/A`
  - Service name, if not using default ofspindue to remapping.

---

## Cancelwait

### CancelWait
*Source: https://docs.nav2.org/configuration/packages/bt-plugins/actions/CancelWait.html*

- **`server_timeout`**
  - Type: `double`
  - Default: `10`
  - Server timeout (ms).

- **`service_name`**
  - Type: `string`
  - Default: `N/A`
  - Service name, if not using default ofwaitdue to remapping.

---

## Clearcostmaparoundpose

### ClearCostmapAroundPose
*Source: https://docs.nav2.org/configuration/packages/bt-plugins/actions/ClearCostmapAroundPose.html*

- **`pose`**
  - Type: `geometry_msgs::msg::PoseStamped`
  - Default: `N/A`
  - Pose around which to clear the costmap

- **`reset_distance`**
  - Type: `double`
  - Default: `1.0`
  - Distance from the pose under which obstacles are cleared

- **`server_timeout`**
  - Type: `double`
  - Default: `10`
  - Action server timeout (ms).

- **`service_name`**
  - Type: `string`
  - Default: `N/A`
  - costmap service name responsible for clearing the costmap.

---

## Clearcostmaparoundrobot

### ClearCostmapAroundRobot
*Source: https://docs.nav2.org/configuration/packages/bt-plugins/actions/ClearCostmapAroundRobot.html*

- **`reset_distance`**
  - Type: `double`
  - Default: `1`
  - side size of the square area centered on the robot that will be cleared on the costmap (the rest of the costmap won’t)

- **`server_timeout`**
  - Type: `double`
  - Default: `10`
  - Action server timeout (ms).

- **`service_name`**
  - Type: `string`
  - Default: `N/A`
  - costmap service name responsible for clearing the costmap.

---

## Clearcostmapexceptregion

### ClearCostmapExceptRegion
*Source: https://docs.nav2.org/configuration/packages/bt-plugins/actions/ClearCostmapExceptRegion.html*

- **`reset_distance`**
  - Type: `double`
  - Default: `1`
  - side size of the square area centered on the robot that will not be cleared on the costmap (all the rest of the costmap will)

- **`server_timeout`**
  - Type: `double`
  - Default: `10`
  - Action server timeout (ms).

- **`service_name`**
  - Type: `string`
  - Default: `N/A`
  - costmap service name responsible for clearing the costmap.

---

## Clearentirecostmap

### ClearEntireCostmap
*Source: https://docs.nav2.org/configuration/packages/bt-plugins/actions/ClearEntireCostmap.html*

- **`server_timeout`**
  - Type: `double`
  - Default: `10`
  - Action server timeout (ms).

- **`service_name`**
  - Type: `string`
  - Default: `N/A`
  - costmap service name responsible for clearing the costmap.

---

## Collision Detector Node

### Collision Detector Node
*Source: https://docs.nav2.org/configuration/packages/collision_monitor/configuring-collision-detector-node.html*

- **`<polygon_name>.action_type`**
  - Type: `string`
  - Default: `N/A`
  - Onlynoneaction type is supported (more options available for collision monitor)

- **`<polygon_name>.min_points`**
  - Type: `int`
  - Default: `4`
  - Minimum number of data readings within a zone to trigger the action. Formermax_pointsparameter for Humble, that meant the maximum number of data readings within a zone to not trigger the action).mi...

- **`<polygon_name>.points`**
  - Type: `string`
  - Default: `N/A`
  - Polygon vertices, listed in"[[p1.x,p1.y],[p2.x,p2.y],[p3.x,p3.y],...]"format (e.g."[[0.5,0.25],[0.5,-0.25],[0.0,-0.25],[0.0,0.25]]"for the square in the front). Used forpolygontype. Minimum 3 point...

- **`<polygon_name>.polygon_pub_topic`**
  - Type: `string`
  - Default: `<polygon_name>`
  - Topic name to publish a polygon to. Used only ifvisualizeis true.

- **`<polygon_name>.polygon_sub_topic`**
  - Type: `string`
  - Default: `N/A`
  - Topic to listen the polygon points from. Causes an error, if not specifiedandpoints are also not specified. If bothpointsandpolygon_sub_topicare specified, the staticpointstakes priority.

- **`<polygon_name>.radius`**
  - Type: `double`
  - Default: `N/A`
  - Circle radius. Used forcircletype. Causes an error, if not specialized.

- **`<polygon_name>.type`**
  - Type: `string`
  - Default: `N/A`
  - Type of polygon shape. Available values arepolygon,circle. Causes an error, if not specialized.

- **`<polygon_name>.visualize`**
  - Type: `bool`
  - Default: `False`
  - Whether to publish the polygon in a separate topic.

- **`<sourcename>.enabled`**
  - Type: `bool`
  - Default: `True`
  - Whether to use this source for collision detection. (Can be dynamically set)

- **`<sourcename>.max_height`**
  - Type: `double`
  - Default: `0.5`
  - Maximum height the PointCloud projection to 2D space ended with. Applicable forpointcloudtype.

- **`<sourcename>.min_height`**
  - Type: `double`
  - Default: `0.05`
  - Minimum height the PointCloud projection to 2D space started from. Applicable forpointcloudtype.

- **`<sourcename>.obstacles_angle`**
  - Type: `double`
  - Default: `PI / 180 (1 degree)`
  - Angle increment (in radians) between nearby obstacle points at the range arc. Two outermost points from the field of view are not taken into account (they will always exist regardless of this value...

- **`<sourcename>.sampling_distance`**
  - Type: `double`
  - Default: `0.1`
  - Internally the polygon is sampled for collision detection. sampling_distance is the distance between sampled points of the polygon. Applicable forpolygonsource type.

- **`<sourcename>.source_timeout`**
  - Type: `double`
  - Default: `(node parametersource_timeoutvalue)`
  - Maximum time interval in which source data is considered as valid. If no new data is received within this interval, an additional warning will be displayed. Settingsource_timeout:0.0disables it. Ov...

- **`<sourcename>.topic`**
  - Type: `string`
  - Default: `“scan”`
  - Topic to listen the source data from.

- **`<sourcename>.transport_type`**
  - Type: `string`
  - Default: `“raw”`
  - Forpointclouddata, specify the transport plugin to use:

- **`<sourcename>.type`**
  - Type: `string`
  - Default: `“scan”`
  - Type of polygon shape. Could bescan,pointcloud,rangeorpolygon.

- **`allow_parameter_qos_overrides`**
  - Type: `bool`
  - Default: `true`
  - Whether to allow QoS profiles to be overwritten with parameterized values.

- **`base_frame_id`**
  - Type: `string`
  - Default: `“base_footprint”`
  - Robot base frame.

- **`base_shift_correction`**
  - Type: `bool`
  - Default: `True`
  - Whether to correct source data towards to base frame movement, considering the difference between current time and latest source time. If enabled, produces more accurate sources positioning in the ...

- **`bond_heartbeat_period`**
  - Type: `double`
  - Default: `0.25`
  - The lifecycle node bond mechanism publishing period (on the /bond topic). Disabled if inferior or equal to 0.0.

- **`draco`**
  - Lossy compression via Google.

- **`frequency`**
  - Type: `double`
  - Default: `10.0`
  - Frequency of the main loop that checks for detections.

- **`observation_sources`**
  - Type: `vector<string>`
  - Default: `N/A`
  - List of data sources (laser scanners, pointclouds, etc…). Causes an error, if not specialized.

- **`odom_frame_id`**
  - Type: `string`
  - Default: `“odom”`
  - Which frame to use for odometry.

- **`polygons`**
  - Type: `vector<string>`
  - Default: `N/A`
  - List of zones to check for data points. Causes an error, if not specialized.

- **`raw`**
  - No compression. Default; highest bandwidth usage.

- **`source_timeout`**
  - Type: `double`
  - Default: `2.0`
  - Maximum time interval in which source data is considered as valid. If no new data is received within this interval, an additional warning will be displayed. Settingsource_timeout:0.0disables it. Th...

- **`transform_tolerance`**
  - Type: `double`
  - Default: `0.1`
  - Time with which to post-date the transform that is published, to indicate that this transform is valid into the future.

- **`zlib`**
  - Lossless compression via Zlib compression.

- **`zstd`**
  - Lossless compression via Zstd compression.

---

## Collision Monitor Node

### Collision Monitor Node
*Source: https://docs.nav2.org/configuration/packages/collision_monitor/configuring-collision-monitor-node.html*

- **`<polygon_name>.action_type`**
  - Type: `string`
  - Default: `N/A`
  - Zone behavior model. Available values arestop,slowdown,limit,approach. Causes an error, if not specialized.

- **`<polygon_name>.angular_limit`**
  - Type: `double`
  - Default: `0.5`
  - Robot angular speed limit. Applicable forlimitaction type.

- **`<polygon_name>.footprint_topic`**
  - Type: `string`
  - Default: `“local_costmap/published_footprint”`
  - Topic to listen the robot footprint from. Applicable only forpolygontype andapproachaction type. If bothpointsandfootprint_topicare specified, the staticpointstakes priority.

- **`<polygon_name>.linear_limit`**
  - Type: `double`
  - Default: `0.5`
  - Robot linear speed limit. Applicable forlimitaction type.

- **`<polygon_name>.min_points`**
  - Type: `int`
  - Default: `4`
  - Minimum number of data readings within a zone to trigger the action. Formermax_pointsparameter for Humble, that meant the maximum number of data readings within a zone to not trigger the action).mi...

- **`<polygon_name>.points`**
  - Type: `string`
  - Default: `N/A`
  - Polygon vertices, listed in"[[p1.x,p1.y],[p2.x,p2.y],[p3.x,p3.y],...]"format (e.g."[[0.5,0.25],[0.5,-0.25],[0.0,-0.25],[0.0,0.25]]"for the square in the front). Used forpolygontype. Minimum 3 point...

- **`<polygon_name>.polygon_pub_topic`**
  - Type: `string`
  - Default: `<polygon_name>`
  - Topic name to publish a polygon to. Used only ifvisualizeis true.

- **`<polygon_name>.polygon_sub_topic`**
  - Type: `string`
  - Default: `N/A`
  - Forpolygontype, topic to listen the polygon points from. Forcircletype, topic to listen the circle radius from. Applicable forstop/slowdown/limitaction types. Causes an error if not specifiedandsta...

- **`<polygon_name>.polygon_subscribe_transient_local`**
  - Type: `bool`
  - Default: `False`
  - QoS durability setting for the incoming polygon or footprint topic subscription.

- **`<polygon_name>.radius`**
  - Type: `double`
  - Default: `N/A`
  - Circle radius. Used forcircletype. If not specified, the collision monitor will use dynamic polygon subscription topolygon_sub_topicfor circle radius in thestop/slowdown/limitaction types.

- **`<polygon_name>.simulation_time_step`**
  - Type: `double`
  - Default: `0.1`
  - Time iteration step for robot movement simulation during collision prediction. Higher values mean lower prediction accuracy but better performance. Applicable forapproachaction type.

- **`<polygon_name>.slowdown_ratio`**
  - Type: `double`
  - Default: `0.5`
  - Robot slowdown (share of its actual speed). Applicable forslowdownaction type.

- **`<polygon_name>.time_before_collision`**
  - Type: `double`
  - Default: `2.0`
  - Time before collision in seconds. Maximum simulation time used in collision prediction. Higher values mean lower performance. Applicable forapproachaction type.

- **`<polygon_name>.type`**
  - Type: `string`
  - Default: `N/A`
  - Type of polygon shape. Available values arepolygon,circle. Causes an error, if not specialized.

- **`<polygon_name>.visualize`**
  - Type: `bool`
  - Default: `False`
  - Whether to publish the polygon in a separate topic.

- **`<polygon_namename>.enabled`**
  - Type: `bool`
  - Default: `True`
  - Whether to use this polygon for collision monitoring. (Can be dynamically set)

- **`<sourcename>.cost_threshold`**
  - Type: `int`
  - Default: `253`
  - Forcostmapsources only. Minimum cell cost (0–255) to be treated as an obstacle. By default this matches inscribed/lethal cells (253–254) and ignores lower-cost cells.

- **`<sourcename>.enabled`**
  - Type: `bool`
  - Default: `True`
  - Whether to use this source for collision monitoring. (Can be dynamically set)

- **`<sourcename>.max_height`**
  - Type: `double`
  - Default: `0.5`
  - Maximum height the PointCloud projection to 2D space ended with. Applicable forpointcloudtype.

- **`<sourcename>.min_height`**
  - Type: `double`
  - Default: `0.05`
  - Minimum height the PointCloud projection to 2D space started from. Applicable forpointcloudtype.

- **`<sourcename>.min_range`**
  - Type: `double`
  - Default: `0.0`
  - Minimum range threshold for PointCloud points. Points closer than this distance (measured as Euclidean distance from sensor origin) will be filtered out before processing. Useful for eliminating no...

- **`<sourcename>.obstacles_angle`**
  - Type: `double`
  - Default: `PI / 180 (1 degree)`
  - Angle increment (in radians) between nearby obstacle points at the range arc. Two outermost points from the field of view are not taken into account (they will always exist regardless of this value...

- **`<sourcename>.sampling_distance`**
  - Type: `double`
  - Default: `0.1`
  - Internally the polygon is sampled for collision detection. sampling_distance is the distance between sampled points of the polygon. Applicable forpolygonsource type.

- **`<sourcename>.source_timeout`**
  - Type: `double`
  - Default: `(node parametersource_timeoutvalue)`
  - Maximum time interval in which source data is considered as valid. If no new data is received within this interval, the robot will be stopped. Settingsource_timeout:0.0disables this blocking mechan...

- **`<sourcename>.topic`**
  - Type: `string`
  - Default: `“scan”`
  - Topic to listen the source data from.

- **`<sourcename>.transport_type`**
  - Type: `string`
  - Default: `“raw”`
  - Forpointclouddata, specify the transport plugin to use:

- **`<sourcename>.treat_unknown_as_obstacle`**
  - Type: `bool`
  - Default: `true`
  - Forcostmapsources only. Iftrue, cells with cost255(NO_INFORMATION) will also be turned into obstacle points. Set tofalseif your costmap has large unknown areas you don’t want to trigger Collision M...

- **`<sourcename>.type`**
  - Type: `string`
  - Default: `“scan”`
  - Type of polygon shape. Could bescan,pointcloud,range,polygonorcostmap.

- **`<sourcename>.use_global_height`**
  - Type: `bool`
  - Default: `false`
  - Set true for pointcloud sources containing a “height” field relative to a real world ground contour. The “height” field will be used for the min and max height checks instead of the “z” field and w...

- **`<vel_poly>.<subpoly>.direction_end_angle`**
  - Type: `double`
  - Default: `PI`
  - End angle of the movement direction(for holomic robot only). Refer to theExamplesection for the common configurations. Applicable forholonomicmode only.

- **`<vel_poly>.<subpoly>.direction_start_angle`**
  - Type: `double`
  - Default: `-PI`
  - Start angle of the movement direction(for holomic robot only). Refer to theExamplesection for the common configurations. Applicable forholonomicmode only.

- **`<vel_poly>.<subpoly>.linear_max`**
  - Type: `double`
  - Default: `N/A`
  - Maximum linear velocity for the sub polygon. In holonomic mode, this is the maximum resultant velocity. Causes an error, if not specified.

- **`<vel_poly>.<subpoly>.linear_min`**
  - Type: `double`
  - Default: `N/A`
  - Minimum linear velocity for the sub polygon. In holonomic mode, this is the minimum resultant velocity. Causes an error, if not specified.

- **`<vel_poly>.<subpoly>.points`**
  - Type: `vector<string>`
  - Default: `N/A`
  - Polygon vertices, listed in"[[p1.x,p1.y],[p2.x,p2.y],[p3.x,p3.y],...]"format (e.g."[[0.5,0.25],[0.5,-0.25],[0.0,-0.25],[0.0,0.25]]"for the square in the front). Used forpolygontype. Minimum 3 point...

- **`<vel_poly>.<subpoly>.theta_max`**
  - Type: `double`
  - Default: `N/A`
  - Maximum angular velocity for the sub polygon. Causes an error, if not specified.

- **`<vel_poly>.<subpoly>.theta_min`**
  - Type: `double`
  - Default: `N/A`
  - Minimum angular velocity for the sub polygon. Causes an error, if not specified.

- **`<vel_poly>.holonomic`**
  - Type: `bool`
  - Default: `False`
  - Whether to use holonomic or non-holonomic robot model for collision prediction. For holonomic robot model, the resultant velocity will be used to compare the linear velocity range. Additionally, th...

- **`<vel_poly>.velocity_polygons`**
  - Type: `vector<string>`
  - Default: `N/A`
  - List of sub polygons for switching based on the robot’s current velocity. When velocity is covered by multiple sub polygons, the first sub polygon in the list will be used. Causes an error, if not ...

- **`allow_parameter_qos_overrides`**
  - Type: `bool`
  - Default: `true`
  - Whether to allow QoS profiles to be overwritten with parameterized values.

- **`base_frame_id`**
  - Type: `string`
  - Default: `“base_footprint”`
  - Robot base frame.

- **`base_shift_correction`**
  - Type: `bool`
  - Default: `True`
  - Whether to correct source data towards to base frame movement, considering the difference between current time and latest source time. If enabled, produces more accurate sources positioning in the ...

- **`bond_heartbeat_period`**
  - Type: `double`
  - Default: `0.25`
  - The lifecycle node bond mechanism publishing period (on the /bond topic). Disabled if inferior or equal to 0.0.

- **`Circle`**
  - is made for the best performance and could be used in the cases where the zone or robot footprint could be approximated by round shape.

- **`cmd_vel_in_topic`**
  - Type: `string`
  - Default: `“cmd_vel_smoothed”`
  - Inputcmd_veltopic with desired robot velocity. Please note, pre-Jazzythis was set tocmd_vel_rawby default.

- **`cmd_vel_out_topic`**
  - Type: `string`
  - Default: `“cmd_vel”`
  - Outputcmd_veltopic with output produced by Collision Monitor velocities.

- **`draco`**
  - Lossy compression via Google.

- **`enable_stamped_cmd_vel`**
  - Type: `bool`
  - Default: `true`
  - Whether to use geometry_msgs::msg::Twist or geometry_msgs::msg::TwistStamped velocity data. True uses TwistStamped, false uses Twist. Note: This parameter is defaultfalsein Jazzy or older! Kilted o...

- **`enabled`**
  - Type: `bool`
  - Default: `True`
  - Sets the initial state. This can come in handy when the robot is docked/inside any of the zones at startup and the node needs to be disabled then. Please note that is not a dynamic parameter, there...

- **`observation_sources`**
  - Type: `vector<string>`
  - Default: `N/A`
  - List of data sources (laser scanners, pointclouds, etc…). Causes an error, if not specialized.

- **`odom_frame_id`**
  - Type: `string`
  - Default: `“odom”`
  - Which frame to use for odometry.

- **`polygons`**
  - Type: `vector<string>`
  - Default: `N/A`
  - List of zones (stop/slowdown/limit bounding boxes, footprint, approach circle, etc…). Causes an error, if not specialized.

- **`raw`**
  - No compression. Default; highest bandwidth usage.

- **`source_timeout`**
  - Type: `double`
  - Default: `2.0`
  - Maximum time interval in which source data is considered as valid. If no new data is received within this interval, the robot will be stopped. Settingsource_timeout:0.0disables this blocking mechan...

- **`state_topic`**
  - Type: `string`
  - Default: `“”`
  - Output the currently activated polygon action type and name. Optional parameter. No publisher will be created if it is unspecified.

- **`stop_pub_timeout`**
  - Type: `double`
  - Default: `1.0`
  - Timeout, after which zero-velocity ceases to be published. It could be used for other overrode systems outside Nav2 are trying to bring the robot out of a state close to a collision, or to allow a ...

- **`transform_tolerance`**
  - Type: `double`
  - Default: `0.1`
  - Time with which to post-date the transform that is published, to indicate that this transform is valid into the future.

- **`use_realtime_priority`**
  - Type: `bool`
  - Default: `false`
  - Adds soft real-time prioritization to the controller server to better ensure resources to time sensitive portions of the codebase. This will set the controller’s execution thread to a higher priori...

- **`VelocityPolygon`**
  - allow switching of polygons based on the command velocity. This is useful for robots to set different safety zones based on their velocity (e.g. a robot that has a larger safety zone when moving at...

- **`zlib`**
  - Lossless compression via Zlib compression.

- **`zstd`**
  - Lossless compression via Zstd compression.

---

## Computeandtrackroute

### ComputeAndTrackRoute
*Source: https://docs.nav2.org/configuration/packages/bt-plugins/actions/ComputeAndTrackRoute.html*

- **`error_code_id`**
  - Type: `uint16`
  - Default: `N/A`
  - Compute route error code. SeeComputeAndTrackRouteaction message for the enumerated set of error codes.

- **`error_msg`**
  - Type: `string`
  - Default: `N/A`
  - Compute route error message. SeeComputeAndTrackRouteaction message for the enumerated set of error codes.

- **`execution_time`**
  - Type: `builtin_interfaces::msg::Duration`
  - Default: `N/A`
  - Time it took to compute the route.

- **`goal`**
  - Type: `geometry_msgs::msg::PoseStamped`
  - Default: `N/A`
  - Goal pose. Takes in a blackboard variable, e.g. “{goal}”.

- **`goal_id`**
  - Type: `int`
  - Default: `N/A`
  - Goal node ID to use.

- **`server_name`**
  - Type: `string`
  - Default: `N/A`
  - Action server name.

- **`server_timeout`**
  - Type: `double`
  - Default: `10`
  - Action server timeout (ms).

- **`start`**
  - Type: `geometry_msgs::msg::PoseStamped`
  - Default: `N/A`
  - Start pose. Optional. Only used if not left empty. Takes in a blackboard variable, e.g. “{start}”.

- **`start_id`**
  - Type: `int`
  - Default: `N/A`
  - Start node ID to use.

- **`use_poses`**
  - Type: `bool`
  - Default: `false`
  - Whether to use the start and goal poses or start and goal node IDs.

- **`use_start`**
  - Type: `bool`
  - Default: `false`
  - Whether to use the start or use TF to obtain the robot’s start pose.

---

## Computecoveragepath

### ComputeCoveragePath
*Source: https://docs.nav2.org/configuration/packages/bt-plugins/actions/ComputeCoveragePath.html*

- **`coverage_path`**
  - Type: `vector<PathComponents>`
  - Default: `N/A`
  - An ordered set of swaths and turns corresponding to the coverage path when its important to distinguish between turns and swaths for applications. Aopennav_coverage::utils::PathComponentsIteratorob...

- **`error_code_id`**
  - Type: `uint16`
  - Default: `N/A`
  - Compute coverage error code. SeeComputeCoveragePathaction message for the enumerated set of error codes.

- **`error_msg`**
  - Type: `string`
  - Default: `N/A`
  - Compute coverage error message. SeeComputeCoveragePathaction message for the enumerated set of error codes.

- **`file_field`**
  - Type: `string`
  - Default: `N/A`
  - The filepath to the field’s GML file to use, if not specifying the field viapolygons

- **`file_field_id`**
  - Type: `int`
  - Default: `0`
  - The ID of the field in the GML File to use, if multiple exist in the same file. This is the ordered number of the fields in the file.

- **`generate_headland`**
  - Type: `bool`
  - Default: `true`
  - Whether or not to generate a headland of the field or polygon to compute coverage of

- **`generate_path`**
  - Type: `bool`
  - Default: `true`
  - Whether or not to generate a path, e.g. adding path connectors to the ordered route

- **`generate_route`**
  - Type: `bool`
  - Default: `true`
  - Whether or not to generate a route, e.g. an ordered set of swaths

- **`nav_path`**
  - Type: `nav_msgs::msg::Path`
  - Default: `N/A`
  - Path created by action server in the form of a navigation path. Takes in a blackboard variable, e.g. “{path}”.

- **`polygons`**
  - Type: `vector<geometry_msgs::msg::Polygon>`
  - Default: `N/A`
  - The polygons of the field, if not specifying via a GML file. The first polygon should be the outermost region, whereas additional polygons are voids.

- **`polygons_frame_id`**
  - Type: `string`
  - Default: `“map”`
  - The polygon’s frame ID, since the GML file provides the frame ID for its format, this is the frame ID for user-defined inputpolygons.

---

## Computepaththroughposes

### ComputePathThroughPoses
*Source: https://docs.nav2.org/configuration/packages/bt-plugins/actions/ComputePathThroughPoses.html*

- **`error_code_id`**
  - Type: `uint16`
  - Default: `N/A`
  - Compute path through poses error code. SeeComputePathThroughPosesaction message for the enumerated set of error codes.

- **`error_msg`**
  - Type: `string`
  - Default: `N/A`
  - Compute path through poses error message. SeeComputePathThroughPosesaction message for the enumerated set of error codes.

- **`goals`**
  - Type: `nav_msgs::msg::Goals`
  - Default: `N/A`
  - Goal poses. Takes in a blackboard variable, e.g. “{goals}”.

- **`last_reached_index`**
  - Type: `int16`
  - Default: `-1`
  - In the case of a partial plan, index of the last reached pose from the goals list. Otherwise -1 which also corresponds to ComputePathThroughPosesResult::ALL_GOALS if a full plan through all the goa...

- **`path`**
  - Type: `nav_msgs::msg::Path`
  - Default: `N/A`
  - Path created by action server. Takes in a blackboard variable, e.g. “{path}”.

- **`planner_id`**
  - Type: `string`
  - Default: `N/A`
  - Mapped name to the planner plugin type to use, e.g. GridBased.

- **`server_name`**
  - Type: `string`
  - Default: `N/A`
  - Action server name.

- **`server_timeout`**
  - Type: `double`
  - Default: `10`
  - Action server timeout (ms).

- **`start`**
  - Type: `geometry_msgs::msg::PoseStamped`
  - Default: `N/A`
  - Start pose. Optional. Only used if not left empty. Takes in a blackboard variable, e.g. “{start}”.

---

## Computepathtopose

### ComputePathToPose
*Source: https://docs.nav2.org/configuration/packages/bt-plugins/actions/ComputePathToPose.html*

- **`error_code_id`**
  - Type: `uint16`
  - Default: `N/A`
  - Compute path to pose error code. SeeComputePathToPoseaction message for the enumerated set of error codes.

- **`error_msg`**
  - Type: `string`
  - Default: `N/A`
  - Compute path to pose error message. SeeComputePathToPoseaction message for the enumerated set of error codes.

- **`goal`**
  - Type: `geometry_msgs::msg::PoseStamped`
  - Default: `N/A`
  - Goal pose. Takes in a blackboard variable, e.g. “{goal}”.

- **`path`**
  - Type: `nav_msgs::msg::Path`
  - Default: `N/A`
  - Path created by action server. Takes in a blackboard variable, e.g. “{path}”.

- **`planner_id`**
  - Type: `string`
  - Default: `N/A`
  - Mapped name to the planner plugin type to use, e.g. GridBased.

- **`server_name`**
  - Type: `string`
  - Default: `N/A`
  - Action server name.

- **`server_timeout`**
  - Type: `double`
  - Default: `10`
  - Action server timeout (ms).

- **`start`**
  - Type: `geometry_msgs::msg::PoseStamped`
  - Default: `N/A`
  - Start pose. Optional. Used as the planner start pose instead of the current robot pose, ifuse_startis not false (i.e. not provided or set to true). Takes in a blackboard variable, e.g. “{start}”.

- **`use_start`**
  - Type: `geometry_msgs::msg::PoseStamped`
  - Default: `N/A`
  - Optional. For using or not using (i.e. ignoring) the provided start posestart. Takes in a blackboard variable, e.g. “{use_start}”.

---

## Computeroute

### ComputeRoute
*Source: https://docs.nav2.org/configuration/packages/bt-plugins/actions/ComputeRoute.html*

- **`error_code_id`**
  - Type: `uint16`
  - Default: `N/A`
  - Compute route error code. SeeComputeRouteaction message for the enumerated set of error codes.

- **`error_msg`**
  - Type: `string`
  - Default: `N/A`
  - Compute route error message. SeeComputeRouteaction message for the enumerated set of error codes.

- **`goal`**
  - Type: `geometry_msgs::msg::PoseStamped`
  - Default: `N/A`
  - Goal pose. Takes in a blackboard variable, e.g. “{goal}”.

- **`goal_id`**
  - Type: `int`
  - Default: `N/A`
  - Goal node ID to use.

- **`path`**
  - Type: `nav_msgs::msg::Path`
  - Default: `N/A`
  - Path created by action server. Takes in a blackboard variable, e.g. “{path}”.

- **`planning_time`**
  - Type: `builtin_interfaces::msg::Duration`
  - Default: `N/A`
  - Time it took to compute the route.

- **`route`**
  - Type: `nav2_msgs::msg::Route`
  - Default: `N/A`
  - Route created by action server. Takes in a blackboard variable, e.g. “{route}”.

- **`server_name`**
  - Type: `string`
  - Default: `N/A`
  - Action server name.

- **`server_timeout`**
  - Type: `double`
  - Default: `10`
  - Action server timeout (ms).

- **`start`**
  - Type: `geometry_msgs::msg::PoseStamped`
  - Default: `N/A`
  - Start pose. Optional. Only used if not left empty. Takes in a blackboard variable, e.g. “{start}”.

- **`start_id`**
  - Type: `int`
  - Default: `N/A`
  - Start node ID to use.

- **`use_poses`**
  - Type: `bool`
  - Default: `false`
  - Whether to use the start and goal poses or start and goal node IDs.

- **`use_start`**
  - Type: `bool`
  - Default: `false`
  - Whether to use the start or use TF to obtain the robot’s start pose.

---

## Concatenatepaths

### ConcatenatePaths
*Source: https://docs.nav2.org/configuration/packages/bt-plugins/actions/ConcatenatePaths.html*

- **`input_path1`**
  - Type: `nav_msgs/Path`
  - Default: `N/A`
  - First path to concatenate.

- **`input_path2`**
  - Type: `nav_msgs/Path`
  - Default: `N/A`
  - Second path to concatenate.

---

## Constrained Smoother

### Constrained smoother
*Source: https://docs.nav2.org/configuration/packages/configuring-constrained-smoother.html*

- **`cost_check_points`**
  - Type: `array of double`
  - Default: `[]`
  - Points in robot frame to grab costmap values from. Format: [x1, y1, weight1, x2, y2, weight2, …].IMPORTANT: Requires much higher number of optimizer iterations to actually improve the path. Use onl...

- **`cusp_zone_length`**
  - Type: `double`
  - Default: `2.5`
  - Length of the section around cusp in which nodes usew_cost_cusp_multiplier(w_cost rises gradually inside the zone towards the cusp point, whose costmap weight eqals w_cost*w_cost_cusp_multiplier)

- **`keep_goal_orientation`**
  - Type: `bool`
  - Default: `true`
  - Whether to prevent the goal orientation from being smoothed

- **`keep_start_orientation`**
  - Type: `bool`
  - Default: `true`
  - Whether to prevent the start orientation from being smoothed

- **`minimum_turning_radius`**
  - Type: `double`
  - Default: `0.4`
  - Minimum turning radius the robot can perform. Can be set to 0.0 (or w_curve can be set to 0.0 with the same effect) for diff-drive/holonomic robots

- **`optimizer.debug_optimizer`**
  - Type: `bool`
  - Default: `false`
  - Whether to print optimizer debug info

- **`optimizer.fn_tol`**
  - Type: `bool`
  - Default: `1e-7`
  - Function tolerance optimization termination criterion

- **`optimizer.gradient_tol`**
  - Type: `bool`
  - Default: `1e-10`
  - Gradient tolerance optimization termination criterion

- **`optimizer.linear_solver_type`**
  - Type: `string`
  - Default: `“SPARSE_NORMAL_CHOLESKY”`
  - Linear solver type to be used by optimizer. Valid values areSPARSE_NORMAL_CHOLESKYandDENSE_QR

- **`optimizer.max_iterations`**
  - Type: `int`
  - Default: `100`
  - Maximum number of optimizer iterations

- **`optimizer.param_tol`**
  - Type: `bool`
  - Default: `1e-15`
  - Parameter tolerance optimization termination criterion

- **`path_downsampling_factor`**
  - Type: `int`
  - Default: `1`
  - Every n-th node of the path is taken for optimization. Useful for speed-up

- **`path_upsampling_factor`**
  - Type: `int`
  - Default: `1`
  - Upsampling factor for refining. 0 - path remains downsampled (seepath_downsampling_factor), 1 - path is upsampled back to original granularity using cubic bezier, 2… - more upsampling

- **`reversing_enabled`**
  - Type: `bool`
  - Default: `true`
  - Whether to detect forward/reverse direction and cusps. Should be set to false for paths without orientations assigned

- **`w_cost`**
  - Type: `double`
  - Default: `0.015`
  - Weight to steer robot away from collision and cost

- **`w_cost_cusp_multiplier`**
  - Type: `double`
  - Default: `3.0`
  - Option to use higher weight during forward/reverse direction change, helping optimizer to converge or add an extra obstacle avoidance at these problematic segments. Following image depicts improvem...

- **`w_curve`**
  - Type: `double`
  - Default: `30.0`
  - Weight to enforce minimum_turning_radius

- **`w_dist`**
  - Type: `double`
  - Default: `0.0`
  - Weight to bind path to original as optional replacement for cost weight

- **`w_smooth`**
  - Type: `double`
  - Default: `2000000.0`
  - Weight to maximize smoothness of path

---

## Controller

### DWB Controller
*Source: https://docs.nav2.org/configuration/packages/dwb-params/controller.html*

- **`<dwbplugin>.critics`**
  - Type: `vector<string>`
  - Default: `N/A`
  - List of critic plugins to use.

- **`<dwbplugin>.debug_trajectory_details`**
  - Type: `bool`
  - Default: `false`
  - Publish debug information (on what topic???).

- **`<dwbplugin>.default_critic_namespaces`**
  - Type: `vector<string>`
  - Default: `[“dwb_critics”]`
  - Namespaces to load critics in.

- **`<dwbplugin>.goal_checker_name`**
  - Type: `string`
  - Default: `“dwb_plugins::SimpleGoalChecker”`
  - Goal checker plugin name.

- **`<dwbplugin>.goal_distance_bias`**
  - Type: `double`
  - Default: `N/A`
  - Old version of GoalAlign.scale, use that instead.

- **`<dwbplugin>.GoalAlign.scale`**
  - Type: `double`
  - Default: `24.0`
  - Scale for goal align critic, overriding local default.

- **`<dwbplugin>.GoalDist.scale`**
  - Type: `double`
  - Default: `24.0`
  - Scale for goal distance critic, overriding local default.

- **`<dwbplugin>.max_scaling_factor`**
  - Type: `double`
  - Default: `N/A`
  - Old version of ObstacleFootprint.max_scaling_factor, use that instead.

- **`<dwbplugin>.occdist_scale`**
  - Type: `double`
  - Default: `N/A`
  - Old version of ObstacleFootprint.scale, use that instead.

- **`<dwbplugin>.path_distance_bias`**
  - Type: `double`
  - Default: `N/A`
  - Old version of PathAlign.scale, use that instead.

- **`<dwbplugin>.PathAlign.scale`**
  - Type: `double`
  - Default: `32.0`
  - Scale for path align critic, overriding local default.

- **`<dwbplugin>.PathDist.scale`**
  - Type: `double`
  - Default: `32.0`
  - Scale for path distance critic, overriding local default.

- **`<dwbplugin>.scaling_speed`**
  - Type: `double`
  - Default: `N/A`
  - Old version of ObstacleFootprint.scaling_speed, use that instead.

- **`<dwbplugin>.short_circuit_trajectory_evaluation`**
  - Type: `bool`
  - Default: `true`
  - Stop evaluating scores after best score is found.

- **`<dwbplugin>.trajectory_generator_name`**
  - Type: `string`
  - Default: `“dwb_plugins::StandardTrajectoryGenerator”`
  - Trajectory generator plugin name.

---

## Controller Server

### Controller Server
*Source: https://docs.nav2.org/configuration/packages/configuring-controller-server.html*

- **`allow_parameter_qos_overrides`**
  - Type: `bool`
  - Default: `true`
  - Whether to allow QoS profiles to be overwritten with parameterized values.

- **`bond_heartbeat_period`**
  - Type: `double`
  - Default: `0.25`
  - The lifecycle node bond mechanism publishing period (on the /bond topic). Disabled if inferior or equal to 0.0.

- **`controller_frequency`**
  - Type: `double`
  - Default: `20.0`
  - Frequency to run controller (Hz).

- **`controller_plugins`**
  - Type: `vector<string>`
  - Default: `[‘FollowPath’]`
  - List of mapped names for controller plugins for processing requests and parameters.

- **`costmap_update_timeout`**
  - Type: `double`
  - Default: `0.3`
  - The timeout value (seconds) for the costmap to be fully updated before a control effort can be computed.

- **`enable_stamped_cmd_vel`**
  - Type: `bool`
  - Default: `true`
  - Whether to use geometry_msgs::msg::Twist or geometry_msgs::msg::TwistStamped velocity data. True uses TwistStamped, false uses Twist. Note: This parameter is defaultfalsein Jazzy or older! Kilted o...

- **`failure_tolerance`**
  - Type: `double`
  - Default: `0.0`
  - The maximum duration in seconds the called controller plugin can fail (i.e. thecomputeVelocityCommandsfunction of the plugin throwing an exception) before thenav2_msgs::action::FollowPathaction fai...

- **`goal_checker_plugins`**
  - Type: `vector<string>`
  - Default: `[“goal_checker”]`
  - Mapped name for goal checker plugin for checking goal is reached. When the number of the plugins is more than 2, eachFollowPathaction needs to specify the goal checker plugin name with itsgoal_chec...

- **`introspection_mode`**
  - Type: `string`
  - Default: `“disabled”`
  - The introspection mode for services and actions. Options are “disabled”, “metadata”, “contents”.

- **`min_theta_velocity_threshold`**
  - Type: `double`
  - Default: `0.0001`
  - The controller server filters the velocity portion of the odometry messages received before sending them to the controller plugin. Odometry values below this threshold (in rad/s) will be set to 0.0.

- **`min_x_velocity_threshold`**
  - Type: `double`
  - Default: `0.0001`
  - The controller server filters the velocity portion of the odometry messages received before sending them to the controller plugin. Odometry values below this threshold (in m/s) will be set to 0.0.

- **`min_y_velocity_threshold`**
  - Type: `double`
  - Default: `0.0001`
  - The controller server filters the velocity portion of the odometry messages received before sending them to the controller plugin. Odometry values below this threshold (in m/s) will be set to 0.0. ...

- **`odom_duration`**
  - Type: `double`
  - Default: `0.3`
  - Time (s) to buffer odometry commands to estimate the robot speed.

- **`odom_topic`**
  - Type: `string`
  - Default: `“odom”`
  - Topic to get instantaneous measurement of speed from.

- **`path_handler_plugins`**
  - Type: `vector<string>`
  - Default: `[“PathHandler”]`
  - Mapped name for path handler plugin for processing path from the planner. When the number of the plugins is more than 2, eachFollowPathaction needs to specify the path handler plugin name with itsp...

- **`progress_checker_plugins`**
  - Type: `vector<string>`
  - Default: `[“progress_checker”]`
  - Mapped name for progress checker plugin for checking progress made by robot. Formerlyprogress_checker_pluginfor Humble and older with a single string plugin.

- **`publish_zero_velocity`**
  - Type: `bool`
  - Default: `true`
  - Whether to publish a zero velocity command on goal exit. This is useful for stopping the robot when a goal terminates.

- **`search_window`**
  - Type: `double`
  - Default: `2.0`
  - How far (in meters) along the path the searching algorithm will look for the closest point.

- **`speed_limit_topic`**
  - Type: `string`
  - Default: `“speed_limit”`
  - Speed limiting topic name to subscribe. This could be published by Speed Filter (please refer toSpeed Filter Parametersconfiguration page). You can also use this without the Speed Filter as well if...

- **`use_realtime_priority`**
  - Type: `bool`
  - Default: `false`
  - Adds soft real-time prioritization to the controller server to better ensure resources to time sensitive portions of the codebase. This will set the controller’s execution thread to a higher priori...

- **`“FollowPath”`**

- **`“goal_checker”`**

- **`“path_handler”`**

- **`“progress_checker”`**

---

## Controllerselector

### ControllerSelector
*Source: https://docs.nav2.org/configuration/packages/bt-plugins/actions/ControllerSelector.html*

- **`default_controller`**
  - Type: `string`
  - Default: `N/A`
  - The default value for the selected Controller if no message is received from the input topic.

- **`selected_controller`**
  - Type: `string`
  - Default: `N/A`
  - The output selected Controller id. This selected_controller string is usually passed to the FollowPath behavior via the controller_id input port.

- **`topic_name`**
  - Type: `string`
  - Default: `controller_selector`
  - The name of the topic used to received select command messages. This is used to support multiple ControllerSelector nodes.

---

## Costmap Filter Info Server

### Costmap Filter Info Server
*Source: https://docs.nav2.org/configuration/packages/map_server/configuring-costmap-filter-info-server.html*

- **`allow_parameter_qos_overrides`**
  - Type: `bool`
  - Default: `true`
  - Whether to allow QoS profiles to be overwritten with parameterized values.

- **`base`**
  - Type: `double`
  - Default: `0.0`
  - Base ofOccupancyGridmask value -> filter space value linear conversion which is being proceeded as:filter_space_value=base+multiplier*mask_value

- **`bond_heartbeat_period`**
  - Type: `double`
  - Default: `0.25`
  - The lifecycle node bond mechanism publishing period (on the /bond topic). Disabled if inferior or equal to 0.0.

- **`filter_info_topic`**
  - Type: `string`
  - Default: `“costmap_filter_info”`
  - Topic to publish costmap filter information to.

- **`mask_topic`**
  - Type: `string`
  - Default: `“filter_mask”`
  - Topic to publish filter mask to. The value of this parameter should be in accordance withtopic_nameparameter of Map Server tuned to filter mask publishing.

- **`multiplier`**
  - Type: `double`
  - Default: `1.0`
  - Multiplier ofOccupancyGridmask value -> filter space value linear conversion which is being proceeded as:filter_space_value=base+multiplier*mask_value

- **`type`**
  - Type: `int`
  - Default: `0`
  - Type of costmap filter used. This is an enum for the type of filter this should be interpreted as. We provide the following pre-defined types:0: keepout zones / preferred lanes filter1: speed filte...

---

## Costmaps

### Costmap 2D
*Source: https://docs.nav2.org/configuration/packages/configuring-costmaps.html*

- **`allow_parameter_qos_overrides`**
  - Type: `bool`
  - Default: `true`
  - Whether to allow QoS profiles to be overwritten with parameterized values.

- **`always_send_full_costmap`**
  - Type: `bool`
  - Default: `False`
  - Whether to send full costmap every update, rather than updates.

- **`filters`**
  - Type: `vector<string>`
  - Default: `{}`
  - List of mapped costmap filter names for parameter namespaces and names.

- **`footprint`**
  - Type: `vector<double>`
  - Default: `“[]”`
  - Ordered set of footprint points passed in as a string, must be closed set. For example, the following defines a square base with side lengths of 0.2 metersfootprint: “[ [0.1, 0.1], [0.1, -0.1], [-0...

- **`footprint_padding`**
  - Type: `double`
  - Default: `0.01`
  - Amount to pad footprint (m).

- **`global_frame`**
  - Type: `string`
  - Default: `“map”`
  - Reference frame.

- **`height`**
  - Type: `int`
  - Default: `5`
  - Height of costmap (m).

- **`initial_transform_timeout`**
  - Type: `double`
  - Default: `60.0`
  - Time to wait for the transform from robot base frame to global frame to become available. If exceeded, the  configuration stage is aborted.

- **`inscribed_obstacle_cost_value`**
  - Type: `int`
  - Default: `99`
  - The OccupancyGrid values that representsINSCRIBED_INFLATED_OBSTACLEduring costmap conversion operations.

- **`introspection_mode`**
  - Type: `string`
  - Default: `“disabled”`
  - The introspection mode for services and actions. Options are “disabled”, “metadata”, “contents”.

- **`lethal_cost_threshold`**
  - Type: `int`
  - Default: `100`
  - Minimum cost of an occupancy grid map to be considered a lethal obstacle.

- **`map_vis_z`**
  - Type: `double`
  - Default: `0.0`
  - The height of map, allows to avoid rviz visualization flickering at -0.008

- **`origin_x`**
  - Type: `double`
  - Default: `0.0`
  - X origin of the costmap relative to width (m).

- **`origin_y`**
  - Type: `double`
  - Default: `0.0`
  - Y origin of the costmap relative to height (m).

- **`plugins`**
  - Type: `vector<string>`
  - Default: `{“static_layer”, “obstacle_layer”, “inflation_layer”}`
  - List of mapped plugin names for parameter namespaces and names.

- **`publish_frequency`**
  - Type: `double`
  - Default: `1.0`
  - Frequency to publish costmap to topic.

- **`resolution`**
  - Type: `double`
  - Default: `0.1`
  - Resolution of 1 pixel of the costmap, in meters.

- **`robot_base_frame`**
  - Type: `string`
  - Default: `“base_link”`
  - Robot base frame.

- **`robot_radius`**
  - Type: `double`
  - Default: `0.1`
  - Robot radius to use, if footprint coordinates not provided. If this parameter is set,isPathValidwill do circular collision checking.

- **`rolling_window`**
  - Type: `bool`
  - Default: `False`
  - Whether costmap should roll with robot base frame.

- **`subscribe_to_stamped_footprint`**
  - Type: `bool`
  - Default: `False`
  - If true, the costmap will subscribe to PolygonStamped footprint messages instead of Polygon messages. This allows the footprint to include timestamp and frame information, which can be useful for a...

- **`track_unknown_space`**
  - Type: `bool`
  - Default: `False`
  - If false, treats unknown space as free space, else as unknown space.

- **`transform_tolerance`**
  - Type: `double`
  - Default: `0.3`
  - TF transform tolerance.

- **`trinary_costmap`**
  - Type: `bool`
  - Default: `True`
  - If occupancy grid map should be interpreted as only 3 values (free, occupied, unknown) or with its stored values.

- **`unknown_cost_value`**
  - Type: `int`
  - Default: `255`
  - Cost of unknown space if tracking it.

- **`update_frequency`**
  - Type: `double`
  - Default: `5.0`
  - Costmap update frequency.

- **`use_maximum`**
  - Type: `bool`
  - Default: `False`
  - whether when combining costmaps to use the maximum cost or override.

- **`width`**
  - Type: `int`
  - Default: `5`
  - Width of costmap (m).

- **`“inflation_layer”`**

- **`“obstacle_layer”`**

- **`“static_layer”`**

---

## Coverage Server

### Coverage Server
*Source: https://docs.nav2.org/configuration/packages/configuring-coverage-server.html*

- **`coordinates_in_cartesian_frame`**
  - Type: `bool`
  - Default: `true`
  - Whether or not requests coming into the server will be in cartesian (e.g. meters) or GPS coordinates. If GPS, they are automatically converted into UTM frame (for meters) to compute the coverage pa...

- **`default_allow_overlap`**
  - Type: `bool`
  - Default: `false`
  - Whether, by default, to allow overlapping of the last row in the coverage plan to obtain coverage at the far edge. Only foropennav_coverage.

- **`default_custom_order`**
  - Type: `vector<int>`
  - Default: `N/A`
  - The default custom swath order for the route planner in theCUSTOMmode. The length of this custom order must be>=swaths.size(). Only relevant when using theCUSTOMRoute Type.

- **`default_headland_type`**
  - Type: `string`
  - Default: `“CONSTANT”`
  - The default headland generation method. Constant is the only valid method currently. Only foropennav_coverage.

- **`default_headland_width`**
  - Type: `double`
  - Default: `2.0`
  - The default headland width to remove from the field or zone from coverage planning. Only foropennav_coverage.

- **`default_offset`**
  - Type: `double`
  - Default: `0.0`
  - Offset to use for computing swaths from annotated rows. Only foropennav_row_coverage.

- **`default_path_continuity_type`**
  - Type: `string`
  - Default: `“CONTINUOUS”`
  - Default continuity type when computing paths to connect routes together. OptionsDISCONTINUOUS,CONTINUOUS.

- **`default_path_type`**
  - Type: `string`
  - Default: `“DUBIN”`
  - Default type when computing paths to connect routes together using curves. Options:DUBIN,REEDS_SHEPP.

- **`default_route_type`**
  - Type: `string`
  - Default: `“BOUSTROPHEDON”`
  - Default order when computing routes to order swaths. Options:BOUSTROPHEDON,SNAKE,SPIRAL,CUSTOM

- **`default_spiral_n`**
  - Type: `int`
  - Default: `4`
  - Default number of swaths to skip and double back on to create a spiral pattern in the route. Only relevant when using theSPIRALRoute Type.SNAKEis a special case when Spiral N = 2.

- **`default_step_angle`**
  - Type: `double`
  - Default: `1.7e-2`
  - The angular step size to try to find the optimal angle for route objective, when usingBRUTE_FORCEswath angle type. Default is 1 deg in rad units. Only foropennav_coverage.

- **`default_swath_angle`**
  - Type: `double`
  - Default: `N/A`
  - The optimal angle for route objective, when usingSET_ANGLEswath angle type. Default is 1 deg in rad units. Only foropennav_coverage.

- **`default_swath_angle_type`**
  - Type: `double`
  - Default: `1.7e-2`
  - Mode to use for generating swaths. Need to find optimal angle by the swath generator objectives, if not given. Options:BRUTE_FORCE,SET_ANGLE. Only foropennav_coverage.

- **`default_swath_type`**
  - Type: `string`
  - Default: `“LENGTH”`
  - Objective to use to score swath generation candidates at different angles when usingBRUTE_FORCEswath angle type. Options:LENGTH,COVERAGE,NUMBERforopennav_coverage. Option:OFFSET,CENTER,ROWSARESWATH...

- **`default_turn_point_distance`**
  - Type: `double`
  - Default: `0.1`
  - Distance between points on the plan and route for sending back in paths (e.g. 0.1m). This impacts the density of the output turn paths and the overall nav paths.

- **`linear_curv_change`**
  - Type: `double`
  - Default: `2.0`
  - The robot’s maximum linear curvature change for computing paths connecting route swaths (1/m^2)

- **`min_turning_radius`**
  - Type: `double`
  - Default: `0.4`
  - The robot’s minimum turning radius for computing paths connecting route swaths (m)

- **`operation_width`**
  - Type: `double`
  - Default: `2.5`
  - The robot’s operational width (cleaning, planting, etc) for computing coverage swath distances

- **`order_ids`**
  - Type: `bool`
  - Default: `0.0`
  - Foropennav_row_coverage, whether to reorder the parsed rows in the order of theirids.

- **`robot_width`**
  - Type: `double`
  - Default: `2.1`
  - The robot’s width in meters.

---

## Denoise

### Denoise Layer Parameters
*Source: https://docs.nav2.org/configuration/packages/costmap-plugins/denoise.html*

- **`<denoiselayer>.enabled`**
  - Type: `bool`
  - Default: `True`
  - Whether it is enabled.

- **`<denoiselayer>.group_connectivity_type`**
  - Type: `int`
  - Default: `8`
  - Obstacles connectivity type (is the way in which obstacles relate to their neighbors). Must be 4 or 8.4 - adjacent obstacles are connected horizontally and vertically.8 - adjacent obstacles are con...

- **`<denoiselayer>.minimal_group_size`**
  - Type: `int`
  - Default: `2`
  - The minimum number of adjacent obstacles that should not be discarded as noise.If 1 or less, all obstacles will be kept.If 2, standalone obstacles (without neighbors in adjacent cells) will be remo...

---

## Distancecontroller

### DistanceController
*Source: https://docs.nav2.org/configuration/packages/bt-plugins/decorators/DistanceController.html*

- **`distance`**
  - Type: `double`
  - Default: `1.0`
  - The distance travelled to trigger an action such as planning a path (m).

- **`global_frame`**
  - Type: `string`
  - Default: `“map”`
  - Reference frame.

- **`robot_base_frame`**
  - Type: `string`
  - Default: `“base_link”`
  - Robot base frame.

---

## Distancetraveled

### DistanceTraveled
*Source: https://docs.nav2.org/configuration/packages/bt-plugins/conditions/DistanceTraveled.html*

- **`distance`**
  - Type: `double`
  - Default: `1.0`
  - The distance that must travel before returning success (m).

- **`global_frame`**
  - Type: `string`
  - Default: `“map”`
  - Reference frame.

- **`robot_base_frame`**
  - Type: `string`
  - Default: `“base_link”`
  - Robot base frame.

- **`transform_tolerance`**
  - Defined and declared inBehavior-Tree Navigator.

---

## Docking Server

### Docking Server
*Source: https://docs.nav2.org/configuration/packages/configuring-docking-server.html*

- **`<dock_name>.charging_threshold`**
  - Type: `double`
  - Default: `0.5`
  - Threshold of current in battery state above whichisCharging()=true.

- **`<dock_name>.detector_service_name`**
  - Type: `string`
  - Default: `“”`
  - Optionalstd_srvs/Triggerservice invoked when detection starts or stops viastartDetectionProcess/stopDetectionProcessif detection method accepts a service call to start and stop.

- **`<dock_name>.detector_service_timeout`**
  - Type: `double`
  - Default: `5.0`
  - Timeout (s) to wait fordetector_service_nameto become available and respond.

- **`<dock_name>.dock_direction`**
  - Type: `string`
  - Default: `“forward”`
  - Whether the robot is docking with the dock forward or backward in motion. This is the replacement for the deprecateddock_backwardsparameter. Options are “forward” or “backward”.

- **`<dock_name>.docking_threshold`**
  - Type: `double`
  - Default: `0.05`
  - If not using stall detection, the pose threshold to the docking pose whereisDocked()=true.

- **`<dock_name>.external_detection_rotation_pitch`**
  - Type: `double`
  - Default: `1.57`
  - Pitch offset from detected pose for docking pose (rad). Note: The external detection rotation angles are setup to work out of the box with Apriltags detectors inimage_procandisaac_ros.

- **`<dock_name>.external_detection_rotation_roll`**
  - Type: `double`
  - Default: `-1.57`
  - Roll offset from detected pose for docking pose (rad). Note: The external detection rotation angles are setup to work out of the box with Apriltags detectors inimage_procandisaac_ros.

- **`<dock_name>.external_detection_rotation_yaw`**
  - Type: `double`
  - Default: `0.0`
  - Yaw offset from detected pose for docking pose (rad).

- **`<dock_name>.external_detection_timeout`**
  - Type: `double`
  - Default: `1.0`
  - Timeout (s) at which if the newest detection update does not meet to fail.

- **`<dock_name>.external_detection_translation_x`**
  - Type: `double`
  - Default: `-0.20`
  - X offset from detected pose for docking pose (m).

- **`<dock_name>.external_detection_translation_y`**
  - Type: `double`
  - Default: `0.0`
  - Y offset from detected pose for docking pose (m).

- **`<dock_name>.filter_coef`**
  - Type: `double`
  - Default: `0.1`
  - Dock external detection method filtering algorithm coefficient.

- **`<dock_name>.rotate_to_dock`**
  - Type: `bool`
  - Default: `false`
  - Enables backward docking without requiring a sensor for detection during the final approach. When enabled, the robot approaches the staging pose facing forward with sensor coverage for dock detecti...

- **`<dock_name>.staging_x_offset`**
  - Type: `double`
  - Default: `-0.7`
  - Staging pose offset forward (negative) of dock pose (m).

- **`<dock_name>.staging_yaw_offset`**
  - Type: `double`
  - Default: `0.0`
  - Staging pose angle relative to dock pose (rad). Ifdock_directionis set to “backward”, this angle must be faced in the opposite direction of the dock pose. However, ifrotate_to_dockis enabled, this ...

- **`<dock_name>.stall_effort_threshold`**
  - Type: `double`
  - Default: `1.0`
  - Current or motor effort in joint state to triggerisDocked()=true.

- **`<dock_name>.stall_joint_names`**
  - Type: `vector<string>`
  - Default: `N/A`
  - Names injoint_statestopic of joints to track.

- **`<dock_name>.stall_velocity_threshold`**
  - Type: `double`
  - Default: `1.0`
  - The joint velocity below which to triggerisDocked()=true.

- **`<dock_name>.subscribe_toggle`**
  - Type: `bool`
  - Default: `false`
  - When true, subscribe todetected_dock_poseonly while detection is active; otherwise keep the subscription persistent.

- **`<dock_name>.use_battery_status`**
  - Type: `bool`
  - Default: `true`
  - Whether to use the battery state message orisDocked()forisCharging().

- **`<dock_name>.use_external_detection_pose`**
  - Type: `bool`
  - Default: `false`
  - Whether to use external detection topic for dock or use the databases’ pose.

- **`<dock_name>.use_stall_detection`**
  - Type: `bool`
  - Default: `false`
  - Whether or not to use stall detection forisDocked()or positional threshold.

- **`allow_parameter_qos_overrides`**
  - Type: `bool`
  - Default: `true`
  - Whether to allow QoS profiles to be overwritten with parameterized values.

- **`base_frame`**
  - Type: `string`
  - Default: `“base_link”`
  - Robot’s base frame for control law.

- **`controller.beta`**
  - Type: `double`
  - Default: `0.4`
  - Parameter to reduce linear velocity proportional to path curvature. Increasing this linearly reduces the velocity (v(t) = v_max / (1 + beta * |curv|^lambda)).

- **`controller.costmap_topic`**
  - Type: `string`
  - Default: `“local_costmap/costmap_raw”`
  - Raw costmap topic for collision checking.

- **`controller.dock_collision_threshold`**
  - Type: `double`
  - Default: `0.3`
  - Distance (m) from the dock pose to ignore collisions, i.e. the robot will not check for collisions within this distance from the dock pose, as the robot will make contact with the dock. Set to0.0wh...

- **`controller.footprint_topic`**
  - Type: `string`
  - Default: `“local_costmap/published_footprint”`
  - Topic for footprint in the costmap frame.

- **`controller.k_delta`**
  - Type: `double`
  - Default: `2.0`
  - Higher values result in converging to the target more quickly.

- **`controller.k_phi`**
  - Type: `double`
  - Default: `3.0`
  - Ratio of the rate of change of angle relative to distance from the target. Much be > 0.

- **`controller.lambda`**
  - Type: `double`
  - Default: `2.0`
  - Parameter to reduce linear velocity proportional to path curvature. Increasing this exponentially reduces the velocity (v(t) = v_max / (1 + beta * |curv|^lambda)).

- **`controller.projection_time`**
  - Type: `double`
  - Default: `1.0`
  - Time to look ahead for collisions (s).

- **`controller.rotate_to_heading_angular_vel`**
  - Type: `double`
  - Default: `1.0`
  - Angular velocity (rad/s) to rotate to the goal heading when rotate_to_dock is enabled.

- **`controller.rotate_to_heading_max_angular_accel`**
  - Type: `double`
  - Default: `3.2`
  - Maximum angular acceleration (rad/s^2) to rotate to the goal heading when rotate_to_dock is enabled.

- **`controller.simulation_time_step`**
  - Type: `double`
  - Default: `0.1`
  - Time step for projections (s).

- **`controller.slowdown_radius`**
  - Type: `double`
  - Default: `0.25`
  - Radius to end goal to commense slow down.

- **`controller.transform_tolerance`**
  - Type: `double`
  - Default: `0.1`
  - Time with which to post-date the transform that is published, to indicate that this transform is valid into the future.

- **`controller.use_collision_detection`**
  - Type: `bool`
  - Default: `true`
  - Whether to use collision detection to avoid obstacles.

- **`controller.v_angular_max`**
  - Type: `double`
  - Default: `0.75`
  - Maximum angular velocity for approaching dock.

- **`controller.v_linear_max`**
  - Type: `double`
  - Default: `0.24`
  - Maximum velocity for approaching dock.

- **`controller.v_linear_min`**
  - Type: `double`
  - Default: `0.1`
  - Minimum velocity for approaching dock.

- **`controller_frequency`**
  - Type: `double`
  - Default: `50.0`
  - Control frequency (Hz) for vision-control loop.

- **`dock_approach_timeout`**
  - Type: `double`
  - Default: `30.0`
  - Timeout (s) to attempt vision-control approach loop.

- **`dock_backwards`**
  - Type: `bool`
  - Default: `false`
  - Whether the robot is docking with the dock forward or backward in motion. This parameter is deprecated. Use the dock plugin’sdock_directionparameter instead.

- **`dock_database`**
  - Type: `string`
  - Default: `N/A`
  - The filepath to the dock database to use for this environment. Usedocksor this param.

- **`dock_plugins`**
  - Type: `vector<string>`
  - Default: `N/A`
  - A set of dock plugins to load.

- **`dock_prestaging_tolerance`**
  - Type: `double`
  - Default: `0.5`
  - L2 distance in X,Y,Theta from the staging pose to bypass navigation.

- **`docks`**
  - Type: `vector<string>`
  - Default: `N/A`
  - Instead ofdock_database, the set of docks specified in the params file itself. Usedock_databaseor this param.

- **`fixed_frame`**
  - Type: `string`
  - Default: `“odom”`
  - Fixed frame to use, recommended to be a smooth odometry framenotmap.

- **`initial_perception_timeout`**
  - Type: `double`
  - Default: `5.0`
  - Timeout (s) to wait to obtain initial perception of the dock.

- **`introspection_mode`**
  - Type: `string`
  - Default: `“disabled”`
  - The introspection mode for services and actions. Options are “disabled”, “metadata”, “contents”.

- **`max_retries`**
  - Type: `int`
  - Default: `3`
  - Maximum number of retries to attempt.

- **`navigator_bt_xml`**
  - Type: `string`
  - Default: `“”`
  - BT XML to use for Navigator, if non-default.

- **`odom_duration`**
  - Type: `double`
  - Default: `0.3`
  - Time (s) to buffer odometry commands to estimate the robot speed.

- **`odom_topic`**
  - Type: `string`
  - Default: `“odom”`
  - The topic to use for the odometry data when rotate_to_dock is enabled.

- **`rotation_angular_tolerance`**
  - Type: `double`
  - Default: `0.05`
  - Angular tolerance (rad) to exit the rotation loop when rotate_to_dock is enabled.

- **`undock_angular_tolerance`**
  - Type: `double`
  - Default: `0.05`
  - Angular tolerance (rad) to exit undocking loop at staging pose.

- **`undock_linear_tolerance`**
  - Type: `double`
  - Default: `0.05`
  - Tolerance (m) to exit the undocking control loop at staging pose.

- **`wait_charge_timeout`**
  - Type: `double`
  - Default: `5.0`
  - Timeout (s) to wait to see if charging starts after docking.

---

## Dockrobot

### DockRobot
*Source: https://docs.nav2.org/configuration/packages/bt-plugins/actions/DockRobot.html*

- **`dock_id`**
  - Type: `string`
  - Default: `N/A`
  - Dock ID or name to use.

- **`dock_pose`**
  - Type: `geometry_msgs/PoseStamped`
  - Default: `N/A`
  - The dock pose, if not using dock id.

- **`dock_type`**
  - Type: `string`
  - Default: `N/A`
  - The dock plugin type, if using dock pose.

- **`error_code_id`**
  - Type: `uint16`
  - Default: `0`
  - Dock robot error code. SeeDockRobotaction message for the enumerated set of error codes.

- **`error_msg`**
  - Type: `string`
  - Default: `0`
  - Dock robot error message. SeeDockRobotaction message for the enumerated set of error codes.

- **`max_staging_time`**
  - Type: `float`
  - Default: `1000.0`
  - Maximum time to navigate to the staging pose.

- **`navigate_to_staging_pose`**
  - Type: `bool`
  - Default: `true`
  - Whether to autonomously navigate to staging pose.

- **`num_retries`**
  - Type: `uint16`
  - Default: `0`
  - The number of retries executed.

- **`success`**
  - Type: `bool`
  - Default: `true`
  - If the action was successful.

- **`use_dock_id`**
  - Type: `bool`
  - Default: `true`
  - Whether to use the dock’s ID or dock pose fields.

---

## Driveonheading

### DriveOnHeading
*Source: https://docs.nav2.org/configuration/packages/bt-plugins/actions/DriveOnHeading.html*

- **`disable_collision_checks`**
  - Type: `bool`
  - Default: `false`
  - Disable collision checking.

- **`dist_to_travel`**
  - Type: `double`
  - Default: `0.15`
  - Distance to travel (m).

- **`error_code_id`**
  - Type: `uint16`
  - Default: `N/A`
  - Drive on heading error code. SeeDriveOnHeadingaction message for the enumerated set of error codes.

- **`error_msg`**
  - Type: `string`
  - Default: `N/A`
  - Drive on heading error message. SeeDriveOnHeadingaction message for the enumerated set of error codes.

- **`server_name`**
  - Type: `string`
  - Default: `N/A`
  - Action server name.

- **`server_timeout`**
  - Type: `double`
  - Default: `10`
  - Action server timeout (ms).

- **`speed`**
  - Type: `double`
  - Default: `0.025`
  - Speed at which to travel (m/s).

- **`time_allowance`**
  - Type: `double`
  - Default: `10.0`
  - Time to invoke behavior for, if exceeds considers it a stuck condition or failure case (seconds).

---

## Extractroutenodesasgoals

### ExtractRouteNodesAsGoals
*Source: https://docs.nav2.org/configuration/packages/bt-plugins/actions/ExtractRouteNodesAsGoals.html*

- **`goals`**
  - Type: `nav_msgs/Goals`
  - Default: `N/A`
  - Goals comparing the route’snodes.

- **`route`**
  - Type: `nav2_msgs/Route`
  - Default: `N/A`
  - Route to convert itsnodesinto Goals.

---

## Feasible_Path_Handler

### FeasiblePathHandler
*Source: https://docs.nav2.org/configuration/packages/nav2_controller-plugins/feasible_path_handler.html*

- **`<nav2_controllerplugin>.enforce_path_inversion`**
  - Type: `bool`
  - Default: `false`
  - If true, it will prune paths containing cusping points for segments changing directions (e.g. path inversions) such that the controller will be forced to change directions at or very near the plann...

- **`<nav2_controllerplugin>.enforce_path_rotation`**
  - Type: `bool`
  - Default: `false`
  - If true, the controller will detect in-place rotation segments (where translation is near zero) and prune the remaining poses after the rotation point. This forces the robot to explicitly perform t...

- **`<nav2_controllerplugin>.inversion_xy_tolerance`**
  - Type: `double`
  - Default: `0.2`
  - Cartesian proximity (m) to path inversion point to be considered “achieved” to pass on the rest of the path after path inversion.

- **`<nav2_controllerplugin>.inversion_yaw_tolerance`**
  - Type: `double`
  - Default: `0.4`
  - Angular proximity (radians) to path inversion point to be considered “achieved” to pass on the rest of the path after path inversion. 0.4 rad = 23 deg.

- **`<nav2_controllerplugin>.max_robot_pose_search_dist`**
  - Type: `double`
  - Default: `Costmap size / 2`
  - Max integrated distance ahead of robot pose to search for nearest path point in case of path looping.

- **`<nav2_controllerplugin>.minimum_rotation_angle`**
  - Type: `double`
  - Default: `0.785`
  - The minimum accumulated rotation (in radians) required to classify a segment as an in-place rotation. 0.785 rad = 45 deg.

- **`<nav2_controllerplugin>.prune_distance`**
  - Type: `double`
  - Default: `2.0`
  - Distance ahead of nearest point on path to robot to prune path to (m). This distance should be at least as great as the furthest distance of interest by a critic (i.e. for maximum velocity projecti...

- **`<nav2_controllerplugin>.reject_unit_path`**
  - Type: `bool`
  - Default: `false`
  - If enabled, the path handler will reject a path that contains only a single pose.

---

## Following Server

### Following Server
*Source: https://docs.nav2.org/configuration/packages/configuring-following-server.html*

- **`angular_tolerance`**
  - Type: `double`
  - Default: `0.15`
  - Angular tolerance (rad) to consider that the target orientation has been reached.

- **`base_frame`**
  - Type: `string`
  - Default: `“base_link”`
  - Robot’s base frame for control law.

- **`controller_frequency`**
  - Type: `double`
  - Default: `50.0`
  - Control frequency (Hz) for the following control loop.

- **`desired_distance`**
  - Type: `double`
  - Default: `1.0`
  - Desired distance (m) to maintain from the followed object.

- **`detection_timeout`**
  - Type: `double`
  - Default: `2.0`
  - Timeout (s) to wait for detection of the object to follow.

- **`filter_coef`**
  - Type: `double`
  - Default: `0.1`
  - Filter coefficient for smoothing object pose detections.

- **`fixed_frame`**
  - Type: `string`
  - Default: `“odom”`
  - Fixed frame to use, recommended to be a smooth odometry framenotmap.

- **`linear_tolerance`**
  - Type: `double`
  - Default: `0.15`
  - Linear tolerance (m) to consider that the target position has been reached.

- **`max_retries`**
  - Type: `int`
  - Default: `3`
  - Maximum number of retries when detection or control fails.

- **`odom_duration`**
  - Type: `double`
  - Default: `0.3`
  - Time (s) to buffer odometry commands to estimate the robot speed.

- **`odom_topic`**
  - Type: `string`
  - Default: `“odom”`
  - Odometry topic to use for obtaining the robot’s current velocity.

- **`rotate_to_object_timeout`**
  - Type: `double`
  - Default: `10.0`
  - Timeout (s) to rotate searching for the object when detection is lost.

- **`search_angle`**
  - Type: `double`
  - Default: `M_PI_2`
  - Maximum angle (rad) to rotate when searching for the object.

- **`search_by_rotating`**
  - Type: `bool`
  - Default: `false`
  - If true, the robot will rotate in place when it loses object detection to try to find it again.

- **`skip_orientation`**
  - Type: `bool`
  - Default: `true`
  - If true, ignore the detected object’s orientation and point toward it from the robot’s position.

- **`static_object_timeout`**
  - Type: `double`
  - Default: `-1.0`
  - Timeout (s) to stop following when the object remains static. If -1.0, the robot will follow indefinitely.

- **`transform_tolerance`**
  - Type: `double`
  - Default: `0.1`
  - Time with which to post-date the transform that is published, to indicate that this transform is valid into the future.

---

## Followobject

### FollowObject
*Source: https://docs.nav2.org/configuration/packages/bt-plugins/actions/FollowObject.html*

- **`error_code_id`**
  - Type: `uint16`
  - Default: `N/A`
  - Follow object error code. SeeFollowObjectaction for the enumerated set of error code definitions.

- **`error_msg`**
  - Type: `string`
  - Default: `N/A`
  - Follow object error message. SeeFollowObjectaction for the enumerated set of error code definitions.

- **`max_duration`**
  - Type: `double`
  - Default: `0.0`
  - The maximum duration to follow the object.

- **`pose_topic`**
  - Type: `string`
  - Default: `dynamic_pose`
  - Topic to publish the pose of the object to follow.

- **`server_name`**
  - Type: `string`
  - Default: `N/A`
  - Action server name.

- **`server_timeout`**
  - Type: `double`
  - Default: `10`
  - Action server timeout (ms).

- **`tracked_frame`**
  - Type: `string`
  - Default: `N/A`
  - Target frame to follow.

---

## Followpath

### FollowPath
*Source: https://docs.nav2.org/configuration/packages/bt-plugins/actions/FollowPath.html*

- **`controller_id`**
  - Type: `string`
  - Default: `N/A`
  - Mapped name of the controller plugin type to use, e.g. FollowPath.

- **`error_code_id`**
  - Type: `uint16`
  - Default: `N/A`
  - Follow path error code. SeeFollowPathaction for the enumerated set of error code definitions.

- **`error_msg`**
  - Type: `string`
  - Default: `N/A`
  - Follow path error message. SeeFollowPathaction for the enumerated set of error code definitions.

- **`goal_checker_id`**
  - Type: `string`
  - Default: `N/A`
  - Mapped name of the goal checker plugin type to use, e.g. SimpleGoalChecker.

- **`path`**
  - Type: `string`
  - Default: `N/A`
  - Takes in a blackboard variable containing the path to follow, eg. “{path}”.

- **`path_handler_id`**
  - Type: `string`
  - Default: `N/A`
  - Mapped name of the path handler plugin type to use, e.g. FeasiblePathHandler.

- **`progress_checker_id`**
  - Type: `string`
  - Default: `N/A`
  - Mapped name of the progress checker plugin type to use, e.g. SimpleProgressChecker.

- **`server_name`**
  - Type: `string`
  - Default: `N/A`
  - Action server name.

- **`server_timeout`**
  - Type: `double`
  - Default: `10`
  - Action server timeout (ms).

- **`tracking_feedback`**
  - Type: `nav2_msgs::msg::TrackingFeedback`
  - Default: `N/A`
  - Tracking feedback message from the controller server, including cross track error, current path index, remaining path length, etc.

---

## General

### Configuration Guide
*Source: https://docs.nav2.org/configuration/index.html*

- **`Behavior`**
  - Tree Navigator

- **`Savitzky`**
  - Golay Smoother

---

## Getcurrentpose

### GetCurrentPose
*Source: https://docs.nav2.org/configuration/packages/bt-plugins/actions/GetCurrentPose.html*

- **`current_pose`**
  - Type: `geometry_msgs::msg::PoseStamped`
  - Default: `N/A`
  - The current pose in the global frame.

- **`global_frame`**
  - Type: `string`
  - Default: `N/A`
  - Global frame to transform poses to if not given in the same frame. If not provided, uses the BT Navigator’sglobal_framesetting automatically.

- **`robot_base_frame`**
  - Type: `string`
  - Default: `N/A`
  - Robot base frame to transform poses to if not given in the same frame. If not provided, uses the BT Navigator’sbase_framesetting automatically.

---

## Getnextfewgoals

### GetNextFewGoals
*Source: https://docs.nav2.org/configuration/packages/bt-plugins/actions/GetNextFewGoals.html*

- **`input_goals`**
  - Type: `nav_msgs/Goals`
  - Default: `N/A`
  - Input goals list.

- **`num_goals`**
  - Type: `int`
  - Default: `N/A`
  - How many of the goals to take from the input goals.

- **`output_goals`**
  - Type: `nav_msgs/Goals`
  - Default: `N/A`
  - The output pruned goals list.

---

## Getposefrompath

### GetPoseFromPath
*Source: https://docs.nav2.org/configuration/packages/bt-plugins/actions/GetPoseFromPath.html*

- **`index`**
  - Type: `int`
  - Default: `0`
  - Index from path to use. Use-1to get the last pose,-2for second to last, and so on.

- **`path`**
  - Type: `nav_msgs/Path`
  - Default: `N/A`
  - Path to extract pose from

- **`pose`**
  - Type: `geometry_msgs/PoseStamped`
  - Default: `N/A`
  - Pose from path, with the Path’s set header.

---

## Globalupdatedgoal

### GlobalUpdatedGoal
*Source: https://docs.nav2.org/configuration/packages/bt-plugins/conditions/GlobalUpdatedGoal.html*

- **`goal`**
  - Type: `geometry_msgs::msg::PoseStamped`
  - Default: `“{goal}”`
  - Destination to check. Takes in a blackboard variable, “{goal}” if not specified.

- **`goals`**
  - Type: `nav_msgs::msg::Goals`
  - Default: `“{goals}”`
  - Vector of goals to check. Takes in a blackboard variable, “{goals}” if not specified.

---

## Goal_Align

### GoalAlignCritic
*Source: https://docs.nav2.org/configuration/packages/trajectory_critics/goal_align.html*

- **`<dwbplugin>.<name>.aggregation_type`**
  - Type: `string`
  - Default: `“last”`
  - last, sum, or product combination methods.

- **`<dwbplugin>.<name>.forward_point_distance`**
  - Type: `double`
  - Default: `0.325`
  - Point in front of robot to look ahead to compute angular change from.

- **`<dwbplugin>.<name>.scale`**
  - Type: `double`
  - Default: `1.0`
  - Weighed scale for critic.

---

## Goal_Dist

### GoalDistCritic
*Source: https://docs.nav2.org/configuration/packages/trajectory_critics/goal_dist.html*

- **`<dwbplugin>.<name>.aggregation_type`**
  - Type: `string`
  - Default: `“last”`
  - last, sum, or product combination methods.

- **`<dwbplugin>.<name>.scale`**
  - Type: `double`
  - Default: `1.0`
  - Weighed scale for critic.

---

## Goalcheckerselector

### GoalCheckerSelector
*Source: https://docs.nav2.org/configuration/packages/bt-plugins/actions/GoalCheckerSelector.html*

- **`default_goal_checker`**
  - Type: `string`
  - Default: `N/A`
  - The default value for the selected GoalChecker if no message is received from the input topic.

- **`selected_goal_checker`**
  - Type: `string`
  - Default: `N/A`
  - The output selected GoalChecker id. This selected_goal_checker string is usually passed to the FollowPath behavior via the goal_checker_id input port.

- **`topic_name`**
  - Type: `string`
  - Default: `goal_checker_selector`
  - The name of the topic used to received select command messages. This is used to support multiple GoalCheckerSelector nodes.

---

## Goalreached

### GoalReached
*Source: https://docs.nav2.org/configuration/packages/bt-plugins/conditions/GoalReached.html*

- **`goal`**
  - Type: `geometry_msgs::msg::PoseStamped`
  - Default: `N/A`
  - Destination to check. Takes in a blackboard variable, e.g. “{goal}”. The global reference frame is taken from the goal’s headerframe_idfield.

- **`goal_reached_tol`**
  - Type: `double`
  - Default: `0.25`
  - Tolerance of accepting pose as the goal (m).

- **`robot_base_frame`**
  - Type: `string`
  - Default: `“base_link”`
  - Robot base frame.

- **`transform_tolerance`**
  - Defined and declared inBehavior-Tree Navigator.

---

## Goalupdated

### GoalUpdated
*Source: https://docs.nav2.org/configuration/packages/bt-plugins/conditions/GoalUpdated.html*

- **`goal`**
  - Type: `geometry_msgs::msg::PoseStamped`
  - Default: `“{goal}”`
  - Destination to check. Takes in a blackboard variable, “{goal}” if not specified.

- **`goals`**
  - Type: `nav_msgs::msg::Goals`
  - Default: `“{goals}”`
  - Vector of goals to check. Takes in a blackboard variable, “{goals}” if not specified.

---

## Goalupdatedcontroller

### GoalUpdatedController
*Source: https://docs.nav2.org/configuration/packages/bt-plugins/decorators/GoalUpdatedController.html*

- **`goal`**
  - Type: `geometry_msgs::msg::PoseStamped`
  - Default: `“{goal}”`
  - Destination to check. Takes in a blackboard variable, “{goal}” if not specified.

- **`goals`**
  - Type: `nav_msgs::msg::Goals`
  - Default: `“{goals}”`
  - Vector of goals to check. Takes in a blackboard variable, “{goals}” if not specified.

---

## Goalupdater

### GoalUpdater
*Source: https://docs.nav2.org/configuration/packages/bt-plugins/decorators/GoalUpdater.html*

- **`goal_updater_topic`**
  - Type: `string`
  - Default: `“goal_update”`
  - The topic to receive the updated goal pose

- **`goals_updater_topic`**
  - Type: `string`
  - Default: `“goals_update”`
  - The topic to receive the updated goals poses

- **`input_goal`**
  - Type: `geometry_msgs/PoseStamped`
  - Default: `N/A`
  - The original goal pose

- **`input_goals`**
  - Type: `nav_msgs/Goals`
  - Default: `N/A`
  - The original goals poses

- **`output_goal`**
  - Type: `geometry_msgs/PoseStamped`
  - Default: `N/A`
  - The resulting updated goal. If no goal received by subscription, it will be the input_goal

- **`output_goals`**
  - Type: `nav_msgs/Goals`
  - Default: `N/A`
  - The resulting updated goals. If no goals received by subscription, it will be the input_goals

---

## Graceful Motion Controller

### Graceful Controller
*Source: https://docs.nav2.org/configuration/packages/configuring-graceful-motion-controller.html*

- **`allow_backward`**
  - Type: `bool`
  - Default: `false`
  - Whether to allow the robot to move backward.

- **`allow_parameter_qos_overrides`**
  - Type: `bool`
  - Default: `true`
  - Whether to allow QoS profiles to be overwritten with parameterized values.

- **`beta`**
  - Type: `double`
  - Default: `0.4`
  - Constant factor applied to the path curvature. This value must be positive. Determines how fast the velocity drops when the curvature increases.

- **`in_place_collision_tolerance`**
  - Type: `double`
  - Default: `0.1`
  - When performing an in-place rotation after the XY goal tolerance has been met, this is the angle (in radians) between poses to check for collision.

- **`initial_rotation`**
  - Type: `bool`
  - Default: `true`
  - Enable a rotation in place to the goal before starting the path. The control law may generate large sweeping arcs to the goal pose, depending on the initial robot orientation andk_phi,k_delta.

- **`initial_rotation_tolerance`**
  - Type: `double`
  - Default: `0.75`
  - The difference in the path orientation and the starting robot orientation to trigger a rotate in place, ifinitial_rotationis enabled. This value is generally acceptable if continuous replanning is ...

- **`k_delta`**
  - Type: `double`
  - Default: `1.0`
  - Constant factor applied to the heading error feedback. Controls the convergence of the fast subsystem. The bigger the value, the robot converge faster to the reference heading. The referenced paper...

- **`k_phi`**
  - Type: `double`
  - Default: `2.0`
  - Ratio of the rate of change in phi to the rate of change in r. Controls the convergence of the slow subsystem. If this value is equal to zero, the controller will behave as a pure waypoint follower...

- **`lambda`**
  - Type: `double`
  - Default: `2.0`
  - Constant factor applied to the path curvature. This value must be greater or equal to 1. Determines the sharpness of the curve: higher lambda implies sharper curves.

- **`max_lookahead`**
  - Type: `double`
  - Default: `1.0`
  - The maximum lookahead distance (m) to use when selecting a target pose for the underlying control law. Using poses that are further away will generally result in smoother operations, but simulating...

- **`min_lookahead`**
  - Type: `double`
  - Default: `0.25`
  - The minimum lookahead distance (m) to use when selecting a target pose for the underlying control law. This parameter avoids instability when an unexpected obstacle appears in the path of the robot...

- **`prefer_final_rotation`**
  - Type: `bool`
  - Default: `true`
  - The control law can generate large arcs when the goal orientation is not aligned with the path. If this is enabled, the orientation of the final pose will be ignored and the robot will follow the o...

- **`rotation_scaling_factor`**
  - Type: `double`
  - Default: `0.5`
  - The scaling factor applied to the rotation in place velocity.

- **`slowdown_radius`**
  - Type: `double`
  - Default: `1.5`
  - Radius (m) around the goal pose in which the robot will start to slow down.

- **`use_collision_detection`**
  - Type: `bool`
  - Default: `true`
  - Whether to use collision detection to avoid obstacles.

- **`v_angular_max`**
  - Type: `double`
  - Default: `1.0`
  - Maximum angular velocity (rad/s) produced by the control law.

- **`v_angular_min_in_place`**
  - Type: `double`
  - Default: `0.25`
  - Minimum angular velocity (rad/s) produced by the control law when rotating in place. This value should be based on the minimum rotation speed controllable by the robot.

- **`v_linear_max`**
  - Type: `double`
  - Default: `0.5`
  - Maximum linear velocity (m/s).

- **`v_linear_min`**
  - Type: `double`
  - Default: `0.1`
  - Minimum linear velocity (m/s).

---

## Inflation

### Inflation Layer Parameters
*Source: https://docs.nav2.org/configuration/packages/costmap-plugins/inflation.html*

- **`<inflationlayer>.cost_scaling_factor`**
  - Type: `double`
  - Default: `10.0`
  - Exponential decay factor across inflation radius.

- **`<inflationlayer>.enabled`**
  - Type: `bool`
  - Default: `True`
  - Whether it is enabled.

- **`<inflationlayer>.inflate_around_unknown`**
  - Type: `bool`
  - Default: `False`
  - Whether to inflate unknown cells.

- **`<inflationlayer>.inflate_unknown`**
  - Type: `bool`
  - Default: `False`
  - Whether to inflate unknown cells as if lethal.

- **`<inflationlayer>.inflation_radius`**
  - Type: `double`
  - Default: `0.55`
  - Radius to inflate costmap around lethal obstacles.

---

## Initialposereceived

### InitialPoseReceived
*Source: https://docs.nav2.org/configuration/packages/bt-plugins/conditions/InitialPoseReceived.html*

- **`initial_pose_received`**
  - Type: `bool`
  - Default: `“{initial_pose_received}”`
  - Success if the value in the port is true. Takes in a blackboard variable,“{initial_pose_received}” if not specified.

- **`Success if the value in the port is true. Takes in a blackboard variable,`**
  - “{initial_pose_received}” if not specified.

---

## Input_At_Waypoint

### InputAtWaypoint
*Source: https://docs.nav2.org/configuration/packages/nav2_waypoint_follower-plugins/input_at_waypoint.html*

- **`<nav2_waypoint_followerplugin>.enabled`**
  - Type: `bool`
  - Default: `true`
  - Whether waypoint_task_executor plugin is enabled.

- **`<nav2_waypoint_followerplugin>.input_topic`**
  - Type: `string`
  - Default: `“input_at_waypoint/input”`
  - Topic input is published to to indicate to move to the next waypoint, instd_msgs/Empty.

- **`<nav2_waypoint_followerplugin>.timeout`**
  - Type: `double`
  - Default: `10.0`
  - Amount of time in seconds to wait for user input before moving on to the next waypoint.

- **`allow_parameter_qos_overrides`**
  - Type: `bool`
  - Default: `true`
  - Whether to allow QoS profiles to be overwritten with parameterized values.

---

## Isbatterycharging

### IsBatteryCharging
*Source: https://docs.nav2.org/configuration/packages/bt-plugins/conditions/IsBatteryCharging.html*

- **`battery_topic`**
  - Type: `string`
  - Default: `“/battery_status”`
  - Topic for battery info.

---

## Isbatterylow

### IsBatteryLow
*Source: https://docs.nav2.org/configuration/packages/bt-plugins/conditions/IsBatteryLow.html*

- **`battery_topic`**
  - Type: `string`
  - Default: `“/battery_status”`
  - Topic for battery info.

- **`is_voltage`**
  - Type: `bool`
  - Default: `false`
  - If true voltage will be used to check for low battery.

- **`min_battery`**
  - Type: `double`
  - Default: `0.0`
  - Min battery percentage or voltage before triggering.

---

## Isgoalnearby

### IsGoalNearby
*Source: https://docs.nav2.org/configuration/packages/bt-plugins/conditions/IsGoalNearby.html*

- **`global_frame`**
  - Type: `string`
  - Default: `“map”`
  - The global reference frame.

- **`max_robot_pose_search_dist`**
  - Type: `double`
  - Default: `-1.0`
  - Maximum forward integrated distance along the path (starting from the last detected pose) to bound the search for the closest pose to the robot. When set to a negative value (default), the entire p...

- **`path`**
  - Type: `nav_msgs::msg::Path`
  - Default: `N/A`
  - The planned path to evaluate.

- **`proximity_threshold`**
  - Type: `double`
  - Default: `1.0`
  - The remaining path length (in meters) considered as “nearby”. When the remaining distance along the path is less than this threshold, the condition returns SUCCESS.

- **`robot_base_frame`**
  - Type: `string`
  - Default: `“base_link”`
  - Robot base frame.

- **`transform_tolerance`**
  - Defined and declared inBehavior-Tree Navigator.

---

## Ispathvalid

### IsPathValid
*Source: https://docs.nav2.org/configuration/packages/bt-plugins/conditions/IsPathValid.html*

- **`check_full_path`**
  - Type: `bool`
  - Default: `false`
  - Whether to check all poses in the path (true) or stop at the first invalid pose (false). When true, all collision poses are reported.

- **`collision_poses`**
  - Type: `std::vector<geometry_msgs::msg::PoseStamped>`
  - Default: `N/A`
  - Vector of poses in the path that are in collision or invalid. Empty if the path is valid.

- **`consider_unknown_as_obstacle`**
  - Type: `bool`
  - Default: `false`
  - Whether to consider unknown cost (255) as obstacle.

- **`footprint`**
  - Type: `string`
  - Default: `“”`
  - Custom footprint specification as a bracketed array of arrays, e.g., “[[x1,y1],[x2,y2],…]”. If empty, uses the robot’s configured footprint.

- **`layer_name`**
  - Type: `string`
  - Default: `“”`
  - Name of the specific costmap layer to check against. If empty, checks against the full costmap.

- **`max_cost`**
  - Type: `unsigned int`
  - Default: `254`
  - The maximum allowable cost for the path to be considered valid.

- **`path`**
  - Type: `nav_msgs::msg::Path`
  - Default: `N/A`
  - The global path to check for validity.

- **`server_timeout`**
  - Type: `double`
  - Default: `20.0`
  - Service response timeout (ms).

---

## Isposeoccupied

### IsPoseOccupied
*Source: https://docs.nav2.org/configuration/packages/bt-plugins/conditions/IsPoseOccupied.html*

- **`consider_unknown_as_obstacle`**
  - Type: `bool`
  - Default: `false`
  - Whether to consider unknown cost (255) as obstacle.

- **`cost_threshold`**
  - Type: `double`
  - Default: `254.0`
  - The cost threshold above which a waypoint is considered in collision and should be removed. Ifuse_footprint=false, consider setting to 253 for occupied.

- **`pose`**
  - Type: `geometry_msgs/PoseStamped`
  - Default: `N/A`
  - Pose to check if it is occupied.

- **`server_timeout`**
  - Type: `double`
  - Default: `20.0`
  - Service response timeout (ms).

- **`service_name`**
  - Type: `string`
  - Default: `/global_costmap/get_cost_global_costmap`
  - costmap service name responsible for getting the cost.

- **`use_footprint`**
  - Type: `bool`
  - Default: `true`
  - Whether to use the footprint cost or the point cost.

---

## Isstopped

### IsStopped
*Source: https://docs.nav2.org/configuration/packages/bt-plugins/conditions/IsStopped.html*

- **`duration_stopped`**
  - Type: `int (ms)`
  - Default: `1000`
  - Duration (ms) the velocity must remain below the threshold

- **`velocity_threshold`**
  - Type: `double`
  - Default: `0.01`
  - Velocity threshold below which robot is considered stopped

---

## Iterator

### XYTheta Iterator
*Source: https://docs.nav2.org/configuration/packages/dwb-params/iterator.html*

- **`<dwbplugin>.vtheta_samples`**
  - Type: `int`
  - Default: `20`
  - Number of velocity samples in the angular directions.

- **`<dwbplugin>.vx_samples`**
  - Type: `int`
  - Default: `20`
  - Number of velocity samples in the X velocity direction.

- **`<dwbplugin>.vy_samples`**
  - Type: `int`
  - Default: `5`
  - Number of velocity samples in the Y velocity direction.

---

## Keepout_Filter

### Keepout Filter Parameters
*Source: https://docs.nav2.org/configuration/packages/costmap-plugins/keepout_filter.html*

- **`<filtername>.enabled`**
  - Type: `bool`
  - Default: `True`
  - Whether it is enabled.

- **`<filtername>.filter_info_topic`**
  - Type: `string`
  - Default: `N/A`
  - Name of the incomingCostmapFilterInfotopic having filter-related information. Published by Costmap Filter Info Server along with filter mask topic. For more details about Map and Costmap Filter Inf...

- **`<filtername>.lethal_override_cost`**
  - Type: `double`
  - Default: `252`
  - The cost value written into those cells instead of lethal cost when override is active. Default sets cost very high to incentivize leaving the area as soon as possible.

- **`<filtername>.override_lethal_cost`**
  - Type: `bool`
  - Default: `False`
  - When true, check if the robot is in a lethal keepout zone, if so, replaces those lethal costs with lethal_override_cost.

- **`<filtername>.transform_tolerance`**
  - Type: `double`
  - Default: `0.1`
  - Time with which to post-date the transform that is published, to indicate that this transform is valid into the future. Used when filter mask and current costmap layer are in different frames.

---

## Kinematic

### Kinematic Parameters
*Source: https://docs.nav2.org/configuration/packages/dwb-params/kinematic.html*

- **`<dwbplugin>.acc_lim_theta`**
  - Type: `double`
  - Default: `0.0`
  - Maximum acceleration rotation (rad/s^2).

- **`<dwbplugin>.acc_lim_x`**
  - Type: `double`
  - Default: `0.0`
  - Maximum acceleration X (m/s^2).

- **`<dwbplugin>.acc_lim_y`**
  - Type: `double`
  - Default: `0.0`
  - Maximum acceleration Y (m/s^2).

- **`<dwbplugin>.decel_lim_theta`**
  - Type: `double`
  - Default: `0.0`
  - Maximum deceleration rotation (rad/s^2).

- **`<dwbplugin>.decel_lim_x`**
  - Type: `double`
  - Default: `0.0`
  - Maximum deceleration X (m/s^2).

- **`<dwbplugin>.decel_lim_y`**
  - Type: `double`
  - Default: `0.0`
  - Maximum deceleration Y (m/s^2).

- **`<dwbplugin>.max_speed_xy`**
  - Type: `double`
  - Default: `0.0`
  - Maximum translational speed (m/s).

- **`<dwbplugin>.max_vel_theta`**
  - Type: `double`
  - Default: `0.0`
  - Maximum angular velocity (rad/s).

- **`<dwbplugin>.max_vel_x`**
  - Type: `double`
  - Default: `0.0`
  - Maximum velocity X (m/s).

- **`<dwbplugin>.max_vel_y`**
  - Type: `double`
  - Default: `0.0`
  - Maximum velocity Y (m/s).

- **`<dwbplugin>.min_speed_theta`**
  - Type: `double`
  - Default: `0.0`
  - Minimum angular speed (rad/s).

- **`<dwbplugin>.min_speed_xy`**
  - Type: `double`
  - Default: `0.0`
  - Minimum translational speed (m/s).

- **`<dwbplugin>.min_vel_x`**
  - Type: `double`
  - Default: `0.0`
  - Minimum velocity X (m/s).

- **`<dwbplugin>.min_vel_y`**
  - Type: `double`
  - Default: `0.0`
  - Minimum velocity Y (m/s).

---

## Lifecycle

### Lifecycle Manager
*Source: https://docs.nav2.org/configuration/packages/configuring-lifecycle.html*

- **`allow_parameter_qos_overrides`**
  - Type: `bool`
  - Default: `true`
  - Whether to allow QoS profiles to be overwritten with parameterized values.

- **`attempt_respawn_reconnection`**
  - Type: `bool`
  - Default: `true`
  - Whether to try to reconnect to servers that go down, presumably because respawn is set totrueto re-create crashed nodes. While default totrue, reconnections will not be made unless respawn is set t...

- **`autostart`**
  - Type: `bool`
  - Default: `false`
  - Whether to transition nodes to active state on startup.

- **`bond_heartbeat_period`**
  - Type: `double`
  - Default: `0.25`
  - The lifecycle node bond mechanism publishing period (on the /bond topic). Disabled if inferior or equal to 0.0.

- **`bond_respawn_max_duration`**
  - Type: `double`
  - Default: `10.0`
  - When a server crashes or becomes non-responsive, the lifecycle manager will bring down all nodes for safety. This is the duration of which the lifecycle manager will attempt to reconnect with the f...

- **`bond_timeout`**
  - Type: `double`
  - Default: `4.0`
  - Timeout to transition down all lifecycle nodes of this manager if a server is non-responsive, in seconds. Set to0to deactivate. Recommended to be always larger than 0.3s for all-local node discover...

- **`introspection_mode`**
  - Type: `string`
  - Default: `“disabled”`
  - The introspection mode for services and actions. Options are “disabled”, “metadata”, “contents”.

- **`node_names`**
  - Type: `vector<string>`
  - Default: `N/A`
  - Ordered list of node names to bringup through lifecycle transition.

---

## Limited_Accel_Generator

### LimitedAccelGenerator
*Source: https://docs.nav2.org/configuration/packages/dwb-plugins/limited_accel_generator.html*

- **`<dwbplugin>.sim_time`**
  - Type: `double`
  - Default: `1.7`
  - Time to simulate ahead by (s).

---

## Loopback Sim

### Loopback Simulator
*Source: https://docs.nav2.org/configuration/packages/configuring-loopback-sim.html*

- **`base_frame_id`**
  - Type: `string`
  - Default: `“base_link”`
  - The base frame to use.

- **`enable_stamped_cmd_vel`**
  - Type: `string`
  - Default: `True`
  - Whether cmd_vel is stamped or unstamped (i.e. Twist or TwistStamped). Note: This parameter is defaultfalsein Jazzy or older! Kilted or newer usesTwistStampedby default.

- **`map_frame_id`**
  - Type: `string`
  - Default: `“map”`
  - The map frame to use.

- **`odom_frame_id`**
  - Type: `string`
  - Default: `“odom”`
  - The odom frame to use.

- **`publish_clock`**
  - Type: `string`
  - Default: `true`
  - Whether or not to publish simulated clock to/clock

- **`publish_map_odom_tf`**
  - Type: `string`
  - Default: `true`
  - Whether or not to publish tf frommap_frame_idtoodom_frame_id

- **`scan_angle_increment`**
  - Type: `double`
  - Default: `0.0261`
  - Angular resolution of the scan in radians (angle between consecutive measurements)

- **`scan_angle_max`**
  - Type: `double`
  - Default: `3.14`
  - Ending angle of the scan in radians (rightmost angle)

- **`scan_angle_min`**
  - Type: `double`
  - Default: `-3.14`
  - Starting angle of the scan in radians (leftmost angle)

- **`scan_frame_id`**
  - Type: `string`
  - Default: `“base_scan”`
  - The scan frame to use to publish a scan

- **`scan_publish_dur`**
  - Type: `string`
  - Default: `0.1`
  - The duration between publishing scan (in sec)

- **`scan_range_max`**
  - Type: `double`
  - Default: `30.0`
  - Maximum measurable distance from the scan in meters. Values beyond this are out of range.

- **`scan_range_min`**
  - Type: `double`
  - Default: `0.05`
  - Minimum measurable distance from the scan in meters. Values below this are considered invalid.

- **`scan_use_inf`**
  - Type: `bool`
  - Default: `true`
  - Whether to useinffor out-of-range values. Iffalse, values are set toscan_range_max-0.1instead.

- **`update_duration`**
  - Type: `double`
  - Default: `0.01`
  - The duration between updates (s)

---

## Map Saver

### Map Saver
*Source: https://docs.nav2.org/configuration/packages/map_server/configuring-map-saver.html*

- **`free_thresh_default`**
  - Type: `double`
  - Default: `0.25`
  - Free space maximum probability threshold value for occupancy grid.

- **`introspection_mode`**
  - Type: `string`
  - Default: `“disabled”`
  - The introspection mode for services and actions. Options are “disabled”, “metadata”, “contents”.

- **`occupied_thresh_default`**
  - Type: `double`
  - Default: `0.65`
  - Occupied space minimum probability threshold value for occupancy grid.

- **`save_map_timeout`**
  - Type: `int`
  - Default: `2.0`
  - Timeout to attempt saving the map (seconds).

---

## Map Server

### Map Server
*Source: https://docs.nav2.org/configuration/packages/map_server/configuring-map-server.html*

- **`frame_id`**
  - Type: `string`
  - Default: `“map”`
  - Frame to publish loaded map in.

- **`introspection_mode`**
  - Type: `string`
  - Default: `“disabled”`
  - The introspection mode for services and actions. Options are “disabled”, “metadata”, “contents”.

- **`topic_name`**
  - Type: `string`
  - Default: `“map”`
  - Topic to publish loaded map to.

- **`yaml_filename`**
  - Type: `string`
  - Default: `N/A`
  - Path to map yaml file. Note from Rolling + Iron-Turtle forward: This parameter can set either from the yaml file or using the launch configuration parametermap. If we set it on launch commandline /...

---

## Mppic

### Model Predictive Path Integral Controller
*Source: https://docs.nav2.org/configuration/packages/configuring-mppic.html*

- **`allow_parameter_qos_overrides`**
  - Type: `bool`
  - Default: `true`
  - Whether to allow QoS profiles to be overwritten with parameterized values.

- **`ax_max`**
  - Type: `double`
  - Default: `3.0`
  - Maximum forward acceleration (m/s^2).

- **`ax_min`**
  - Type: `double`
  - Default: `-3.0`
  - Maximum deceleration along the X-axis (m/s^2).

- **`ay_max`**
  - Type: `double`
  - Default: `3.0`
  - Maximum lateral acceleration in either direction, if usingOmnimotion model (m/s^2).

- **`ay_min`**
  - Type: `double`
  - Default: `-3.0`
  - Minimum lateral acceleration in either direction, if usingOmnimotion model (m/s^2).

- **`az_max`**
  - Type: `double`
  - Default: `3.5`
  - Maximum angular acceleration (rad/s^2).

- **`batch_size`**
  - Type: `int`
  - Default: `1000`
  - Count of randomly sampled candidate trajectories from current optimal control sequence in a given iteration. 1000 @ 50 Hz or 2000 @ 30 Hz seems to produce good results.

- **`collision_cost`**
  - Type: `double`
  - Default: `100000.0`
  - Cost to apply to a true collision in a trajectory.

- **`collision_lookahead_time`**
  - Type: `double`
  - Default: `2.0`
  - The time in seconds to look ahead for potential collisions when validating the trajectory.

- **`collision_margin_distance`**
  - Type: `double`
  - Default: `0.10`
  - Margin distance (m) from collision to apply severe penalty, similar to footprint inflation. Between 0.05-0.2 is reasonable. Note that it will highly influence the controller not to enter spaces mor...

- **`consider_footprint`**
  - Type: `bool`
  - Default: `false`
  - Whether to consider the robot’s footprint when validating the trajectory. Else, will use the center point cost of a circular robot

- **`cost_power`**
  - Type: `int`
  - Default: `1`
  - Power order to apply to term.

- **`cost_scaling_factor`**
  - Type: `double`
  - Default: `10.0`
  - Exponential decay factor across inflation radius. This should be the same as for your inflation layer (Humble only)

- **`cost_weight`**
  - Type: `double`
  - Default: `4.0`
  - Weight to apply to critic term.

- **`critical_cost`**
  - Type: `double`
  - Default: `300.0`
  - Cost to apply to a pose with a cost higher than the near_collision_cost.

- **`critical_weight`**
  - Type: `double`
  - Default: `20.0`
  - Weight to apply to critic for near collisions closer thancollision_margin_distanceto prevent near collisionsonlyas a method of virtually inflating the footprint. This should not be used to generall...

- **`critics`**
  - Type: `string vector`
  - Default: `N/A`
  - A vector of critic plugin functions to use, withoutmppi::critic::namespace which will be automatically added on loading.

- **`deadband_velocities`**
  - Type: `array of double`
  - Default: `[0.05, 0.05, 0.05]`
  - The array of deadband velocities [vx, vz, wz]. A zero array indicates that the critic will take no action.

- **`gamma`**
  - Type: `double`
  - Default: `0.015`
  - A trade-off between smoothness (high) and low energy (low). This is a complex parameter that likely won’t need to be changed from the default. See Section 3D-2 in “Information Theoretic Model Predi...

- **`inflation_layer_name`**
  - Type: `string`
  - Default: `“”`
  - Name of the inflation layer. If empty, it uses the last inflation layer in the costmap. If you have multiple inflation layers, you may want to specify the name of the layer to use.

- **`inflation_radius`**
  - Type: `double`
  - Default: `0.55`
  - Radius to inflate costmap around lethal obstacles. This should be the same as for your inflation layer (Humble only)

- **`iteration_count`**
  - Type: `int`
  - Default: `1`
  - Iteration count in the MPPI algorithm. Recommended to remain as 1 and instead prefer larger batch sizes.

- **`max_angle_to_furthest`**
  - Type: `double`
  - Default: `0.785398`
  - Angular distance (rad) between robot and goal above which path angle cost starts being considered

- **`max_path_occupancy_ratio`**
  - Type: `double`
  - Default: `0.07`
  - Maximum proportion of the path that can be occupied before this critic is not considered to allow the obstacle and path follow critics to avoid obstacles while following the path’s intent in presen...

- **`min_turning_r`**
  - Type: `double`
  - Default: `0.2`
  - The minimum turning radius possible for the vehicle platform (m).

- **`mode`**
  - Type: `int`
  - Default: `0`
  - Enum type for mode of operations for the path angle critic depending on path input types and behavioral desires. 0: Forward Preference, penalizes high path angles relative to the robot’s orientatio...

- **`model_dt`**
  - Type: `double`
  - Default: `0.05`
  - Length of each time step’sdttimestep, in seconds.time_steps*model_dtis the prediction horizon.

- **`motion_model`**
  - Type: `string`
  - Default: `“DiffDrive”`
  - The desired motion model to use for trajectory planning. Options areDiffDrive,Omni, orAckermann. Differential drive robots may use forward/reverse and angular velocities; Omni add in lateral motion...

- **`near_collision_cost`**
  - Type: `int`
  - Default: `253`
  - Costmap cost value to set a maximum proximity for avoidance.

- **`near_goal_distance`**
  - Type: `double`
  - Default: `0.50`
  - Distance (m) near goal to stop applying preferential obstacle term to allow robot to smoothly converge to goal pose in close proximity to obstacles.

- **`offset_from_furthest`**
  - Type: `int`
  - Default: `20`
  - Checks that the candidate trajectories are sufficiently far along their way tracking the path to apply the alignment critic. This ensures that path alignment is only considered when actually tracki...

- **`open_loop`**
  - Type: `bool`
  - Default: `false`
  - Whether to use last command velocity or use odometry for MPPI initial state estimation. When enable, use last command velocity for MPPI initial state estimation.

- **`publish_critics_stats`**
  - Type: `bool`
  - Default: `false`
  - Whether to publish statistics about each critic’s performance. When enabled, publishes anav2_msgs::msg::CriticsStatsmessage containing critic names, whether they changed costs, and the sum of costs...

- **`publish_optimal_trajectory`**
  - Type: `bool`
  - Default: `false`
  - Whether to publish the optimal trajectory (pose, velocity, timestamps of via points) computed by MPC for visualization, debugging, or injection by lower-level control systems and/or collision avoid...

- **`regenerate_noises`**
  - Type: `bool`
  - Default: `false`
  - Whether to regenerate noises each iteration or use single noise distribution computed on initialization and reset. Practically, this is found to work fine since the trajectories are being sampled s...

- **`repulsion_weight`**
  - Type: `double`
  - Default: `1.5`
  - Weight to apply to critic for generally preferring routes in lower cost space. This is separated from the critical term to allow for fine tuning of obstacle behaviors with path alignment for dynami...

- **`reset_period`**
  - Type: `double`
  - Default: `1.0`
  - Required time of inactivity to reset optimizer  (only in Humble due to backport ABI policies).

- **`retry_attempt_limit`**
  - Type: `int`
  - Default: `1`
  - Number of attempts to find feasible trajectory on failure for soft-resets before reporting total failure.

- **`symmetric_yaw_tolerance`**
  - Type: `bool`
  - Default: `false`
  - Enable symmetric goal orientation acceptance. When enabled, the critic prefers trajectories that approach the goal at either the goal orientation or the goal orientation + 180°. This is useful for ...

- **`temperature`**
  - Type: `double`
  - Default: `0.3`
  - Selectiveness of trajectories by their costs (The closer this value to 0, the “more” we take in consideration controls with less cost), 0 mean use control with best cost, huge value will lead to ju...

- **`threshold_to_consider`**
  - Type: `double`
  - Default: `0.5`
  - Minimal distance (m) between robot and goal above which angle goal cost considered.

- **`time_step`**
  - Type: `int`
  - Default: `3`
  - The step between points on trajectories to visualize to downsample trajectory density.

- **`time_steps`**
  - Type: `int`
  - Default: `56`
  - Number of time steps (points) in candidate trajectories

- **`trajectory_point_step`**
  - Type: `int`
  - Default: `2`
  - The step to take in trajectories for evaluating them in the critic. Since trajectories are extremely dense, its unnecessary to evaluate each point and computationally expensive.

- **`trajectory_step`**
  - Type: `int`
  - Default: `5`
  - The step between trajectories to visualize to downsample candidate trajectory pool.

- **`TrajectoryValidator.plugin`**
  - Type: `string`
  - Default: `“mppi::DefaultOptimalTrajectoryValidator”`
  - The plugin to use for validating final optimal trajectories.

- **`use_path_orientations`**
  - Type: `bool`
  - Default: `false`
  - Whether to consider path’s orientations in path alignment, which can be useful when paired with feasible smac planners to incentivize directional changes only where/when the smac planner requests t...

- **`visualize`**
  - Type: `bool`
  - Default: `false`
  - Whether to publish debugging trajectories for visualization. This can slow down the controller substantially (e.g. 1000 batches of 56 size every 30hz is a lot of data).

- **`vx_max`**
  - Type: `double`
  - Default: `0.5`
  - Target maximum forward velocity (m/s).

- **`vx_min`**
  - Type: `double`
  - Default: `-0.35`
  - Maximum reverse velocity (m/s).

- **`vx_std`**
  - Type: `double`
  - Default: `0.2`
  - Sampling standard deviation for Vx

- **`vy_max`**
  - Type: `double`
  - Default: `0.5`
  - Target maximum lateral velocity, if usingOmnimotion model (m/s).

- **`vy_std`**
  - Type: `double`
  - Default: `0.2`
  - Sampling standard deviation for Vy

- **`wz_max`**
  - Type: `double`
  - Default: `1.9`
  - Maximum rotational velocity (rad/s).

- **`wz_std`**
  - Type: `double`
  - Default: `0.2`
  - Sampling standard deviation for Wz (angular velocity)

---

## Navfn

### NavFn Planner
*Source: https://docs.nav2.org/configuration/packages/configuring-navfn.html*

- **`<name>.allow_unknown`**
  - Type: `bool`
  - Default: `True`
  - Whether to allow planning in unknown space.

- **`<name>.tolerance`**
  - Type: `double`
  - Default: `0.5`
  - Tolerance in meters between requested goal pose and end of path.

- **`<name>.use_astar`**
  - Type: `bool`
  - Default: `False`
  - Whether to use A*. If false, uses Dijkstra’s expansion.

- **`<name>.use_final_approach_orientation`**
  - Type: `bool`
  - Default: `false`
  - If true, the last pose of the path generated by the planner will have its orientation set to the approach orientation, i.e. the orientation of the vector connecting the last two points of the path

- **`allow_parameter_qos_overrides`**
  - Type: `bool`
  - Default: `true`
  - Whether to allow QoS profiles to be overwritten with parameterized values.

---

## Navigatethroughposes

### NavigateThroughPoses
*Source: https://docs.nav2.org/configuration/packages/bt-plugins/actions/NavigateThroughPoses.html*

- **`behavior_tree`**
  - Type: `string`
  - Default: `N/A`
  - Behavior tree absolute path or ID. If none is specified, NavigateThroughPoses action server uses a default behavior tree.

- **`error_code_id`**
  - Type: `uint16`
  - Default: `N/A`
  - The lowest error code in the list of theerror_code_name_prefixesparameter.

- **`error_msg`**
  - Type: `string`
  - Default: `N/A`
  - The error message associated with the lowest error code in the list of theerror_code_name_prefixesparameter.

- **`goals`**
  - Type: `nav_msgs::msg::Goals`
  - Default: `N/A`
  - Goal poses. Takes in a blackboard variable, e.g. “{goals}”.

- **`server_name`**
  - Type: `string`
  - Default: `N/A`
  - Action server name.

- **`server_timeout`**
  - Type: `double`
  - Default: `10`
  - Action server timeout (ms).

---

## Navigatetopose

### NavigateToPose
*Source: https://docs.nav2.org/configuration/packages/bt-plugins/actions/NavigateToPose.html*

- **`behavior_tree`**
  - Type: `string`
  - Default: `N/A`
  - Behavior tree absolute path or ID. If none is specified, NavigateToPose action server uses a default behavior tree.

- **`error_code_id`**
  - Type: `uint16`
  - Default: `N/A`
  - The lowest error code in the list of theerror_code_names_prefixes+_error_codesuffix parameter.

- **`error_msg`**
  - Type: `string`
  - Default: `N/A`
  - The error messages associated with the lowest error code in the list of theerror_code_name_prefixes+_error_codeparameter.

- **`goal`**
  - Type: `PoseStamped`
  - Default: `N/A`
  - Takes in a blackboard variable containing the goal, eg. “{goal}”.

- **`server_name`**
  - Type: `string`
  - Default: `N/A`
  - Action server name.

- **`server_timeout`**
  - Type: `double`
  - Default: `10`
  - Action server timeout (ms).

---

## Obstacle

### Obstacle Layer Parameters
*Source: https://docs.nav2.org/configuration/packages/costmap-plugins/obstacle.html*

- **`<obstaclelayer>.<datasource>.clearing`**
  - Type: `bool`
  - Default: `False`
  - Whether source should raytrace clear in costmap.

- **`<obstaclelayer>.<datasource>.data_type`**
  - Type: `string`
  - Default: `“LaserScan”`
  - Data type of input, LaserScan or PointCloud2.

- **`<obstaclelayer>.<datasource>.expected_update_rate`**
  - Type: `double`
  - Default: `0.0`
  - Expected rate to get new data from sensor.

- **`<obstaclelayer>.<datasource>.inf_is_valid`**
  - Type: `bool`
  - Default: `False`
  - Are infinite returns from laser scanners valid measurements to raycast.

- **`<obstaclelayer>.<datasource>.marking`**
  - Type: `bool`
  - Default: `True`
  - Whether source should mark in costmap.

- **`<obstaclelayer>.<datasource>.max_obstacle_height`**
  - Type: `double`
  - Default: `0.0`
  - Maximum height to add return to occupancy grid.

- **`<obstaclelayer>.<datasource>.min_obstacle_height`**
  - Type: `double`
  - Default: `0.0`
  - Minimum height to add return to occupancy grid.

- **`<obstaclelayer>.<datasource>.observation_persistence`**
  - Type: `double`
  - Default: `0.0`
  - How long to store messages in a buffer to add to costmap before removing them (s).

- **`<obstaclelayer>.<datasource>.obstacle_max_range`**
  - Type: `double`
  - Default: `2.5`
  - Maximum range to mark obstacles in costmap.

- **`<obstaclelayer>.<datasource>.obstacle_min_range`**
  - Type: `double`
  - Default: `0.0`
  - Minimum range to mark obstacles in costmap.

- **`<obstaclelayer>.<datasource>.raytrace_max_range`**
  - Type: `double`
  - Default: `3.0`
  - Maximum range to raytrace clear obstacles from costmap.

- **`<obstaclelayer>.<datasource>.raytrace_min_range`**
  - Type: `double`
  - Default: `0.0`
  - Minimum range to raytrace clear obstacles from costmap.

- **`<obstaclelayer>.<datasource>.sensor_frame`**
  - Type: `string`
  - Default: `“”`
  - Frame of sensor, to use if not provided by message. If empty, uses message frame_id.

- **`<obstaclelayer>.<datasource>.topic`**
  - Type: `string`
  - Default: `“”`
  - Topic of data.

- **`<obstaclelayer>.<datasource>.transport_type`**
  - Type: `string`
  - Default: `“raw”`
  - ForPointCloud2data, specify the transport plugin to use:

- **`<obstaclelayer>.combination_method`**
  - Type: `int`
  - Default: `1`
  - Enum for method to add data to master costmap. Must be 0, 1 or 2, default to 1 (see below).

- **`<obstaclelayer>.enabled`**
  - Type: `bool`
  - Default: `True`
  - Whether it is enabled.

- **`<obstaclelayer>.footprint_clearing_enabled`**
  - Type: `bool`
  - Default: `True`
  - Clear any occupied cells under robot footprint.

- **`<obstaclelayer>.max_obstacle_height`**
  - Type: `double`
  - Default: `2.0`
  - Maximum height to add return to occupancy grid.

- **`<obstaclelayer>.min_obstacle_height`**
  - Type: `double`
  - Default: `0.0`
  - Minimum height to add return to occupancy grid.

- **`<obstaclelayer>.observation_sources`**
  - Type: `vector<string>`
  - Default: `{“”}`
  - namespace of sources of data.

- **`<obstaclelayer>.tf_filter_tolerance`**
  - Type: `double`
  - Default: `0.05`
  - Tolerance for thetf2_ros::MessageFilter.

- **`draco`**
  - Lossy compression via Google.

- **`raw`**
  - No compression. Default; highest bandwidth usage.

- **`zlib`**
  - Lossless compression via Zlib compression.

- **`zstd`**
  - Lossless compression via Zstd compression.

---

## Obstacle_Footprint

### ObstacleFootprintCritic
*Source: https://docs.nav2.org/configuration/packages/trajectory_critics/obstacle_footprint.html*

- **`<dwbplugin>.<name>.scale`**
  - Type: `double`
  - Default: `1.0`
  - Weighed scale for critic.

- **`<dwbplugin>.<name>.sum_scores`**
  - Type: `bool`
  - Default: `false`
  - Whether to allow for scores to be summed up.

---

## Oscillation

### OscillationCritic
*Source: https://docs.nav2.org/configuration/packages/trajectory_critics/oscillation.html*

- **`<dwbplugin>.<name>.oscillation_reset_angle`**
  - Type: `double`
  - Default: `0.2`
  - Minimum angular distance to move to reset watchdog (rad).

- **`<dwbplugin>.<name>.oscillation_reset_dist`**
  - Type: `double`
  - Default: `0.05`
  - Minimum distance to move to reset oscillation watchdog (m).

- **`<dwbplugin>.<name>.oscillation_reset_time`**
  - Type: `double`
  - Default: `-1`
  - Duration when a reset may be called. If -1, cannot be reset..

- **`<dwbplugin>.<name>.scale`**
  - Type: `double`
  - Default: `1.0`
  - Weighed scale for critic.

- **`<dwbplugin>.<name>.x_only_threshold`**
  - Type: `double`
  - Default: `0.05`
  - Threshold to check in the X velocity direction.

---

## Path_Align

### PathAlignCritic
*Source: https://docs.nav2.org/configuration/packages/trajectory_critics/path_align.html*

- **`<dwbplugin>.<name>.aggregation_type`**
  - Type: `string`
  - Default: `“last”`
  - last, sum, or product combination methods.

- **`<dwbplugin>.<name>.forward_point_distance`**
  - Type: `double`
  - Default: `0.325`
  - Point in front of robot to look ahead to compute angular change from.

- **`<dwbplugin>.<name>.scale`**
  - Type: `double`
  - Default: `1.0`
  - Weighed scale for critic.

---

## Path_Dist

### PathDistCritic
*Source: https://docs.nav2.org/configuration/packages/trajectory_critics/path_dist.html*

- **`<dwbplugin>.<name>.aggregation_type`**
  - Type: `string`
  - Default: `“last”`
  - last, sum, or product combination methods.

- **`<dwbplugin>.<name>.scale`**
  - Type: `double`
  - Default: `1.0`
  - Weighed scale for critic.

---

## Pathexpiringtimer

### PathExpiringTimer
*Source: https://docs.nav2.org/configuration/packages/bt-plugins/conditions/PathExpiringTimer.html*

- **`path`**
  - Type: `nav_msgs::msg::Path`
  - Default: `N/A`
  - Check if path has been updated to enable timer reset.

- **`seconds`**
  - Type: `double`
  - Default: `1.0`
  - Time to check if expired.

---

## Pathhandlerselector

### PathHandlerSelector
*Source: https://docs.nav2.org/configuration/packages/bt-plugins/actions/PathHandlerSelector.html*

- **`default_path_handler`**
  - Type: `string`
  - Default: `N/A`
  - The default value for the selected PathHandler if no message is received from the input topic.

- **`selected_path_handler`**
  - Type: `string`
  - Default: `N/A`
  - The output selected PathHandler id. This selected_path_handler string is usually passed to the FollowPath behavior via the path_handler_id input port.

- **`topic_name`**
  - Type: `string`
  - Default: `path_handler_selector`
  - The name of the topic used to received select command messages. This is used to support multiple PathHandlerSelector nodes.

---

## Pathlongeronapproach

### PathLongerOnApproach
*Source: https://docs.nav2.org/configuration/packages/bt-plugins/decorators/PathLongerOnApproach.html*

- **`length_factor`**
  - Type: `double`
  - Default: `2.0`
  - Length multiplication factor to check if the path is significantly longer.

- **`path`**
  - Type: `nav_msgs::msg::Path`
  - Default: `N/A`
  - Path created by action server. Takes in a blackboard variable, e.g. “{path}”.

- **`prox_len`**
  - Type: `double`
  - Default: `3.0`
  - Proximity length (m) for the path to be longer on approach.

---

## Pauseresumecontroller

### PauseResumeController
*Source: https://docs.nav2.org/configuration/packages/bt-plugins/controls/PauseResumeController.html*

- **`pause_service_name`**
  - name of the service to pause

- **`resume_service_name`**
  - name of the service to resume

---

## Photo_At_Waypoint

### PhotoAtWaypoint
*Source: https://docs.nav2.org/configuration/packages/nav2_waypoint_follower-plugins/photo_at_waypoint.html*

- **`<nav2_waypoint_followerplugin>.camera_image_topic_name`**
  - Type: `string`
  - Default: `“/camera/color/image_raw”`
  - Camera image topic name to subscribe

- **`<nav2_waypoint_followerplugin>.enabled`**
  - Type: `bool`
  - Default: `true`
  - Whether waypoint_task_executor plugin is enabled.

- **`<nav2_waypoint_followerplugin>.image_format`**
  - Type: `string`
  - Default: `“png”`
  - Desired image format.

- **`<nav2_waypoint_followerplugin>.save_images_dir`**
  - Type: `string`
  - Default: `“/tmp/waypoint_images”`
  - Path to directory to save taken photos at waypoint arrivals.

- **`allow_parameter_qos_overrides`**
  - Type: `bool`
  - Default: `true`
  - Whether to allow QoS profiles to be overwritten with parameterized values.

---

## Planner Server

### Planner Server
*Source: https://docs.nav2.org/configuration/packages/configuring-planner-server.html*

- **`allow_parameter_qos_overrides`**
  - Type: `bool`
  - Default: `true`
  - Whether to allow QoS profiles to be overwritten with parameterized values.

- **`allow_partial_planning`**
  - Type: `bool`
  - Default: `false`
  - Allows planner server to output partial paths in the presence of obstacles when planning through poses. Otherwise planner fails and aborts the plan request in such a case by default.

- **`bond_heartbeat_period`**
  - Type: `double`
  - Default: `0.25`
  - The lifecycle node bond mechanism publishing period (on the /bond topic). Disabled if inferior or equal to 0.0.

- **`costmap_update_timeout`**
  - Type: `double`
  - Default: `1.0`
  - The timeout value (seconds) for the costmap to be fully updated before a planning request.

- **`expected_planner_frequency`**
  - Type: `double`
  - Default: `20.0`
  - Expected planner frequency. If the current frequency is less than the expected frequency, display the warning message.

- **`introspection_mode`**
  - Type: `string`
  - Default: `“disabled”`
  - The introspection mode for services and actions. Options are “disabled”, “metadata”, “contents”.

- **`planner_plugins`**
  - Type: `vector<string>`
  - Default: `[‘GridBased’]`
  - List of Mapped plugin names for parameters and processing requests.

- **`“GridBased”`**

---

## Plannerselector

### PlannerSelector
*Source: https://docs.nav2.org/configuration/packages/bt-plugins/actions/PlannerSelector.html*

- **`default_planner`**
  - Type: `string`
  - Default: `N/A`
  - The default value for the selected planner if no message is received from the input topic.

- **`selected_planner`**
  - Type: `string`
  - Default: `N/A`
  - The output selected planner id. This selected_planner string is usually passed to the ComputePathToPose behavior via the planner_id input port.

- **`topic_name`**
  - Type: `string`
  - Default: `planner_selector`
  - The name of the topic used to received select command messages. This is used to support multiple PlannerSelector nodes.

---

## Plugin_Container

### Plugin Container Layer Parameters
*Source: https://docs.nav2.org/configuration/packages/costmap-plugins/plugin_container.html*

- **`<plugincontainerlayer>.enabled`**
  - Type: `bool`
  - Default: `True`
  - Whether it is enabled.

- **`<plugincontainerlayer>.plugins`**
  - Type: `vector<string>`
  - Default: `{}`
  - List of mapped costmap layer names for parameter namespaces and names.

---

## Pose_Progress_Checker

### PoseProgressChecker
*Source: https://docs.nav2.org/configuration/packages/nav2_controller-plugins/pose_progress_checker.html*

- **`<nav2_controllerplugin>.movement_time_allowance`**
  - Type: `double`
  - Default: `10.0`
  - Maximum amount of time a robot has to move the minimum radius or the mnimum angle (s).

- **`<nav2_controllerplugin>.required_movement_angle`**
  - Type: `double`
  - Default: `0.5`
  - Minimum amount a robot must rotate to be progressing to goal (rad).

- **`<nav2_controllerplugin>.required_movement_radius`**
  - Type: `double`
  - Default: `0.5`
  - Minimum amount a robot must move to be progressing to goal (m).

---

## Position_Goal_Checker

### PositionGoalChecker
*Source: https://docs.nav2.org/configuration/packages/nav2_controller-plugins/position_goal_checker.html*

- **`<nav2_controllerplugin>.path_length_tolerance`**
  - Type: `double`
  - Default: `1.0`
  - Tolerance to meet goal completion criteria (m).

- **`<nav2_controllerplugin>.stateful`**
  - Type: `bool`
  - Default: `true`
  - Whether to check for XY position tolerance after rotating to goal orientation in case of minor localization changes.

- **`<nav2_controllerplugin>.xy_goal_tolerance`**
  - Type: `double`
  - Default: `0.25`
  - Tolerance to meet goal completion criteria (m).

---

## Prefer_Forward

### PreferForwardCritic
*Source: https://docs.nav2.org/configuration/packages/trajectory_critics/prefer_forward.html*

- **`<dwbplugin>.<name>.penalty`**
  - Type: `double`
  - Default: `1.0`
  - Penalty to apply to backward motion.

- **`<dwbplugin>.<name>.scale`**
  - Type: `double`
  - Default: `1.0`
  - Weighed scale for critic.

- **`<dwbplugin>.<name>.strafe_theta`**
  - Type: `double`
  - Default: `0.2`
  - Minimum angular velocity before applying penalty.

- **`<dwbplugin>.<name>.strafe_x`**
  - Type: `double`
  - Default: `0.1`
  - Minimum X velocity before penalty.

- **`<dwbplugin>.<name>.theta_scale`**
  - Type: `double`
  - Default: `10.0`
  - Weight for angular velocity component.

---

## Progresscheckerselector

### ProgressCheckerSelector
*Source: https://docs.nav2.org/configuration/packages/bt-plugins/actions/ProgressCheckerSelector.html*

- **`default_progress_checker`**
  - Type: `string`
  - Default: `N/A`
  - The default value for the selected ProgressChecker if no message is received from the input topic.

- **`selected_progress_checker`**
  - Type: `string`
  - Default: `N/A`
  - The output selected ProgressChecker id. This selected_progress_checker string is usually passed to the FollowPath behavior via the progress_checker_id input port.

- **`topic_name`**
  - Type: `string`
  - Default: `progress_checker_selector`
  - The name of the topic used to received select command messages. This is used to support multiple ProgressCheckerSelector nodes.

---

## Range

### Range Sensor Parameters
*Source: https://docs.nav2.org/configuration/packages/costmap-plugins/range.html*

- **`<rangelayer>.clear_on_max_reading`**
  - Type: `bool`
  - Default: `False`
  - Whether to clear the sensor readings on max range.

- **`<rangelayer>.clear_threshold`**
  - Type: `double`
  - Default: `0.2`
  - Probability below which cells are marked as free.

- **`<rangelayer>.enabled`**
  - Type: `bool`
  - Default: `True`
  - Whether it is enabled.

- **`<rangelayer>.inflate_cone`**
  - Type: `double`
  - Default: `1.0`
  - Inflate the triangular area covered by the sensor (percentage).

- **`<rangelayer>.input_sensor_type`**
  - Type: `string`
  - Default: `ALL`
  - Input sensor type is either ALL (automatic selection), VARIABLE (min range != max range), or FIXED (min range == max range).

- **`<rangelayer>.mark_threshold`**
  - Type: `double`
  - Default: `0.8`
  - Probability above which cells are marked as occupied.

- **`<rangelayer>.no_readings_timeout`**
  - Type: `double`
  - Default: `0.0`
  - If zero, this parameter has no effect. Otherwise if the layer does not receive sensor data for this amount of time, the layer will warn the user and the layer will be marked as not current.

- **`<rangelayer>.phi`**
  - Type: `double`
  - Default: `1.2`
  - Phi value.

- **`<rangelayer>.topics`**
  - Type: `vector<string>`
  - Range topics to subscribe to.

---

## Ratecontroller

### RateController
*Source: https://docs.nav2.org/configuration/packages/bt-plugins/decorators/RateController.html*

- **`hz`**
  - Type: `double`
  - Default: `10.0`
  - Rate to throttle an action or a group of actions.

---

## Recoverynode

### RecoveryNode
*Source: https://docs.nav2.org/configuration/packages/bt-plugins/controls/RecoveryNode.html*

- **`number_of_retries`**
  - Type: `int`
  - Default: `1`
  - Number of retries.

---

## Regulated Pp

### Regulated Pure Pursuit
*Source: https://docs.nav2.org/configuration/packages/configuring-regulated-pp.html*

- **`allow_parameter_qos_overrides`**
  - Type: `bool`
  - Default: `true`
  - Whether to allow QoS profiles to be overwritten with parameterized values.

- **`allow_reversing`**
  - Type: `bool`
  - Default: `false`
  - Enables the robot to drive in the reverse direction, when the path planned involves reversing (which is represented by orientation cusps). Variants of the smac_planner comes with the support of rev...

- **`approach_velocity_scaling_dist`**
  - Type: `double`
  - Default: `0.6`
  - The distance (m) left on the path at which to start slowing down. Should be less than the half the costmap width.

- **`cancel_deceleration`**
  - Type: `double`
  - Default: `3.2`
  - Linear deceleration (m/s/s) to apply when the goal is canceled.

- **`cost_scaling_dist`**
  - Type: `double`
  - Default: `0.6`
  - The minimum distance from an obstacle to trigger the scaling of linear velocity, ifuse_cost_regulated_linear_velocity_scalingis enabled. The value set should be smaller or equal to theinflation_rad...

- **`cost_scaling_gain`**
  - Type: `double`
  - Default: `1.0`
  - A multiplier gain, which should be <= 1.0, used to further scale the speed when an obstacle is withincost_scaling_dist. Lower value reduces speed more quickly.

- **`curvature_lookahead_dist`**
  - Type: `double`
  - Default: `0.6`
  - Distance to look ahead on the path to detect curvature.

- **`interpolate_curvature_after_goal`**
  - Type: `bool`
  - Default: `false`
  - Interpolate a carrot after the goal dedicated to the curvate calculation (to avoid oscilaltions at the end of the path). For visualization, it will be published on the/curvature_lookahead_pointtopi...

- **`lookahead_dist`**
  - Type: `double`
  - Default: `0.6`
  - The lookahead distance (m) to use to find the lookahead point whenuse_velocity_scaled_lookahead_distisfalse.

- **`lookahead_time`**
  - Type: `double`
  - Default: `1.5`
  - The time (s) to project the velocity by whenuse_velocity_scaled_lookahead_dististrue. Also known as the lookahead gain.

- **`max_allowed_time_to_collision_up_to_carrot`**
  - Type: `double`
  - Default: `1.0`
  - The time (s) to project a velocity command forward to check for collisions whenuse_collision_detectionistrue. Pre-Humble, this wasmax_allowed_time_to_collision.

- **`max_angular_accel`**
  - Type: `double`
  - Default: `3.2`
  - The maximum angular acceleration (rad/s^2) to use.

- **`max_angular_decel`**
  - Type: `double`
  - Default: `-3.2`
  - The maximum angular deceleration (rad/s^2) used whenuse_dynamic_windowistrue.

- **`max_angular_vel`**
  - Type: `double`
  - Default: `2.5`
  - The maximum angular velocity (rad/s) used whenuse_dynamic_windowistrue.

- **`max_linear_accel`**
  - Type: `double`
  - Default: `2.5`
  - The maximum linear acceleration (m/s^2) used whenuse_dynamic_windowistrue.

- **`max_linear_decel`**
  - Type: `double`
  - Default: `-2.5`
  - The maximum linear deceleration (m/s^2) used whenuse_dynamic_windowistrue.

- **`max_linear_vel`**
  - Type: `double`
  - Default: `0.5`
  - The maximum linear velocity (m/s) to use.  Previouslydesired_linear_vel

- **`max_lookahead_dist`**
  - Type: `double`
  - Default: `0.9`
  - The maximum lookahead distance (m) threshold whenuse_velocity_scaled_lookahead_dististrue.

- **`min_angular_vel`**
  - Type: `double`
  - Default: `-2.5`
  - The minimum angular velocity (rad/s) used whenuse_dynamic_windowistrue.

- **`min_approach_linear_velocity`**
  - Type: `double`
  - Default: `0.05`
  - The minimum velocity (m/s) threshold to apply when approaching the goal to ensure progress. Must be>0.01.

- **`min_distance_to_obstacle`**
  - Type: `double`
  - Default: `-1.0`
  - The shortest distance at which the robot is allowed to be from an obstacle along its trajectory. Set <= 0.0 to disable. It is limited to maximum distance of lookahead distance selected.

- **`min_linear_vel`**
  - Type: `double`
  - Default: `-0.5`
  - The minimum linear velocity (m/s) used whenuse_dynamic_windowistrue.

- **`min_lookahead_dist`**
  - Type: `double`
  - Default: `0.3`
  - The minimum lookahead distance (m) threshold whenuse_velocity_scaled_lookahead_dististrue.

- **`regulated_linear_scaling_min_radius`**
  - Type: `double`
  - Default: `0.90`
  - The turning radius (m) for which the regulation features are triggered whenuse_regulated_linear_velocity_scalingistrue. Remember, sharper turns have smaller radii.

- **`regulated_linear_scaling_min_speed`**
  - Type: `double`
  - Default: `0.25`
  - The minimum speed (m/s) for which any of the regulated heuristics can send, to ensure process is still achievable even in high cost spaces with high curvature. Must be>0.1.

- **`rotate_to_heading_angular_vel`**
  - Type: `double`
  - Default: `1.8`
  - Ifuse_rotate_to_headingistrue, this is the angular velocity to use.

- **`rotate_to_heading_min_angle`**
  - Type: `double`
  - Default: `0.785`
  - The difference in the path orientation and the starting robot orientation (radians) to trigger a rotate in place, ifuse_rotate_to_headingistrue.

- **`stateful`**
  - Type: `bool`
  - Default: `true`
  - Enables stateful goal handling behavior. When set to true, the controller will persist the goal state once the robot reaches the XY tolerance. It will then focus on aligning to the goal heading wit...

- **`use_cancel_deceleration`**
  - Type: `bool`
  - Default: `false`
  - Whether to use deceleration when the goal is canceled.

- **`use_collision_detection`**
  - Type: `bool`
  - Default: `true`
  - Whether to enable collision detection.

- **`use_cost_regulated_linear_velocity_scaling`**
  - Type: `bool`
  - Default: `true`
  - Whether to use the regulated features for proximity to obstacles (e.g. slow in close proximity to obstacles).

- **`use_dynamic_window`**
  - Type: `bool`
  - Default: `false`
  - Whether to use the Dynamic Window Pure Pursuit (DWPP) Algorithm. This algorithm computes command velocities that track the path as accurately as possible while respecting velocity and acceleration ...

- **`use_fixed_curvature_lookahead`**
  - Type: `bool`
  - Default: `false`
  - Whether to use a fixed lookahead distance to compute curvature from. Since a lookahead distance may be set to vary on velocity, it can introduce a reference cycle that can be problematic for large ...

- **`use_regulated_linear_velocity_scaling`**
  - Type: `bool`
  - Default: `true`
  - Whether to use the regulated features for path curvature (e.g. slow on high curvature paths).

- **`use_rotate_to_heading`**
  - Type: `bool`
  - Default: `true`
  - Whether to enable rotating to rough heading and goal orientation when using holonomic planners. Recommended on for all robot types that can rotate in place.Note: bothuse_rotate_to_headingandallow_r...

- **`use_velocity_scaled_lookahead_dist`**
  - Type: `bool`
  - Default: `false`
  - Whether to use the velocity scaled lookahead distances or constantlookahead_distance.

---

## Reinitializegloballocalization

### ReinitializeGlobalLocalization
*Source: https://docs.nav2.org/configuration/packages/bt-plugins/actions/ReinitializeGlobalLocalization.html*

- **`server_timeout`**
  - Type: `double`
  - Default: `10`
  - Server timeout (ms).

- **`service_name`**
  - Type: `string`
  - Default: `N/A`
  - Service name.

---

## Removeincollisiongoals

### RemoveInCollisionGoals
*Source: https://docs.nav2.org/configuration/packages/bt-plugins/actions/RemoveInCollisionGoals.html*

- **`consider_unknown_as_obstacle`**
  - Type: `bool`
  - Default: `false`
  - Whether to consider unknown cost (255) as obstacle.

- **`cost_threshold`**
  - Type: `double`
  - Default: `254.0`
  - The cost threshold above which a waypoint is considered in collision and should be removed. Ifuse_footprint=false, consider setting to 253 for occupied.

- **`input_goals`**
  - Type: `nav_msgs::msg::Goals`
  - Default: `N/A`
  - A vector of goals to check if in collision

- **`input_waypoint_statuses`**
  - Type: `std::vector<nav2_msgs::msg::WaypointStatus>`
  - Default: `N/A`
  - Original waypoint_statuses to mark waypoint status from.

- **`output_goals`**
  - Type: `geometry_msgs::msg::PoseStamped`
  - Default: `N/A`
  - A vector of goals containing only those that are not in collision.

- **`output_waypoint_statuses`**
  - Type: `std::vector<nav2_msgs::msg::WaypointStatus>`
  - Default: `N/A`
  - Waypoint_statuses with in-collision waypoints marked.

- **`service_name`**
  - Type: `string`
  - Default: `/global_costmap/get_cost_global_costmap`
  - costmap service name responsible for getting the cost.

- **`use_footprint`**
  - Type: `bool`
  - Default: `true`
  - Whether to use the footprint cost or the point cost.

---

## Removepassedgoals

### RemovePassedGoals
*Source: https://docs.nav2.org/configuration/packages/bt-plugins/actions/RemovePassedGoals.html*

- **`input_goals`**
  - Type: `nav_msgs::msg::Goals`
  - Default: `N/A`
  - A vector of goals to check if it passed any in the current iteration.

- **`input_waypoint_statuses`**
  - Type: `std::vector<nav2_msgs::msg::WaypointStatus>`
  - Default: `N/A`
  - Original waypoint_statuses to mark waypoint status from.

- **`output_goals`**
  - Type: `nav_msgs::msg::Goals`
  - Default: `N/A`
  - A vector of goals with goals removed in proximity to the robot

- **`output_waypoint_statuses`**
  - Type: `std::vector<nav2_msgs::msg::WaypointStatus>`
  - Default: `N/A`
  - Waypoint_statuses with passed waypoints marked.

- **`radius`**
  - Type: `double`
  - Default: `0.5`
  - The radius (m) in proximity to the viapoint for the BT node to remove from the list as having passed.

- **`robot_base_frame`**
  - Type: `string`
  - Default: `“base_link”`
  - Robot base frame.

---

## Rotate_To_Goal

### RotateToGoalCritic
*Source: https://docs.nav2.org/configuration/packages/trajectory_critics/rotate_to_goal.html*

- **`<dwbplugin>.<name>.lookahead_time`**
  - Type: `double`
  - Default: `-1`
  - If > 0, amount of time to look forward for a collision for..

- **`<dwbplugin>.<name>.scale`**
  - Type: `double`
  - Default: `1.0`
  - Weighed scale for critic.

- **`<dwbplugin>.<name>.slowing_factor`**
  - Type: `double`
  - Default: `5.0`
  - Factor to slow robot motion by while rotating to goal.

- **`<dwbplugin>.path_length_tolerance`**
  - Type: `double`
  - Default: `1.0`
  - Tolerance to meet goal completion criteria (m).

- **`<dwbplugin>.trans_stopped_velocity`**
  - Type: `double`
  - Default: `0.25`
  - Velocity below is considered to be stopped at tolerance met (rad/s).

- **`<dwbplugin>.xy_goal_tolerance`**
  - Type: `double`
  - Default: `0.25`
  - Tolerance to meet goal completion criteria (m).

---

## Rotation Shim Controller

### Rotation Shim Controller
*Source: https://docs.nav2.org/configuration/packages/configuring-rotation-shim-controller.html*

- **`angular_disengage_threshold`**
  - Type: `double`
  - Default: `0.3925`
  - New to Jazzy, the threshold to the path’s heading before disengagement (radians). Prior to Jazzy, disengagement occurs at theangular_dist_thresholdinstead. This allows for better alignment before p...

- **`angular_dist_threshold`**
  - Type: `double`
  - Default: `0.785`
  - Maximum angular distance, in radians, away from the path heading to trigger rotation

- **`closed_loop`**
  - Type: `bool`
  - Default: `true`
  - If false, the rotationShimController will use the last commanded velocity as the next iteration’s current velocity. When acceleration limits are set appropriately and the robot’s controllers are re...

- **`forward_sampling_distance`**
  - Type: `double`
  - Default: `0.5`
  - Forward distance, in meters, along path to select a sampling point to use to approximate path heading. This distance should not be larger than the path handler’s prune distance.

- **`max_angular_accel`**
  - Type: `double`
  - Default: `3.2`
  - Maximum angular acceleration for rotation to heading (rad/s/s)

- **`primary_controller`**
  - Type: `string`
  - Default: `N/A`
  - Internal controller plugin to use for actual control behavior after rotating to heading

- **`rotate_to_goal_heading`**
  - Type: `bool`
  - Default: `false`
  - If true, the rotationShimController will take back control of the robot when in XY tolerance of the goal and start rotating towards the goal heading.

- **`rotate_to_heading_angular_vel`**
  - Type: `double`
  - Default: `1.8`
  - Angular rotational velocity, in rad/s, to rotate to the path heading

- **`rotate_to_heading_once`**
  - Type: `bool`
  - Default: `false`
  - If true, the rotationShimController will only rotate to heading once on a new goal, not each time a path is set.

- **`simulate_ahead_time`**
  - Type: `double`
  - Default: `1.0`
  - Time in seconds to forward simulate a rotation command to check for collisions. If a collision is found, forwards control back to the primary controller plugin.

- **`use_path_orientations`**
  - Type: `bool`
  - Default: `false`
  - If true, the controller will use the orientations of the path points to compute the heading of the path instead of computing the heading from the path point’s relative locations. If true, the contr...

---

## Roundrobin

### RoundRobin
*Source: https://docs.nav2.org/configuration/packages/bt-plugins/controls/RoundRobin.html*

- **`wrap_around`**
  - Type: `bool`
  - Default: `false`
  - Controls wrap-around behavior. Whenfalse, the node returns FAILURE instead of wrapping to the first child after all children have been attempted. Whentrue, the node wraps around to the first child ...

---

## Route Server

### Route Server
*Source: https://docs.nav2.org/configuration/packages/configuring-route-server.html*

- **`<for each class>`**
  - Type: `double`
  - Default: `N/A`
  - The cost to assign to this semantic class. For example:highway:8.4.

- **`<name>.plugin`**
  - Type: `string`
  - Default: `“”`
  - The plugin to load under that name. Theedge_cost_functions.<name>namespaces is also where plugin-specific parameters are defined.

- **`aggregate_blocked_ids`**
  - Type: `bool`
  - Default: `false`
  - Whether to aggregate the blocked IDs reported by route operations over the lifespan of the navigation request or only use the currently marked blocked IDs.

- **`allow_parameter_qos_overrides`**
  - Type: `bool`
  - Default: `true`
  - Whether to allow QoS profiles to be overwritten with parameterized values.

- **`base_frame`**
  - Type: `string`
  - Default: `“base_link”`
  - The base frame of the robot to use to obtain the robot’s pose from when not using theuse_startrequest parameter.

- **`boundary_radius_to_achieve_node`**
  - Type: `double`
  - Default: `1.0`
  - The radius at a boundary condition (start, goal) to mark the node achieved by the tracker when usingComputeAndTrackRoute. Note that this is not the same as the goal tolerance, as the route or path ...

- **`check_resolution`**
  - Type: `int`
  - Default: `1`
  - Resolution to check costs at (1 = costmap resolution, 2 = 2x costmap resolution, etc)

- **`costmap_topic`**
  - Type: `string`
  - Default: `‘global_costmap/costmap_raw’`
  - The costmap to use for the server-level costmap subscriber. This is created to aid the goal intent extractor (if BFS-based terminal route node finding is enabled) and also shared with the Collision...

- **`edge_cost_functions`**
  - Type: `vector<string>`
  - Default: `[“DistanceScorer”, “DynamicEdgesScorer”]`
  - Which edge cost functions should be used for planning purposes to score the edges. By default, we optimize for minimum distance while providing a service cost function to set arbitrary costs or mar...

- **`enable_nn_search`**
  - Type: `bool`
  - Default: `true`
  - Whether to use Breadth-first search to find the nearest traversable node (true) or simply the nearest node (false) for the start and goal when using pose requests.

- **`graph_file_loader`**
  - Type: `string`
  - Default: `“GeoJsonGraphFileLoader”`
  - The name of the graph file loader plugin to use.

- **`graph_file_loader.plugin`**
  - Type: `string`
  - Default: `“nav2_route::GeoJsonGraphFileLoader”`
  - The graph loading plugin to use. By default, we usegeojson.

- **`graph_filepath`**
  - Type: `string`
  - Default: `“”`
  - The filepath to the graph file for loading. It may be empty on initialization, but then the graph must be set from the server’s set graph service later.

- **`introspection_mode`**
  - Type: `string`
  - Default: `“disabled”`
  - The introspection mode for services and actions. Options are “disabled”, “metadata”, “contents”.

- **`invalid_off_map`**
  - Type: `bool`
  - Default: `true`
  - Whether to consider route going off the map invalid

- **`invalid_on_collision`**
  - Type: `bool`
  - Default: `true`
  - Whether to consider collision status as a terminal condition

- **`MAP_POSES_DICT`**
  - A dictionary containing the Gazebo spawn poses for the robot in the depot and warehouse environments.

- **`MAP_POSES_DICT:`**
  - A dictionary containing the Gazebo spawn poses for the robot in the depot and warehouse environments.

- **`MAP_TYPE`**
  - Set to eitherdepotorwarehouseto choose the environment.

- **`MAP_TYPE:`**
  - Set to eitherdepotorwarehouseto choose the environment.

- **`max_collision_dist`**
  - Type: `double`
  - Default: `5.0`
  - The distance (meters) ahead of the robot’s position on the route to collision check during.

- **`max_cost`**
  - Type: `double`
  - Default: `253.0`
  - Maximum cost to consider an route blocked (253.0)

- **`max_iterations`**
  - Type: `int`
  - Default: `0`
  - The maximum number of planning iterations to perform. If 0, the maximum number of iterations is used.

- **`max_nn_search_iterations`**
  - Type: `int`
  - Default: `10000`
  - The maximum number of iterations to perform Breadth-first search to find the start and goal closest traversable nodes.

- **`max_planning_time`**
  - Type: `double`
  - Default: `2.0`
  - The maximum planning time to use.

- **`max_prune_dist_from_edge`**
  - Type: `double`
  - Default: `8.0`
  - Maximum distance from an edge to consider pruning it as in-progress (i.e. if we’re to far away from an edge, it is nonsensical to prune it).

- **`max_vel`**
  - Type: `double`
  - Default: `0.5`
  - Maximum velocity to use if speed limit or time taken is not set.

- **`min_prune_dist_from_goal`**
  - Type: `double`
  - Default: `0.15`
  - Minimum distance from the goal node away from the request’s goal pose (if usinguse_poses) to consider pruning as being passed, in case the goal pose is very close to the goal node, but is not exact.

- **`min_prune_dist_from_start`**
  - Type: `double`
  - Default: `0.1`
  - Minimum distance from the start node away from the start pose (if usinguse_poses) to consider pruning as being passed, in case the start pose is very close to the start node, but is not exact. Sett...

- **`num_nearest_nodes`**
  - Type: `int`
  - Default: `5`
  - The number of nearest-neighbors to extract from a Kd-tree in order to check against in the Breadth-first search.

- **`operations`**
  - Type: `vector<string>`
  - Default: `[“AdjustSpeedLimit”, “ReroutingService”]`
  - The route operation plugins to use forComputeAndTrackRoute. By default, we have a speed limit adjuster and a ROS service request rerouting operation.

- **`orientation_tolerance`**
  - Type: `double`
  - Default: `PI/2`
  - The angular threshold to reject edges’ angles if greater than this w.r.t. starting pose, whenuse_orientation_threshold:true.

- **`orientation_weight`**
  - Type: `double`
  - Default: `1.0`
  - Relative edge scoring weighting.

- **`path_density`**
  - Type: `double`
  - Default: `0.05`
  - The density of path-points in the output route, if using thenav_msgs/Pathroute rather than the collection of nodes and edges. This is used to upsample the route into a path that may be followed.

- **`penalty_tag`**
  - Type: `string`
  - Default: `“penalty”`
  - Graph metadata key to look for penalty value.

- **`prune_goal`**
  - Type: `bool`
  - Default: `true`
  - Whether pruning the goal node from the route due to it being spatially past the goal pose requested (pose requests onlyuse_poses).

- **`radius_to_achieve_node`**
  - Type: `double`
  - Default: `1.0`
  - The radius for non-boundary conditions to mark the node as achieved once within tolerance of, when usingComputeAndTrackRoute. Note that this is a radius to consider achievable, however a refinement...

- **`rate`**
  - Type: `double`
  - Default: `1.0`
  - The rate to collision at, rather than the tracker’s update rate since this is an expensive operation.

- **`reroute_on_collision`**
  - Type: `bool`
  - Default: `true`
  - Whether to reroute on collision or exit the tracking task as a failure when future collision is detected.

- **`route_frame`**
  - Type: `string`
  - Default: `“map”`
  - The frame of the route graph to plan within. If values in the graph file are not w.r.t. this frame, they will be automatically transformed.

- **`ROUTE_POSES_DICT`**
  - A dictionary containing the start and goal poses for the robot in the depot and warehouse environments.

- **`ROUTE_POSES_DICT:`**
  - A dictionary containing the start and goal poses for the robot in the depot and warehouse environments.

- **`semantic_classes`**
  - Type: `vector<string>`
  - Default: `[]`
  - The list of semantic classes in your graph that you would like to score based off of.

- **`semantic_key`**
  - Type: `string`
  - Default: `class`
  - The key to search for edge’s semantic data with the edge’s metadata. If empty string, will look at key names instead.

- **`smooth_corners`**
  - Type: `bool`
  - Default: `false`
  - Whether to smooth corners formed between subsequent edges after a route has been found

- **`smoothing_radius`**
  - Type: `double`
  - Default: `1.0`
  - Radius to fit to corners formed by edges if corner smoothing is enabled

- **`speed_limit_topic`**
  - Type: `string`
  - Default: `speed_limit`
  - The topic to publish new speed limits to.

- **`speed_tag`**
  - Type: `string`
  - Default: `“speed_limit”`
  - Graph metadata key to look for percentage speed limits (speed_limit).

- **`time_tag`**
  - Type: `string`
  - Default: `“abs_time_taken”`
  - Graph metadata key to look for abs traversal times.

- **`tracker_update_rate`**
  - Type: `double`
  - Default: `50.0`
  - The update rate of the tracker (when usingComputeAndTrackRouteaction) to check the status of path tracking and execute route operations.

- **`use_maximum`**
  - Type: `bool`
  - Default: `true`
  - Whether to score based on single maximum or average

- **`use_orientation_threshold`**
  - Type: `bool`
  - Default: `false`
  - Whether to use the orientation threshold for binary validity of traversal or weighted-angular distance scoring.

- **`weight`**
  - Type: `double`
  - Default: `1.0`
  - Relative edge scoring weighting.

---

## Savitzky Golay Smoother

### Savitzky-Golay Smoother
*Source: https://docs.nav2.org/configuration/packages/configuring-savitzky-golay-smoother.html*

- **`do_refinement`**
  - Type: `bool`
  - Default: `True`
  - Whether to smooth the smoothed resultsrefinement_numtimes to get an improved result.

- **`enforce_path_inversion`**
  - Type: `bool`
  - Default: `True`
  - Whether to consider input path discontinuities as path inversions from feasible planning to be respected or smooth other them. Leave on for Smac Planner feasible planners, but may want to disable f...

- **`poly_order`**
  - Type: `int`
  - Default: `3`
  - Order of the polynomial used to fit the samples in each smoothing window

- **`refinement_num`**
  - Type: `int`
  - Default: `2`
  - Number of times to recursively smooth a segment

- **`window_size`**
  - Type: `int`
  - Default: `7`
  - Size of the smoothing window. Must be an odd integer, with a minimum value of 3

---

## Simple Smoother

### Simple Smoother
*Source: https://docs.nav2.org/configuration/packages/configuring-simple-smoother.html*

- **`do_refinement`**
  - Type: `bool`
  - Default: `True`
  - Whether to smooth the smoothed path recursively to refine the quality further

- **`enforce_path_inversion`**
  - Type: `bool`
  - Default: `True`
  - Whether to consider input path discontinuities as path inversions from feasible planning to be respected or smooth other them. Leave on for Smac Planner feasible planners, but may want to disable f...

- **`max_its`**
  - Type: `int`
  - Default: `1000`
  - Maximum number of iterations to attempt smoothing before termination

- **`refinement_num`**
  - Type: `int`
  - Default: `2`
  - Number of times to recursively attempt to smooth, must be>=1.

- **`tolerance`**
  - Type: `double`
  - Default: `1.0e-10`
  - Change in parameter values across path to terminate smoothing

- **`w_data`**
  - Type: `double`
  - Default: `0.2`
  - Weight to apply to path data given (bounds it)

- **`w_smooth`**
  - Type: `double`
  - Default: `0.3`
  - Weight to apply to smooth the path (smooths it)

---

## Simple_Goal_Checker

### SimpleGoalChecker
*Source: https://docs.nav2.org/configuration/packages/nav2_controller-plugins/simple_goal_checker.html*

- **`<nav2_controllerplugin>.path_length_tolerance`**
  - Type: `double`
  - Default: `1.0`
  - Tolerance to meet goal completion criteria (m).

- **`<nav2_controllerplugin>.stateful`**
  - Type: `bool`
  - Default: `true`
  - Whether to check for XY position tolerance after rotating to goal orientation in case of minor localization changes.

- **`<nav2_controllerplugin>.symmetric_yaw_tolerance`**
  - Type: `bool`
  - Default: `false`
  - Enable symmetric goal orientation acceptance. When enabled, the robot accepts the goal as reached when oriented at either the goal orientation or the goal orientation + 180°. This is useful for sym...

- **`<nav2_controllerplugin>.xy_goal_tolerance`**
  - Type: `double`
  - Default: `0.25`
  - Tolerance to meet goal completion criteria (m).

- **`<nav2_controllerplugin>.yaw_goal_tolerance`**
  - Type: `double`
  - Default: `0.25`
  - Tolerance to meet goal completion criteria (rad).

---

## Simple_Progress_Checker

### SimpleProgressChecker
*Source: https://docs.nav2.org/configuration/packages/nav2_controller-plugins/simple_progress_checker.html*

- **`<nav2_controllerplugin>.movement_time_allowance`**
  - Type: `double`
  - Default: `10.0`
  - Maximum amount of time a robot has to move the minimum radius (s).

- **`<nav2_controllerplugin>.required_movement_radius`**
  - Type: `double`
  - Default: `0.5`
  - Minimum amount a robot must move to be progressing to goal (m).

---

## Smac 2D

### Smac 2D Planner
*Source: https://docs.nav2.org/configuration/packages/smac/configuring-smac-2d.html*

- **`<name>.allow_unknown`**
  - Type: `bool`
  - Default: `True`
  - Whether to allow traversing/search in unknown space.

- **`<name>.cost_travel_multiplier`**
  - Type: `double`
  - Default: `2.0`
  - Cost multiplier to apply to search to steer away from high cost areas. Larger values will place in the center of aisles more exactly (if non-FREEcost potential field exists) but take slightly longe...

- **`<name>.downsample_costmap`**
  - Type: `bool`
  - Default: `False`
  - Whether to downsample costmap to another resolution for search.

- **`<name>.downsampling_factor`**
  - Type: `int`
  - Default: `1`
  - Multiplier factor to downsample costmap by (e.g. if 5cm costmap at 2downsample_factor, 10cm output).

- **`<name>.max_iterations`**
  - Type: `int`
  - Default: `1000000`
  - Maximum number of search iterations before failing to limit compute time, disabled by -1.

- **`<name>.max_on_approach_iterations`**
  - Type: `int`
  - Default: `1000`
  - Maximum number of iterations after the search is withintolerancebefore returning approximate path with best heuristic if exact path is not found.

- **`<name>.max_planning_time`**
  - Type: `double`
  - Default: `2.0`
  - Maximum planning time in seconds.

- **`<name>.smoother.do_refinement`**
  - Type: `bool`
  - Default: `true`
  - Performs extra refinement smoothing runs. Essentially, this recursively calls the smoother using the output from the last smoothing cycle to further smooth the path for macro-trends.

- **`<name>.smoother.max_iterations`**
  - Type: `int`
  - Default: `1000`
  - The maximum number of iterations the smoother has to smooth the path, to bound potential computation.

- **`<name>.smoother.refinement_num`**
  - Type: `int`
  - Default: `2`
  - Number of times to recursively attempt to smooth, must be>=1.

- **`<name>.smoother.tolerance`**
  - Type: `double`
  - Default: `1e-10`
  - Parameter tolerance change amount to terminate smoothing session

- **`<name>.smoother.w_data`**
  - Type: `double`
  - Default: `0.2`
  - Weight for smoother to apply to retain original data information

- **`<name>.smoother.w_smooth`**
  - Type: `double`
  - Default: `0.3`
  - Weight for smoother to apply to smooth out the data points

- **`<name>.terminal_checking_interval`**
  - Type: `int`
  - Default: `5000`
  - Number of iterations between checking if the goal has been cancelled or planner timed out

- **`<name>.tolerance`**
  - Type: `double`
  - Default: `0.125`
  - Tolerance in meters between requested goal pose and end of path.

- **`<name>.use_final_approach_orientation`**
  - Type: `bool`
  - Default: `false`
  - If true, the last pose of the path generated by the planner will have its orientation set to the approach orientation, i.e. the orientation of the vector connecting the last two points of the path

- **`allow_parameter_qos_overrides`**
  - Type: `bool`
  - Default: `true`
  - Whether to allow QoS profiles to be overwritten with parameterized values.

---

## Smac Hybrid

### Smac Hybrid-A* Planner
*Source: https://docs.nav2.org/configuration/packages/smac/configuring-smac-hybrid.html*

- **`<name>.allow_primitive_interpolation`**
  - Type: `bool`
  - Default: `false`
  - Advanced feature: Allows a user to add additional primitives to the exploration set to interpolate between the angular quantization jumps between the normal primitive set (e.g. left, right, straigh...

- **`<name>.allow_unknown`**
  - Type: `bool`
  - Default: `True`
  - Whether to allow traversing/search in unknown space.

- **`<name>.analytic_expansion_max_cost`**
  - Type: `double`
  - Default: `200.0`
  - For Hybrid/Lattice nodes: The maximum single cost for any part of an analytic expansion to contain and be considered valid (except when necessary on approach to goal). This allows for removing of p...

- **`<name>.analytic_expansion_max_cost_override`**
  - Type: `bool`
  - Default: `false`
  - For Hybrid/Lattice nodes: Whether or not to override the maximum cost setting if within critical distance to goal (ie probably required). If expansion is within 2*pi*min_r of the goal, then it will...

- **`<name>.analytic_expansion_max_length`**
  - Type: `double`
  - Default: `3.0`
  - If the length is too far, reject this expansion. This prevents shortcutting of search with its penalty functions far out from the goal itself (e.g. so we don’t reverse half-way across open maps or ...

- **`<name>.analytic_expansion_ratio`**
  - Type: `double`
  - Default: `3.5`
  - Planner will attempt to complete an analytic expansions in a frequency proportional to this value and the minimum heuristic.

- **`<name>.angle_quantization_bins`**
  - Type: `int`
  - Default: `72`
  - Number of angular bins to use for SE2 search. This can be any even number, but a good baseline is 64 or 72 (for 5 degree increments).

- **`<name>.cache_obstacle_heuristic`**
  - Type: `bool`
  - Default: `false`
  - Advanced feature: Cache the obstacle map dynamic programming distance expansion heuristic between subsequent replannings of the same goal location. Dramatically speeds up replanning performance (40...

- **`<name>.change_penalty`**
  - Type: `double`
  - Default: `0.0`
  - Heuristic penalty to apply to SE2 node if changing direction (e.g. left to right) in search. Disabled by default after change to guarantee admissibility of the Hybrid-A* planner.

- **`<name>.coarse_search_resolution`**
  - Type: `int`
  - Default: `4`
  - Number of goal heading bins to skip during the coarse search phase of analytic expansion goal-finding. When a goal is found, a fine search is performed to determine the exact path during full-resol...

- **`<name>.cost_penalty`**
  - Type: `double`
  - Default: `2.0`
  - Heuristic penalty to apply to SE2 node for cost at pose. Allows Hybrid-A* to be cost aware.

- **`<name>.debug_visualizations`**
  - Type: `bool`
  - Default: `false`
  - Whether to publish expansions on the/expansionstopic as an array of poses and the path’s footprints on the/planned_footprintstopic. WARNING: heavy to compute and to display, for debug only as it de...

- **`<name>.downsample_costmap`**
  - Type: `bool`
  - Default: `False`
  - Whether to downsample costmap to another resolution for search.

- **`<name>.downsample_obstacle_heuristic`**
  - Type: `bool`
  - Default: `true`
  - Advanced feature: This allows a user to disable downsampling of the obstacle heuristic’s costmap representation to search at the costmap’s full-resolution. This will come at increased up-front cost...

- **`<name>.downsampling_factor`**
  - Type: `int`
  - Default: `1`
  - Multiplier factor to downsample costmap by (e.g. if 5cm costmap at 2downsample_factor, 10cm output).

- **`<name>.goal_heading_mode`**
  - Type: `string`
  - Default: `“DEFAULT”`
  - Goal heading mode enum string to plan goal with multiple orientation. Options are “DEFAULT”, “BIDIRECTIONAL” and “ALL_DIRECTION”. With default mode, the planner will plan the goal with the orientat...

- **`<name>.lookup_table_size`**
  - Type: `double`
  - Default: `20.0`
  - Size of the dubin/reeds-sheep distance window to cache, in meters.

- **`<name>.max_iterations`**
  - Type: `int`
  - Default: `1000000`
  - Maximum number of search iterations before failing to limit compute time, disabled by -1.

- **`<name>.max_on_approach_iterations`**
  - Type: `int`
  - Default: `1000`
  - Maximum number of iterations once a visited node is within the goal tolerances to continue to try to find an exact match before returning the best path solution within tolerances. Negative values c...

- **`<name>.max_planning_time`**
  - Type: `double`
  - Default: `5.0`
  - Maximum planning time in seconds.

- **`<name>.minimum_turning_radius`**
  - Type: `double`
  - Default: `0.4`
  - Minimum turning radius in meters of vehicle. Also used in the smoother to compute maximum curvature. Must be greater than 0.

- **`<name>.motion_model_for_search`**
  - Type: `string`
  - Default: `“DUBIN”`
  - Motion model enum string to search with. For Hybrid-A* node, default is “DUBIN”. Options for SE2 are DUBIN or REEDS_SHEPP.

- **`<name>.non_straight_penalty`**
  - Type: `double`
  - Default: `1.20`
  - Heuristic penalty to apply to SE2 node if searching in non-straight direction.

- **`<name>.retrospective_penalty`**
  - Type: `double`
  - Default: `0.015`
  - Heuristic penalty to apply to SE2 node penalty. Causes Hybrid-A* to prefer later maneuvers before earlier ones along the path. Saves search time since earlier (shorter) branches are not expanded un...

- **`<name>.reverse_penalty`**
  - Type: `double`
  - Default: `2.0`
  - Heuristic penalty to apply to SE2 node if searching in reverse direction. Only used inREEDS_SHEPPmotion model.

- **`<name>.smooth_path`**
  - Type: `bool`
  - Default: `true`
  - If true, does simple and fast smoothing post-processing to the path from search

- **`<name>.smoother.do_refinement`**
  - Type: `bool`
  - Default: `true`
  - Performs extra refinement smoothing runs. Essentially, this recursively calls the smoother using the output from the last smoothing cycle to further smooth the path for macro-trends. This typically...

- **`<name>.smoother.max_iterations`**
  - Type: `int`
  - Default: `1000`
  - The maximum number of iterations the smoother has to smooth the path, to bound potential computation.

- **`<name>.smoother.refinement_num`**
  - Type: `int`
  - Default: `2`
  - Number of times to recursively attempt to smooth, must be>=1.

- **`<name>.smoother.tolerance`**
  - Type: `double`
  - Default: `1e-10`
  - Parameter tolerance change amount to terminate smoothing session

- **`<name>.smoother.w_data`**
  - Type: `double`
  - Default: `0.2`
  - Weight for smoother to apply to retain original data information

- **`<name>.smoother.w_smooth`**
  - Type: `double`
  - Default: `0.3`
  - Weight for smoother to apply to smooth out the data points

- **`<name>.terminal_checking_interval`**
  - Type: `int`
  - Default: `5000`
  - Number of iterations between checking if the goal has been cancelled or planner timed out

- **`<name>.tolerance`**
  - Type: `double`
  - Default: `0.25`
  - If an exact path cannot be found, the tolerance (as measured by the heuristic cost-to-goal) that would be acceptable to diverge from the requested pose.

- **`<name>.use_quadratic_cost_penalty`**
  - Type: `bool`
  - Default: `false`
  - Advanced feature: This allows a user to specify a quadratic traversal and heuristic cost computation (e.g.cost*cost) rather than linear. This will speed up the planner since the optimal channel for...

- **`allow_parameter_qos_overrides`**
  - Type: `bool`
  - Default: `true`
  - Whether to allow QoS profiles to be overwritten with parameterized values.

---

## Smac Lattice

### Smac State Lattice Planner
*Source: https://docs.nav2.org/configuration/packages/smac/configuring-smac-lattice.html*

- **`<name>.allow_reverse_expansion`**
  - Type: `bool`
  - Default: `false`
  - If true, allows the robot to use the primitives to expand in the mirrored opposite direction of the current robot’s orientation (to reverse).

- **`<name>.allow_unknown`**
  - Type: `bool`
  - Default: `True`
  - Whether to allow traversing/search in unknown space.

- **`<name>.analytic_expansion_max_cost`**
  - Type: `double`
  - Default: `200.0`
  - For Hybrid/Lattice nodes: The maximum single cost for any part of an analytic expansion to contain and be considered valid (except when necessary on approach to goal). This allows for removing of p...

- **`<name>.analytic_expansion_max_cost_override`**
  - Type: `bool`
  - Default: `false`
  - For Hybrid/Lattice nodes: Whether or not to override the maximum cost setting if within critical distance to goal (ie probably required). If expansion is within 2*pi*min_r of the goal, then it will...

- **`<name>.analytic_expansion_max_length`**
  - Type: `double`
  - Default: `3.0`
  - If the length is too far, reject this expansion. This prevents shortcutting of search with its penalty functions far out from the goal itself (e.g. so we don’t reverse half-way across open maps or ...

- **`<name>.analytic_expansion_ratio`**
  - Type: `double`
  - Default: `3.5`
  - SE2 node will attempt to complete an analytic expansion with frequency proportional to this value and the minimum heuristic. Negative values convert to infinite.

- **`<name>.cache_obstacle_heuristic`**
  - Type: `bool`
  - Default: `false`
  - Cache the obstacle map dynamic programming distance expansion heuristic between subsequent replannings of the same goal location. Dramatically speeds up replanning performance (40x) if costmap is l...

- **`<name>.change_penalty`**
  - Type: `double`
  - Default: `0.05`
  - Heuristic penalty to apply to SE2 node if changing direction (e.g. left to right) in search.

- **`<name>.coarse_search_resolution`**
  - Type: `int`
  - Default: `1`
  - Number of goal heading bins to skip during the coarse search phase of analytic expansion goal-finding. When a goal is found, a fine search is performed to determine the exact path during full-resol...

- **`<name>.cost_penalty`**
  - Type: `double`
  - Default: `2.0`
  - Heuristic penalty to apply to SE2 node for cost at pose. Allows State Lattice to be cost aware.

- **`<name>.debug_visualizations`**
  - Type: `bool`
  - Default: `false`
  - Whether to publish expansions on the/expansionstopic as an array of poses and the path’s footprints on the/planned_footprintstopic. WARNING: heavy to compute and to display, for debug only as it de...

- **`<name>.downsample_obstacle_heuristic`**
  - Type: `bool`
  - Default: `true`
  - Advanced feature: This allows a user to disable downsampling of the obstacle heuristic’s costmap representation to search at the costmap’s full-resolution. This will come at increased up-front cost...

- **`<name>.goal_heading_mode`**
  - Type: `string`
  - Default: `“DEFAULT”`
  - Goal heading mode enum string to plan goal with multiple orientation. Options are “DEFAULT”, “BIDIRECTIONAL” and “ALL_DIRECTION”. With default mode, the planner will plan the goal with the orientat...

- **`<name>.lattice_filepath`**
  - Type: `string`
  - Default: `“”`
  - The filepath to the state lattice minimum control set graph, this will default to a 16 bin, 0.5m turning radius control set located intest/for basic testing and evaluation (opposed to Hybrid-A*’s d...

- **`<name>.lookup_table_size`**
  - Type: `double`
  - Default: `20.0`
  - Size of the dubin/reeds-sheep distance window to cache, in meters.

- **`<name>.max_iterations`**
  - Type: `int`
  - Default: `1000000`
  - Maximum number of search iterations before failing to limit compute time, disabled by -1.

- **`<name>.max_on_approach_iterations`**
  - Type: `int`
  - Default: `1000`
  - Maximum number of iterations once a visited node is within the goal tolerances to continue to try to find an exact match before returning the best path solution within tolerances.

- **`<name>.max_planning_time`**
  - Type: `double`
  - Default: `5.0`
  - Maximum planning time in seconds.

- **`<name>.non_straight_penalty`**
  - Type: `double`
  - Default: `1.05`
  - Heuristic penalty to apply to SE2 node if searching in non-straight direction.

- **`<name>.retrospective_penalty`**
  - Type: `double`
  - Default: `0.015`
  - Heuristic penalty to apply to SE2 node penalty. Causes State Lattice to prefer later maneuvers before earlier ones along the path. Saves search time since earlier (shorter) branches are not expande...

- **`<name>.reverse_penalty`**
  - Type: `double`
  - Default: `2.0`
  - Heuristic penalty to apply to SE2 node if searching in reverse direction. Only used inallow_reverse_expansion=true.

- **`<name>.rotation_penalty`**
  - Type: `double`
  - Default: `5.0`
  - Penalty to apply for rotations in place, if minimum control set contains in-place rotations. This should always be set sufficiently high to weight against in-place rotations unless strictly necessa...

- **`<name>.smooth_path`**
  - Type: `bool`
  - Default: `true`
  - If true, does simple and fast smoothing post-processing to the path from search

- **`<name>.smoother.do_refinement`**
  - Type: `bool`
  - Default: `true`
  - Performs extra refinement smoothing runs. Essentially, this recursively calls the smoother using the output from the last smoothing cycle to further smooth the path for macro-trends. This typically...

- **`<name>.smoother.max_iterations`**
  - Type: `int`
  - Default: `1000`
  - The maximum number of iterations the smoother has to smooth the path, to bound potential computation.

- **`<name>.smoother.refinement_num`**
  - Type: `int`
  - Default: `2`
  - Number of times to recursively attempt to smooth, must be>=1.

- **`<name>.smoother.tolerance`**
  - Type: `double`
  - Default: `1e-10`
  - Parameter tolerance change amount to terminate smoothing session

- **`<name>.smoother.w_data`**
  - Type: `double`
  - Default: `0.2`
  - Weight for smoother to apply to retain original data information

- **`<name>.smoother.w_smooth`**
  - Type: `double`
  - Default: `0.3`
  - Weight for smoother to apply to smooth out the data points

- **`<name>.terminal_checking_interval`**
  - Type: `int`
  - Default: `5000`
  - Number of iterations between checking if the goal has been cancelled or planner timed out

- **`<name>.tolerance`**
  - Type: `double`
  - Default: `0.25`
  - If an exact path cannot be found, the tolerance (as measured by the heuristic cost-to-goal) that would be acceptable to diverge from the requested pose in distance-to-goal.

- **`<name>.use_quadratic_cost_penalty`**
  - Type: `bool`
  - Default: `false`
  - Advanced feature: This allows a user to specify a quadratic traversal and heuristic cost computation (e.g.cost*cost) rather than linear. This will speed up the planner since the optimal channel for...

- **`allow_parameter_qos_overrides`**
  - Type: `bool`
  - Default: `true`
  - Whether to allow QoS profiles to be overwritten with parameterized values.

---

## Smac Planner

### Smac Planner
*Source: https://docs.nav2.org/configuration/packages/configuring-smac-planner.html*

- **`Hybrid`**
  - A* computed the path in 144ms

---

## Smooth

### SmoothPath
*Source: https://docs.nav2.org/configuration/packages/bt-plugins/actions/Smooth.html*

- **`check_for_collisions`**
  - Type: `bool`
  - Default: `false`
  - Whether to check the output smoothed path for collisions.

- **`error_code_id`**
  - Type: `uint16`
  - Default: `N/A`
  - Follow smoother error code. SeeSmoothPathaction for the enumerated set of error code definitions.

- **`error_msg`**
  - Type: `string`
  - Default: `N/A`
  - Follow smoother error message. SeeSmoothPathaction for the enumerated set of error code definitions.

- **`max_smoothing_duration`**
  - Type: `double`
  - Default: `3.0`
  - Maximum time to smooth for (seconds)

- **`smoothed_path`**
  - Type: `string`
  - Default: `N/A`
  - The output blackboard variable to assign the smoothed path to

- **`smoother_id`**
  - Type: `string`
  - Default: `N/A`
  - The smoother plugin ID to use for smoothing in the smoother server

- **`smoothing_duration`**
  - Type: `double`
  - Default: `N/A`
  - The actual duration used for smoothing

- **`unsmoothed_path`**
  - Type: `string`
  - Default: `N/A`
  - The blackboard variable or hard-coded input path to smooth

- **`was_completed`**
  - Type: `bool`
  - Default: `N/A`
  - Indicates if the smoothing process was completed. Will returnfalseifcheck_for_collisionsis set totrueand a collision is detected.

---

## Smoother Server

### Smoother Server
*Source: https://docs.nav2.org/configuration/packages/configuring-smoother-server.html*

- **`allow_parameter_qos_overrides`**
  - Type: `bool`
  - Default: `true`
  - Whether to allow QoS profiles to be overwritten with parameterized values.

- **`bond_heartbeat_period`**
  - Type: `double`
  - Default: `0.25`
  - The lifecycle node bond mechanism publishing period (on the /bond topic). Disabled if inferior or equal to 0.0.

- **`costmap_topic`**
  - Type: `string`
  - Default: `“global_costmap/costmap_raw”`
  - Raw costmap topic for collision checking.

- **`footprint_topic`**
  - Type: `string`
  - Default: `“global_costmap/published_footprint”`
  - Topic for footprint in the costmap frame.

- **`introspection_mode`**
  - Type: `string`
  - Default: `“disabled”`
  - The introspection mode for services and actions. Options are “disabled”, “metadata”, “contents”.

- **`robot_base_frame`**
  - Type: `string`
  - Default: `“base_link”`
  - Robot base frame.

- **`smoother_plugins`**
  - Type: `vector<string>`
  - Default: `{“nav2_smoother::SimpleSmoother”}`
  - List of plugin names to use, also matches action server names.

- **`transform_tolerance`**
  - Type: `double`
  - Default: `0.1`
  - TF transform tolerance.

---

## Smootherselector

### SmootherSelector
*Source: https://docs.nav2.org/configuration/packages/bt-plugins/actions/SmootherSelector.html*

- **`default_smoother`**
  - Type: `string`
  - Default: `N/A`
  - The default value for the selected Smoother if no message is received from the input topic.

- **`selected_smoother`**
  - Type: `string`
  - Default: `N/A`
  - The output selected Smoother id.

- **`topic_name`**
  - Type: `string`
  - Default: `smoother_selector`
  - The name of the topic used to received select command messages. This is used to support multiple SmootherSelector nodes.

---

## Speed_Filter

### Speed Filter Parameters
*Source: https://docs.nav2.org/configuration/packages/costmap-plugins/speed_filter.html*

- **`<filtername>.enabled`**
  - Type: `bool`
  - Default: `True`
  - Whether it is enabled.

- **`<filtername>.filter_info_topic`**
  - Type: `string`
  - Default: `N/A`
  - Name of the incomingCostmapFilterInfotopic having filter-related information. Published by Costmap Filter Info Server along with filter mask topic. For more details about Map and Costmap Filter Inf...

- **`<filtername>.speed_limit_topic`**
  - Type: `string`
  - Default: `“speed_limit”`
  - speed_limitexpressed in a percent should belong to(0.0..100.0]range.

- **`<filtername>.transform_tolerance`**
  - Type: `double`
  - Default: `0.1`
  - Time with which to post-date the transform that is published, to indicate that this transform is valid into the future. Used when filter mask and current costmap layer are in different frames.

- **`percentage`**
  - speed limit is expressed in percentage iftrueor in absolute values infalsecase. This parameter is set depending ontypefield ofCostmapFilterInfomessage.

- **`speed_limit`**
  - non-zero values show maximum allowed speed expressed in a percent of maximum robot speed or in absolute value depending onpercentagevalue. Zero value means no speed restriction (independently onper...

---

## Speedcontroller

### SpeedController
*Source: https://docs.nav2.org/configuration/packages/bt-plugins/decorators/SpeedController.html*

- **`goal`**
  - Type: `geometry_msgs::msg::PoseStamped`
  - Default: `“{goal}”`
  - Destination to check. Takes in a blackboard variable, “{goal}” if not specified.

- **`goals`**
  - Type: `nav_msgs::msg::Goals`
  - Default: `“{goals}”`
  - Vector of goals to check. Takes in a blackboard variable, “{goals}” if not specified.

- **`max_rate`**
  - Type: `double`
  - Default: `1.0`
  - The maximum rate at which child node can be ticked (hz).

- **`max_speed`**
  - Type: `double`
  - Default: `0.5`
  - The maximum robot speed above which the child node is ticked at maximum rate (m/s).

- **`min_rate`**
  - Type: `double`
  - Default: `0.1`
  - The minimum rate at which child node can be ticked (hz).

- **`min_speed`**
  - Type: `double`
  - Default: `0.0`
  - The minimum robot speed below which the child node is ticked at minimum rate (m/s).

---

## Spin

### Spin
*Source: https://docs.nav2.org/configuration/packages/bt-plugins/actions/Spin.html*

- **`disable_collision_checks`**
  - Type: `bool`
  - Default: `false`
  - Disable collision checking.

- **`error_code_id`**
  - Type: `uint16`
  - Default: `N/A`
  - Spin error code. SeeSpinaction message for the enumerated set of error codes.

- **`error_msg`**
  - Type: `string`
  - Default: `N/A`
  - Spin error message. SeeSpinaction message for the enumerated set of error codes.

- **`is_recovery`**
  - Type: `bool`
  - Default: `True`
  - True if the action is being used as a recovery.

- **`server_name`**
  - Type: `string`
  - Default: `N/A`
  - Action server name.

- **`server_timeout`**
  - Type: `double`
  - Default: `10`
  - Action server timeout (ms).

- **`spin_dist`**
  - Type: `double`
  - Default: `1.57`
  - Spin distance (radians).

- **`time_allowance`**
  - Type: `double`
  - Default: `10.0`
  - Time to invoke behavior for, if exceeds considers it a stuck condition or failure case (seconds).

---

## Standard_Traj_Generator

### StandardTrajectoryGenerator
*Source: https://docs.nav2.org/configuration/packages/dwb-plugins/standard_traj_generator.html*

- **`<dwbplugin>.angular_granularity`**
  - Type: `double`
  - Default: `0.025`
  - Angular distance to project.

- **`<dwbplugin>.discretize_by_time`**
  - Type: `bool`
  - Default: `false`
  - If true, forward simulate by time. If False, forward simulate by linear and angular granularity.

- **`<dwbplugin>.include_last_point`**
  - Type: `bool`
  - Default: `true`
  - Whether to include the last pose in the trajectory.

- **`<dwbplugin>.limit_vel_cmd_in_traj`**
  - Type: `bool`
  - Default: `false`
  - Whether to limit velocity command in trajectory using sampled velocity instead of the commanded velocity.

- **`<dwbplugin>.linear_granularity`**
  - Type: `double`
  - Default: `0.5`
  - Linear distance forward to project.

- **`<dwbplugin>.sim_time`**
  - Type: `double`
  - Default: `1.7`
  - Time to simulate ahead by (s).

- **`<dwbplugin>.time_granularity`**
  - Type: `double`
  - Default: `0.5`
  - Time ahead to project.

---

## Static

### Static Layer Parameters
*Source: https://docs.nav2.org/configuration/packages/costmap-plugins/static.html*

- **`<staticlayer>.enabled`**
  - Type: `bool`
  - Default: `True`
  - Whether it is enabled.

- **`<staticlayer>.footprint_clearing_enabled`**
  - Type: `bool`
  - Default: `False`
  - Clear any occupied cells under robot footprint.

- **`<staticlayer>.map_subscribe_transient_local`**
  - Type: `bool`
  - Default: `True`
  - QoS settings for map topic.

- **`<staticlayer>.map_topic`**
  - Type: `string`
  - Default: `“map”`
  - Map topic to subscribe to.

- **`<staticlayer>.restore_cleared_footprint`**
  - Type: `bool`
  - Default: `True`
  - Restore map after clearing the area the footprint occupied.

- **`<staticlayer>.subscribe_to_updates`**
  - Type: `bool`
  - Default: `False`
  - Subscribe to static map updates after receiving first.

- **`<staticlayer>.transform_tolerance`**
  - Type: `double`
  - Default: `0.0`
  - TF tolerance.

---

## Stopped_Goal_Checker

### StoppedGoalChecker
*Source: https://docs.nav2.org/configuration/packages/nav2_controller-plugins/stopped_goal_checker.html*

- **`<nav2_controllerplugin>.path_length_tolerance`**
  - Type: `double`
  - Default: `1.0`
  - Tolerance to meet goal completion criteria (m).

- **`<nav2_controllerplugin>.rot_stopped_velocity`**
  - Type: `double`
  - Default: `0.25`
  - Velocity below is considered to be stopped at tolerance met (rad/s).

- **`<nav2_controllerplugin>.stateful`**
  - Type: `bool`
  - Default: `true`
  - Whether to check for XY position tolerance after rotating to goal orientation in case of minor localization changes.

- **`<nav2_controllerplugin>.symmetric_yaw_tolerance`**
  - Type: `bool`
  - Default: `false`
  - Enable symmetric goal orientation acceptance. When enabled, the robot accepts the goal as reached when oriented at either the goal orientation or the goal orientation + 180°. This is useful for sym...

- **`<nav2_controllerplugin>.trans_stopped_velocity`**
  - Type: `double`
  - Default: `0.25`
  - Velocity below is considered to be stopped at tolerance met (m/s).

- **`<nav2_controllerplugin>.xy_goal_tolerance`**
  - Type: `double`
  - Default: `0.25`
  - Tolerance to meet goal completion criteria (m).

- **`<nav2_controllerplugin>.yaw_goal_tolerance`**
  - Type: `double`
  - Default: `0.25`
  - Tolerance to meet goal completion criteria (rad).

---

## Thetastar

### Theta Star Planner
*Source: https://docs.nav2.org/configuration/packages/configuring-thetastar.html*

- **`<name>.allow_unknown`**
  - Type: `bool`
  - Default: `True`
  - Whether to allow planning in unknown space.

- **`<name>.how_many_corners`**
  - Type: `int`
  - Default: `8`
  - To choose between 4-connected (up, down, left, right) and 8-connected (all the adjacent cells) graph expansions, the accepted values are 4 and 8

- **`<name>.terminal_checking_interval`**
  - Type: `int`
  - Default: `5000`
  - Number of iterations between checking if the goal has been cancelled or planner timed out

- **`<name>.use_final_approach_orientation`**
  - Type: `bool`
  - Default: `false`
  - If true, the last pose of the path generated by the planner will have its orientation set to the approach orientation, i.e. the orientation of the vector connecting the last two points of the path

- **`<name>.w_euc_cost`**
  - Type: `double`
  - Default: `1.0`
  - Weight applied on the length of the path.

- **`<name>.w_traversal_cost`**
  - Type: `double`
  - Default: `2.0`
  - It tunes how harshly the nodes of high cost are penalised. From the above g(neigh) equation you can see that the cost-aware component of the cost function forms a parabolic curve, thus this paramet...

- **`allow_parameter_qos_overrides`**
  - Type: `bool`
  - Default: `true`
  - Whether to allow QoS profiles to be overwritten with parameterized values.

---

## Timeexpired

### TimeExpired
*Source: https://docs.nav2.org/configuration/packages/bt-plugins/conditions/TimeExpired.html*

- **`seconds`**
  - Type: `double`
  - Default: `1.0`
  - The time passed to return success (s).

---

## Togglecollisionmonitor

### ToggleCollisionMonitor
*Source: https://docs.nav2.org/configuration/packages/bt-plugins/actions/ToggleCollisionMonitor.html*

- **`enable`**
  - Type: `bool`
  - Default: `true`
  - Whether to enable or disable the collision monitor.

- **`server_timeout`**
  - Type: `double`
  - Default: `10`
  - Server timeout (ms).

- **`service_name`**
  - Type: `string`
  - Default: `N/A`
  - Service name.

---

## Transformavailable

### TransformAvailable
*Source: https://docs.nav2.org/configuration/packages/bt-plugins/conditions/TransformAvailable.html*

- **`child`**
  - Type: `string`
  - Default: `“”`
  - Child frame for transform.

- **`parent`**
  - Type: `string`
  - Default: `“”`
  - Parent frame for transform.

---

## Truncatepath

### TruncatePath
*Source: https://docs.nav2.org/configuration/packages/bt-plugins/actions/TruncatePath.html*

- **`distance`**
  - Type: `double`
  - Default: `1.0`
  - The distance to the original goal for truncating the path.

- **`input_path`**
  - Type: `nav_msgs/Path`
  - Default: `N/A`
  - The original path to be truncated.

- **`output_path`**
  - Type: `nav_msgs/Path`
  - Default: `N/A`
  - The resulting truncated path.

---

## Truncatepathlocal

### TruncatePathLocal
*Source: https://docs.nav2.org/configuration/packages/bt-plugins/actions/TruncatePathLocal.html*

- **`angular_distance_weight`**
  - Type: `double`
  - Default: `0.0`
  - Weight of angular distance relative to positional distance when finding which path pose is closest to robot. Not applicable on paths without orientations assigned.

- **`distance_backward`**
  - Type: `double`
  - Default: `4.0`
  - The trimming distance in backward direction.

- **`distance_forward`**
  - Type: `double`
  - Default: `8.0`
  - The trimming distance in forward direction.

- **`input_path`**
  - Type: `nav_msgs/Path`
  - Default: `N/A`
  - The original path to be truncated.

- **`max_robot_pose_search_dist`**
  - Type: `double`
  - Default: `infinity`
  - Maximum forward integrated distance along the path (starting from the last detected pose) to bound the search for the closest pose to the robot. When set to infinity (default), whole path is search...

- **`output_path`**
  - Type: `nav_msgs/Path`
  - Default: `N/A`
  - The resulting truncated path.

- **`pose`**
  - Type: `geometry_msgs/PoseStamped`
  - Default: `N/A`
  - Manually specified pose to be used alternatively to current robot pose.

- **`robot_frame`**
  - Type: `string`
  - Default: `“base_link”`
  - Robot base frame id.

- **`transform_tolerance`**
  - Type: `double`
  - Default: `0.2`
  - Robot pose lookup tolerance.

---

## Twirling

### TwirlingCritic
*Source: https://docs.nav2.org/configuration/packages/trajectory_critics/twirling.html*

- **`<dwbplugin>.<name>.scale`**
  - Type: `double`
  - Default: `1.0`
  - Weighed scale for critic.

---

## Undockrobot

### UndockRobot
*Source: https://docs.nav2.org/configuration/packages/bt-plugins/actions/UndockRobot.html*

- **`dock_type`**
  - Type: `string`
  - Default: `N/A`
  - The dock plugin type, if not previous instance used for docking.

- **`error_code_id`**
  - Type: `uint16`
  - Default: `0`
  - Dock robot error code. SeeUndockRobotaction message for the enumerated set of error codes.

- **`error_msg`**
  - Type: `string`
  - Default: `0`
  - Dock robot error message. SeeUndockRobotaction message for the enumerated set of error codes.

- **`max_undocking_time`**
  - Type: `float`
  - Default: `30.0`
  - Maximum time to get back to the staging pose.

- **`success`**
  - Type: `bool`
  - Default: `true`
  - If the action was successful.

---

## Vector Object Server

### Vector Object Server
*Source: https://docs.nav2.org/configuration/packages/map_server/configuring-vector-object-server.html*

- **`<shape_name>.center`**
  - Type: `vector<double>`
  - Default: `N/A`
  - Center of the circle, listed in{center.x,center.y}format (e.g.{0.2,0.3}). Should contain exactly 2 items: X and Y coordinate of the circle’s center in a given frame. Otherwise, causes an error.

- **`<shape_name>.closed`**
  - Type: `bool`
  - Default: `true`
  - Whether the polygon is closed (and filled), or drawn as polygonal chain otherwise.

- **`<shape_name>.fill`**
  - Type: `bool`
  - Default: `true`
  - Whether the circle to be filled with a given value, or drawn only circle’s border otherwise.

- **`<shape_name>.frame_id`**
  - Type: `string`
  - Default: `“”`
  - Frame ID of the given shape. Empty value is being treated as map’s global frame.

- **`<shape_name>.points`**
  - Type: `vector<double>`
  - Default: `N/A`
  - Polygon vertices, listed in[p1.x,p1.y,p2.x,p2.y,p3.x,p3.y,...]format (e.g.[0.5,0.5,0.5,-0.5,-0.5,-0.5,-0.5,0.5]for the square). Minimum 3 points for a triangle polygon. Causes an error, if not spec...

- **`<shape_name>.radius`**
  - Type: `double`
  - Default: `N/A`
  - Circle radius. Causes an error, if less than zero or not specialized.

- **`<shape_name>.type`**
  - Type: `string`
  - Default: `N/A`
  - Type of vector object shape. Available values arepolygonandcircle. Causes an error, if not specialized.

- **`<shape_name>.uuid`**
  - Type: `string`
  - Default: `N/A`
  - UUID of the shape specified in12345678-9abc-def0-1234-56789abcdef0format. Parameter is optional and could be skipped: if not specialized, Vector Object server will automatically generate a new one ...

- **`<shape_name>.value`**
  - Type: `int`
  - Default: `100 (occupied)`
  - Shape’s value to be put on map with.

- **`AddShapes.srv`**
  - adds new shapes or modifies existing ones

- **`default_value`**
  - Type: `int`
  - Default: `-1 (unknown)`
  - Default OccupancyGrid value to fill the background of output map with.

- **`GetShapes.srv`**
  - gets all shapes and their properties

- **`global_frame_id`**
  - Type: `string`
  - Default: `“map”`
  - The name of the coordinate frame where the map is being published at.

- **`map_topic`**
  - Type: `string`
  - Default: `“vo_map”`
  - Output topic, publishing an OccupancyGrid map with vector objects put on it.

- **`No`**
  - access zone

- **`overlay_type`**
  - Type: `int`
  - Default: `0`
  - How one vector object to be overlaid with other and the map. The following values are supported:0 (OVERLAY_SEQ): Vector objects are superimposed in the order in which they have arrived.1 (OVERLAY_M...

- **`RemoveShapes.srv`**
  - removes any or all shapes from the map

- **`resolution`**
  - Type: `double`
  - Default: `0.05`
  - Output map resolution in meters.

- **`shapes`**
  - Type: `vector<string>`
  - Default: `{}`
  - List of vector objects (polygons and circles). Empty by-default.

- **`Speed`**
  - restriction areas

- **`transform_tolerance`**
  - Type: `double`
  - Default: `0.1`
  - Transform tolerance for the case when any of the shapes are placed in different than map’s frame.

- **`update_frequency`**
  - Type: `double`
  - Default: `1.0`
  - Output map update frequency (when dynamic update model is switched-on).

---

## Velocity Smoother

### Velocity Smoother
*Source: https://docs.nav2.org/configuration/packages/configuring-velocity-smoother.html*

- **`allow_parameter_qos_overrides`**
  - Type: `bool`
  - Default: `true`
  - Whether to allow QoS profiles to be overwritten with parameterized values.

- **`bond_heartbeat_period`**
  - Type: `double`
  - Default: `0.25`
  - The lifecycle node bond mechanism publishing period (on the /bond topic). Disabled if inferior or equal to 0.0.

- **`deadband_velocity`**
  - Type: `vector<double>`
  - Default: `[0.0, 0.0, 0.0]`
  - Minimum velocities (m/s) in[x,y,theta]axes or[x,y,z,roll,pitch,yaw]for full 6-DoF support to send to the robot hardware controllers, to prevent small commands from damaging hardware controllers if ...

- **`enable_stamped_cmd_vel`**
  - Type: `bool`
  - Default: `true`
  - Whether to use geometry_msgs::msg::Twist or geometry_msgs::msg::TwistStamped velocity data. True uses TwistStamped, false uses Twist. Note: This parameter is defaultfalsein Jazzy or older! Kilted o...

- **`feedback`**
  - Type: `string`
  - Default: `“OPEN_LOOP”`
  - Type of feedback to use for the current state of the robot’s velocity. InOPEN_LOOP, it will use the last commanded velocity as the next iteration’s current velocity. When acceleration limits are se...

- **`max_accel`**
  - Type: `vector<double>`
  - Default: `[2.5, 0.0, 3.2]`
  - Maximum acceleration to apply to each axis[x,y,theta]or[x,y,z,roll,pitch,yaw]for full 6-DoF support.

- **`max_decel`**
  - Type: `vector<double>`
  - Default: `[-2.5, 0.0, -3.2]`
  - Minimum acceleration to apply to each axis[x,y,theta]or[x,y,z,roll,pitch,yaw]for full 6-DoF support. This issignedand thus these should generally all benegative.

- **`max_velocity`**
  - Type: `vector<double>`
  - Default: `[0.5, 0.0, 2.5]`
  - Maximum velocities (m/s) in[x,y,theta]axes or[x,y,z,roll,pitch,yaw]for full 6-DoF support.

- **`min_velocity`**
  - Type: `vector<double>`
  - Default: `[-0.5, 0.0, -2.5]`
  - Minimum velocities (m/s) in[x,y,theta]axes or[x,y,z,roll,pitch,yaw]for full 6-DoF support. This issignedand thus must benegativeto reverse. Note: rotational velocities negative direction is a right...

- **`odom_duration`**
  - Type: `double`
  - Default: `0.1`
  - Time (s) to buffer odometry commands to estimate the robot speed, if inCLOSED_LOOPoperational mode.

- **`odom_topic`**
  - Type: `string`
  - Default: `“odom”`
  - Topic to find robot odometry, if inCLOSED_LOOPoperational mode.

- **`scale_velocities`**
  - Type: `bool`
  - Default: `false`
  - Whether or not to adjust other components of velocity proportionally to a component’s required changes due to acceleration limits. This will try to adjust all components to follow the same directio...

- **`smoothing_frequency`**
  - Type: `double`
  - Default: `20.0`
  - Frequency (Hz) to use the last received velocity command to smooth by velocity, acceleration, and deadband constraints. If set approximately to the rate of your local trajectory planner, it should ...

- **`stamp_smoothed_velocity_with_smoothing_time`**
  - Type: `bool`
  - Default: `false`
  - Whether to interpolate the timestamps of the smoothedgeometery_msgs:msg::TwistStampedcmd_vel message after the last command velocity received. Only available in Jazzy as a backport of the now-defau...

- **`use_realtime_priority`**
  - Type: `bool`
  - Default: `false`
  - Adds soft real-time prioritization to the controller server to better ensure resources to time sensitive portions of the codebase. This will set the controller’s execution thread to a higher priori...

- **`velocity_timeout`**
  - Type: `double`
  - Default: `1.0`
  - Timeout (s) after which the velocity smoother will send a zero-ed outTwistcommand and stop publishing.

---

## Visualization

### Publisher
*Source: https://docs.nav2.org/configuration/packages/dwb-params/visualization.html*

- **`<dwbplugin>.marker_lifetime`**
  - Type: `double`
  - Default: `0.1`
  - How long for the marker to remain.

- **`<dwbplugin>.publish_cost_grid_pc`**
  - Type: `bool`
  - Default: `false`
  - Whether to publish the cost grid.

- **`<dwbplugin>.publish_evaluation`**
  - Type: `bool`
  - Default: `true`
  - Whether to publish the local plan evaluation.

- **`<dwbplugin>.publish_local_plan`**
  - Type: `bool`
  - Default: `true`
  - Whether to publish the local planner’s plan.

- **`<dwbplugin>.publish_trajectories`**
  - Type: `bool`
  - Default: `true`
  - Whether to publish debug trajectories.

---

## Voxel

### Voxel Layer Parameters
*Source: https://docs.nav2.org/configuration/packages/costmap-plugins/voxel.html*

- **`<voxellayer>.<datasource>.clearing`**
  - Type: `bool`
  - Default: `False`
  - Whether source should raytrace clear in costmap.

- **`<voxellayer>.<datasource>.data_type`**
  - Type: `string`
  - Default: `“LaserScan”`
  - Data type of input, LaserScan or PointCloud2.

- **`<voxellayer>.<datasource>.expected_update_rate`**
  - Type: `double`
  - Default: `0.0`
  - Expected rate to get new data from sensor.

- **`<voxellayer>.<datasource>.inf_is_valid`**
  - Type: `bool`
  - Default: `False`
  - Are infinite returns from laser scanners valid measurements to raycast.

- **`<voxellayer>.<datasource>.marking`**
  - Type: `bool`
  - Default: `True`
  - Whether source should mark in costmap.

- **`<voxellayer>.<datasource>.max_obstacle_height`**
  - Type: `double`
  - Default: `0.0`
  - Maximum height to add return to occupancy grid.

- **`<voxellayer>.<datasource>.min_obstacle_height`**
  - Type: `double`
  - Default: `0.0`
  - Minimum height to add return to occupancy grid.

- **`<voxellayer>.<datasource>.observation_persistence`**
  - Type: `double`
  - Default: `0.0`
  - How long to store messages in a buffer to add to costmap before removing them (s).

- **`<voxellayer>.<datasource>.obstacle_max_range`**
  - Type: `double`
  - Default: `2.5`
  - Maximum range to mark obstacles in costmap.

- **`<voxellayer>.<datasource>.obstacle_min_range`**
  - Type: `double`
  - Default: `0.0`
  - Minimum range to mark obstacles in costmap.

- **`<voxellayer>.<datasource>.raytrace_max_range`**
  - Type: `double`
  - Default: `3.0`
  - Maximum range to raytrace clear obstacles from costmap.

- **`<voxellayer>.<datasource>.raytrace_min_range`**
  - Type: `double`
  - Default: `0.0`
  - Minimum range to raytrace clear obstacles from costmap.

- **`<voxellayer>.<datasource>.sensor_frame`**
  - Type: `string`
  - Default: `“”`
  - Frame of sensor, to use if not provided by message. If empty, uses message frame_id.

- **`<voxellayer>.<datasource>.topic`**
  - Type: `string`
  - Default: `“”`
  - Topic of data.

- **`<voxellayer>.<datasource>.transport_type`**
  - Type: `string`
  - Default: `“raw”`
  - ForPointCloud2data, specify the transport plugin to use:

- **`<voxellayer>.combination_method`**
  - Type: `int`
  - Default: `1`
  - Enum for method to add data to master costmap. Must be 0, 1 or 2, default to 1 (see below).

- **`<voxellayer>.enabled`**
  - Type: `bool`
  - Default: `True`
  - Whether it is enabled.

- **`<voxellayer>.footprint_clearing_enabled`**
  - Type: `bool`
  - Default: `True`
  - Clear any occupied cells under robot footprint.

- **`<voxellayer>.mark_threshold`**
  - Type: `int`
  - Default: `0`
  - Minimum number of voxels in a column to mark as occupied in 2D occupancy grid.

- **`<voxellayer>.max_obstacle_height`**
  - Type: `double`
  - Default: `2.0`
  - Maximum height to add return to occupancy grid.

- **`<voxellayer>.min_obstacle_height`**
  - Type: `double`
  - Default: `0.0`
  - Minimum height to add return to occupancy grid.

- **`<voxellayer>.observation_sources`**
  - Type: `vector<string>`
  - Default: `{“”}`
  - namespace of sources of data.

- **`<voxellayer>.origin_z`**
  - Type: `double`
  - Default: `0.0`
  - Where to start marking voxels (m).

- **`<voxellayer>.publish_voxel_map`**
  - Type: `bool`
  - Default: `False`
  - Whether to publish 3D voxel grid for debug, computationally expensive.

- **`<voxellayer>.tf_filter_tolerance`**
  - Type: `double`
  - Default: `0.05`
  - Tolerance for thetf2_ros::MessageFilter.

- **`<voxellayer>.unknown_threshold`**
  - Type: `int`
  - Default: `15`
  - Minimum number of empty voxels in a column to mark as unknown in 2D occupancy grid.

- **`<voxellayer>.z_resolution`**
  - Type: `double`
  - Default: `0.2`
  - Resolution of voxels in height (m).

- **`<voxellayer>.z_voxels`**
  - Type: `int`
  - Default: `10`
  - Number of voxels high to mark, maximum 16.

- **`draco`**
  - Lossy compression via Google.

- **`raw`**
  - No compression. Default; highest bandwidth usage.

- **`zlib`**
  - Lossless compression via Zlib compression.

- **`zstd`**
  - Lossless compression via Zstd compression.

---

## Wait

### Wait
*Source: https://docs.nav2.org/configuration/packages/bt-plugins/actions/Wait.html*

- **`error_code_id`**
  - Type: `uint16`
  - Default: `N/A`
  - Wait error code. SeeWaitaction message for the enumerated set of error codes.

- **`error_msg`**
  - Type: `string`
  - Default: `N/A`
  - Wait error message. SeeWaitaction message for the enumerated set of error codes.

- **`server_name`**
  - Type: `string`
  - Default: `N/A`
  - Action server name.

- **`server_timeout`**
  - Type: `double`
  - Default: `10`
  - Action server timeout (ms).

- **`wait_duration`**
  - Type: `double`
  - Default: `1.0`
  - Wait time (s).

---

## Wait_At_Waypoint

### WaitAtWaypoint
*Source: https://docs.nav2.org/configuration/packages/nav2_waypoint_follower-plugins/wait_at_waypoint.html*

- **`<nav2_waypoint_followerplugin>.enabled`**
  - Type: `bool`
  - Default: `true`
  - Whether waypoint_task_executor plugin is enabled.

- **`<nav2_waypoint_followerplugin>.waypoint_pause_duration`**
  - Type: `int`
  - Default: `0`
  - Amount of time in milliseconds, for robot to sleep/wait after each waypoint is reached. If zero, robot will directly continue to next waypoint.

---

## Waypoint Follower

### Waypoint Follower
*Source: https://docs.nav2.org/configuration/packages/configuring-waypoint-follower.html*

- **`allow_parameter_qos_overrides`**
  - Type: `bool`
  - Default: `true`
  - Whether to allow QoS profiles to be overwritten with parameterized values.

- **`bond_heartbeat_period`**
  - Type: `double`
  - Default: `0.25`
  - The lifecycle node bond mechanism publishing period (on the /bond topic). Disabled if inferior or equal to 0.0.

- **`global_frame_id`**
  - Type: `string`
  - Default: `‘map’`
  - The name of the global coordinate frame published by robot_localization. Only used by the gps_waypoint_follower to convert GPS waypoints to this frame.

- **`introspection_mode`**
  - Type: `string`
  - Default: `“disabled”`
  - The introspection mode for services and actions. Options are “disabled”, “metadata”, “contents”.

- **`loop_rate`**
  - Type: `int`
  - Default: `20`
  - Rate to check for results from current navigation task.

- **`stop_on_failure`**
  - Type: `bool`
  - Default: `true`
  - Whether to fail action task if a single waypoint fails. If false, will continue to next waypoint.

- **`waypoint_task_executor_plugin`**
  - Type: `string`
  - Default: `‘wait_at_waypoint’`
  - A plugin to define tasks to be executed when robot arrives to a waypoint.

- **`“wait_at_waypoint”`**

---

## Wouldacontrollerrecoveryhelp

### WouldAControllerRecoveryHelp
*Source: https://docs.nav2.org/configuration/packages/bt-plugins/conditions/WouldAControllerRecoveryHelp.html*

- **`error_code`**
  - Type: `unsigned short`
  - Default: `N/A`
  - The active error code to compare against. This should match the controller server error code.

---

## Wouldaplannerrecoveryhelp

### WouldAPlannerRecoveryHelp
*Source: https://docs.nav2.org/configuration/packages/bt-plugins/conditions/WouldAPlannerRecoveryHelp.html*

- **`error_code`**
  - Type: `unsigned short`
  - Default: `N/A`
  - The active error code to compare against. This should match the planner server error code.

---

## Wouldarouterecoveryhelp

### WouldARouteRecoveryHelp
*Source: https://docs.nav2.org/configuration/packages/bt-plugins/conditions/WouldARouteRecoveryHelp.html*

- **`error_code`**
  - Type: `unsigned short`
  - Default: `N/A`
  - The active error code to compare against. This should match the route server error code.

---

## Wouldasmootherrecoveryhelp

### WouldASmootherRecoveryHelp
*Source: https://docs.nav2.org/configuration/packages/bt-plugins/conditions/WouldASmootherRecoveryHelp.html*

- **`error_code`**
  - Type: `unsigned short`
  - Default: `N/A`
  - The active error code to compare against. This should match the smoother server error code.

---
