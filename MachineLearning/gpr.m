function [guess, guess_var] = gpr(X,Y,sigma,beta, x_star)
% Gaussian Process Regression, adapted from http://www.robots.ox.ac.uk/~mebden/reports/GPtutorial.pdf
% X is an nxd, n examples and d dimensions
% Y is an nx1
% sigma is the smoothing factor / gaussian kernel variance
% beta is an nx1 representing the error variance for each Y

% Output is guess
% Uncertainty of guess is captured as variance by guess_var 

N = size(X,1);

K = zeros(N,N);
K_star = zeros(1,N);
for i=1:N
    for j=1:N
    	K(i,j) = kernel(X(i,:), X(j,:), sigma);
	if i==j
	   K(i,j) = K(i,j) + beta(i);
	end
    end
    K_star(1,i) = kernel(x_star, X(i,:), sigma);
end

K_star_star = kernel(x_star, x_star, sigma);

guess = K_star * inv(K) * Y;
guess_var = K_star_star - K_star * inv(K) * K_star';

end


function [out] = kernel(x,y,sigma)
	out = normpdf(x-y, 0, sigma);
end