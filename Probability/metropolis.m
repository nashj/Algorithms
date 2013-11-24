function [out] = metropolis(num_samples)
	 % The MCMC Metropolis method for generating samples from an arbitrary probability distribution
	 % This algorithm is useful when you lack an analytic expression for the CDF, 
	 % which you could otherwise use in the Smirnov transform to generate samples
	 
	 samples = zeros(1, num_samples);
	 
	 % Choose a random initial point
	 x = .2;

	 % Generate samples from the distribution
	 for i=1:num_samples	 
	 	 % Generate a new sample 
	 	 x_new = Q(x);
 
		 % Calculate the acceptance ratio
		  alpha = unnorm_pdf(x_new) / unnorm_pdf(x);
		  alpha
		  if alpha >= 1
		     fprintf("Accepted\n");
		     x = x_new;
		  else
		     r = rand;
		     if r <= alpha
		     	fprintf("Accepted\n");
		     	% accept the new point
			x = x_new;
		     else
		     	fprintf("Rejected\n");
		        x = x;	
		     end
		  end
		  samples(i) = x;
	 end
	 out = samples;
end

function [out] = Q(x)
	 % Q is called the proposal density or jumping density
	 % Q is an arbitrary probability density that must be symmetric
	 % Here, we're using the Gaussian distribution, which is pretty standard
	 % for Metropolis algorithms. 
	 sigma = .3;
	 out = normrnd(x, sigma);
end	

%function [out] = unnorm_pdf(x)
%	 out = exp(-x^4);
	 % Integrates to about 1.8128
%end

function [out] = unnorm_pdf(x)
	 % Function that is proportional to the pdf we wish to sample from	
	 % Note that the integral of the function does not need to equal 1,
	 % because we only use the value of this function in ratios that 
	 % divide out the normalization factor

	 % This function will model the pdf of a beta distribution	 
	 alpha = 2;
	 beta = 5;
	 if x < 0
	    out = 0;
	 elseif x > 1
	    out = 0
	 else 
	    out = (x^(alpha-1) * (1-x)^(beta-1));
	    % We're ignoring the beta constant because this function doesn't need to be normalized
	 end

end