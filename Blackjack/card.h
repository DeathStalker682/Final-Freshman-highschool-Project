//Name: Card Class
//Author: Owen Maguire
//Date: 11/17/22
//Desc: Determine suit and number of card

#include <iostream>

#ifndef C_A_R_D
#define C_A_R_D

class card { // Declaration
public:
  card();  // Constructor

  ~card() {}; // Destructor

  int setCard(int newNum);

  std::string showCard();

  int getValue();

private:
  int cardNum;
}; // End of card declaration

/*********************
* Class  Definitions *
**********************/
card::card() {
  cardNum = 52;
} // End constructor

int card:: setCard(int newNum) {
  cardNum = newNum;
  return 0;
} // End setCard()

/******************************************/
std::string card::showCard() {
  // Variables
  std::string suits[4] = {"\u2666", "\u2665", "\u2663", "\u2660"}; // Unicode for diamond, heart, club, spade
  std::string values= "234567890JQKA"; // Number of cards
  std::string passout = "\033[7;49;39m"; // White background
  
  int num = cardNum % 13; // Set num to 0-13
  int symbol = cardNum / 13; // Set suit

  // Build card string value
  if(num == 8) { // 8th character is 0 so change to 10
    passout += "10";
  }
  else {
    passout += values[num]; // Add character value
  }
  // Add suit to passout string
  if(symbol < 2) { passout += "\033[0;31;47m"; } // Red text
  passout += suits[symbol];
    
  passout += "\033[0m"; // Stop text & BG color
  
  return passout;
} // End showCard()

/**********************************************/
int card::getValue() {
  // Add 2 since zero evaluates to a 2
  return (cardNum % 13) + 2;
} // End getValue()

#endif // C_A_R_D