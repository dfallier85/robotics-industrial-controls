(*
structured_text_handshake_example.st

Starter Structured Text example for a PLC-to-robot command handshake.

This is intentionally simple and readable.
Adapt tag names, timeout counters, and bit mapping to your platform.
*)

VAR
    PLC_Cmd_Code       : USINT;
    PLC_Cmd_Valid      : BOOL;

    Robot_Cmd_Code     : USINT;
    Robot_Cmd_Active   : BOOL;

    Robot_Ack          : BOOL;
    Robot_Ack_Last     : BOOL;
    Robot_Ack_Edge     : BOOL;

    Robot_Busy         : BOOL;
    Robot_Done         : BOOL;
    Robot_Fault        : BOOL;

    Ack_Timeout_Count  : INT;
    Ack_Timeout_Limit  : INT := 25;   (* Example: 25 scans *)
    Ack_Timeout        : BOOL;
END_VAR


(* Load a new command into the robot-facing interface *)
IF PLC_Cmd_Valid AND NOT Robot_Cmd_Active THEN
    Robot_Cmd_Code := PLC_Cmd_Code;
    Robot_Cmd_Active := TRUE;

    Ack_Timeout_Count := 0;
    Ack_Timeout := FALSE;
END_IF;


(* Detect ACK edge *)
Robot_Ack_Edge := (Robot_Ack <> Robot_Ack_Last);


(* Clear active command when ACK is observed *)
IF Robot_Cmd_Active AND Robot_Ack_Edge THEN
    Robot_Cmd_Active := FALSE;
    Ack_Timeout_Count := 0;
    Ack_Timeout := FALSE;
END_IF;


(* Count timeout if command is active and no ACK seen yet *)
IF Robot_Cmd_Active THEN
    IF NOT Robot_Ack_Edge THEN
        Ack_Timeout_Count := Ack_Timeout_Count + 1;
    END_IF;

    IF Ack_Timeout_Count >= Ack_Timeout_Limit THEN
        Ack_Timeout := TRUE;
    END_IF;
END_IF;


(* Store current ACK for next scan *)
Robot_Ack_Last := Robot_Ack;
