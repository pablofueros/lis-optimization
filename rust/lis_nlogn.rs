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

/// Find the lower_bound index (first index with value >= target)
fn lower_bound(tails: &Vec<i32>, target: i32) -> usize {
    let mut left: isize = 0;
    let mut right: isize = (tails.len() as isize) - 1;
    let mut ans: usize = tails.len(); // default insert at end
    while left <= right {
        let mid = ((left + right) / 2) as usize;
        if tails[mid] >= target {
            ans = mid;
            right = (mid as isize) - 1;
        } else {
            left = (mid as isize) + 1;
        }
    }
    ans
}

/// O(n log n) LIS returning one LIS (values)
fn lis_nlogn(sequence: &[i32]) -> Vec<i32> {
    let n = sequence.len();
    if n == 0 {
        return Vec::new();
    }

    let mut tails_values: Vec<i32> = Vec::new(); // tail values
    let mut tails_idx: Vec<usize> = Vec::new(); // indices of those tails in sequence
    let mut prev: Vec<Option<usize>> = vec![None; n];

    for (i, &val) in sequence.iter().enumerate() {
        let pos = if tails_values.is_empty() {
            0usize
        } else {
            lower_bound(&tails_values, val)
        };

        if pos == tails_values.len() {
            tails_values.push(val);
            tails_idx.push(i);
        } else {
            tails_values[pos] = val;
            tails_idx[pos] = i;
        }

        if pos > 0 {
            prev[i] = Some(tails_idx[pos - 1]);
        }
    }

    // reconstruct LIS from tails_idx last element
    let mut lis_rev: Vec<i32> = Vec::new();
    let mut cur: Option<usize> = tails_idx.last().cloned();
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
        eprintln!("Usage: rust-script rust/lis_nlogn.rs <N>");
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

    let lis = lis_nlogn(&sequence);
    println!("LIS length = {}", lis.len());
    // println!("LIS = {:?}", lis);

    Ok(())
}
