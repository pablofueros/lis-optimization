//! ```cargo
//! [dependencies]
//! serde = { version = "1.0", features = ["derive"] }
//! serde_json = "1.0"
//! ```

use std::error::Error;
use std::fs;

/// Load a sequence from JSON (same format as Python).
fn load_sequence(path: &str) -> Result<Vec<i32>, Box<dyn Error>> {
    let content = fs::read_to_string(path)?;
    let sequence: Vec<i32> = serde_json::from_str(&content)?;
    Ok(sequence)
}

/// Compute the Longest Increasing Subsequence using naive backtracking approach (O(2^n)).
fn lis_bruteforce(sequence: &[i32]) -> Vec<i32> {
    let mut best: Vec<i32> = Vec::new();

    fn backtrack(seq: &[i32], index: usize, current: &mut Vec<i32>, best: &mut Vec<i32>) {
        let n = seq.len();

        // pruning: if remaining elements cannot beat the best, stop exploring
        if current.len() + (n - index) <= best.len() {
            return;
        }

        // reached end: update best if needed
        if index >= n {
            if current.len() > best.len() {
                *best = current.clone();
            }
            return;
        }

        // Option 1: skip element
        backtrack(seq, index + 1, current, best);

        // Option 2: take element if it forms an increasing subsequence
        if current.is_empty() || seq[index] > *current.last().unwrap() {
            current.push(seq[index]);
            backtrack(seq, index + 1, current, best);
            current.pop();
        }
    }

    backtrack(sequence, 0, &mut Vec::new(), &mut best);
    best
}

fn main() -> Result<(), Box<dyn Error>> {
    let args: Vec<String> = std::env::args().collect();
    if args.len() < 2 {
        eprintln!("Usage: rust-script rust/lis_bruteforce.rs <N>");
        std::process::exit(1);
    }

    let n_arg = &args[1];
    let n: u32 = n_arg.replace('_', "").parse().unwrap();
    let file_path = format!("data/sequence_{}.json", n);

    let sequence = match load_sequence(&file_path) {
        Ok(seq) => seq,
        Err(_) => {
            eprintln!("Error: file '{}' does not exist.", file_path);
            eprintln!("Run 'uv run python/generator.py' to generate the data.");
            std::process::exit(1);
        }
    };

    let lis = lis_bruteforce(&sequence);
    println!("LIS length = {}", lis.len());
    // println!("LIS = {:?}", lis);

    Ok(())
}
