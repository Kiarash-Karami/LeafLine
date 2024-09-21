from setuptools import setup, find_packages

setup(
    name="leafline",
    version="0.1.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "sqlite3",
    ],
    entry_points={
        "console_scripts": [
            "leafline=leafline.main:main",
        ],
    },
    author="Your Name",
    author_email="your.email@example.com",
    description="A productivity timer that grows a forest of emoji plants",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/leafline",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
