program prog697;
var L, W, H, x:integer;
 
begin
readln(L, W, H);

x := ((L*H)+(W*H))*2;
if x mod 16 > 0 then
  writeln((x div 16)+1)
else
  write(x div 16);
end.