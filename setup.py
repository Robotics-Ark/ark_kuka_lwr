from setuptools import setup, find_packages

setup(
    name="kuka-lwr",
    version="0.1.0",
    description="Kuka LWR robot driver for the ARK framework",
    author="Sarthak Das",
    author_email="sdas4@icloud.com",
    packages=find_packages(),
    install_requires=[
        "ark",
        "numpy",
        "scipy",
     ],
     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
     ],
     python_requires='>=3.10',
 )
