program prog691;

var
normsim: string = 'ABCEHKMOPTXY';
normnum: string = '0123456789';
      s: string;
      t: integer;

begin
readln(t);
for var i := 1 to t do
  begin
  readln(s);
	if (Length(s) = 6) and
	  (copy(s, 1, 1)  in normsim) and
	  (copy(s, 5, 1) in normsim) and
	  (copy(s, 6, 1) in normsim) and
	  (copy(s, 2, 1) in normnum) and
	  (copy(s, 3, 1) in normnum) and
	  (copy(s, 4, 1) in normnum) then
		writeln('Yes')
	else
		writeln ('No');
	end;
end.