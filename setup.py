from setuptools import setup, find_packages

setup(
    name='IX-ThermaForge',
    version='0.1.0',
    author='Bryce Wooster',
    description='Advanced industrial energy beam system using Tesla harmonic principles.',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[
        'numpy>=1.21.0',
    ],
    python_requires='>=3.10',
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
)
