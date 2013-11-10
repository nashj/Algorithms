function [out] = woodbury(invA, B, C, D)
	 % Woodbury matrix identity
	 % This method is used for updating the inverse of a matrix A for A + BCD. 
	 out = invA - invA * B * inv(inv(C) * D * invA * B) * D * invA;
end
