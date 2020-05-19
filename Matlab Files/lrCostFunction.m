function [J, grad] = lrCostFunction(theta, X, y, lambda)

%LRCOSTFUNCTION Compute cost and gradient for logistic regression with 
%regularization
%   J = LRCOSTFUNCTION(theta, X, y, lambda) computes the cost of using
%   theta as the parameter for regularized logistic regression and the
%   gradient of the cost w.r.t. to the parameters. 

% Initialize some useful values
m = length(y); % number of training examples

J = 0;
grad = zeros(size(theta));

J = -1/m * sum((y'*log(sigmoid(X*theta)) + (1-y')*(log(1-sigmoid(X*theta))))) ...
    + (lambda/(2*m)) * sum(theta(2:end,1).^2);

unRegularizedGrad = 1/m * (X'*(sigmoid(X*theta)-y)); 
grad(1,1) = unRegularizedGrad(1,1);
grad(2:end) = unRegularizedGrad(2:end) + (lambda/m * theta(2:end));

% =============================================================
%turns matrix into a vector by putting all columns under first one
grad = grad(:);

end
