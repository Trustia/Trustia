from setuptools import setup, find_packages

setup(
    name="trustia_robotaxi_sdk",
    version="2.4.0",
    description="Trustia Autonomous Technologies — Level-4 Robotaxi Enterprise SDK & Safety Arbiter",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    author="Murat Furkan Bayram",
    author_email="contact@trustia.ai",
    packages=find_packages(),
    python_requires=">=3.8",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: Other/Proprietary License",
        "Operating System :: POSIX :: Linux",
        "Topic :: Scientific/Engineering :: Robotics",
    ],
    entry_points={
        "console_scripts": [
            "trustia-robotaxi=robotaxi_cli:main",
        ],
    },
)
