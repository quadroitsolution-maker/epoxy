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
    $pattern1 = '(?s)      <!-- Header Action -->\s*<a href="about\.html#contact" class="btn btn-gold">Request Quote</a>'
    $content = $content -replace $pattern1, $avatarHtml
    Set-Content -Path $file -Value $content -NoNewline
}

Write-Host "Success"
