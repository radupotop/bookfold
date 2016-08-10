function list = edit (start,last)
	while((last/4)~=round(last/4))
		last=last+1;
	endwhile
	frontalleft = start+1;
	frontalrght = last-1;
	reverseleft = last;
	reverserght = start;
	list=[];
	while(frontalleft<=(last/2))
		list=[list frontalleft frontalrght reverseleft reverserght];
		frontalleft = frontalleft+2;
		frontalrght = frontalrght-2;
		reverseleft = reverseleft-2;
		reverserght = reverserght+2;
	endwhile
endfunction



