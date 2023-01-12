// Name: Card Game
// Author: Owen Maguire
// Date: 1/12/23
// Desc: Play a game of Blackjack
// Location: Beaverton high School, Oregon

#include <iostream>
#include "card.h"
#include "deck.h"
#include "hand.h"


int main() {
  deck one;
  hand player;
  hand house;

  int wins = 0; // W/L counter
  int losses = 0;
  
  while(true) {

  std::string again;
  std::string choice = "";

  // Deal two cards to each player
  player.get_card(one.deal());
  house.get_card(one.deal());
  std::cout << "\nDealer's hand:\t ## ";
  house.display();
  std::cout << '\n';
  player.get_card(one.deal());
  house.get_card(one.deal());  

  // Players turn
  while(true) {
    std::cout << "Player's hand:\t";
    player.display();
    std::cout << "Total = " << player.total() << '\n';
    if(player.total() > 21) { // Break if player busts
      break;}
    else if(player.total() == 21){
    break;} // Break if player wins
    std::cout << "Hit: {1} | Stand: {2}\n"
              << "Please enter your choice: ";
    std::cin >> choice;
    if(choice[0] == '1') {
      player.get_card(one.deal());
    }
    else if(choice[0] == '2') { break; }
    else {
      std::cout << "Invalid Input. Valid inputs are 1 and 2. \n";
    } // End decision
  }// End player loop

  if(player.total() != 21 and player.total() < 21){//don't run if player has already won/lost
  //Dealer's Turn
  while(true) {
  std::cout << "\nDealer's hand:\t";
  house.display(); // display dealer hand
  std::cout << "Total:\t";
  std::cout << house.total(); //display dealer total
  if (house.total() < 17) { 
  house.get_card(one.deal());} // decide if dealer hits/stands
  else if(house.total() >= 17){ 
  break;}// End hit/stand
  }// End Dealer's Turn
    }
  // Win/Lose Text
  if(player.total() > house.total() and player.total() <= 21){ std::cout << "\n\nYou Win!"; wins += 1;} //increment w/l counter
  else if(house.total() > 21){
  std::cout << "\n\nYou Win!"; wins += 1;}
  else if(player.total() == house.total())
    std::cout << "\n\nYou Tied!";
  else{std::cout << "\n\nYou Lose!"; losses += 1;} //  End Win/Lose Text 

  std::cout << "\n\nWins: " << wins;
  std::cout << "\nLosses: " << losses << "\n\n";
    
  //Repeat program
std::cout << "Play Again? (Y/N)";
std::cin >> again;
again = toupper(again[0]);
if (again.compare("N") == 0) {
  return 0; }

player.reset(); //reset hands if play again
house.reset();

    }//end while true
  }//End Main
  }//End Main
