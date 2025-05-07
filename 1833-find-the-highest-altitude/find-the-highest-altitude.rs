impl Solution {
    pub fn largest_altitude(gain: Vec<i32>) -> i32 {
        let mut max_height = 0;
        let mut current_height = 0;

        for i in gain{
            current_height += i;
            if current_height > max_height{
                max_height = current_height;
            }
        }
        return max_height;
    }
}