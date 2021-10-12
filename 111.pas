program prog893;
 
var N:int64;
 
begin
  read(N);
  if N < 3 then
    writeln(N)
  else
    writeln(N*(N-1)*(N-2));
end.