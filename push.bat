@echo off
:: ��ʾ�û������ύ��Ϣ
set /p commit_message=������git commit���ύ��Ϣ: 

:: ִ��git add .
git add .

:: ִ��git commit -m "�ύ��Ϣ"
git commit -m "%commit_message%"

:: ��ʾ�û����س�������
echo ���س�������ִ��git push...
pause >nul

:: ִ��git push
git push

:: ���ӻ��г�git log
git log --graph --pretty=format:'%Cred%h%Creset -%C(yellow)%d%Creset %s %Cgreen(%cr) %C(bold blue)<%an>%Creset' --abbrev-commit

:: ��ͣ�Բ鿴���
pause    