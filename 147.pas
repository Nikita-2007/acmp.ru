program prog147;
  
var n,a,b,r:int64;
  
begin
readln(N);
a := 1;
b := 1;
for var i := 1 to n do
begin
  a := b;
  b := r;
  r := a+b;
end;
writeln(r)
end.