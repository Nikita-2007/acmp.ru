program prog07;
   
var A,B,C, min, max:integer;
   
begin
read(A, B, C);
  if (A > 100000) or (B >100000) or (C > 100000) then exit;
  if (A >= B) and (A >= C) then max := A;
  if (B >= C) and (B >= A) then max := B;
  if (C >= A) and (C >= B) then max := C;
  if (A <= B) and (A <= C) then min := A;
  if (B <= C) and (B <= A) then min := B;
  if (C <= A) and (C <= B) then min := C;
  write(max - min);
end.