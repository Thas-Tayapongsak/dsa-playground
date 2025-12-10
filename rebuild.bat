@echo off
setlocal

if exist build (
    rmdir /s /q build
    cmake --preset default
    call ./build -a
)

endlocal