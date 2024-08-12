$currentDirectory = Get-Location
$directoryName = $currentDirectory.Name

git init

gh repo create $directoryName --private --source=. --remote=origin

Remove-Item -Path "Klib\.git" -Recurse -Force

git add .

git commit -m update

git branch -m main

git push -u origin main