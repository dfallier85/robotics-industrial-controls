(*
    structured_text_example.st
    Example PLC handshake logic for one robot cell using:
    - command byte
    - valid bit
    - ACK toggle detection
    - timeout counter
    - heartbeat bit

    This is example logic and may need to be adapted for your PLC brand and tag names.
*)

VAR
    (* Global / incoming command interface *)
    Cmd_Target         : USINT;
    Cmd_Code           : USINT;
    Cmd_Valid          : BOOL;

    (* Cell-specific command handling *)
    Fanuc_Target_ID    : USINT := 1;
    Fanuc_Cmd          : USINT;
    Fanuc_Cmd_Active   : BOOL;

    (* ACK handling *)
    Fanuc_ACK          : BOOL;   (* Input from robot *)
    Fanuc_Ack_Last     : BOOL;   (* Stored previous ACK state *)
    Fanuc_Ack_Edge     : BOOL;   (* True for one scan when ACK changes *)

    (* Timeout handling *)
    Fanuc_NoAck_Count  : INT;
    Fanuc_Tx_Timeout   : BOOL;
    Fanuc_Timeout_Limit: INT := 25;   (* 25 scans @ 20 ms = 500 ms *)

    (* Heartbeat handling *)
    Heartbeat_Bit      : BOOL;
    Heartbeat_Count    : INT;
    Heartbeat_Limit    : INT := 25;   (* 500 ms at 20 ms task time *)
END_VAR


(* ------------------------------------------------------------ *)
(* 1) Route command to Fanuc if target matches and valid is set *)
(* ------------------------------------------------------------ *)
IF Cmd_Valid AND (Cmd_Target = Fanuc_Target_ID) AND NOT Fanuc_Cmd_Active THEN
    Fanuc_Cmd := Cmd_Code;
    Fanuc_Cmd_Active := TRUE;

    (* Reset timeout state when a new command is issued *)
    Fanuc_NoAck_Count := 0;
    Fanuc_Tx_Timeout := FALSE;
END_IF;


(* ---------------------------------------- *)
(* 2) Detect either edge of the robot ACK   *)
(* ---------------------------------------- *)
Fanuc_Ack_Edge := (Fanuc_ACK <> Fanuc_Ack_Last);


(* ------------------------------------------------------ *)
(* 3) If command is active and ACK edge happens, clear it *)
(* ------------------------------------------------------ *)
IF Fanuc_Cmd_Active AND Fanuc_Ack_Edge THEN
    Fanuc_Cmd_Active := FALSE;
    Fanuc_NoAck_Count := 0;
    Fanuc_Tx_Timeout := FALSE;
END_IF;


(* ------------------------------------------------------- *)
(* 4) If command is active and no ACK yet, count for fault *)
(* ------------------------------------------------------- *)
IF Fanuc_Cmd_Active THEN
    IF NOT Fanuc_Ack_Edge THEN
        Fanuc_NoAck_Count := Fanuc_NoAck_Count + 1;
    END_IF;

    IF Fanuc_NoAck_Count >= Fanuc_Timeout_Limit THEN
        Fanuc_Tx_Timeout := TRUE;
    END_IF;
END_IF;


(* ----------------------------------------------- *)
(* 5) Store current ACK state for next scan compare *)
(* ----------------------------------------------- *)
Fanuc_Ack_Last := Fanuc_ACK;


(* ----------------------------------- *)
(* 6) Simple heartbeat toggle example  *)
(* ----------------------------------- *)
Heartbeat_Count := Heartbeat_Count + 1;

IF Heartbeat_Count >= Heartbeat_Limit THEN
    Heartbeat_Bit := NOT Heartbeat_Bit;
    Heartbeat_Count := 0;
END_IF;
