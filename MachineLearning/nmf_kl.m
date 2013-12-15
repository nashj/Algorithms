function [W,H] = nmf_kl(V, k, max_iter, threshold)
% This is the multiplicative update rules for NMF, proposed by Seung
  more off;

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
      
      % Update H
      Hnew = H;
      WH = W*H;
      for a=1:size(H,1)
      	  for mu=1:size(H,2)
	      num_sum = 0;
	      for i = 1:size(W,1)
	      	  num_sum = num_sum + W(i,a) * V(i,mu) / WH(i,mu);
	      end
	      denom_sum = 0;
	      for k=1:size(W,1)
	      	  denom_sum = denom_sum + W(k,a);
	      end      
	      Hnew(a,mu) = H(a,mu) * num_sum / denom_sum;
	  end
      end
      H = Hnew;
      
      % Update W
      Wnew = W;
      WH = W*H;
      for i=1:size(W,1)
      	  for a=1:size(W,2)
	      num_sum = 0;
	      for mu=1:size(H,2)
	      	  num_sum = num_sum + H(a,mu) * V(i,mu) / WH(i,mu);
	      end
	      denom_sum = 0;
	      for v=1:size(H,2)
	      	  denom_sum = denom_sum + H(a,v);
	      end
	      Wnew(i,a) = W(i,a) * num_sum / denom_sum;
	  end
      end
      W = Wnew;
 
      % Compute the KL divergence
      KL_div = kldiv(V,W*H);
      if KL_div < threshold
      	 break	 
      end
      fprintf('KL divergence: %g\n\n', KL_div);
  end

end


function [sum] = kldiv(A, B)
% Formula adapted from Seung and Lee 2001
% Assumes size(A) == size(B)
% Note that kldiv is not a symmetric function, kldiv(A,B) != kldiv(B,A)
  sum = 0;
  for i=1:size(A,1)
      for j=1:size(A,2)
      	  term = A(i,j) * log(A(i,j)/B(i,j) + 1.0e-9) - A(i,j) + B(i,j);
      	  sum = sum + term;
      end
  end
end

