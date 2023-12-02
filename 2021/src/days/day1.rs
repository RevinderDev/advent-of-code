use std::fs;

pub fn run() {
    run_a();
    run_b();
}

fn run_a() {
    let contents = fs::read_to_string("src/days/input_files/day1_input.txt")
        .expect("Something went wrong reading the file");

    let input: Vec<i32> = contents
        .split('\n')
        .map(|x| x.trim().parse::<i32>().unwrap())
        .collect();

    let mut count = 0;
    let mut previous_measure = input[0];
    for measure in input.into_iter().skip(1) {
        if measure > previous_measure {
            count += 1;
        }
        previous_measure = measure;
    }
    println!("a) Answer => {}", count);
}

fn run_b() {
    let result = include_str!("input_files/day1_input.txt")
        .lines()
        .map(|n| n.parse().unwrap())
        .collect::<Vec<i32>>()
        .windows(3)
        .map(|x| x[0] + x[1] + x[2])
        .collect::<Vec<i32>>()
        .windows(2)
        .filter(|a| a[0] < a[1])
        .count();

    println!("b) Answer => {}", result);
}
