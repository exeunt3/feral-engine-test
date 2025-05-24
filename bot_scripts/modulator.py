from datetime import datetime

with open("logB.txt", "r") as log:
    entries = log.readlines()
flip_count = len([line for line in entries if "Flip to" in line])

with open("meta_activity.txt", "a") as meta:
    meta.write(f"{datetime.now()}: flips={flip_count}\n")

# Simple modulation: adjust flipper timing below 1s if active
interval = 1.0 if flip_count < 10 else 0.5 if flip_count < 20 else 0.2

with open("flipper_config.txt", "w") as cfg:
    cfg.write(f"active_interval = {interval}\n")
