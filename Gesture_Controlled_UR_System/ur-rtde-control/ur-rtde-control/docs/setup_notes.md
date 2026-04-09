# Setup Notes

## Goal

Get a clean RTDE connection working before adding bigger control logic.

## Core pieces

You need:
- robot reachable by IP
- RTDE Python library installed
- Python environment confirmed
- safe robot test conditions

## Install example

```bash
pip3 install ur-rtde
```

## Good first checks

Before running motion code, confirm:
- you can ping the robot
- the script uses the correct IP
- the correct Python environment has the RTDE package installed
