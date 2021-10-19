program prog529;
 
var x1, x2, y1, y2, kat1, kat2, g:real;
 
begin
read(x1, y1, x2, y2);
kat1 := abs(x1-x2);
kat2 := abs(y1-y2);
g := sqrt((kat1*kat1)+(kat2*kat2));
write(g:0:5)
end.