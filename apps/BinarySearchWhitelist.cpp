/**
 * @file 
 * @brief Filter and return integers not found inside a whitelist
 * 
 * This application uses binary search algorithm to return integers from a given list, 
 * which is not a member of a given whitelist
 * 
 * The whitelist is given as the name of the text file containing the whitelist as the 
 * first argument. The whitelist is a newline-delimited list of integers.
 * 
 * The list to be filtered is given as the name of the text file containing the list of 
 * integers as standard input
 */

#include <cstdlib>
#include <iostream>
#include <string>
#include <string_view>
#include "my_dsa.h"

void print_usage(std::string_view  app_name) {
    std::cerr << "Usage: " << app_name << " [options] <white_list> < <full_list>" << std::endl 
        << "Options:" << std::endl
        << "\t-h, --help\tDisplay the help message" << std::endl
        << std::endl
        << "Examples:" << std::endl
        << "\t" << app_name << " whitelist.txt < full_list.txt" << std::endl
        << "\t" << app_name << " --help" << std::endl;  
}

struct AppArgs {
    std::string app_name;
    bool valid = true;
    bool help_flag = false;
    std::string whitelist_path;
};

AppArgs parse_arguments(int argc, char* argv[]) {
    AppArgs args;

    args.app_name = argv[0];
    
    if (argc < 2) {
        std::cerr << "Error: Missing argument for path to whitelist file." << std::endl;
        args.valid = false;
        return args;
    }

    std::string arg1 = argv[1];
    if ((arg1 == "-h") || (arg1 == "--help")) {
        args.help_flag = true;
        return args;
    }

    if (argc != 2) {
        std::cerr << "Error: Invalid number of arguments." << std::endl;
        args.valid = false;
        return args;
    }

    args.whitelist_path = arg1;

    return args;
}

int main(int argc, char* argv[]) {
    AppArgs args = parse_arguments(argc, argv);

    if (!args.valid) {
        print_usage(args.app_name);
        return EXIT_FAILURE;
    }

    if (args.help_flag) {
        print_usage(args.app_name);
        return EXIT_SUCCESS;
    }

    std::cout << args.whitelist_path;

    return EXIT_SUCCESS;
}