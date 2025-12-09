cmake_minimum_required(VERSION 3.12)

project(Scratchpad)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED True)

file(GLOB SOURCES CONFIGURE_DEPENDS "src/*.cpp")

foreach(sourcefile ${SOURCES})
    get_filename_component(name ${sourcefile} NAME_WE)
    add_executable(${name} ${sourcefile})
endforeach()