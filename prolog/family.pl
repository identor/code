father(X, Y) :- 
	male(X), parent(X, Y).

mother(X, Y) :-
	female(X), parent(X, Y).

sibbling(X, Y) :-
	parent(Z, X), parent(Z, Y).

parent(papaBear, teddyBear).
parent(papaBear, gummyBear).
parent(mamaBear, teddyBear).
parent(mamaBear, gummyBear).
male(papaBear).
female(mamaBear).