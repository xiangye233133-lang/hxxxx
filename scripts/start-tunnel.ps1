# 通过 Cloudflare Quick Tunnel 将本地 8000 端口暴露到公网
# 用法: powershell -File scripts\start-tunnel.ps1
# 首次运行会自动下载 cloudflared 到 .tools\（已存在则跳过）
$root = Split-Path -Parent $PSScriptRoot
$exe = Join-Path $root ".tools\cloudflared.exe"
if (-not (Test-Path $exe)) {
    New-Item -ItemType Directory -Force -Path (Join-Path $root ".tools") | Out-Null
    Invoke-WebRequest -Uri "https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-windows-amd64.exe" -OutFile $exe
}
& $exe tunnel --url http://localhost:8000 --no-autoupdate
