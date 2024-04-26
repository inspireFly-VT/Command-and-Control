clc;
clear;
M = 8;
n = 2^M - 1; %codeword length
k = 207; %message length
nwords = 1; %number of words to encode
msgTx = gf([1 0 1 0]);
t = bchnumerr(n,k)
enc = bchenc(msgTx, n, k);
msgRx = bchdec(enc, n, k);

