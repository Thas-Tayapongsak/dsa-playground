set(Python3_FIND_VIRTUALENV ONLY)
find_package(Python3 3.11 COMPONENTS Interpreter REQUIRED)

file(GLOB INTEGRATION_TEST_SOURCES CONFIGURE_DEPENDS "test_*.py")

foreach(testfile ${INTEGRATION_TEST_SOURCES})
    get_filename_component(testname ${testfile} NAME_WE)
    add_test(NAME Integration.${testname} COMMAND ${Python3_EXECUTABLE} -m pytest "${testfile}")
    set_tests_properties(Integration.${testname} PROPERTIES ENVIRONMENT "EXECUTABLE_DIR=${CMAKE_RUNTIME_OUTPUT_DIRECTORY}")
endforeach()