#include <iostream>
#include "card.h"
#include "deck.h"
#include "hand.h"


int main() {
  deck one;
  hand player;
  hand house;
  
  std::string choice = " ";

  // Deal two cards to each
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
    getline(std::cin, choice);
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
  if(player.total() > house.total() and player.total() <= 21){ std::cout << "\n\nYou Win!";}
  else if(house.total() > 21){
  std::cout << "\n\nYou Win!";}
  else if(player.total() == house.total())
    std::cout << "\n\nYou Tied!";
  else{std::cout << "\n\nYou Lose!";} //  End Win/Lose Text 

  return 0;

  }//End Main