program prog803;

var
  A, B, K, x, i: integer;

begin
  readln(A, B, K);
  for i := 1 to K do
  begin
    A := A mod B*10;
  end;
  writeln(A div B);
end.