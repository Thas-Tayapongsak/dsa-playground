cmake_minimum_required(VERSION 3.12)

project(Scratchpad)

set(CMAKE_EXPORT_COMPILE_COMMANDS ON)

# Output Directories
# Executables (.exe) go to build/bin
set(CMAKE_RUNTIME_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/bin)
# Static Libs (.a, .lib) go to build/lib
set(CMAKE_ARCHIVE_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/lib)
# Shared Libs (.dll, .so) go to build/lib
set(CMAKE_LIBRARY_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/lib)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED True)

################################################################
# LIBRARIES
################################################################
file(GLOB_RECURSE LIB_SOURCES CONFIGURE_DEPENDS "src/*.cpp")

add_library(my_libs STATIC ${LIB_SOURCES})
target_include_directories(my_libs PUBLIC "${CMAKE_CURRENT_SOURCE_DIR}/include")

################################################################
# APPLICATIONS
################################################################
file(GLOB APP_SOURCES CONFIGURE_DEPENDS "apps/*.cpp")

foreach(appfile ${APP_SOURCES})
    get_filename_component(appname ${appfile} NAME_WE)
    add_executable(${appname} ${appfile})
    target_link_libraries(${appname} PRIVATE my_libs)
endforeach()

################################################################
# TESTS
################################################################
include(FetchContent)
FetchContent_Declare(
  googletest
  URL https://github.com/google/googletest/archive/03597a01ee50ed33e9dfd640b249b4be3799d395.zip
  DOWNLOAD_EXTRACT_TIMESTAMP TRUE
)
# For Windows: Prevent overriding the parent project's compiler/linker settings
set(gtest_force_shared_crt ON CACHE BOOL "" FORCE)
FetchContent_MakeAvailable(googletest)

enable_testing()

add_subdirectory(tests)