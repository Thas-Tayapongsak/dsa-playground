@echo off
setlocal

set "HELP_FLAG="
if /I "%~1"=="-h" set HELP_FLAG=1
if /I "%~1"=="--help" set HELP_FLAG=1
if defined HELP_FLAG goto :help

set "ALL_FLAG="
if /I "%~1"=="-a" set ALL_FLAG=1
if /I "%~1"=="--all" set ALL_FLAG=1
if defined ALL_FLAG goto :test_all

if "%~1"=="" (
    echo Error: No argument provided.
    goto :help
)

set "TARGET=%~1"
goto :test_target

:help
    echo Usage: .\test ^<testname^>
    echo.
    echo Runs an executable test from the "build/bin" directory.
    echo.
    echo Parameters:
    echo   ^<testname^>     Name of the test to run (without extension).
    echo.
    echo Options:
    echo   -h, --help     Show this help message.
    exit /b 0

:test_all
    echo Running all tests...
    echo ---------------------------------------------------
    ctest --preset test
    goto :check_error

:test_target
    echo Testing: %TARGET%...
    echo ---------------------------------------------------
    ctest --preset test -R %TARGET%
    goto :check_error

:check_error
    echo.
    if %errorlevel% neq 0 (
        echo Test failed :^(
        exit /b %errorlevel%
    )
    echo Test succeeded :D

endlocal