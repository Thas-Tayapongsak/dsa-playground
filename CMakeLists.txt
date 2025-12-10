cmake_minimum_required(VERSION 3.12)

project(Scratchpad)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED True)

################################################################
# LIBRARIES
################################################################
file(GLOB_RECURSE LIB_SOURCES CONFIGURE_DEPENDS "src/*.cpp")

add_library(libs STATIC ${LIB_SOURCES})
target_include_directories(libs PUBLIC "${CMAKE_CURRENT_SOURCE_DIR}/include")

################################################################
# APPLICATIONS
################################################################
file(GLOB APP_SOURCES CONFIGURE_DEPENDS "app/*.cpp")

foreach(appfile ${APP_SOURCES})
    get_filename_component(appname ${appfile} NAME_WE)
    add_executable(${appname} ${appfile})
    target_link_libraries(${appname} PRIVATE libs)
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

file(GLOB TEST_SOURCES CONFIGURE_DEPENDS "tests/*.cpp")

foreach(testfile ${TEST_SOURCES})
    get_filename_component(testname ${testfile} NAME_WE)
    add_executable(${testname} ${testfile})
    target_link_libraries(
        ${testname} PRIVATE libs
        GTest::gtest_main
    )
    include(GoogleTest)
    gtest_discover_tests(${testname})
endforeach()
