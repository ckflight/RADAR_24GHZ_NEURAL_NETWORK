%% Train Data and Create Theta Matrix

clear;clc;

lambda = 0.1;
numOfClass = 3;

[X, y, Z, t] = load_data();

m = size(X,1);
n = size(X,2);
X = [ones(m, 1) X];
allTheta = zeros(numOfClass , n+1);

for c = 1 : numOfClass %One vs. All
    initial_theta = zeros(n+1,1);
    options = optimset('GradObj','on','MaxIter',20);
    [theta] = fmincg(@(t)(lrCostFunction(t, X, y==c, lambda)), initial_theta, options);
    allTheta(c,:) = theta;
end

output = sigmoid(X * allTheta');
predictedY = zeros(m,1);

for i=1:m
    [~,index] = max(output(i,:),[],2);
    predictedY(i,1) = index;    
end

fprintf('\nTraining Set Accuracy: %f\n', mean(double(predictedY == y)) * 100)
save allTheta.mat allTheta;


%% Estimate New Data

load('allTheta.mat');

for i = 1 : size(t)
    
    newInput = Z(i,:);
    
    output = sigmoid(([1 newInput]) * allTheta')
    
    [~, index] = max(output(1,:),[],2);
    
    estimation_results(1,i) = index;
    
end

estimation_results



