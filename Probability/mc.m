function [out] = mc
	% Monte Carlo integration method
	% Generate samples from a uniform distribution over the integral bounds
	% Use law of large numbers to treat the integral as an expectation with
	% respect to a uniform distribution	 

	% Integrate exp(-x^4) over -10 to 10
	a = -10;
	b =  10;
	num_samples = 10000;
	
	sum_val = 0;
	for i=1:num_samples
	    r = unifrnd(a,b);
	    sum_val = sum_val + test_fxn(r);
	end
	out = sum_val / num_samples * (b - a);
end

function [out] = test_fxn(x)
	out = exp(-(x^4));
end

