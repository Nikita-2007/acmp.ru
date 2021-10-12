program prog05;
  
var A,B:integer;
  
begin
read(A);
read(B);
if A>B then write('>')
else if A<B then write('<')
else write('=');
end.