@echo off
setlocal enabledelayedexpansion

set input_file=tests.txt

rem Olvasd be a fájl tartalmát
for /f "tokens=1,2 delims=:" %%A in ('findstr /n "^" "%input_file%"') do (
    set "line=%%B"
    if !line! neq "" (
        if !count! lss 1 (
            set /a n=!line!
            set count=1
        ) else (
            set "boss_nodes=!line!"
            echo !n! > temp_input.txt
            echo !boss_nodes! >> temp_input.txt
            python feladat4.py < temp_input.txt
            if errorlevel 1 (
                echo "Hiba"
                pause
                exit /b
            )
            set count=0
        )
    )
)

del temp_input.txt

pause > nul

endlocal
