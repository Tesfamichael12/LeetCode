/**
 * @param {number[][]} intervals
 * @return {number[][]}
 */
var merge = function(intervals) {
    intervals.sort((a, b) => a[0] - b[0]);
    let i = 1;
    while (i < intervals.length) {
        if (intervals[i-1][1] >= intervals[i][0]) {
            intervals[i-1][1] = Math.max(intervals[i][1], intervals[i-1][1]);
            intervals.splice(i, 1);
        } else {
            i++;
        }
    }
    return intervals;
};