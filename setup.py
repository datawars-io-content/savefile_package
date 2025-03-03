from setuptools import setup, find_packages

setup(
    name="savefile",  # Package name (unique on PyPI)
    version="0.1.0",  # Version number (increment on updates)
    packages=find_packages(),  # Automatically detect package modules
    install_requires=["numpy", "pandas", "matplotlib"],  # Dependencies
    author="Anurag Verma", 
    description="A utility package to save various data formats and zip them.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/anurag629/savefile",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
