$num_commits = Read-Host "Enter the number of commits to add (1-100)"

if (-not ($num_commits -match '^\d+$') -or $num_commits -lt 1 -or $num_commits -gt 100) {
    Write-Host "Error: Please enter a valid number between 1 and 100."
    exit 1
}

for ($i = 1; $i -le $num_commits; $i++) {
    Write-Host "Running python script: iteration $i"
    python your_script.py
}