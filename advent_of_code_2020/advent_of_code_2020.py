#!/usr/bin/env python3

# ----------------------------------------------------------------------------#
# Packages
# ----------------------------------------------------------------------------#
import logging
import os
import re
import math

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

    def day04(self, input, output):
        """
        Calculate the number of valid passports
        """
        result = {"Part1": {}, "Part2": {}}

        # Create a new log handler
        self.log_create_handler(output)

        # Parse the input into a list
        with open(input, "r") as file:
            input_text = file.read()
            # Separate passports are separated by a newline
            input_split = input_text.split("\n\n")
            # Standardize field sep to all be spaces
            input_split = [item.replace("\n", " ") for item in input_split]

        # Setup
        required_fields = [
            "byr",  # birth year
            "iyr",  # issue year
            "eyr",  # expiration year
            "hgt",  # height
            "hcl",  # hair color
            "ecl",  # eye color
            "pid",  # passport id
            # "cid", # country id (not mandatory)
        ]

        def validate_byr(byr):
            if (
                byr.isdigit()
                and len(byr) == 4
                and int(byr) >= 1920
                and int(byr) <= 2002
            ):
                return True
            else:
                return False

        def validate_iyr(iyr):
            if (
                iyr.isdigit()
                and len(iyr) == 4
                and int(iyr) >= 2010
                and int(iyr) <= 2020
            ):
                return True
            else:
                return False

        def validate_eyr(eyr):
            if (
                eyr.isdigit()
                and len(eyr) == 4
                and int(eyr) >= 2020
                and int(eyr) <= 2030
            ):
                return True
            else:
                return False

        def validate_hgt(hgt):
            if (
                hgt[:-2].isdigit()
                and (hgt[-2:] == "cm" and int(hgt[:-2]) >= 150 and int(hgt[:-2]) <= 193)
                or (hgt[-2:] == "in" and int(hgt[:-2]) >= 59 and int(hgt[:-2]) <= 76)
            ):
                return True
            else:
                return False

        def validate_hcl(hcl):
            if hcl[0] == "#" and re.match("^[0-9a-z]*$", hcl[1:]):
                return True
            else:
                return False

        def validate_ecl(ecl):
            if ecl in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
                return True
            else:
                return False

        def validate_pid(pid):
            if len(pid) == 9 and pid.isdigit():
                return True
            else:
                return False

        # Part 1 - Count the number of valid passports
        passports_info = input_split
        passports_dict = {}

        valid_passports = 0
        id = 1

        # Iterate through the numerous passports
        for passport in passports_info:
            # Initialize passport id
            if id not in passports_dict:
                passports_dict[id] = {}

            # Separate the space-delimtied fields
            passport_split = passport.split(" ")

            # Iterate through the numerous fields
            for field in passport_split:
                if not field:
                    continue
                # Separate the colon-delimited key:val
                field_key = field.split(":")[0]
                field_val = field.split(":")[1]
                passports_dict[id][field_key] = field_val

            # Validate the password fields
            is_valid = True
            for field in required_fields:
                if field not in passports_dict[id]:
                    is_valid = False
                    # Remove the passport if it's invalid
                    passports_dict.pop(id)
                    break

            if is_valid:
                valid_passports += 1

            id += 1

        result["Part1"]["valid_passports"] = valid_passports

        # Log the output
        self.logger.info("DAY 4")
        self.logger.info(log_underline)
        self.logger.info("PART 1")
        self.logger.info(str(result["Part1"]["valid_passports"]))

        # Part 2 - Count the number of valid passports with data validation
        valid_passports = 0

        # Iterate through the vaidated passports from Part 1
        for id in passports_dict:
            # Assume valid by default
            is_valid = True
            passport_fields = passports_dict[id]

            # Iterate through each field within a pasport
            for field in passport_fields:
                # Skip validation of country id
                if field == "cid":
                    continue

                value = passport_fields[field]
                # Get the validator function for this field
                validate_func = locals()["validate_" + field]

                # If the field wasn't validate, set passport to invalid
                if not validate_func(value):
                    is_valid = False

            if is_valid:
                valid_passports += 1

        result["Part2"]["valid_passports"] = valid_passports

        # Log the output
        self.logger.info("PART 2")
        self.logger.info(str(result["Part2"]["valid_passports"]))
        self.logger.info(log_separator)

        # Remove the log handler
        self.log_remove_handler()

        return result

    def day05(self, input, output):
        """
        Identify your seat from other boarding passes
        """
        result = {"Part1": {}, "Part2": {}}

        # Create a new log handler
        self.log_create_handler(output)

        # Parse the input into a list
        lines = self.parse_file(input)

        # Manipulate the lines list (ex. type conversion)

        # Setup
        seat_rows = [0, 127]  # 0-127
        seat_columns = [0, 7]  # 0-7

        def seat_search_binary(pattern, seat_range):
            """
            Perform a  binary search using pattern operators and seat_range bbox.
            """

            # If no operator's left, we've found the seat
            if len(pattern) == 0:
                return seat_range

            # Current operator is the first character in the pattern
            operator = pattern[0]

            # Row operators
            if operator == "F":
                seat_midpoint = math.floor((seat_range[0][0] + seat_range[0][1]) / 2)
                seat_rows = [seat_range[0][0], seat_midpoint]
                seat_range = [seat_rows, seat_range[1]]

            elif operator == "B":
                seat_midpoint = math.ceil((seat_range[0][0] + seat_range[0][1]) / 2)
                seat_rows = [seat_midpoint, seat_range[0][1]]
                seat_range = [seat_rows, seat_range[1]]

            # Column operators
            elif operator == "L":
                seat_midpoint = math.floor((seat_range[1][0] + seat_range[1][1]) / 2)
                seat_columns = [seat_range[1][0], seat_midpoint]
                seat_range = [seat_range[0], seat_columns]

            elif operator == "R":
                seat_midpoint = math.ceil((seat_range[1][0] + seat_range[1][1]) / 2)
                seat_columns = [seat_midpoint, seat_range[1][1]]
                seat_range = [seat_range[0], seat_columns]

            # New pattern occurs after the current operator
            pattern = pattern[1:]

            return seat_search_binary(pattern, seat_range)

        # Part 1 - Find the seat with the highest id
        boarding_passes = lines
        boarding_passes_dict = {}  # {row:[columns]}
        seat_id_list = []

        # Iterate through all the boarding passes
        for boarding_pass in boarding_passes:
            final_range = seat_search_binary(
                pattern=boarding_pass, seat_range=[seat_rows, seat_columns]
            )
            seat_coord = [final_range[0][0], final_range[1][1]]
            seat_row = seat_coord[0]
            seat_col = seat_coord[1]

            # Add the seat_coord to the dictionary
            if seat_row not in boarding_passes_dict:
                boarding_passes_dict[seat_row] = []
            boarding_passes_dict[seat_row].append(seat_col)

            # Add the seat_id to the dictionary
            # Seat ID: multiply the row by 8, then add the column
            seat_id = (seat_row * 8) + seat_col
            seat_id_list.append(seat_id)

        result["Part1"]["seat_id"] = max(seat_id_list)

        # Log the output
        self.logger.info("DAY 05")
        self.logger.info(log_underline)
        self.logger.info("PART 1")
        self.logger.info(str(result["Part1"]["seat_id"]))

        # Part 2 - Find your seat by process of elimination

        my_seat_id = 0

        # Iterate through all the boarding passes
        for row, cols in boarding_passes_dict.items():
            # Find rows that are short a few seats
            if len(cols) != seat_columns[1] + 1:
                # look for missing seat columns
                for col in range(seat_columns[0], seat_columns[1] + 1):
                    if col not in cols:
                        seat_id = (row * 8) + col
                        # +1, and -1 of my seat id will be in the list
                        if seat_id + 1 in seat_id_list and seat_id - 1 in seat_id_list:
                            my_seat_id = seat_id

        result["Part2"]["seat_id"] = my_seat_id

        # Log the output
        self.logger.info("PART 2")
        self.logger.info(str(result["Part2"]["seat_id"]))
        self.logger.info(log_separator)

        # Remove the log handler
        self.log_remove_handler()

        return result


if __name__ == "__main__":
    # Execute only if run as script
    advent = AdventOfCode2020()

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

    advent.day03(
        input=os.path.join(project_dir, "input", "day03.txt"),
        output=os.path.join(project_dir, "output", "day03.log"),
    )

    advent.day04(
        input=os.path.join(project_dir, "input", "day04.txt"),
        output=os.path.join(project_dir, "output", "day04.log"),
    )

    advent.day05(
        input=os.path.join(project_dir, "input", "day05.txt"),
        output=os.path.join(project_dir, "output", "day05.log"),
    )
