try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    "description": "Heat Space Detector",
    "version": "0.1",
    "install_requires": ["cv2", "numpy", "yml"],
    "packages": ["parking_lot"],
    "scripts": [],
    "name": "motion"
}

setup(**config)
