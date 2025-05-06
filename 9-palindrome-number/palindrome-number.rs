impl Solution {
    pub fn is_palindrome(x: i32) -> bool {
        let num_str = x.to_string();
        let rev_num_str = num_str.chars().rev().collect::<String>();
        num_str == rev_num_str   
    }
}