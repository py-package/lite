from setuptools import setup, find_packages

setup(
    name="lite",
    version="0.1.0",
    description="A simple web framework built from scratch",
    author="Yubaraj Shrestha",
    author_email="yubaraj@py-package.com",
    url="https://github.com/py-package/lite",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "click",
    ],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    python_requires=">=3.6",
    entry_points={
        "console_scripts": [
            "lite=lite.cli:lite",
        ],
    },
)