.D0 00000000
MS 2100 00000002
MM 2000;DI
 LEA.L $002100,A1
 MOVE.L #2,-(A1)
 BSR $00002050

MM 2050;DI
 MOVE.L (A1)+,D1
 MOVE.L (A1),D2
 ADD.L D1,D2
 MOVE.L D2,D0
 RTS

.D0 00000000
.D3 00000100
.D4 00000200
.D5 00000300
MM 2000;DI
 CMP D3,D4
 BGE $002100
 CMP D3,D5
 BGE $002150
 MOVE.L D3,D0
.
MM 2100;DI
 CMP D4,D5
 BGE $002150
 MOVE.L D4,D0
.
MM 2150;DI
 MOVE.L D5,D0
.

.PC 2000
TR