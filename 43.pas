program prog43;
var s, maxi:integer;
          N:string;

begin
  read(N);
  for var i := 1 to Length(N) do
    begin
    	if copy(N, i, 1) = '0' then
      begin
    		s := s + 1;
    		maxi := Max(s, maxi);
    	end
    	else
        s := 0;
    end;
  write(maxi);
end.