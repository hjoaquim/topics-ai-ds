% Genealogy exercice

% facts
mother(maria,henrique).			% 1st gen
mother(maria,isabel).			% 1st gen
mother(isabel,claudia).   		% 2nd gen left
mother(isabel,ricardo).   		% 2nd gen left
mother(isabel_c,henrique_f). 	% 2nd gen right
mother(isabel_c,nadia). 		% 2nd gen right
mother(nadia,miguel).			% 3rd gen
mother(nadia,leonor).			% 3rd gen

father(narciso,henrique).		% 1st gen
father(narciso,isabel).			% 1st gen
father(leonardo,claudia). 		% 2nd gen left
father(leonardo,ricardo). 		% 2nd gen left
father(henrique,henrique_f).	% 2nd gen right
father(henrique,nadia).			% 2nd gen right
father(louis,miguel).			% 3rd gen
father(louis,leonor).			% 3rd gen

died(narciso).
died(maria).

% rules
grand_parent(X,Y):-
    ( father(X,A),father(A,Y) );
    ( mother(X,A),mother(A,Y) ).

grand_child(X,Y):-
    son(X,A),son(A,Y).

parent(X,Y):-
    mother(X,Y);father(X,Y).

sibling(X,Y):-
    (father(A,X),father(A,Y);mother(A,X))
    ,mother(A,Y),X\==Y.

uncle(X,Y):-
    sibling(X,A),mother(A,Y);sibling(X,A),father(A,Y).

son(X,Y):-
    father(Y,X);mother(Y,X).

has_parents(X):-
    mother(Mother,X), not(died(Mother));
	father(Father,X), not(died(Father)).

has_son(X):-
    son(Son,X), not(died(Son)).

can_inherit(X,Y):-		% X can inherit from Y if
    grand_parent(X,Y); 	% X is grandparent of Y
    mother(X,Y);		% X is mother of Y
    father(X,Y);		% X is father of Y
    uncle(X,Y);			% X is uncle of Y
    son(X,Y);			% X is son of Y
    grand_child(X,Y).	% X is grandchild of Y

inherit(X,Y):- 			% X inherit from Y if
    can_inherit(X,Y), not(died(X)),
    (grand_parent(X,Y), not(has_parents(Y)), not(has_son(Y))); 	% grandparent inherit if no parents nor sons
    (uncle(X,Y), not(has_parents(Y)), not(has_son(Y)));			% uncle inherit if no parents nor sons
    (parent(X,Y), not(has_son(Y)));								% parents inherit if no sons
    son(X,Y).