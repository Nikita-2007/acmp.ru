program prog777;
 
var S,T:integer;
 
begin
read(S, T);
if S < T then
  write(T-S)
else
  write(T-S+12);
end.