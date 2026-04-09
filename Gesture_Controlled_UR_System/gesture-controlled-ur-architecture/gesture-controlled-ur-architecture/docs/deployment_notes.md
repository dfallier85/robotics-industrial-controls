# Deployment Notes

## Key things to document

- camera used
- lighting conditions
- host device
- robot IP
- Python environment
- RTDE package version if important
- gesture thresholds
- deadman configuration
- workspace limits

## Why this matters

A system like this depends on more than one script.

It depends on:
- runtime setup
- environment
- robot state assumptions
- camera placement
- config values

If those are undocumented, the project becomes hard to rerun.
