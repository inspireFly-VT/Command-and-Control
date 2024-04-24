clc;
clear;
M = 4;
n = 2^M - 1; %codeword length
k = 5; %message length
nwords = 1; %number of words to encode
msgTx = gf([0 1 0 0 1]);
t = bchnumerr(n,k)
enc = bchenc(msgTx, n, k);


