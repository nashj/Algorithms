function [out] = multivariate_normal(mu, Sigma)
% mu is the mean for the multivariate normal distribution, Sigma is the covariance matrix

% To sample from an arbitrary multivariate normal distribution, we use a routine for normal, zero mean, unit variance samples
% Let x ~ N(0,I)
% Let y = mu + Sigma_sqrt * x
% Then E[y] = mu
% And var[y] = E[(y-E[y])^2] = E[(mu + Sigma_sqrt*x - mu)^2] = E[(Sigma_sqrt*x)' * (Sigma_sqrt*x)]
%     	     = Sigma_sqrt*E[xx']*Sigma_sqrt' = Sigma_sqrt * Sigma_sqrt' = Sigma

dim = length(mu);
Sigma_sqrt = chol(Sigma);
out = mu + Sigma_sqrt * randn(dim,1);

end

