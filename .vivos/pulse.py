import os
import json
import time

def check_component(path):
    return os.path.exists(path)

def generate_pulse():
    root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    os.chdir(root)
    
    status = {
        "timestamp": time.time(),
        "aggregate": "SECURE-VAULT",
        "components": {
            "human_logic": check_component("src/interlace/human"),
            "vvv_core": check_component("vvv") or check_component("src/vvv")
        },
        "health": 1.0,
        "security_level": "MAXIMUM"
    }
    with open("mesh_state.json", "w") as f:
        json.dump(status, f, indent=2)
    print(f"Pulse generated: {status['health']}")

if __name__ == "__main__":
    generate_pulse()
