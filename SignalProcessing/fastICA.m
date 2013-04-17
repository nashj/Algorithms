function [ unmixed_signal ] = fastICA( mixed_signals )
    %FASTICA for single component extraction
    
    num_signals = size(mixed_signals,1);
    num_samples = size(mixed_signals,2);

    % We need to center and whiten the data before computing unmixing weights
    % Center the signals by subtracting the mean
    centered = mixed_signals - repmat(mean(mixed_signals,2), 1, num_samples);
    
    % Compute the covariance matrix
    cov_center = centered * centered' ./ num_samples;
    
    % Take an eigenvalue decomposition of the covariance matrix
    [E,D] = eig(cov_center);
    
    % This transformation ensures that the covariance matrix of the
    % transformed data is the identity matrix.
    whitened = D^(-1/2) * E' * centered;
    
    % Estimate the weights for the unmixing vector w
    w = ones(num_signals, 1);
    w = w ./ norm(w);
    w_old = 0;
    
    while(norm(w-w_old) > .0001)
        norm(w-w_old)
        term1 = mean(whitened .* repmat(g(w' * whitened), num_signals, 1),2);
        term2 = mean(h(w'*whitened)) * w;
        w_new = term1 - term2;
        w_old = w;
        w = w_new ./ norm(w_new);
        
    end

    % Output one of the whitened original signals. Note that this could
    % be any of the source signals and it could be scaled improperly
    unmixed_signal = w' * whitened;
    
end

function y = g(x)
    y = tanh(x);
end

function y = h(x)
    y = 1 - (tanh(x)).^(2);
end
