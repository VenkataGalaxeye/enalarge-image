from setuptools import setup, find_packages

setup(
    name="enlarge",
    version="0.1.0",
    description="A simple package to duplicate an image into two identical copies",
    author="Your Name",
    author_email="your.email@example.com",
    license="MIT",
    packages=find_packages(),
    install_requires=[
        "Pillow>=10.0.0",
    ],
    python_requires=">=3.7",
    entry_points={
        "console_scripts": [
            "enlarge=enlarge.enlarge:main",
        ],
    },
)
