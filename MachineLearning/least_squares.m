function [theta] = least_squares(X, Y)
% Assume that X is nxd, where n is the number of examples and d is the dimension
% Y is an nx1 training label vector

Xb = [ones(size(X,1), 1) X]; # Add ones for the bias term
theta = inv(Xb' * Xb) * Xb' * Y;

end
