$avatarHtml = @"
      <!-- Header Actions -->
      <div style="display:flex; align-items:center; gap:var(--space-3);">
        <a href="about.html#contact" class="btn btn-gold">Request Quote</a>
        <!-- Avatar icon -->
        <a href="account.html" style="width:36px;height:36px;border-radius:50%;background:var(--color-teal-light);display:flex;align-items:center;justify-content:center;cursor:pointer;text-decoration:none;" aria-label="Account">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="var(--color-teal)" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"/><circle cx="12" cy="7" r="4"/>
          </svg>
        </a>
      </div>
"@

$files = @("index.html", "products.html", "services.html", "generate_pages.py")

foreach ($file in $files) {
    $content = Get-Content -Path $file -Raw
    
    # The existing target is:
    #       <!-- Header Actions -->
    #       <a href="about.html#contact" class="btn btn-gold">Request Quote</a>
    # Or something similar in generate_pages.py it has indentation. Let's match more loosely.
    
    # We can replace:
    #       <!-- Header Actions -->
    #       <a href="about.html#contact" class="btn btn-gold">Request Quote</a>
    $pattern = '(?s)      <!-- Header Actions -->\s*<a href="about\.html#contact" class="btn btn-gold">Request Quote</a>'
    
    $content = $content -replace $pattern, $avatarHtml
    Set-Content -Path $file -Value $content -NoNewline
}

# Now for about.html which already has the avatar div
$aboutContent = Get-Content -Path "about.html" -Raw
$aboutPattern = '(?s)        <!-- Avatar icon -->\s*<div style="width:36px;height:36px;border-radius:50%;background:var\(--color-teal-light\);display:flex;align-items:center;justify-content:center;cursor:pointer;" aria-label="Account">\s*<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="var\(--color-teal\)" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">\s*<path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"/><circle cx="12" cy="7" r="4"/>\s*</svg>\s*</div>'

$aboutReplacement = @"
        <!-- Avatar icon -->
        <a href="account.html" style="width:36px;height:36px;border-radius:50%;background:var(--color-teal-light);display:flex;align-items:center;justify-content:center;cursor:pointer;text-decoration:none;" aria-label="Account">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="var(--color-teal)" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"/><circle cx="12" cy="7" r="4"/>
          </svg>
        </a>
"@
$aboutContent = $aboutContent -replace $aboutPattern, $aboutReplacement
Set-Content -Path "about.html" -Value $aboutContent -NoNewline

Write-Host "Replaced navbars"
