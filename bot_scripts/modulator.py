import os
from datetime import datetime

with open("logB.txt", "r") as log:
    entries = log.readlines()
last_15min = [line for line in entries if "Flip to" in line]
flip_count = len(last_15min)

with open("meta_activity.txt", "a") as meta:
    meta.write(f"{datetime.now()}: flips={flip_count}\n")
