@echo off

REM Check if the virtual environment directory exists
if not exist .venv (
    echo Error: Virtual environment directory '.venv' does not exist.
    python -m venv .venv
)

REM Activate the virtual environment
call .venv\Scripts\activate

REM Check if the activation was successful
if errorlevel 1 (
    echo Error: Failed to activate the virtual environment.
    exit /b 1
)

echo Virtual environment activated successfully.
python -m pip install --upgrade pip
pip install pyinstaller
pip install -r requirements.txt

REM Copy sudoku.ico to the build directory
xcopy "assets\images\sudoku.ico" "build\" /Y

pyinstaller "src/App.py" --name "Sudoku App" --clean --noconfirm --add-data "../assets:assets" --windowed --icon "sudoku.ico" --specpath "build"

REM Copy the assets folder from _internal to the root of the distribution
xcopy "dist\Sudoku App\_internal\assets" "dist\Sudoku App\assets" /E /I /Y
rmdir /s /q "dist\Sudoku App\_internal\assets"
del /q "build\sudoku.ico"

call deactivate
pause