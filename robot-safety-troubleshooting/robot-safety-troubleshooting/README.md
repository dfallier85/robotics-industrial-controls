# Robot Safety Troubleshooting Guide

A practical guide for troubleshooting robot safety faults in an industrial cell.

This repo is meant to capture a real troubleshooting workflow for issues like:
- door open faults
- E-stop faults
- safety relay problems
- controller-side safety input problems
- PLC or HMI reset failures

## Folder Structure

```text
robot-safety-troubleshooting/
├── README.md
├── docs/
│   ├── troubleshooting_workflow.md
│   ├── relay_testing_notes.md
│   └── controller_fault_isolation.md
├── checklists/
│   └── safety_fault_checklist.md
├── templates/
│   └── maintenance_report_template.md
└── .gitignore
```

## Core Troubleshooting Philosophy

Do not guess.

Work through the fault in layers:
1. exact symptom
2. input device
3. wiring path
4. relay / safety hardware
5. controller interpretation
6. reset logic

That structure keeps you from wasting time and helps you make defensible conclusions.

## Typical Fault Examples

- Door Opened
- Emergency Stop
- Safety Input Open
- Reset button does not clear fault
- HMI says station must be reset but sequence does not restart
- Safety relay coil has voltage but contacts do not transfer correctly

## How to Use This Repo

Start with:
- `checklists/safety_fault_checklist.md`

Then use:
- `docs/troubleshooting_workflow.md`
- `docs/relay_testing_notes.md`
- `docs/controller_fault_isolation.md`

If you need to hand results to a supervisor or maintenance lead, use:
- `templates/maintenance_report_template.md`

## Author Notes

This repo is meant to capture real industrial troubleshooting habits in a clean format.
It is not a substitute for site safety rules, manuals, or lockout/tagout procedures.
Always follow plant policy and approved safety practices before testing anything.
