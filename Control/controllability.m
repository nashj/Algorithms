function [C] = controllability(A,B)
% Currently only works with nx1 B matrix

C = zeros(size(B,1), size(A,2));

C(:,1:size(B,2)) = B;
for i=2:size(A,2)
	C(:,i) = A * C(:,i-1);
end

end
