@echo off
for /l %%i in (84,1,88) do (
    pipenv run you-get  https://www.bilibili.com/video/BV1et411b73Z?p=%%i
)
pause