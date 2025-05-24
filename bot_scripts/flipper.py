import time
from datetime import datetime

# Read config
with open("flipper_config.txt", "r") as cfg:
    config_line = cfg.read().strip()
interval = float(config_line.split("=")[1].strip())

# Read perturbation times
with open("perturbation_times.txt", "r") as f:
    perturb_times = [float(line.strip()) for line in f.readlines()]

# Track elapsed time from file
start_time_path = "start_time.txt"
try:
    with open(start_time_path, "r") as f:
        start_time = float(f.read().strip())
except FileNotFoundError:
    start_time = time.time()
    with open(start_time_path, "w") as f:
        f.write(str(start_time))

elapsed = time.time() - start_time

# Check for perturbation (within 0.1s tolerance)
perturbed = any(abs(elapsed - pt) < 0.1 for pt in perturb_times)

# Read and flip state
with open("stateA.txt", "r") as f:
    state = f.read().strip()

# If perturbed, force a flip to "1" to destabilize pattern
if perturbed:
    new_state = "1"
else:
    new_state = "1" if state == "0" else "0"

with open("stateA.txt", "w") as f:
    f.write(new_state)

print(f"Flipper: elapsed={elapsed:.2f}, perturbed={perturbed}, new_state={new_state} (interval: {interval}s)")

time.sleep(interval)
