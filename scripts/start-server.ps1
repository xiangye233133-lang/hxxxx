# 启动学习工作台本地服务（工作区根目录，端口 8000）
# 用法: powershell -File scripts\start-server.ps1
$root = Split-Path -Parent $PSScriptRoot
python -m http.server 8000 --bind 0.0.0.0 --directory $root
