@echo off
:: 提示用户输入提交信息
set /p commit_message=请输入git commit的提交信息: 

:: 执行git add .
git add .

:: 执行git commit -m "提交信息"
git commit -m "%commit_message%"

:: 提示用户按回车键继续
echo 按回车键继续执行git push...
pause >nul

:: 执行git push
git push

:: 可视化列出git log
git log --graph --pretty=format:'%Cred%h%Creset -%C(yellow)%d%Creset %s %Cgreen(%cr) %C(bold blue)<%an>%Creset' --abbrev-commit

:: 暂停以查看结果
pause    