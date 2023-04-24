/* Question 1: 
*/ 
/* function for question one requesting 4 parameters the list of int, and will return back the first middle and last*/ 
first_middle_last(List, First, Middle, Last) :-
    
    /*calculate the length of the input list and set it to Length*/
    length(List, Length),
    
    /*calculates the index of the middle element of the list*/
    MiddleIndex is Length // 2,
    
    /* retrieve the element at index 0*/
    nth0(0, List, First),
    
    /* retrieve the middleindex element to middle */
    nth0(MiddleIndex, List, Middle),
    
    /* retrueve the last index arr length - 1*/
    nth0(Length-1, List, Last).
/**
   
?- first_middle_last([1,2,3], First, Middle, Last).
   First = 1,
   Middle = 2,
   Last = 3.
 
   
?- first_middle_last([1,2,3,4,5], First, Middle, Last).
   First = 1,
   Middle = 3,
   Last = 5
 
 
?- first_middle_last([19,25,72,9,4,15,23,19,32,41,53], First, Middle, Last).
   First = 19,
   Middle = 15,
   Last = 53.
 
*/



/* Question 2 */
/*This is the block/2 where each block(#) is connect to []*/
blocks(1, [2,3,4,5]).
blocks(2, [1,3]).
blocks(3, [1,2,4]).
blocks(4, [1,3,5]).
blocks(5, [1,4]).

/* function taking 5 parameter representing the block/5 */
grid(A,B,C,D,E) :-
    
    /*Set to color for each parameter*/
    color(A), color(B), color(C), color(D), color(E),
    
    /*ensure that no two blocks are assigned the same color.*/
    A \= B, A \= C, A \= D, A \= E,
    B \= C, B \= D, B \= E,
    C \= D, C \= E,
    D \= E
    
    /*line returns true only if there is no block with the same color as its connected blocks.*/
    \+ (blocks(X,Y), nth1(I,Y,X), nth1(J,Y,Z), nth1(I,[A,B,C,D,E],Z), nth1(J,[A,B,C,D,E],Y)).

/* Set avialabale colors */
color(red).
color(blue).
color(yellow).
color(green).


/**
	?- grid(A,B,C,D,E).
A = red,
B = blue,
C = yellow,
D = green,
E = blue ;
A = red,
B = blue,
C = green,
D = yellow,
E = blue ;
A = red,
B = yellow,
C = blue,
D = green,
E = blue ;
A = blue,
B = green,
C = yellow,
D = red,
E = green ;
A = blue,
B = yellow,
C = green,
D = red,
E = green ;
A = green,
B = blue,
C = red,
D = yellow,
E = blue ;
A = green,
B = red,
C = blue,
D = yellow,
E = blue ;
A = yellow,
B = blue,
C = red,
D = green,
E = blue ;
A = yellow,
B = green,
C = blue,
D = red,
E = green ;
false.

Total of 10
*/

/* Question 3 */
/* Define all of the crosswords */
word(c, _, _, _, _).
word(compiled, _, _, _, _).
word(declarative, _, _, _, _).
word(functional, _, _, _, _).
word(imperative, _, _, _, _).
word(interpreted, _, _, _, _).
word(java, _, _, _, _).
word(logic, _, _, _, _).
word(objectoriented, _, _, _, _).
word(prolog, _, _, _, _).
word(python, _, _, _, _).
word(scheme, _, _, _, _).

puzzle([
    [_, _, _, _, _, _, _, _, _, _, _, _, _, _],
    [_, _, _, _, _, _, _, _, _, _, _, _, _, _],
    [_, _, _, _, _, _, _, _, _, _, _, _, _, _],
    [_, _, _, _, _, _, _, _, _, _, _, _, _, _],
    [_, _, _, _, _, _, _, _, _, _, _, _, _, _],
    [_, _, _, _, _, _, _, _, _, _, _, _, _, _],
    [_, _, _, _, _, _, _, _, _, _, _, _, _, _],
    [_, _, _, _, _, _, _, _, _, _, _, _, _, _],
    [_, _, _, _, _, _, _, _, _, _, _, _, _, _],
    [_, _, _, _, _, _, _, _, _, _, _, _, _, _],
    [_, _, _, _, _, _, _, _, _, _, _, _, _, _],
    [_, _, _, _, _, _, _, _, _, _, _, _, _, _],
    [_, _, _, _, _, _, _, _, _, _, _, _, _, _],
    [_, _, _, _, _, _, _, _, _, _, _, _, _, _]
]).

place_word_horizontal(Word, Grid, Row, Col) :-
    word(Word, _, _, _, _),
    length(Word, Length),
    ColEnd is Col + Length - 1,
    ColEnd =< 14,
    place_word_horizontal_helper(Word, Grid, Row, Col).

place_word_horizontal_helper([], _, _, _).
place_word_horizontal_helper([H|T], Grid, Row, Col) :-
    nth0(Row, Grid, RowList),
    nth0(Col, RowList, H),
    Col1 is Col + 1,
    place_word_horizontal_helper(T, Grid, Row, Col1).

place_word_vertical(Word, Grid, Row, Col) :-
    word(Word, _, _, _, _),
    length(Word, Length),
    RowEnd is Row + Length - 1,
    RowEnd =< 14,
    place_word_vertical_helper(Word, Grid, Row, Col).

place_word_vertical_helper([], _, _, _).
place_word_vertical_helper([H|T], Grid, Row, Col) :-
    nth0(Row, Grid, RowList),
    nth0(Col, RowList, H),
    Row1 is Row + 1,
    place_word_vertical_helper(T, Grid, Row1, Col).


solve_puzzle(Grid) :-
    puzzle(Grid),
    word(c, CRow, CCol, c, _),
    word(compiled, CompiledRow, CompiledCol, _, compiled),
    word(declarative, DeclarativeRow, DeclarativeCol, _, declarative),
    word(functional, FunctionalRow, FunctionalCol, _, functional),
    word(imperative, ImperativeRow, ImperativeCol, _, imperative),
    word(interpreted, InterpretedRow, InterpretedCol, _, interpreted),
    word(java, JavaRow, JavaCol, _, java),
    word(logic, LogicRow, LogicCol, _, logic),
    word(objectoriented, ObjectOrientedRow, ObjectOrientedCol, _, objectoriented),
    word(prolog, PrologRow, PrologCol, _, prolog),
    word(python, PythonRow, PythonCol, _, python),
    word(scheme, SchemeRow, SchemeCol, _, scheme),
    










