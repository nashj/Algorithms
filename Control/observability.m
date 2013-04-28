function [O] = observability(A, C)
% Currently only works with 1xn C matrix

O = zeros(size(A,2), size(C,2));

O(1,:) = C;
for i = 2:size(A,2)
	  O(i,:) = O(i-1,:) * A;
end

end
