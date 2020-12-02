#!/usr/bin/env python3

# ----------------------------------------------------------------------------#
# Packages
# ----------------------------------------------------------------------------#
import os
import advent_of_code_2020.advent_of_code_2020 as adv

# ----------------------------------------------------------------------------#
# Setup
# ----------------------------------------------------------------------------#
advent = adv.AdventOfCode2020()
script_dir = os.path.dirname(os.path.realpath(__file__))
project_dir = os.path.dirname(script_dir)

# ----------------------------------------------------------------------------#
# Test Functions
# ----------------------------------------------------------------------------#


def test_day01_part1():
    """Test Day01 - Part 1"""
    matches = [215, 1805]
    product = 388075

    result = advent.day01(
        input=os.path.join(project_dir, "input", "day01.txt"),
        output=os.path.join(project_dir, "test", "day01.log"),
    )
    assert (
        matches == result["Part1"]["matches"] and product == result["Part1"]["product"]
    )


def test_day01_part2():
    """Test Day01 - Part 2"""
    matches = [558, 823, 639]
    product = 293450526

    result = advent.day01(
        input=os.path.join(project_dir, "input", "day01.txt"),
        output=os.path.join(project_dir, "test", "day01.log"),
    )
    assert (
        matches == result["Part2"]["matches"] and product == result["Part2"]["product"]
    )
