#!/usr/bin/env python3

# Packages
import logging
import os

# Setup
script_dir = os.path.dirname(os.path.realpath(__file__))
input_path = os.path.join(script_dir, "input.txt")
logging.basicConfig(
    filename=os.path.join(script_dir, "day01.log"),
    filemode="w",
    format="[%(asctime)s] %(levelname)s:\t%(message)s",
    datefmt="%D %H:%M:%S",
    level=logging.DEBUG,
)

# Day 01 - Part 1
# Find the two entries that sum to 2020 (from input.txt)
# and then multiply those two entries together.

match_found = False

with open(input_path, "r") as file:
    # Store the input as two separate lists (copies)
    lines1_list = [int(line.strip()) for line in file]
    lines2_list = lines1_list

    # Compare every element in one list to the copy
    for line1 in lines1_list:
        for line2 in lines2_list:
            if line1 + line2 == 2020:
                match_found = True
                break
        if match_found:
            break

# Print the answer
logging.info("PART 1")
if match_found:
    logging.info("Matches Found: " + str(line1) + " " + str(line2))
    logging.info("Product: " + str(line1 * line2))
else:
    logging.info("No matches found.")

# Day 01 - Part 2
# Find the three entries that sum to 2020 (from input.txt)
# and then multiply those three entries together.

match_found = False

with open(input_path, "r") as file:
    # Store the input as three separate lists (copies)
    lines1_list = [int(line.strip()) for line in file]
    lines2_list = lines1_list
    lines3_list = lines1_list

    # Compare every element in one list to the others
    for line1 in lines1_list:
        for line2 in lines2_list:
            for line3 in lines3_list:
                if line1 + line2 + line3 == 2020:
                    match_found = True
                    break
            if match_found:
                break
        if match_found:
            break

# Print the answer
logging.info("PART2")
if match_found:
    logging.info("Matches Found: " + str(line1) + " " + str(line2) + " " + str(line3))
    logging.info("Product: " + str(line1 * line2 * line3))
else:
    logging.info("No matches found.")
