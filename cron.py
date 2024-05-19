import os
import time
import subprocess

run_every = os.getenv('RUN_EVERY')

# Make the string to seconds
run_every = int(run_every) * 60

# Define the function to run your script
def run_script():
    subprocess.run(["/usr/local/bin/python", "/app/main.py"])

# Run the script every 5 minutes
while True:
    run_script()
    print('Script ran successfully')
    print(f'Waiting for {run_every} seconds')
    # Wait for 5 minutes before running the script again
    time.sleep(run_every)  # 300 seconds = 5 minutes