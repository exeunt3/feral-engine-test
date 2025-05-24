import time

with open("flipper_config.txt", "r") as cfg:
    config_line = cfg.read().strip()
interval = float(config_line.split("=")[1].strip())

with open("stateA.txt", "r") as f:
    state = f.read().strip()
new_state = "1" if state == "0" else "0"
with open("stateA.txt", "w") as f:
    f.write(new_state)

time.sleep(interval)