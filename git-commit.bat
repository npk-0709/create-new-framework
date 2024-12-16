@echo off

:: Kiểm tra tham số truyền vào
if "%~1"=="" (
    set "comment=update"
) else (
    set "comment=%~1"
)

echo Thực hiện lệnh: git add .
git add .

echo Thực hiện lệnh: git commit -m "%comment%"
git commit -m "%comment%"

echo Thực hiện lệnh: git push
git push

pause
