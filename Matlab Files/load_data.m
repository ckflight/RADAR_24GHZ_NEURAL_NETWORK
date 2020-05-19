% X is training set array
% y is class assignment of each training set data
% Z is test set array
% t is class assignment of each test set data

function [X, y, Z, t] = load_data()

clear;clc;

% I will use 25 of each type as training set and 5 for test data
MAX_SIZE_EACH_TYPE = 30;
TESTSET_SIZE_EACH_TYPE = 15;
TRAININGSET_SIZE_EACH_TYPE = MAX_SIZE_EACH_TYPE - TESTSET_SIZE_EACH_TYPE;
NUMBER_OF_TYPE = 3;

TRAINING_SET_SIZE = TRAININGSET_SIZE_EACH_TYPE * NUMBER_OF_TYPE; 
TEST_SET_SIZE = TESTSET_SIZE_EACH_TYPE * NUMBER_OF_TYPE; 

all_results = load('/radar_result/abs_result.txt');

% Training set
X = [all_results(1:15,:); all_results(31:45,:); all_results(61:75,:)];

y = zeros(TRAINING_SET_SIZE,1);

% Test set
Z = [all_results(16:30,:); all_results(46:60,:); all_results(76:90,:)];

t = zeros(TESTSET_SIZE_EACH_TYPE * NUMBER_OF_TYPE,1);

for i = 1:TRAINING_SET_SIZE
    
    if i <= TRAININGSET_SIZE_EACH_TYPE
        y(i,1) = 1;
    elseif i > TRAININGSET_SIZE_EACH_TYPE && i <= TRAININGSET_SIZE_EACH_TYPE * 2
        y(i,1) = 2;
    else
        y(i,1) = 3;
    end
end

for i = 1:TEST_SET_SIZE
    
    if i <= TESTSET_SIZE_EACH_TYPE
        t(i,1) = 1;
    elseif i > TESTSET_SIZE_EACH_TYPE && i <= TESTSET_SIZE_EACH_TYPE * 2
        t(i,1) = 2;
    else
        t(i,1) = 3;
    end
end









