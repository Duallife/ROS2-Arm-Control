from setuptools import find_packages, setup
from glob import glob
import os

package_name = 'ROBOv2'

setup(
    name=package_name,
    version='1.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'), glob('launch/*.launch.py')),
        (os.path.join('share', package_name, 'urdf'), glob('urdf/**')),
        (os.path.join('share', package_name, 'meshes'), glob('meshes/*')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='duallife',
    maintainer_email='rtxgamer274@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
                "test_sub = ROBOv2.test_sub:main",
        	"test_pub = ROBOv2.test_pub:main",
        	"jointAnglePub = ROBOv2.jointAnglePub:main"
        ],
    },
)
