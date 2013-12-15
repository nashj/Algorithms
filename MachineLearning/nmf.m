function [W,H] = nmf(V, k, max_iter, threshold)
% This is the multiplicative update rules for NMF, proposed by Seung
  if nargin < 3
     max_iter = 1000;
  end

  if nargin < 4
     threshold = .01;
  end

  W = rand(size(V,1), k);
  H = rand(k, size(V,2));

  % Iterate on W and H until convergence
  for i=1:max_iter % Use actual stopping criteria here
      fprintf('Update #%d:\n', i);
      
      % Apply update rule to W and H
      H = H .* ((W'*V) ./ (W'*W*H + 1e-9));
      W = W .* ((V*H') ./ (W*H*H' + 1e-9));
 
      % Compute the Frobenius norm
      S_norm = norm(V - W*H, 'fro'); % Shows how close W*H is to V
      if S_norm < threshold
      	 break	 
      end
      fprintf('S_norm: %g\n\n', S_norm);
  end

end


