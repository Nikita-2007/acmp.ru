program prog26;
 
var x1, x2, y1, y2, r1, r2, g:real;

begin
readln(x1, y1, r1);
readln(x2, y2, r2);
g := Sqrt(Sqr(x1-x2)+Sqr(y1-y2));
if (g <= r1+r2) and (g >= Abs(r1-r2)) then
  writeln('YES')
else
  writeln('NO');
end.