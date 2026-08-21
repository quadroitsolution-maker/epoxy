$content = Get-Content -Path index.html -Raw
$startStr = "    <!-- ═══════════════════════════════════════`n         APPLICATION CATEGORIES"
if ($content.IndexOf($startStr) -eq -1) {
    $startStr = "    <!-- ═══════════════════════════════════════`r`n         APPLICATION CATEGORIES"
}
$endStr = "    </section>`n"
if ($content.IndexOf($endStr) -eq -1) {
    $endStr = "    </section>`r`n"
}

$startIndex = $content.IndexOf($startStr)
if ($startIndex -eq -1) {
    Write-Host "Start string not found in index.html"
    exit
}
$endIndex = $content.IndexOf($endStr, $startIndex) + $endStr.Length
$section = $content.Substring($startIndex, $endIndex - $startIndex)

# Remove from index.html
$content = $content.Remove($startIndex, $endIndex - $startIndex)
Set-Content -Path index.html -Value $content -NoNewline

# Insert into about.html
$aboutContent = Get-Content -Path about.html -Raw
$targetStr = "    <!-- ═══════════════════════════════════════`n         FOUNDER / ABOUT SECTION"
if ($aboutContent.IndexOf($targetStr) -eq -1) {
    $targetStr = "    <!-- ═══════════════════════════════════════`r`n         FOUNDER / ABOUT SECTION"
}
if ($aboutContent.IndexOf($targetStr) -eq -1) {
    Write-Host "Target string not found in about.html"
    exit
}
$aboutContent = $aboutContent.Replace($targetStr, $section + "`n" + $targetStr)
Set-Content -Path about.html -Value $aboutContent -NoNewline

Write-Host "Success"
