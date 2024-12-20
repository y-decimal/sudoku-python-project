@echo off


pip 3 install pyinstaller

REM Copy sudoku.ico to the build directory
xcopy "assets\images\sudoku.ico" "build\" /Y

pyinstaller "src/App.py" --name "Sudoku App" --clean --noconfirm --add-data "../assets:assets" --windowed --icon "sudoku.ico" --specpath "build"

REM Copy the assets folder from _internal to the root of the distribution
xcopy "dist\Sudoku App\_internal\assets" "dist\Sudoku App\assets" /E /I /Y
rmdir /s /q "dist\Sudoku App\_internal\assets"
del /q "build\sudoku.ico"
pause