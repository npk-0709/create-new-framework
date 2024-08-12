$currentDirectory = Get-Location
$directoryName = $currentDirectory.Name

git init

gh repo create [FNAME] --private --source=. --remote=origin

Remove-Item -Path $directoryName -Recurse -Force

git add .

git commit -m update

git branch -m main

git push -u origin main