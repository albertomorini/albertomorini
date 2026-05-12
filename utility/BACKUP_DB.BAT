@echo off
setlocal enabledelayedexpansion

REM === CONFIGURAZIONE ===
set DB_NAME=DBNAME
set BACKUP_DIR=D:\DBBACKUP
set SQLCMD_PATH="C:\Program Files\Microsoft SQL Server\Client SDK\ODBC\170\Tools\Binn\sqlcmd.exe"
set SERVER=.\MYINSTANCESERVER

REM === CREA CARTELLA SE NON ESISTE ===
if not exist "%BACKUP_DIR%" mkdir "%BACKUP_DIR%"

REM === DATA FORMATTATA YYYYMMDD ===
for /f "tokens=2 delims==" %%I in ('wmic os get localdatetime /value') do set datetime=%%I
set YYYY=%datetime:~0,4%
set MM=%datetime:~4,2%
set DD=%datetime:~6,2%
set DATESTAMP=%YYYY%%MM%%DD%

REM === FILE DI BACKUP ===
set BACKUP_FILE=%BACKUP_DIR%\%DB_NAME%_%DATESTAMP%.bak

REM === ESECUZIONE BACKUP ===
%SQLCMD_PATH% -S %SERVER% -U sa -P $$PSW -Q "BACKUP DATABASE [%DB_NAME%] TO DISK='%BACKUP_FILE%' WITH INIT"

IF %ERRORLEVEL% NEQ 0 (
    echo ERRORE DURANTE IL BACKUP
    exit /b 1
)

REM === CANCELLA FILE PIU VECCHI DI 5 GIORNI ===
forfiles /p "%BACKUP_DIR%" /s /m *.bak /d -5 /c "cmd /c del @path"

echo Backup completato: %BACKUP_FILE%

endlocal
pause