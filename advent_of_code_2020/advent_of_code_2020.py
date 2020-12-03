#!/usr/bin/env python3

# ----------------------------------------------------------------------------#
# Packages
# ----------------------------------------------------------------------------#
import logging
import os

# ----------------------------------------------------------------------------#
# Setup
# ----------------------------------------------------------------------------#
script_dir = os.path.dirname(os.path.realpath(__file__))
project_dir = os.path.dirname(script_dir)

formatter = logging.Formatter("[%(asctime)s] %(levelname)s:\t%(message)s")

log_underline = "-" * 40
log_separator = "\n"

# ----------------------------------------------------------------------------#
# Classes
# ----------------------------------------------------------------------------#


class AdventOfCode2020:
    """Advent of Code 2020 Imlemtation."""

    def __init__(self):
        """
        Constructor method.
        """
        # Create the class logger
        self.logger = logging.getLogger("dev")
        self.logger.setLevel(logging.INFO)

        # Configure a logging handler to the console
        consoleHandler = logging.StreamHandler()
        consoleHandler.setLevel(logging.INFO)
        consoleHandler.setFormatter(formatter)

        # Add the console handler to the class logger
        self.logger.addHandler(consoleHandler)

    # ------------------------------------------------------------------------#
    # Helper Functions
    # ------------------------------------------------------------------------#
    def parse_file(self, path):
        """
        Parse a text file of lines into a list.
        """
        with open(path) as file:
            return [line.strip() for line in file]

    def log_create_handler(self, path):
        """
        Create a the logging file associated with path.
        """
        # Configure a new file handler
        fileHandler = logging.FileHandler(path, mode="w",)
        fileHandler.setLevel(logging.INFO)
        fileHandler.setFormatter(formatter)

        # Add the new file handler to class logger
        self.logger.addHandler(fileHandler)

        # Write a test message
        # self.logger.info("Test information message to" + path)

    def log_remove_handler(self):
        """
        Remove logging file handlers.
        """
        self.logger.handlers = [
            h for h in self.logger.handlers if not isinstance(h, logging.FileHandler)
        ]

    # ------------------------------------------------------------------------#
    # Day Challenges
    # ------------------------------------------------------------------------#

    def _dayX(self, input, output):
        """
        Template function for upcoming challenge days.
        """
        result = {"Part1": {}, "Part2": {}}

        # Create a new log handler
        self.log_create_handler(output)

        # Parse the input into a list
        # lines = self.parse_file(input)

        # Manipulate the lines list (ex. type conversion)

        # Part 1 - Description

        result["Part1"]["answer"] = None

        # Log the output
        self.logger.info("DAY X")
        self.logger.info(log_underline)
        self.logger.info("PART 1")

        # Part 2 - Description

        result["Part2"]["answer"] = None

        # Log the output
        self.logger.info("PART 2")
        self.logger.info(log_separator)

        # Remove the log handler
        self.log_remove_handler()

        return result

    def day01(self, input, output):
        """
        Find the entries that sum to 2020 and find their product.
        """
        result = {"Part1": {}, "Part2": {}}
        # Create a new log handler
        self.log_create_handler(output)

        # Parse the input into a list
        lines = self.parse_file(input)

        # Convert the elements to integers and make two copies
        lines1_list = [int(line) for line in lines]
        lines2_list = lines1_list
        lines3_list = lines1_list

        # Part 1 - Find the product of two entries that sum to 2020.
        match_found = False
        for line1 in lines1_list:
            for line2 in lines2_list:
                if line1 + line2 == 2020:
                    result["Part1"]["matches"] = [line1, line2]
                    result["Part1"]["product"] = line1 * line2
                    match_found = True
                    break
            if match_found:
                break

        # Log the output
        self.logger.info("DAY 01")
        self.logger.info(log_underline)
        self.logger.info("PART 1")
        if match_found:
            self.logger.info("Matches found: " + str(line1) + " " + str(line2))
            self.logger.info("Product: " + str(line1 * line2))
        else:
            self.logger.info("No matches found.")

        # Part 2 - Find the product of three entries that sum to 2020.
        match_found = False
        for line1 in lines1_list:
            for line2 in lines2_list:
                for line3 in lines3_list:
                    if line1 + line2 + line3 == 2020:
                        result["Part2"]["matches"] = [line1, line2, line3]
                        result["Part2"]["product"] = line1 * line2 * line3
                        match_found = True
                        break
                if match_found:
                    break
            if match_found:
                break

        self.logger.info("PART 2")
        if match_found:
            self.logger.info(
                "Matches found: " + str(line1) + " " + str(line2) + " " + str(line3)
            )
            self.logger.info("Product: " + str(line1 * line2 * line3))
        else:
            self.logger.info("No matches found.")

        self.logger.info(log_separator)

        # Remove the log handler
        self.log_remove_handler()

        return result

    def day02(self, input, output):
        """
        Calculate the number of valid passwords from the input.
        """
        result = {"Part1": {}, "Part2": {}}
        # Create a new log handler
        self.log_create_handler(output)

        # Parse the input into a list
        lines = self.parse_file(input)

        # Separate the elements in to a list:
        # 3-5 x: xxqxm -> ['3', '5', 'x', 'xxqxm']
        split_lines = [
            line.replace("-", " ").replace(":", "").split(" ") for line in lines
        ]

        # Part 1 - The first two elements describe character counts
        valid_pass = 0

        for pass_validator in split_lines:
            # Store the min and max number of times the character must appear
            min_count, max_count = int(pass_validator[0]), int(pass_validator[1])
            char = pass_validator[2]
            password = pass_validator[3]
            char_count = password.count(char)
            # If the character count matches the password validator
            if char_count >= min_count and char_count <= max_count:
                valid_pass += 1

        result["Part1"]["passwords"] = valid_pass

        # Log the output
        self.logger.info("DAY 02")
        self.logger.info(log_underline)
        self.logger.info("PART 1")
        self.logger.info("Valid passwords: " + str(valid_pass))

        # Part 2 - The first two elements describe character positions
        valid_pass = 0

        for pass_validator in split_lines:
            index_first = int(pass_validator[0]) - 1
            index_second = int(pass_validator[1]) - 1
            char = pass_validator[2]
            password = pass_validator[3]

            matches = 0
            if password[index_first] == char:
                matches += 1
            if password[index_second] == char:
                matches += 1
            if matches == 1:
                valid_pass += 1

        result["Part2"]["passwords"] = valid_pass

        # Log the output
        self.logger.info("PART 2")
        self.logger.info("Valid passwords: " + str(valid_pass))
        self.logger.info(log_separator)

        # Remove the log handler
        self.log_remove_handler()

        return result

    def day03(self, input, output):
        """
        Calculate the number of trees encountered during the hill traversal.
        """
        result = {"Part1": {}, "Part2": {}}

        # Create a new log handler
        self.log_create_handler(output)

        # Parse the input into a list
        lines = self.parse_file(input)

        # General variables for all parts
        orig_terrain = lines
        # terrain_open = "."
        terrain_tree = "#"
        terrain_height = len(orig_terrain)
        terrain_width = len(orig_terrain[0])

        # Manipulate the lines list (ex. type conversion)

        # Part 1 - Calculate the number of trees encountered with slope (3,1).
        terrain = orig_terrain
        coord_x, coord_y = 0, 0
        slope_x, slope_y = 3, 1
        trees = 0

        # Traverse the terrain
        for _i in range(0, terrain_height, slope_y):
            # Check if we need to extend the terrain (repeats horizontally)
            if coord_x >= terrain_width:
                terrain = [
                    level + new_level for level, new_level in zip(terrain, orig_terrain)
                ]
            coord_terrain = terrain[coord_y][coord_x]
            # Check if the terrain at the current coordinate is a tree
            if coord_terrain == terrain_tree:
                trees += 1
            coord_x += slope_x
            coord_y += slope_y

        result["Part1"]["trees"] = trees

        # Log the output
        self.logger.info("DAY 3")
        self.logger.info(log_underline)
        self.logger.info("PART 1")
        self.logger.info("Trees: " + str(trees))

        # Part 2 - For 5 different slopes, calculate the product of the trees
        slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
        trees_list = []

        # Iterate through the different slopes
        for slope in slopes:
            # Retrieve the slope values
            slope_x, slope_y = slope[0], slope[1]
            # Initialize the traversal values
            trees = 0
            coord_x, coord_y = 0, 0
            terrain = orig_terrain

            # Traverse the terrain
            for _i in range(0, terrain_height, slope_y):
                # Check if we need to extend the terrain (repeats horizontally)
                if coord_x >= terrain_width:
                    terrain = [
                        level + new_level
                        for level, new_level in zip(terrain, orig_terrain)
                    ]
                coord_terrain = terrain[coord_y][coord_x]
                # Check if the terrain at the current coordinate is a tree
                if coord_terrain == terrain_tree:
                    trees += 1
                coord_x += slope_x
                coord_y += slope_y

            # Store the calculated number of trees for this slope
            trees_list.append(trees)

        # Calculate the product of all the trees
        product = 1
        for count in trees_list:
            product = count * product

        result["Part2"]["trees"] = product

        # Log the output
        self.logger.info("PART 2")
        self.logger.info("Trees: " + str(product))
        self.logger.info(log_separator)

        # Remove the log handler
        self.log_remove_handler()

        return result


if __name__ == "__main__":
    # execute only if run as a script
    advent = AdventOfCode2020()

    """
    advent._dayX(
        input=os.path.join(project_dir, "input", "dayX.txt"),
        output=os.path.join(project_dir, "output", "dayX.log"),
    )

    advent.day01(
        input=os.path.join(project_dir, "input", "day01.txt"),
        output=os.path.join(project_dir, "output", "day01.log"),
    )

    advent.day02(
        input=os.path.join(project_dir, "input", "day02.txt"),
        output=os.path.join(project_dir, "output", "day02.log"),
    )
    """
    advent.day03(
        input=os.path.join(project_dir, "input", "day03.txt"),
        output=os.path.join(project_dir, "output", "day03.log"),
    )
