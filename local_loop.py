import time
import subprocess

while True:
    subprocess.run(["python3", "bot_scripts/flipper.py"])
    subprocess.run(["python3", "bot_scripts/reactor.py"])
    subprocess.run(["python3", "bot_scripts/modulator.py"])
    time.sleep(1)  # minimal delay between cycles
