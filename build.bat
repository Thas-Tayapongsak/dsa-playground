@echo off

REM Check for the target file
if "%~1"=="" (
    echo Usage: .\build ^<filename^> [-r|--run] [args]
    exit /b 1
)

REM Check if target file exists
set "TARGET=%~1"
if not exist "src/%TARGET%.cpp" (
    echo Error: File "src/%TARGET%.cpp" not found.
    exit /b 1
)

REM Run the CMake Build
echo Building: %TARGET%...
cmake --build --preset debug --target "%TARGET%"

REM If build fails, stop here
if %errorlevel% neq 0 (
    echo Build failed :^(
    exit /b %errorlevel%
)
echo Build succeeded :D

REM Run the executable if indicated
shift
set "SHOULD_RUN="
if /I "%~1"=="-r" set SHOULD_RUN=1
if /I "%~1"=="--run" set SHOULD_RUN=1
if not defined SHOULD_RUN goto :eof

REM Collect program arguments
shift
set "PROGRAM_ARGS="
:collect_args
if "%~1"=="" goto :run_program
set "PROGRAM_ARGS=%PROGRAM_ARGS% %1"
shift
goto :collect_args

REM Run the program
:run_program
echo -----------------------------------
call run.bat "%TARGET%" %PROGRAM_ARGS%