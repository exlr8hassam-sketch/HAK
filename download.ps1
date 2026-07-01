$domains = @("rivaj.com.pk", "goldenpearl.com.pk", "garnierusa.com", "missrose.com.pk", "adidas.com", "unilever.com", "johnsonsbaby.com", "mothercare.com", "macley.pk", "heavenbeauty.pk", "fairmenz.pk", "skinwhite.com.ph", "sadoer.com", "parleycosmetics.com")
New-Item -ItemType Directory -Force -Path "logos" | Out-Null
foreach ($d in $domains) {
    try {
        Invoke-WebRequest -Uri "https://logo.clearbit.com/$d" -OutFile "logos\$d.png" -UserAgent "Mozilla/5.0" -UseBasicParsing
        Write-Host "Downloaded $d"
    } catch {
        Write-Host "Failed $d"
    }
}
