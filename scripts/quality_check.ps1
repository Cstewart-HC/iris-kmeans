#!/usr/bin/env pwsh

Write-Host "Running project quality checks"

$results = @()

function Invoke-QualityTool {
    param(
        [string]$Name,
        [string]$Command,
        [string[]]$Args
    )

    Write-Host "`n== $Name =="

    if (Get-Command $Command -ErrorAction SilentlyContinue) {
        & $Command @Args
        $exitCode = $LASTEXITCODE
    }
    elseif (Get-Command python -ErrorAction SilentlyContinue) {
        Write-Host "Running via python -m $Command"
        & python -m $Command @Args
        $exitCode = $LASTEXITCODE
    }
    else {
        Write-Host "$Name not found - skipping"
        $exitCode = -1
    }

    if ($exitCode -gt 0) {
        Write-Host "$Name returned exit code $exitCode"
    }

    $script:results += [pscustomobject]@{
        Tool = $Name
        Exit = $exitCode
    }
}

Invoke-QualityTool -Name "flake8" -Command "flake8" `
    -Args @("src", "tests", "scripts")
Invoke-QualityTool -Name "isort" -Command "isort" `
    -Args @("--check-only", "--diff", "src", "tests", "scripts")
Invoke-QualityTool -Name "black" -Command "black" `
    -Args @("--check", "src", "tests", "scripts")

Write-Host "`n== complexity (radon / lizard) =="
if (Get-Command radon -ErrorAction SilentlyContinue) {
    radon cc -s -a src
}
elseif (Get-Command lizard -ErrorAction SilentlyContinue) {
    lizard -C src
}
else {
    Write-Host "radon/lizard not installed - skipping complexity check"
}

Write-Host "`nSummary:"
foreach ($result in $results) {
    if ($result.Exit -eq 0) {
        $status = "OK"
    }
    elseif ($result.Exit -eq -1) {
        $status = "MISSING"
    }
    else {
        $status = "WARN($($result.Exit))"
    }

    Write-Host " - $($result.Tool): $status"
}

Write-Host "`nQuality checks complete."
