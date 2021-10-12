program prog05;
 
var a1,a2,a3,a4,b1,b2,b3,b4,x,y:integer;
 
begin
read(a1,b1);
read(a2,b2);
read(a3,b3);
read(a4,b4);
x := a1+a2+a3+a4;
y := b1+b2+b3+b4;
if x > y then write('1')
else if x < y then write('2')
else write('DRAW')
end.