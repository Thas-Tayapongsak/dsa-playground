@echo off
setlocal 

set "TEST_FLAG="
if /I "%~1"=="-t" set TEST_FLAG=1
if /I "%~1"=="--test" set TEST_FLAG=1
if defined TEST_FLAG goto :build_target_test

if not "%~2"=="" (
    echo Error: Too many arguments or mixed flags.
    goto :help
)

set "HELP_FLAG="
if /I "%~1"=="-h" set HELP_FLAG=1
if /I "%~1"=="--help" set HELP_FLAG=1
if defined HELP_FLAG goto :help

set "ALL_FLAG="
if /I "%~1"=="-a" set ALL_FLAG=1
if /I "%~1"=="--all" set ALL_FLAG=1
if defined ALL_FLAG goto :build_all

if "%~1"=="" (
    echo Error: No argument provided.
    goto :help
)

set "TARGET=%~1"
goto :build_target

:help
    echo Usage: .\build [option] ^<filename^>
    echo.
    echo Options:
    echo   -a, --all      Build the entire project (Apps, Libs, Tests).
    echo   -h, --help     Show this help message.
    echo.
    echo Parameters:
    echo   ^<filename^>     Name of the specific target app to build (e.g., EuclidsAlgo).
    echo.
    exit /b 0

:build_all
    echo Building the entire project...
    echo ---------------------------------------------------
    cmake --build --preset debug
    goto :check_error

:build_target
    set "TARGET=%~1"
    if not exist "apps/%TARGET%.cpp" (
        echo Error: File "apps/%TARGET%.cpp" not found.
        exit /b 1
    )
    echo Building: %TARGET%...
    echo ---------------------------------------------------
    cmake --build --preset debug --target "%TARGET%"
    goto :check_error

:build_target_test
    set "TARGET=%~2"
    if not exist "tests/%TARGET%.cpp" (
        echo Error: File "tests/%TARGET%.cpp" not found.
        exit /b 1
    )
    echo Building: %TARGET%...
    echo ---------------------------------------------------
    cmake --build --preset debug --target "%TARGET%"
    goto :check_error

:check_error
    echo. >&2
    if %errorlevel% neq 0 (
        echo Build failed :^( >&2
        exit /b %errorlevel%
    )
    echo Build succeeded :D >&2

endlocal