file(GLOB TEST_SOURCES CONFIGURE_DEPENDS "*.cpp")

foreach(testfile ${TEST_SOURCES})
    get_filename_component(testname ${testfile} NAME_WE)
    add_executable(${testname} ${testfile})
    target_link_libraries(
        ${testname} PRIVATE my_libs
        GTest::gtest_main
    )
    include(GoogleTest)
    gtest_discover_tests(${testname} TEST_PREFIX "${testname}.")
endforeach()