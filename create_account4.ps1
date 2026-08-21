$lines = Get-Content -Path about.html

$mainIndex = -1
for ($i = 0; $i -lt $lines.Length; $i++) {
    if ($lines[$i] -match '<main id="main-content">') {
        $mainIndex = $i
        break
    }
}

$footerIndex = -1
for ($i = $mainIndex; $i -lt $lines.Length; $i++) {
    if ($lines[$i] -match 'FOOTER \(dark teal variant\)') {
        $footerIndex = $i - 1
        break
    }
}

if ($mainIndex -eq -1 -or $footerIndex -eq -1) {
    Write-Host "Failed to find main or footer"
    exit
}

$headContent = $lines[0..$mainIndex] -join "`r`n"
$footerContent = $lines[$footerIndex..($lines.Length - 1)] -join "`r`n"

$accountMain = @"

    <style>
      .account-section {
        padding: 100px 0 var(--space-20);
        background: #F7F5F0;
        min-height: calc(100vh - 200px);
        display: flex;
        align-items: center;
      }
      .account-grid {
        display: grid;
        grid-template-columns: 1fr 1fr;
        gap: var(--space-12);
        max-width: 900px;
        margin: 0 auto;
        background: #FFFFFF;
        padding: var(--space-10);
        border-radius: var(--radius-md);
        box-shadow: 0 12px 40px rgba(0,0,0,0.06);
      }
      .account-col {
        display: flex;
        flex-direction: column;
        gap: var(--space-6);
      }
      .account-col-title {
        font-size: var(--text-lg);
        font-weight: 800;
        color: var(--color-ink);
        margin-bottom: var(--space-2);
      }
      .divider-line {
        width: 1px;
        background: var(--color-border);
        margin: 0 -calc(var(--space-6) + 1px);
      }
      @media (max-width: 768px) {
        .account-grid {
          grid-template-columns: 1fr;
          padding: var(--space-6);
        }
        .divider-line {
          width: 100%;
          height: 1px;
          margin: var(--space-6) 0;
        }
      }
    </style>

    <section class="account-section">
      <div class="container">
        <div class="account-grid reveal">
          
          <!-- Login -->
          <div class="account-col">
            <div>
              <h2 class="account-col-title">Sign In</h2>
              <p class="contact-subtext" style="font-size:var(--text-sm);">Welcome back to your Rapid Epoxy account.</p>
            </div>
            
            <form>
              <div class="fc-group">
                <label class="fc-label" for="loginEmail">Email Address</label>
                <input type="email" id="loginEmail" class="fc-input" required>
              </div>
              <div class="fc-group" style="margin-top:var(--space-4);">
                <label class="fc-label" for="loginPassword">Password</label>
                <input type="password" id="loginPassword" class="fc-input" required>
              </div>
              <button type="submit" class="btn btn-gold" style="width:100%; margin-top:var(--space-6); justify-content:center;">Sign In</button>
            </form>
          </div>

          <div class="divider-line"></div>

          <!-- Registration -->
          <div class="account-col">
            <div>
              <h2 class="account-col-title">Create Account</h2>
              <p class="contact-subtext" style="font-size:var(--text-sm);">Register to manage your quotes and warranty documents.</p>
            </div>
            
            <form>
              <div class="fc-group">
                <label class="fc-label" for="regName">Full Name</label>
                <input type="text" id="regName" class="fc-input" required>
              </div>
              <div class="fc-group" style="margin-top:var(--space-4);">
                <label class="fc-label" for="regEmail">Email Address</label>
                <input type="email" id="regEmail" class="fc-input" required>
              </div>
              <div class="fc-group" style="margin-top:var(--space-4);">
                <label class="fc-label" for="regPassword">Password</label>
                <input type="password" id="regPassword" class="fc-input" required>
              </div>
              <button type="submit" class="btn btn-outline-gold" style="width:100%; margin-top:var(--space-6); justify-content:center;">Create Account</button>
            </form>
          </div>

        </div>
      </div>
    </section>

  </main>
"@

$headContent = $headContent -replace "<title>.*</title>", "<title>Rapid Epoxy - My Account</title>"
$headContent = $headContent -replace '(?s)    /\* ════════════════════════════════════════\s*ABOUT PAGE — specific styles(.*?)</style>', "</style>"

$fullContent = $headContent + "`r`n" + $accountMain + "`r`n" + $footerContent
Set-Content -Path "account.html" -Value $fullContent -NoNewline
Write-Host "Created account.html"
