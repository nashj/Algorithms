function [out] = kernel_kmeans(X, K) % , kernel)
	 % Initialize the means to be random points
	 % Assume X is nxd, where n is the number of examples and d the dimensions of the data
	 % means = zeros( k, size(X,2) );
	 
	 % We can randomly assign points to clusters for initialization, but this is a bad idea because
	 % the algorithm has a strong dependence on initialization and is only capable of finding local minima
	 % http://users.cs.uoi.gr/~gtzortzi/docs/publications/Global_Kernel_K-Means_IJCNN08.pdf

	 N = size(X,1);
	 C = unidrnd( K, 1, N ); 
	 C_new = zeros( 1, N );
 	 
	 % kernel = @(x,y) (norm(x-y)^2 / 2);

	 for q = 1:15
	    % q
	    total_dist = 0;
	    for i = 1:N
	    	min_dist = realmax;
		closest_k = 0;
	    	for k=1:K
		    x = X(i,:);
		    ck = X((C==k),:);
		    m = size(ck, 1); 
		    term_two = 0;
		    term_three = 0;
		    for j=1:m
		    	term_two = term_two + kernel(x, ck(j,:));
			for l=1:m
			    term_three = term_three + kernel( ck(j,:),ck(l,:) ); 
			end
		    end
		    
		    term_two = term_two * -2 / m;
		    term_three = term_three / (m*m);
		    d = kernel(x,x) + term_two + term_three;
		    % assert(d>0)
		    if d < min_dist
		       closest_k = k;
		       min_dist = d;
		    end
		end
		total_dist = total_dist + min_dist;
 	    	C_new(i) = closest_k;
 	    end
	    % total_dist
	    if ~any(C_new - C)
	       break
	    end	       
	    C = C_new;
	    C
	 end
end


function [out] = kernel(x,y)
	 sigma = 1;
	 out = exp(norm(x-y)^2 / (2*sigma^2));
	 %out = (x * y' + 1)^8;
end