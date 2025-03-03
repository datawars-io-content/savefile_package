from setuptools import setup, find_packages

setup(
    name="savefile",
    version="0.1",
    packages=find_packages(),
    install_requires=["numpy", "pandas", "matplotlib"],
    author="Anurag Verma",
    description="A utility package to save different file formats, including images, and zip them.",
)
