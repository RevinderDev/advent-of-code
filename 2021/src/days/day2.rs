use core::panic;

pub fn run() {
    run_a();
    run_b();
}

fn run_a() {
    let input = include_str!("input_files/day2_input.txt").lines();
    let mut horizontal = 0;
    let mut depth = 0;
    for line in input {
        let (direction, movement) = line.split_at(line.find(' ').unwrap());
        let movement: i32 = movement[1..].parse().unwrap();
        match direction {
            "forward" => horizontal += movement,
            "down" => depth += movement,
            "up" => depth -= movement,
            _ => panic!("Unexpected direction"),
        }
    }
    println!("a) Answer => {}", horizontal * depth);
}

fn run_b() {
    let input = include_str!("input_files/day2_input.txt").lines();
    let mut horizontal = 0;
    let mut depth = 0;
    let mut aim = 0;
    for line in input {
        let (direction, movement) = line.split_at(line.find(' ').unwrap());
        let movement: i32 = movement[1..].parse().unwrap();
        match direction {
            "forward" => {
                horizontal += movement;
                depth += aim * movement;
            }
            "down" => aim += movement,
            "up" => aim -= movement,
            _ => panic!("Unexpected direction"),
        }
    }
    println!("b) Answer => {}", horizontal * depth);
}
