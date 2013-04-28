function [q] = pbh_test(A,B)
% Returns true if the system is controllable
% Does not test for observability
% Requires B to be an nx1

L = left_eig(A);

q = true;
% Check the orthogonality of each left eigenvector to the vectors in B
% If the eigenvector is orthogonal, the rank will increase
for i=1:size(L,2)
	% Test if the left eigenvector is orthogonal to B
	if (B' * L(:,i) < 1e-4)
	  q = false;
        end
end

end
