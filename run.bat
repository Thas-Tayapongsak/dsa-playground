@echo off

REM Check for the target file
if "%~1"=="" (
    echo Usage: .\run ^<filename^> 
    exit /b 1
)

REM Check if target file exists
set "TARGET=%~1"
if not exist "build\%TARGET%.exe" (
    echo Error: File "%TARGET%.exe" not found.
    exit /b 1
)

REM Collect program arguments
set "PROGRAM_ARGS="
shift
:collect_args
if "%~1"=="" goto :run_program
set "PROGRAM_ARGS=%PROGRAM_ARGS% %1"
shift
goto :collect_args

REM Run the executable 
:run_program
if exist "build\%TARGET%.exe" (
    echo Running: %TARGET% %PROGRAM_ARGS%... 
    echo.
    "build\%TARGET%.exe" %PROGRAM_ARGS%
) else (
    echo Error: Executable not found.
)