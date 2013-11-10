function [theta] = weighted_least_squares(X, Y, sigma_sq)
% Assume that X is nxd, where n is the number of examples and d is the dimension
% Y is an nx1 training label vector
% sigma_sq is an nx1 vector of the 'weight' or error variances for each target variable

W = diag(1 ./ sigma_sq);
Xb = [ones(size(X,1), 1) X]; # Add ones for the bias term
theta = inv(Xb' * W * Xb) * Xb' * W * Y;

end
