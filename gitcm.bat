@echo off

if "%~1"=="" (
    set "comment=update"
) else (
    set "comment=%~1"
)

git add .
git commit -m "%comment%"
git push
