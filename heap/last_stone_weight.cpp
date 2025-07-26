class Solution {
public:
    int lastStoneWeight(vector<int>& stones) {
        
        priority_queue<int> maxHeap(stones.begin(), stones.end());

        int x = {}, y = {};
        while (maxHeap.size() > 1) {
        
            y = maxHeap.top();
            maxHeap.pop();
            x = maxHeap.top();
            maxHeap.pop();

            if (x != y) {
                maxHeap.push(y - x);
            }
        }

        if (maxHeap.size() > 0) {
            return maxHeap.top();
        }
        return 0;
    }
};
