# TowerOfHanoi
Python algorithm to solve the Tower Of Hanoi puzzle by data movement

The Tower of Hanoi puzzle consists of 3 pegs with rings of descending size on each peg.
The object of the puzzle is to move the entire tower to the third peg, but the player
can only move one ring at a time, and a larger peg cannot be placed on top of a smaller
peg.

          This:

                    |                    |                    |          
                   ---                   |                    |          
                  -----                  |                    |          
                 -------                 |                    |          
                    |                    |                    |          
          ===============================================================

          Must become this:

                    |                    |                    |          
                    |                    |                   ---         
                    |                    |                  -----        
                    |                    |                 -------       
                    |                    |                    |          
          ===============================================================

  
My solution was made specifically with the challenge of moving data.  Most solutions
of this problem use recursion to determine which steps to print, however they do not move
data.  As you might guess, this solution is not recursive.

While writing this, I could not find any solutions on the web that move data like my
own, however I might not have looked hard enough.  Please let me know if anyone else
has solved this puzzle using data movement; I'd love to see another solution.
