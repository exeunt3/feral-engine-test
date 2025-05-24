with open("stateA.txt", "r") as f:
    state = f.read().strip()
new_state = "1" if state == "0" else "0"
with open("stateA.txt", "w") as f:
    f.write(new_state)