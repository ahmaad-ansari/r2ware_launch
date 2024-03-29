import os

from ament_index_python import get_package_share_directory

from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch_ros.actions import Node
from launch.substitutions import LaunchConfiguration
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_xml.launch_description_sources import XMLLaunchDescriptionSource


def generate_launch_description():
    return LaunchDescription([
        Node(
            package='r2ware_launch',
            executable='r2ware_launch_node',
            output='screen',
            prefix=[],
        ),

        # Include the first launch script
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource('/root/r2ware/src/sensing/r2ware_sensing/launch/r2ware_sensing_launch.py'),
        ),

        # Include the second launch script
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource('/root/r2ware/src/control/r2ware_control/launch/r2ware_control_launch.py'),
        ),

        # Include the third launch script
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource('/root/r2ware/src/status/r2ware_status/launch/r2ware_status_launch.py'),
        ),
    ])
