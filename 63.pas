program prog05;
 
var x, y, S, P:integer;
 
begin
readln(S, P);
  for x := 1 to 1000 do
  begin
  if (x-1 + y = S) and ((x-1) * y = P) then
    break;
  for y := 1 to 1000 do
    begin
      if (x + y = S) and (x * y = P) then
        break;
    end;
  end;
writeln(x-1, ' ', y);
end.