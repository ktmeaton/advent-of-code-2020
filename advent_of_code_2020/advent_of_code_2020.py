#!/usr/bin/env python3

# ----------------------------------------------------------------------------#
# Packages
# ----------------------------------------------------------------------------#
import logging
import os
import re
import networkx
import matplotlib.pyplot as plt

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

        # Convert boarding pass patterns to ids
        def binary_convert(pattern):
            """
            Convert a seat pattern to binary int
            """
            # Replace the string operators with 0,1
            bin_pattern = (
                pattern.replace("F", "0")
                .replace("B", "1")
                .replace("L", "0")
                .replace("R", "1")
            )
            return int(bin_pattern, 2)

        # Part 1 - Find the seat with the highest id
        boarding_passes = lines
        seat_id_list = []

        # Iterate through all the boarding passes
        for boarding_pass in boarding_passes:
            seat_id = binary_convert(boarding_pass)
            seat_id_list.append(seat_id)

        result["Part1"]["seat_id"] = max(seat_id_list)

        # Log the output
        self.logger.info("DAY 05")
        self.logger.info(log_underline)
        self.logger.info("PART 1")
        self.logger.info(str(result["Part1"]["seat_id"]))

        # Part 2 - Find your seat by process of elimination

        my_seat_id = 0

        # Iterate through the range of possible seat_ids
        for seat_id in range(min(seat_id_list), max(seat_id_list)):
            # My seat will not be in the list
            if seat_id not in seat_id_list:
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

    def day06(self, input, output):
        """
        Airplane customs declaration checker.
        """
        result = {"Part1": {}, "Part2": {}}

        # Create a new log handler
        self.log_create_handler(output)

        # Parse the input into a list
        with open(input, "r") as file:
            input_text = file.read()
            # Separate groups are separated by a newline
            input_split = input_text.split("\n\n")
            # Standardize field sep to all be spaces
            input_split = [item.replace("\n", " ") for item in input_split]

        # Manipulate the lines list (ex. type conversion)

        # Part 1 - Sum of yes answers per group
        yes_count = 0

        # Iterate through all the groups
        for group in input_split:
            # Remove spaces separating people
            group_split = group.replace(" ", "")
            matches = re.findall("^[a-z]*$", group_split)[0]
            yes_count += len(set(matches))

        result["Part1"]["answer"] = yes_count

        # Log the output
        self.logger.info("DAY 6")
        self.logger.info(log_underline)
        self.logger.info("PART 1")
        self.logger.info("answer: " + str(yes_count))

        # Part 2 - Sum of answers that eveyone in group answered yes to
        yes_count = 0

        for group in input_split:
            # Split up each group answer by person
            group_split = group.split(" ")
            # count the number of people in the group
            num_people = len(group_split)
            # Convoluted way to match a-z and then remove duplicates
            ind_yes = [
                "".join(set(re.findall("^[a-z]*$", person)[0]))
                for person in group_split
            ]
            # Now combine all answers in a group and remove duplicates
            group_yes = "".join(ind_yes)

            for i in range(ord("a"), ord("z") + 1):
                # Count the occurrences of the current char
                group_count = group_yes.count(chr(i))
                # If all people answered yes to his question
                if group_count == num_people:
                    yes_count += 1

        result["Part2"]["answer"] = yes_count

        # Log the output
        self.logger.info("PART 2")
        self.logger.info("answer: " + str(yes_count))
        self.logger.info(log_separator)

        # Remove the log handler
        self.log_remove_handler()

        return result

    def day07(self, input, output):
        """
        Count suitcase containing shiny gold bags.
        """
        result = {"Part1": {}, "Part2": {}}

        # Create a new log handler
        self.log_create_handler(output)

        # Parse the input into a list
        # lines = self.parse_file(input)

        # Part 1 - How many bag colors can eventually contain at
        # least one gold shiny bag
        # rules = lines
        bag_graph = networkx.DiGraph()

        test_rules = [
            "bright white bags contain 1 shiny gold bag.",
            "muted yellow bags contain 1 shiny gold bag, 2 other bags.",
            "dark orange bags contain 2 bright white bags, 2 muted yellow bags.",
            "light red bags contain 2 bright white bags, 2 muted yellow bags.",
        ]

        # rules_dict = {}

        # Parse the rules into a dictionary
        for rule in test_rules:
            # Remove unnecessasry char
            rule = rule.replace(".", "").replace(" bags", "").replace(" bag", "")
            split_rule = rule.split(" contain ")
            bag = split_rule[0]
            split_contents = split_rule[1].split(", ")

            for contents in split_contents:
                split_content = contents.split(" ")
                val, name = int(split_content[0]), " ".join(split_content[1:])
                bag_graph.add_edge(name, bag, weight=val)

        print(networkx.shortest_path(bag_graph, "shiny gold", "light red"))
        plt.subplot(121)
        networkx.draw(bag_graph, with_labels=True, font_weight="bold")
        plt.show()

        result["Part1"]["answer"] = None

        # Log the output
        self.logger.info("DAY 7")
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


if __name__ == "__main__":
    # Execute only if run as script
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

    advent.day06(
        input=os.path.join(project_dir, "input", "day06.txt"),
        output=os.path.join(project_dir, "output", "day06.log"),
    )
    """
    advent.day07(
        input=os.path.join(project_dir, "input", "day07.txt"),
        output=os.path.join(project_dir, "output", "day07.log"),
    )
