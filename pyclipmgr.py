import platform
import os
import subprocess

def copy(text):
    if platform.system() == "Linux" :

        if os.getenv('WAYLAND_DISPLAY'):
            os.system(f'echo "{text}" | wl-copy')

        else:
            os.system(f'echo "{text}" | xclip -selection clipboard')

    elif platform.system() == "Darwin":
        os.system(f'echo "{text}" | pbcopy')

    elif platform.system() == "Windows":
        os.system(f'echo "{text}" | clip')

def run_command(command):
   
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    if result.returncode == 0:
        return result.stdout.strip()
    else:
        raise RuntimeError(f"Command '{command}' failed with exit code {result.returncode}")

def paste():
    if platform.system() == "Linux" :

        if os.getenv('WAYLAND_DISPLAY'):
            text = run_command('wl-paste')

        else:
            text = run_command('xclip -o -selection clipboard')

    elif platform.system() == "Darwin":
        text = run_command('pbpaste')

    elif platform.system() == "Windows":
        text = run_command('echo | clip')
    
    return text