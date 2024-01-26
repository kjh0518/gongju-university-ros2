from setuptools import find_packages, setup
import os
from glob import glob

package_name = 'kongju_ros'
share_dir = 'share/' + package_name

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (share_dir +'/launch', glob(os.path.join('launch', '*.launch.py')))
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='aa',
    maintainer_email='aa@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'move_turtlesim = kongju_ros.move_turtlesim:main',
            'move_turtlebot = kongju_ros.move_turtlebot:main',
            'simple_pub = kongju_ros.simple_pub:main',
            'simple_sub = kongju_ros.simple_sub:main',
            'simple_sub2 = kongju_ros.simple_sub2:main',
            'simple_time_pub = kongju_ros.simple_time_pub:main',
            'simple_time_sub = kongju_ros.simple_time_sub:main',
        ],
    },
)
