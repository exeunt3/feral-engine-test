with open("stateA.txt", "r") as f:
    state = f.read().strip()
with open("logB.txt", "a") as log:
    log.write(f"Flip to {state}\n")
with open("logB.txt", "r") as log:
    lines = log.readlines()
if len(lines) % 2 == 0:
    reverted_state = "1" if state == "0" else "0"
    with open("stateA.txt", "w") as f:
        f.write(reverted_state)