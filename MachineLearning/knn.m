function [y] = knn(x_train, y_train, k, x)

% Assume that x_train is mxn, where m is the number of examples and n is the number of dimensions
% This is an O(n*k) implementation, where n = number of training examples

closest_k = zeros(1,k);
closest_k_distances = ones(1,k) * 999999;

for i = 1:size(x_train,1)
    distance = norm(x_train(i,:) - x);
    if distance <= closest_k_distances(end)
        for j=1:k
    	    if distance <= closest_k_distances(j)
	       closest_k_distances(j+1:end) = closest_k_distances(j:end-1);
	       closest_k_distances(j) = distance;
	       closest_k(j+1:end) = closest_k(j:end-1);
	       closest_k(j) = i;
	       break 
	    end
	end
    end
end

closest_k
closest_k_distances

class_sum = 0;
for i = 1:k
  class_sum += y_train( closest_k(i) ); 
end

y = class_sum / abs(class_sum); 


end




