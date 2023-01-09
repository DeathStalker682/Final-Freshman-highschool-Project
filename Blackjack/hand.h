//Name: Deck Class
//Author: Owen Maguire
//Date: 1-3-2023
//Desc: Simulate a hand of playiung cards

#include <iostream>
#include "card.h"

#ifndef H_A_N_D
#define H_A_N_D

class hand { // Declaration
public:
  hand();  // Constructor

  ~hand() {}; // Destructor

  int get_card(card dealt);

  int display();

  int reset();

  int total();

private:
  card group[25];
  int cardCount;
}; // End of hand declaration

/*********************
* Class  Definitions *
**********************/
hand::hand() {
  reset();
} // End hand constructor

int hand::reset() {
  cardCount = 0;
  return 0;
} // End hand reload


int hand::get_card(card dealt) {
  group[cardCount] = dealt;
  cardCount++;
  return 0;
} // End get_card()

int hand::display() {
  for(int i = 0; i < cardCount; i++) {
    std::cout << group[i].showCard() << ' ';
  } // End for loop
  std::cout << '\n';
  return 0;
} // End hand display()

int hand::total() {
  int total = 0;
  int value = 0;
  int ace = 0;
  
  // loop through group of cards
  for(int i = 0; i < cardCount; i++) {
    value = group[i].getValue();
    if(value == 14) { // 14 is an ace
      total += 11;
      ace++; // keep track of aces for later
    }
    else if (value > 10) {
      total += 10;
    }
    else {
      total += value;
    } // End decision
  } // End for loop
  
  // adjust if hand has aces and total is > 21
  while (ace > 0 && total > 21) {
    total -= 10;
    ace--;
  }
  
  return total;
} // End total()

#endif // End of ifndef then define