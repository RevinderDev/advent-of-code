use std::cmp::Ordering;
use std::iter::FromIterator;

pub fn run() {
    run_a();
    run_b();
}

fn run_a() {
    let input: Vec<String> = include_str!("input_files/day3_input.txt")
        .lines()
        .map(|s| s.to_string())
        .collect();

    let number_of_bits = input[0].len();
    let mut gamma: Vec<char> = vec![];
    for bit in 0..number_of_bits {
        let mut ones = 0;
        let mut zeroes = 0;
        for line in input.iter() {
            match line.chars().nth(bit).unwrap() {
                '0' => zeroes += 1,
                '1' => ones += 1,
                _ => panic!("Unknown bit"),
            }
        }
        match ones > zeroes {
            true => gamma.push('1'),
            false => gamma.push('0'),
        }
    }
    let byte_mask = isize::from_str_radix("1".repeat(number_of_bits).as_str(), 2).unwrap();
    let gamma = isize::from_str_radix(String::from_iter(gamma).as_str(), 2).unwrap();
    let epsilon = gamma ^ byte_mask;
    println!(
        "a) Gamma => {:b}  Epsilon => {:b}  Answer => {}",
        gamma,
        epsilon,
        gamma * epsilon
    );
}

fn run_b() {
    let input: Vec<String> = include_str!("input_files/day3_input.txt")
        .lines()
        .map(|s| s.to_string())
        .collect();

    let input_clone = input.clone();
    let oxygen_raiting = get_raiting(input, &most_common);
    let co2_scrubber = get_raiting(input_clone, &least_common);
    println!(
        "a) Oxygen raiting => {:b}  CO2 Scrubber => {:b}  Answer => {}",
        oxygen_raiting,
        co2_scrubber,
        oxygen_raiting * co2_scrubber
    );
}

fn get_raiting(mut input: Vec<String>, compare_fn: &dyn Fn(i32, i32) -> char) -> isize {
    let number_of_bits = input[0].len();
    let mut result = None;
    for bit in 0..number_of_bits {
        let mut ones = 0;
        let mut zeroes = 0;
        for line in input.iter() {
            match line.chars().nth(bit).unwrap() {
                '0' => zeroes += 1,
                '1' => ones += 1,
                _ => panic!("Unknown bit"),
            }
        }
        let winner = compare_fn(ones, zeroes);
        input = input
            .into_iter()
            .filter(|x| x.chars().nth(bit).unwrap() == winner)
            .collect();
        if input.len() == 1 {
            result = input.pop();
            break;
        }
    }

    isize::from_str_radix(String::from_iter(result).as_str(), 2).unwrap()
}

fn most_common(a: i32, b: i32) -> char {
    match a.cmp(&b) {
        Ordering::Greater => '1',
        Ordering::Less => '0',
        Ordering::Equal => '1',
    }
}

fn least_common(a: i32, b: i32) -> char {
    match a.cmp(&b) {
        Ordering::Greater => '0',
        Ordering::Less => '1',
        Ordering::Equal => '0',
    }
}
