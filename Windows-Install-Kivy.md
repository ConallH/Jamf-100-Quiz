Commands to install Kivy on Windows

```batch
@ECHO OFF

REM Install dependencies
python -m pip install --upgrade pip setuptools wheel
python -m pip install docutils pygments pypiwin32 kivy.deps.sdl2 kivy.deps.glew

REM Install Kivy
python -m pip install kivy
```