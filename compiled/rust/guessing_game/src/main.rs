use std::io;
use std::rand;

fn main() {
    println!("Guess the number!");
    
    let secret_number = (rand::random::<i32>() % 100) + 1; // secret number: i32
    
    println!("Please input your guess.");
    
    let input = io::stdin().read_line()
                           .ok()
                           .expect("Failed to read line");

    println!("You guessed: {}", input);
}
