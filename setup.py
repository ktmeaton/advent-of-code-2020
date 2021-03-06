import setuptools

with open("README.md", "r") as f:
    long_description = f.read()

with open("requirements.txt", "r") as r:
    require_list = r.read().strip().split("\n")

setuptools.setup(
    name="advent-of-code-2020",
    version="0.1.0",
    description=("Katherine Eaton's Advent of Code 2020 challenge."),
    python_requires=">=3.6",
    license="MIT",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Katherine Eaton",
    author_email="ktmeaton@gmail.com",
    url="https://ktmeaton.github.io/advent-of-code-2020/",
    # packages=setuptools.find_packages(),
    packages=["advent_of_code_2020"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
    install_requires=require_list,  # external packages as dependencies
    extras_require={
        "dev": [
            "coverage==4.5.4",
            "codecov==2.0.15",
            "pytest==5.3.1",
            "pytest-cov==2.8.1",
            "pre-commit==2.6.0",
            "grip==4.5.2",
            "flake8==3.8.3",
            "flake8-bugbear==20.1.4",
            "black==19.10b0",
        ]
    },
)
