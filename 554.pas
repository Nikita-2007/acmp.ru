program prog554;
 
var N, s, i:integer;
 
begin
s := 1;
readln(N);
for i := 0 to N do
  s := s + i;
writeln(s);
end.