from setuptools import find_packages, setup

package_name = 'igvc_cv'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Camden Laursen-Carr',
    maintainer_email='laursc@rpi.edu',
    description='Computer Vision for the 2026 IGVC Robot',
    license='MIT',
    extras_require={
    },
    entry_points={
        'console_scripts': [
            'cv_node = igvc_cv.cv_node:main',
        ],
    },
)
