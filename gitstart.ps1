$currentDirectory = Get-Location
$directoryName = $currentDirectory.Name
echo "Current directory: $currentDirectory"
echo "Directory name: $directoryName"
git init
echo "Git init"
gh repo create $directoryName --private --source=. --remote=origin
echo "Create repository"

if (Test-Path -Path "Klib\.git") {
    Remove-Item -Path "Klib\.git" -Recurse -Force
    echo "Remove Klib\.git"
}

git add .
echo "Add all files"

git commit -m update
echo "Commit"

git branch -m main
echo "Rename branch to main"

git push -u origin main
echo "Push to origin"