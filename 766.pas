program prog05;
 
var N,M,K,X:integer;
 
begin
read(N, M, K);
X := N*M;
if X >= K then write('YES')
else write('NO');
end.