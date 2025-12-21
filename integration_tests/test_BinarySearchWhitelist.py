"""
Tests for BinarySearchWhitelist

This application should
1. Accept the file path of the whitelist as a command line argument.
2. Read the list of integers from the standard input.
3. Output the integers from standard input (including duplicates) that are NOT in the whitelist
4. The whitelist, input, and output is newline-delimited.
"""

APP_NAME = "BinarySearchWhitelist"

def create_file(directory, filename, content):
    """
    Helper function to create temporary file.
    
    :param file_name: Name of file
    :param content: Content of file
    """
    fp = directory / filename
    fp.write_text(content, encoding="utf-8")
    return str(fp)

def test_filter(run_app, temp_path):
    """
    Scenario: Happy Path.
    
    Given:
        `temp/whitelist.txt` containing [3,7,8]
        `temp/fulllist.txt` containing [4,3,9,7]

    Output:
        [4, 9]

    Returns:
        0
    """
    whitelist = create_file(temp_path, "whitelist.txt", "3\n7\n8\n")
    fulllist = create_file(temp_path, "fulllist.txt", "4\n3\n9\n7\n")

    result = run_app(APP_NAME, args=[whitelist], input_path=fulllist)

    assert result.returncode == 0
    assert result.stdout.strip().splitlines() == ["4","9"]

# def test_empty_whitelist(run_app, temp_path):
#     """
#     Scenario: The whitelist is empty.

#     Given:
#         `temp/whitelist.txt` containing []
#         `temp/fulllist.txt` containing [1,2,3]

#     Output:
#         [1,2,3]

#     Returns:
#         0
#     """
#     pass

"""
test_filter 
    - given a whitelist and a list, output the correct newline-delimited integers.

test_empty_whitelist 
    - given an empty whitelist and a list, output the original list in the original order.

test_empty_stdin 
    - given a whitelist and no input, output nothing.

test_filter_all_items 
    - given an identical pair of whitelist and input list, output nothing.

test_filter_preserve_duplicates 
    - given a whitelist and a list with duplicates, output the filtered integers including duplicates.

test_help 
    - running with help flag, output the usage and success status

test_missing_whitelist 
    - given no whitelist, output the usage and error status

test_nonexistent_whitelist 
    - given a path to a nonexistent whitelist, output error message
"""


