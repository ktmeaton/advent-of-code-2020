# 🎅 Advent Of Code 2020 🎄

**Katherine Eaton's page for the [Advent of Code 2020 Challenge](https://adventofcode.com/2020).**  

[![Gitpod ready-to-code](https://img.shields.io/badge/Gitpod-ready--to--code-blue?logo=gitpod)](https://gitpod.io/#https://github.com/ktmeaton/advent-of-code-2020)
[![codecov](https://codecov.io/gh/ktmeaton/advent-of-code-2020/branch/main/graph/badge.svg)](https://codecov.io/gh/ktmeaton/advent-of-code-2020/branch/main)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://github.com/ktmeaton/advent-of-code-2020/blob/main/LICENSE)

## Install

### Pip

```bash
git clone https://github.com/ktmeaton/advent-of-code-2020.git
cd advent-of-code-2020/
pip install .[dev]
```

### Gitpod

Start up a Gitpod workspace:

[![Gitpod ready-to-code](https://img.shields.io/badge/Gitpod-ready--to--code-blue?logo=gitpod)](https://gitpod.io/#https://github.com/ktmeaton/advent-of-code-2020)

## Usage

Run as a script:

```bash
advent_of_code_2020/advent_of_code_2020.py
```

Run as a module:

```python
from advent_of_code_2020.advent_of_code_2020 import AdventOfCode2020
advent = AdventOfCode2020()
advent.day01(input="input/day01.txt", output="output/day01.log")
```

Check the output for a particular day:

```bash
cat output/day01.log
```

## Answers

- [Day 01](https://raw.githubusercontent.com/ktmeaton/advent-of-code-2020/main/output/day01.log)
- [Day 02](https://raw.githubusercontent.com/ktmeaton/advent-of-code-2020/main/output/day02.log)
- [Day 03](https://raw.githubusercontent.com/ktmeaton/advent-of-code-2020/main/output/day03.log)
- [Day 04](https://raw.githubusercontent.com/ktmeaton/advent-of-code-2020/main/output/day04.log)
- [Day 05](https://raw.githubusercontent.com/ktmeaton/advent-of-code-2020/main/output/day05.log)

## Implementation

- [Day 01](https://github.com/ktmeaton/advent-of-code-2020/blob/main/advent_of_code_2020/advent_of_code_2020.py#L117)
- [Day 02](https://github.com/ktmeaton/advent-of-code-2020/blob/main/advent_of_code_2020/advent_of_code_2020.py#L186)
- [Day 03](https://github.com/ktmeaton/advent-of-code-2020/blob/main/advent_of_code_2020/advent_of_code_2020.py#L253)
- [Day 04](https://github.com/ktmeaton/advent-of-code-2020/blob/main/advent_of_code_2020/advent_of_code_2020.py#L351)
- [Day 05](https://github.com/ktmeaton/advent-of-code-2020/blob/main/advent_of_code_2020/advent_of_code_2020.py#L527)

## Testing

```bash
python -m coverage run -m pytest --cov=advent_of_code_2020 --cov-report=xml test/test_advent.py
```
