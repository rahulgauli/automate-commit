$num_commits = Read-Host "Enter the number of commits to add (1-100)"

if (-not ($num_commits -match '^\d+$') -or [int]$num_commits -lt 1 -or [int]$num_commits -gt 100) {
    Write-Host "Error: Please enter a valid number between 1 and 100."
    exit 1
}

$num_commits = [int]$num_commits

# Install dependencies once before the loop
Write-Host "Installing dependencies..."
pipenv install
pipenv install --dev

for ($i = 1; $i -le $num_commits; $i++) {
    Write-Host "Running python script: iteration $i"
    pipenv run python -m scripts.main
    Start-Sleep -Seconds 8
}