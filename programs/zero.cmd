@echo off
setlocal enabledelayedexpansion
for %%a in (%1) do (
      fsutil file setzerodata offset=0 length=%%~za %%a
  )
  endlocal
