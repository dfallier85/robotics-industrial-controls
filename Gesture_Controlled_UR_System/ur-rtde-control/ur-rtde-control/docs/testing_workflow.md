# Testing Workflow

## Step 1: Confirm package import

Make sure the RTDE library imports in the environment you plan to use.

## Step 2: Confirm network reachability

Ping the robot and verify the correct IP is in the script.

## Step 3: Run receive-only checks first

Confirm the script can connect and read:
- robot mode
- safety mode

## Step 4: Run very small motion test

If appropriate and safe, run the small motion example and verify:
- motion begins as expected
- motion stops cleanly
- no unexpected faults occur

## Step 5: Document the working setup

Write down:
- robot IP
- environment used
- package version if important
- what test motion succeeded
