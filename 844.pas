program prog844;
 
var a, b:real;
 
begin
read(a, b);
if Frac(sqrt(a*b)) = 0 then
  write(sqrt(a*b))
else write(0);
end.