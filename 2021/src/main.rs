mod days;

use clap::{App, Arg};
use days::{day1, day2, day3};

fn main() {
    let matches = App::new("Advent of Code 2021")
        .version("1.0")
        .author("Michal K. <michal0kasprzyk@gmail.com>")
        .about("Rust solutions!")
        .arg(
            Arg::with_name("Days")
                .short("d")
                .long("days")
                .value_name("[1 - 31]")
                .help("Choose days to run")
                .takes_value(true)
                .required(true)
                .multiple(true),
        )
        .get_matches();

    let days = matches.values_of("Days").expect("Provide days to run");
    for day in days {
        let parsed_day = day.parse().unwrap_or(-1);
        let func = match parsed_day {
            1 => day1::run,
            2 => day2::run,
            3 => day3::run,
            _ => {
                eprintln!(" >> Incorrect day value `{}`. Skipping..<< ", day);
                continue;
            }
        };
        println!(" >> Running Day {} <<", day);
        func();
    }
}
