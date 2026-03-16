#!/usr/bin/env pwsh
Write-Host "Running project quality checks"

$results = @()

function Run-Tool {
    param(
        [string]$Name,
        [string]$Cmd,
        [string[]]$Args
    )

    Write-Host "`n== $Name =="
    if (Get-Command $Cmd -ErrorAction SilentlyContinue) {
        & $Cmd @Args
        $exit = $LASTEXITCODE
        $results += @{tool=$Name; exit=$exit}
        if ($exit -ne 0) { Write-Host "$Name returned exit code $exit" }
    }
    elseif (Get-Command python -ErrorAction SilentlyContinue) {
        Write-Host "Running via python -m $Cmd"
        & python -m $Cmd @Args
        $exit = $LASTEXITCODE
        $results += @{tool=$Name; exit=$exit}
        if ($exit -ne 0) { Write-Host "$Name returned exit code $exit" }
    }
    else {
        Write-Host "$Name not found — skipping"
        $results += @{tool=$Name; exit=-1}
    }
}

Run-Tool -Name 'flake8' -Cmd 'flake8' -Args '.'
Run-Tool -Name 'isort' -Cmd 'isort' -Args @('--check-only','--diff','.')
Run-Tool -Name 'black' -Cmd 'black' -Args @('--check','.')

Write-Host "`n== complexity (radon / lizard) =="
if (Get-Command radon -ErrorAction SilentlyContinue) {
    radon cc -s -a src
}
elseif (Get-Command lizard -ErrorAction SilentlyContinue) {
    lizard -C src
}
else {
    Write-Host "radon/lizard not installed — skipping complexity check"
}

Write-Host "`nSummary:"
$results | ForEach-Object {
    $status = if ($_.exit -eq 0) { 'OK' } elseif ($_.exit -eq -1) { 'MISSING' } else { "WARN($($_.exit))" }
    Write-Host " - $($_.tool): $status"
}

Write-Host "`nQuality checks complete."
