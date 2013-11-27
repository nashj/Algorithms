function [out] = multivariate_normal_conditional(mu, Sigma, conditioning_vars, conditioned_values) 
% Expects conditioned_vars to be a vector of variable indices, i.e. [1 2 4 6] indicating x1, x2, x4, x6 conditioned on the other variables
% Conditioned values will then correspond to concrete values for x3, x5, x7, x8, etc.
num_cond_vars = length(conditioning_vars);

% Permute conditioning_vars to the front 
permuted_mu = mu;
permuted_Sigma = Sigma;
for i=1:num_cond_vars
    c = conditioning_vars(i);
    if i != c
       % Permute columns and rows corresponding to switched variables
       temp = permuted_Sigma(:,i);
       permuted_Sigma(:,i) = permuted_Sigma(:,c);
       permuted_Sigma(:,c) = temp;

       temp = permuted_Sigma(i,:);
       permuted_Sigma(i,:) = permuted_Sigma(c,:);
       permuted_Sigma(c,:) = temp;

       % Permute mu values 
       temp = permuted_mu(i);
       permuted_mu(i) = permuted_mu(c);
       permuted_mu(c) = permuted_mu(i);
    end
end

W = inv(permuted_Sigma);
A = W(1:num_cond_vars, 1:num_cond_vars);
B = W(1:num_cond_vars, num_cond_vars+1:end);

conditional_mu = permuted_mu(1:num_cond_vars) - inv(A) * B * (conditioned_values - permuted_mu(num_cond_vars+1:end));
out = multivariate_normal( conditional_mu, A ); 

end