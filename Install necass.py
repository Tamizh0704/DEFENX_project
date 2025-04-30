import subprocess

def run_cmd(command):
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        print("Output:\n", result.stdout)
        if result.stderr:
            print("Errors:\n", result.stderr)
    except Exception as e:
        print("Exception occurred:", e)

# Fixed: All packages in one line
cmd_input = "pip install darkdetect httpx PyQt6 PyQt6-WebEngine screeninfo py-cpuinfo psutil vulners WMI getmac portscan windows_tools"
run_cmd(cmd_input)
