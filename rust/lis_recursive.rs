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

/// Compute the Longest Increasing Subsequence using naive recursive approach (O(2^n)).
pub fn lis_recursive(sequence: &[i32]) -> Vec<i32> {
    fn helper(sequence: &[i32], prev: i32, index: usize) -> Vec<i32> {
        if index == sequence.len() {
            return Vec::new();
        }

        // Option 1: skip current element
        let exclude = helper(sequence, prev, index + 1);

        // Option 2: include current element if it's greater than previous
        if sequence[index] > prev {
            let mut include = helper(sequence, sequence[index], index + 1);
            include.insert(0, sequence[index]); // prepend current element

            // Return the longer subsequence
            if include.len() > exclude.len() {
                return include;
            }
        }

        exclude
    }

    helper(sequence, i32::MIN, 0)
}

fn main() -> Result<(), Box<dyn Error>> {
    let args: Vec<String> = std::env::args().collect();
    if args.len() < 2 {
        eprintln!("Usage: rust-script rust/lis_recursive.rs <N>");
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

    let lis = lis_recursive(&sequence);
    println!("LIS length = {}", lis.len());
    println!("LIS = {:?}", lis);

    Ok(())
}
