@echo off
setlocal

set "HELP_FLAG="
if /I "%~1"=="-h" set HELP_FLAG=1
if /I "%~1"=="--help" set HELP_FLAG=1
if defined HELP_FLAG goto :help

if "%~1"=="" (
    echo Error: No argument provided.
    goto :help
)

set "TARGET=%~1"
goto :run_target

:help
    echo Usage: .\run ^<filename^> [args...]
    echo.
    echo Runs an executable from the "build" directory.
    echo.
    echo Parameters:
    echo   ^<filename^>     Name of the app to run (without extension).
    echo   [args...]        Arguments to pass to the application.
    echo.
    echo Options:
    echo   -h, --help     Show this help message.
    exit /b 0

:run_target
    if not exist "build/bin/%TARGET%.exe" (
        echo Error: File "build/bin/%TARGET%.exe" not found.
        exit /b 1
    )
    shift
    set "PROGRAM_ARGS="

:collect_args
    if "%~1"=="" goto :run_app
    set "PROGRAM_ARGS=%PROGRAM_ARGS% %1"
    shift
    goto :collect_args

:run_app
    echo Running: %TARGET%%PROGRAM_ARGS%...
    echo ---------------------------------------------------
    "build\bin\%TARGET%.exe" %PROGRAM_ARGS%
    goto :check_error

:check_error
    echo.
    if %errorlevel% neq 0 (
        echo Run failed :^(
        exit /b %errorlevel%
    )
    echo Run succeeded :D

endlocal