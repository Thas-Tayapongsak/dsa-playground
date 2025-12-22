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
        [4,9]

    Returns:
        0
    """
    whitelist = create_file(temp_path, "whitelist.txt", "3\n7\n8\n")
    fulllist = create_file(temp_path, "fulllist.txt", "4\n3\n9\n7\n")

    result = run_app(APP_NAME, args=[whitelist], input_path=fulllist)

    assert result.returncode == 0
    assert result.stdout.strip().splitlines() == ["4","9"]

def test_empty_whitelist(run_app, temp_path):
    """
    Scenario: The whitelist is empty
    
    Given:
        `temp/whitelist.txt` containing []
        `temp/fulllist.txt` containing [1,2,3]

    Output:
        [1,2,3]

    Returns:
        0
    """
    whitelist = create_file(temp_path, "whitelist.txt", "")
    fulllist = create_file(temp_path, "fulllist.txt", "1\n2\n3\n")

    result = run_app(APP_NAME, args=[whitelist], input_path=fulllist)

    assert result.returncode == 0
    assert result.stdout.strip().splitlines() == ["1","2","3"]

def test_empty_stdin(run_app, temp_path):
    """
    Scenario: The list to be filtered is empty
    
    Given:
        `temp/whitelist.txt` containing [456,123]
        `temp/fulllist.txt` containing []

    Output:
        []

    Returns:
        0
    """
    whitelist = create_file(temp_path, "whitelist.txt", "456\n123\n")
    fulllist = create_file(temp_path, "fulllist.txt", "")

    result = run_app(APP_NAME, args=[whitelist], input_path=fulllist)

    assert result.returncode == 0
    assert result.stdout.strip().splitlines() == []


def test_filter_all_items(run_app, temp_path):
    """
    Scenario: Filter all items for lists with the same integers
    
    Given:
        `temp/whitelist.txt` containing [1,5,13,9]
        `temp/fulllist.txt` containing [9,13,1,5]

    Output:
        []

    Returns:
        0
    """
    whitelist = create_file(temp_path, "whitelist.txt", "1\n5\n13\n9\n")
    fulllist = create_file(temp_path, "fulllist.txt", "9\n13\n1\n5")

    result = run_app(APP_NAME, args=[whitelist], input_path=fulllist)

    assert result.returncode == 0
    assert result.stdout.strip().splitlines() == []

def test_filter_preserve_duplicates(run_app, temp_path):
    """
    Scenario: Filtered integers include duplicate integers

    Given:
        `temp/whitelist.txt` containing [41,42,43]
        `temp/fulllist.txt` containing [41,42,44,45,44]

    Output:
        [44,45,44]

    Returns:
        0
    """
    whitelist = create_file(temp_path, "whitelist.txt", "41\n42\n43\n")
    fulllist = create_file(temp_path, "fulllist.txt", "41\n42\n44\n45\n44")

    result = run_app(APP_NAME, args=[whitelist], input_path=fulllist)

    assert result.returncode == 0
    assert result.stdout.strip().splitlines() == ["44","45","44"]

def test_help(run_app):
    """
    Scenario: Using the help flag to display usage information

    Output:
        A usage message for the application
    
    Returns:
        0
    """
    result = run_app(APP_NAME, args=["-h"])

    assert result.returncode == 0

    help_message = result.stderr.strip()

    assert "Usage:" in help_message
    assert "-h, --help" in help_message
    assert "Display the help message" in help_message

"""
test_missing_whitelist 
    - given no whitelist, output the usage and error status

test_nonexistent_whitelist 
    - given a path to a nonexistent whitelist, output error message
"""


