// Name: Deck Class
// Author: Owen Maguire
// Date: 11/29/22
// Desc: Shuffle and display full deck of cards

#include <iostream>
#include "card.h"

#ifndef D_E_C_K
#define D_E_C_K

class deck { // Declaration
public:
  deck();  // Constructor

  ~deck() {}; // Destructor

  int display();

  int randomize();

  card deal();

  int reload();

private:
  card stack[52];
  int cardCount;
}; // End of deck declaration

/*********************
* Class  Definitions *
**********************/
deck::deck() {
  reload();
} // End deck constructor

int deck::reload() {
  cardCount = 52;
  for(int i = 0; i < cardCount; i++) {
    stack[i].setCard(i);
  } // End for loop
  randomize();
  return 0;
} // End deck reload

int deck::display() {
  for(int i = 0; i < cardCount; i++) {
    if(i % 13 == 0) std::cout << '\n';
    std::cout << stack[i].showCard() << ' ';
  } // End for loop
  std::cout << '\n';
  return 0;
} // End deck display()

int deck::randomize() {
  card temp;
  srand(time(NULL));
  int rnum;
  for(int i = 0; i < cardCount; i++) {
    temp = stack[i]; // Set to curr card in loop
    rnum = rand() % 52; // Random number within deck
    stack[i] = stack[rnum];
    stack[rnum] = temp;
  } // End for loop
  return 0;
} // End randomize()

card deck::deal() {
  if(cardCount == 0) reload();
  cardCount--;
  card outgoing = stack[cardCount];
  stack[cardCount].setCard(0);
  return outgoing;
} // End deal()

#endif // End of ifndef then define