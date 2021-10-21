program prog14;
 
var N, M, i, x:integer;
 
begin
read(N, M);
for i := 1 to N*M do
  begin
  x := N*i;
  if x mod M = 0 then
    begin
    writeln(x);
    break;
    end;
    end;
