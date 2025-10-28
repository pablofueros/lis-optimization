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

/// Compute the Longest Increasing Subsequence using dynamic programming (O(n^2)).
fn lis_dp(sequence: &[i32]) -> Vec<i32> {
    let n = sequence.len();
    if n == 0 {
        return vec![];
    }

    let mut dp: Vec<usize> = vec![1; n];
    let mut prev: Vec<Option<usize>> = vec![None; n];

    for i in 0..n {
        for j in 0..i {
            if sequence[j] < sequence[i] && dp[j] + 1 > dp[i] {
                dp[i] = dp[j] + 1;
                prev[i] = Some(j);
            }
        }
    }

    // find index of maximum dp
    let mut max_idx = 0usize;
    for i in 1..n {
        if dp[i] > dp[max_idx] {
            max_idx = i;
        }
    }

    // reconstruct LIS
    let mut lis_rev: Vec<i32> = Vec::new();
    let mut cur: Option<usize> = Some(max_idx);
    while let Some(idx) = cur {
        lis_rev.push(sequence[idx]);
        cur = prev[idx];
    }
    lis_rev.reverse();
    lis_rev
}

fn main() -> Result<(), Box<dyn Error>> {
    let args: Vec<String> = std::env::args().collect();
    if args.len() < 2 {
        eprintln!("Usage: rust-script rust/lis_dp_n2.rs <N>");
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

    let lis = lis_dp(&sequence);
    println!("LIS length = {}", lis.len());
    // println!("LIS = {:?}", lis);

    Ok(())
}
