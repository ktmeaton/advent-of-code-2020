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


def test_dayX_part1():
    """Test DayX - Part 1"""
    answer = None

    result = advent._dayX(
        input=os.path.join(project_dir, "input", "dayX.txt"),
        output=os.path.join(project_dir, "test", "dayX.log"),
    )
    assert answer == result["Part1"]["answer"]


def test_dayX_part2():
    """Test DayX - Part 2"""
    answer = None

    result = advent._dayX(
        input=os.path.join(project_dir, "input", "dayX.txt"),
        output=os.path.join(project_dir, "test", "dayX.log"),
    )
    assert answer == result["Part2"]["answer"]


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


def test_day02_part1():
    """Test Day02 - Part 1"""
    passwords = 398

    result = advent.day02(
        input=os.path.join(project_dir, "input", "day02.txt"),
        output=os.path.join(project_dir, "test", "day02.log"),
    )
    assert passwords == result["Part1"]["passwords"]


def test_day02_part2():
    """Test Day02 - Part 2"""
    passwords = 562

    result = advent.day02(
        input=os.path.join(project_dir, "input", "day02.txt"),
        output=os.path.join(project_dir, "test", "day02.log"),
    )
    assert passwords == result["Part2"]["passwords"]


def test_day3_part1():
    """Test Day3 - Part 1"""
    trees = 289

    result = advent.day03(
        input=os.path.join(project_dir, "input", "day03.txt"),
        output=os.path.join(project_dir, "test", "day03.log"),
    )
    assert trees == result["Part1"]["trees"]


def test_day3_part2():
    """Test Day3 - Part 2"""
    trees = 5522401584

    result = advent.day03(
        input=os.path.join(project_dir, "input", "day03.txt"),
        output=os.path.join(project_dir, "test", "day03.log"),
    )
    assert trees == result["Part2"]["trees"]
