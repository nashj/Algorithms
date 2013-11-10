function [out] = kde(X, xtest)
% X is an nxd matrix, where n is the number of samples, d is the dimension
  N = size(X,1);
  out = 0;
  for i = 1:N
      out = out + kernel(xtest, X(i,:));
  end   

  out = out / N;

end

function [out] = kernel(x, y)
	 d = length(x);
	 sig_sq = 1;
	 out = normpdf((x-y), zeros(1,d), sig_sq * eye(d)); 
end


