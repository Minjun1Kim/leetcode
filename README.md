# LeetCode Tracker — NeetCode 150

> A clean, editable tracker for the **NeetCode 150** set. Check boxes to mark solved, keep short notes on the approach, and record complexity.

![Progress](https://img.shields.io/badge/Progress-0%2F150-lightgrey)
![License](https://img.shields.io/badge/license-MIT-informational)

---

## How to use

1. **Mark solved** by toggling the checkbox (`[ ]` → `[x]`).  
2. **Keep notes** on the core idea (e.g., “two‑pass hashmap”, “monotonic stack”).  
3. **Tag** each problem with primary algorithm(s) to group by topic during review.  
4. **Track complexity** to build intuition for time/space trade‑offs.  
5. Use the CSV (in this repo or below) if you prefer maintaining entries there and generating the table automatically.

> **Tip:** Keep notes ultra‑short (≤ 2–3 lines). When revisiting, add “Gotchas” you tripped on.

---

## Legend

- **Solved** — GitHub checkbox you can click to tick/untick.
- **Tags / Algo** — e.g., `Array, Hash Map`, `Two Pointers`, `Heap`, `Graph`, `DP (1‑D)`, `DP (2‑D)`, `Trie`, `Greedy`, `Intervals`, `Backtracking`, `Bit`, `Math`.
- **Date Solved** — `YYYY‑MM‑DD`.
- **Time / Space** — e.g., `O(n log n)` / `O(1)`.

---

## Progress

- Overall: **0 / 150** (edit this line as you go, or use a script to count `[x]` below)
- By Category (targets per NeetCode 150; check off as you finish):
  - Arrays & Hashing (≈ 9–10)
  - Two Pointers (≈ 5)
  - Stack (≈ 6)
  - Binary Search (≈ 6)
  - Sliding Window (≈ 6)
  - Linked List (≈ 10)
  - Trees (≈ 15)
  - Tries (≈ 3)
  - Heap / Priority Queue (≈ 6)
  - Backtracking (≈ 9)
  - Graphs (≈ 18)
  - 1‑D DP (≈ 12)
  - 2‑D DP (≈ 10)
  - Greedy (≈ 9)
  - Intervals (≈ 6)
  - Math & Geometry (≈ 7)
  - Bit Manipulation (≈ 6)

---

## Master Table (NeetCode 150)

> **Columns:** Solved, LC #, Title, Difficulty, Tags / Algo, Approach Notes, Time, Space, Date Solved, URL

| Solved | # | Title | Difficulty | Tags / Algo | Approach Notes | Time | Space | Date Solved | URL |
|:-----:|---:|---|:---:|---|---|---|---|:---:|---|
| [x] | 217 | Contains Duplicate | Easy | Array, Hash Map | Use a set; early exit on seen element | O(n) | O(n) |  | https://leetcode.com/problems/contains-duplicate/ |
| [x] | 242 | Valid Anagram | Easy | Hash Map, Sorting | Count letters or sort strings | O(n) / O(n log n) | O(1) or O(k) |  | https://leetcode.com/problems/valid-anagram/ |
| [x] | 1 | Two Sum | Easy | Hash Map | One‑pass map from value→index | O(n) | O(n) |  | https://leetcode.com/problems/two-sum/ |
| [x] | 49 | Group Anagrams | Medium | Hash Map | Count‑key by 26‑freq tuple | O(n·k) | O(n·k) |  | https://leetcode.com/problems/group-anagrams/ |
| [x] | 238 | Product of Array Except Self | Medium | Array, Prefix | Prefix & suffix products | O(n) | O(1) |  | https://leetcode.com/problems/product-of-array-except-self/ |
| [] | 125 | Valid Palindrome | Easy | Two Pointers | Normalize; move inwards | O(n) | O(1) |  | https://leetcode.com/problems/valid-palindrome/ |
| [] | 167 | Two Sum II - Input Array Is Sorted | Medium | Two Pointers | Left+right shrink window | O(n) | O(1) |  | https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/ |
| [ ] | 15 | 3Sum | Medium | Two Pointers | Sort + fixed i + 2‑sum | O(n^2) | O(1) |  | https://leetcode.com/problems/3sum/ |
| [ ] | 11 | Container With Most Water | Medium | Two Pointers | Two‑pointer max area | O(n) | O(1) |  | https://leetcode.com/problems/container-with-most-water/ |
| [ ] | 20 | Valid Parentheses | Easy | Stack | Push opens; match closes | O(n) | O(n) |  | https://leetcode.com/problems/valid-parentheses/ |
| [ ] | 155 | Min Stack | Medium | Stack, Design | Keep value and min so far | O(1) ops | O(n) |  | https://leetcode.com/problems/min-stack/ |
| [ ] | 150 | Evaluate Reverse Polish Notation | Medium | Stack | Evaluate tokens on stack | O(n) | O(n) |  | https://leetcode.com/problems/evaluate-reverse-polish-notation/ |
| [ ] | 22 | Generate Parentheses | Medium | Backtracking, Stack | Build valid using counts | O(C_n) | O(n) |  | https://leetcode.com/problems/generate-parentheses/ |
| [ ] | 739 | Daily Temperatures | Medium | Monotonic Stack | Decreasing stack of temps | O(n) | O(n) |  | https://leetcode.com/problems/daily-temperatures/ |
| [ ] | 84 | Largest Rectangle in Histogram | Hard | Monotonic Stack | Next‑smaller left/right | O(n) | O(n) |  | https://leetcode.com/problems/largest-rectangle-in-histogram/ |
| [ ] | 704 | Binary Search | Easy | Binary Search | Classic mid shrink | O(log n) | O(1) |  | https://leetcode.com/problems/binary-search/ |
| [ ] | 74 | Search a 2D Matrix | Medium | Binary Search | Treat as 1‑D index | O(log mn) | O(1) |  | https://leetcode.com/problems/search-a-2d-matrix/ |
| [ ] | 875 | Koko Eating Bananas | Medium | Binary Search | Search answer (speed) | O(n log M) | O(1) |  | https://leetcode.com/problems/koko-eating-bananas/ |
| [ ] | 153 | Find Minimum in Rotated Sorted Array | Medium | Binary Search | Compare mid to right | O(log n) | O(1) |  | https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/ |
| [ ] | 33 | Search in Rotated Sorted Array | Medium | Binary Search | Decide sorted side | O(log n) | O(1) |  | https://leetcode.com/problems/search-in-rotated-sorted-array/ |
| [ ] | 121 | Best Time to Buy and Sell Stock | Easy | Sliding Window | Track min‑so‑far | O(n) | O(1) |  | https://leetcode.com/problems/best-time-to-buy-and-sell-stock/ |
| [ ] | 3 | Longest Substring Without Repeating Characters | Medium | Sliding Window | Map last seen; move left | O(n) | O(k) |  | https://leetcode.com/problems/longest-substring-without-repeating-characters/ |
| [ ] | 424 | Longest Repeating Character Replacement | Medium | Sliding Window | Keep max‑count char | O(n) | O(1) |  | https://leetcode.com/problems/longest-repeating-character-replacement/ |
| [ ] | 567 | Permutation in String | Medium | Sliding Window | Count diff, slide | O(n) | O(1) |  | https://leetcode.com/problems/permutation-in-string/ |
| [ ] | 76 | Minimum Window Substring | Hard | Sliding Window | Expand/contract windows | O(n) | O(1) |  | https://leetcode.com/problems/minimum-window-substring/ |
| [ ] | 239 | Sliding Window Maximum | Hard | Monotonic Deque | Deque of indices | O(n) | O(k) |  | https://leetcode.com/problems/sliding-window-maximum/ |
| [ ] | 206 | Reverse Linked List | Easy | Linked List | Iterative pointer flip | O(n) | O(1) |  | https://leetcode.com/problems/reverse-linked-list/ |
| [ ] | 21 | Merge Two Sorted Lists | Easy | Linked List | Dummy head merge | O(n+m) | O(1) |  | https://leetcode.com/problems/merge-two-sorted-lists/ |
| [ ] | 143 | Reorder List | Medium | Linked List | Middle + reverse + weave | O(n) | O(1) |  | https://leetcode.com/problems/reorder-list/ |
| [ ] | 19 | Remove Nth Node From End of List | Medium | Linked List, Two Pointers | Fast/slow; delete | O(n) | O(1) |  | https://leetcode.com/problems/remove-nth-node-from-end-of-list/ |
| [ ] | 138 | Copy List with Random Pointer | Medium | Linked List | Interleave nodes trick | O(n) | O(1) |  | https://leetcode.com/problems/copy-list-with-random-pointer/ |
| [ ] | 2 | Add Two Numbers | Medium | Linked List, Math | Carry‑sum across lists | O(n) | O(1) |  | https://leetcode.com/problems/add-two-numbers/ |
| [ ] | 141 | Linked List Cycle | Easy | Linked List | Floyd’s two pointers | O(n) | O(1) |  | https://leetcode.com/problems/linked-list-cycle/ |
| [ ] | 146 | LRU Cache | Medium | Design, Linked List, Hash Map | DLL + hashmap | O(1) ops | O(n) |  | https://leetcode.com/problems/lru-cache/ |
| [ ] | 23 | Merge k Sorted Lists | Hard | Heap, Linked List | Heap of heads | O(n log k) | O(k) |  | https://leetcode.com/problems/merge-k-sorted-lists/ |
| [ ] | 226 | Invert Binary Tree | Easy | Tree, BFS/DFS | Swap children recursively | O(n) | O(h) |  | https://leetcode.com/problems/invert-binary-tree/ |
| [ ] | 104 | Maximum Depth of Binary Tree | Easy | Tree, DFS | Depth = 1 + max(children) | O(n) | O(h) |  | https://leetcode.com/problems/maximum-depth-of-binary-tree/ |
| [ ] | 543 | Diameter of Binary Tree | Easy | Tree, DFS | Track best path via node | O(n) | O(h) |  | https://leetcode.com/problems/diameter-of-binary-tree/ |
| [ ] | 110 | Balanced Binary Tree | Easy | Tree, DFS | Height or -1 early stop | O(n) | O(h) |  | https://leetcode.com/problems/balanced-binary-tree/ |
| [ ] | 100 | Same Tree | Easy | Tree | DFS compare | O(n) | O(h) |  | https://leetcode.com/problems/same-tree/ |
| [ ] | 572 | Subtree of Another Tree | Easy | Tree, DFS | Compare roots + subcalls | O(n·m) | O(h) |  | https://leetcode.com/problems/subtree-of-another-tree/ |
| [ ] | 235 | Lowest Common Ancestor of a BST | Medium | Tree | BST property | O(h) | O(1) |  | https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/ |
| [ ] | 102 | Binary Tree Level Order Traversal | Medium | Tree, BFS | Queue per level | O(n) | O(n) |  | https://leetcode.com/problems/binary-tree-level-order-traversal/ |
| [ ] | 199 | Binary Tree Right Side View | Medium | Tree, BFS | Last per level | O(n) | O(n) |  | https://leetcode.com/problems/binary-tree-right-side-view/ |
| [ ] | 1448 | Count Good Nodes in Binary Tree | Medium | Tree, DFS | Track max‑so‑far | O(n) | O(h) |  | https://leetcode.com/problems/count-good-nodes-in-binary-tree/ |
| [ ] | 98 | Validate Binary Search Tree | Medium | Tree, DFS | Min/max bounds | O(n) | O(h) |  | https://leetcode.com/problems/validate-binary-search-tree/ |
| [ ] | 230 | Kth Smallest Element in a BST | Medium | Tree, In‑order | Early stop k | O(h+k) | O(h) |  | https://leetcode.com/problems/kth-smallest-element-in-a-bst/ |
| [ ] | 105 | Construct Binary Tree from Preorder and Inorder Traversal | Medium | Tree | Map inorder indices | O(n) | O(n) |  | https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/ |
| [ ] | 124 | Binary Tree Maximum Path Sum | Hard | Tree, DFS | Return best down‑path | O(n) | O(h) |  | https://leetcode.com/problems/binary-tree-maximum-path-sum/ |
| [ ] | 297 | Serialize and Deserialize Binary Tree | Hard | Tree, BFS | Null sentinels | O(n) | O(n) |  | https://leetcode.com/problems/serialize-and-deserialize-binary-tree/ |
| [ ] | 208 | Implement Trie (Prefix Tree) | Medium | Trie | Node map children + end | O(m) ops | O(Σ) |  | https://leetcode.com/problems/implement-trie-prefix-tree/ |
| [ ] | 211 | Design Add and Search Words Data Structure | Medium | Trie | DFS when wildcard | O(Σ^m) worst | O(Σ·m) |  | https://leetcode.com/problems/design-add-and-search-words-data-structure/ |
| [ ] | 212 | Word Search II | Hard | Trie, Backtracking | Prune by trie; mark visited | O(Σ·4^L) | O(Σ·L) |  | https://leetcode.com/problems/word-search-ii/ |
| [ ] | 703 | Kth Largest Element in a Stream | Easy | Heap | Min‑heap of size k | O(log k) | O(k) |  | https://leetcode.com/problems/kth-largest-element-in-a-stream/ |
| [ ] | 973 | K Closest Points to Origin | Medium | Heap | N log k or sort | O(n log k) | O(k) |  | https://leetcode.com/problems/k-closest-points-to-origin/ |
| [ ] | 215 | Kth Largest Element in an Array | Medium | Heap / Quickselect | Quickselect average | O(n) avg | O(1) |  | https://leetcode.com/problems/kth-largest-element-in-an-array/ |
| [ ] | 295 | Find Median from Data Stream | Hard | Heaps (two) | Max‑left, min‑right | O(log n) | O(n) |  | https://leetcode.com/problems/find-median-from-data-stream/ |
| [ ] | 621 | Task Scheduler | Medium | Greedy, Heap | Idle math or heap sim | O(n) | O(1) |  | https://leetcode.com/problems/task-scheduler/ |
| [ ] | 200 | Number of Islands | Medium | Graph, DFS/BFS | Flood‑fill | O(mn) | O(mn) |  | https://leetcode.com/problems/number-of-islands/ |
| [ ] | 133 | Clone Graph | Medium | Graph, BFS/DFS | Map node→clone | O(V+E) | O(V) |  | https://leetcode.com/problems/clone-graph/ |
| [ ] | 695 | Max Area of Island | Medium | Graph, DFS | Track visited | O(mn) | O(mn) |  | https://leetcode.com/problems/max-area-of-island/ |
| [ ] | 417 | Pacific Atlantic Water Flow | Medium | Graph, BFS/DFS | Multi‑source BFS | O(mn) | O(mn) |  | https://leetcode.com/problems/pacific-atlantic-water-flow/ |
| [ ] | 130 | Surrounded Regions | Medium | Graph, BFS/DFS | Edge‑connected O’s survive | O(mn) | O(mn) |  | https://leetcode.com/problems/surrounded-regions/ |
| [ ] | 994 | Rotting Oranges | Medium | Graph, BFS | Minutes as layers | O(mn) | O(mn) |  | https://leetcode.com/problems/rotting-oranges/ |
| [ ] | 207 | Course Schedule | Medium | Graph, Topo | Kahn or DFS detect cycle | O(V+E) | O(V+E) |  | https://leetcode.com/problems/course-schedule/ |
| [ ] | 210 | Course Schedule II | Medium | Graph, Topo | Return topo order | O(V+E) | O(V+E) |  | https://leetcode.com/problems/course-schedule-ii/ |
| [ ] | 743 | Network Delay Time | Medium | Graph, Dijkstra | Min‑heap shortest paths | O(E log V) | O(E) |  | https://leetcode.com/problems/network-delay-time/ |
| [ ] | 278 | First Bad Version | Easy | Binary Search | Shrink by predicate | O(log n) | O(1) |  | https://leetcode.com/problems/first-bad-version/ |
| [ ] | 70 | Climbing Stairs | Easy | DP (1‑D) | Fib bottom‑up | O(n) | O(1) |  | https://leetcode.com/problems/climbing-stairs/ |
| [ ] | 746 | Min Cost Climbing Stairs | Easy | DP (1‑D) | dp[i]=cost[i]+min(dp[i-1],dp[i-2]) | O(n) | O(1) |  | https://leetcode.com/problems/min-cost-climbing-stairs/ |
| [ ] | 198 | House Robber | Medium | DP (1‑D) | rolling two | O(n) | O(1) |  | https://leetcode.com/problems/house-robber/ |
| [ ] | 213 | House Robber II | Medium | DP (1‑D), Circle | rob line twice, skip ends | O(n) | O(1) |  | https://leetcode.com/problems/house-robber-ii/ |
| [ ] | 5 | Longest Palindromic Substring | Medium | DP / Expand Center | expand or dp | O(n^2) | O(1)/O(n^2) |  | https://leetcode.com/problems/longest-palindromic-substring/ |
| [ ] | 647 | Palindromic Substrings | Medium | Expand Center | count centers | O(n^2) | O(1) |  | https://leetcode.com/problems/palindromic-substrings/ |
| [ ] | 91 | Decode Ways | Medium | DP | dp[i] by 1‑ or 2‑digit validity | O(n) | O(1) |  | https://leetcode.com/problems/decode-ways/ |
| [ ] | 322 | Coin Change | Medium | DP (1‑D) | min coins for each sum | O(n·A) | O(A) |  | https://leetcode.com/problems/coin-change/ |
| [ ] | 152 | Maximum Product Subarray | Medium | DP / Kadane variant | track max & min | O(n) | O(1) |  | https://leetcode.com/problems/maximum-product-subarray/ |
| [ ] | 139 | Word Break | Medium | DP (1‑D) | dp[i] from dict matches | O(n·k) | O(n) |  | https://leetcode.com/problems/word-break/ |
| [ ] | 300 | Longest Increasing Subsequence | Medium | DP + Binary Search | patience piles | O(n log n) | O(n) |  | https://leetcode.com/problems/longest-increasing-subsequence/ |
| [ ] | 416 | Partition Equal Subset Sum | Medium | DP (1‑D knapsack) | boolean subset sum | O(n·S) | O(S) |  | https://leetcode.com/problems/partition-equal-subset-sum/ |
| [ ] | 62 | Unique Paths | Medium | DP (2‑D) | comb or dp grid | O(mn) | O(mn) |  | https://leetcode.com/problems/unique-paths/ |
| [ ] | 1143 | Longest Common Subsequence | Medium | DP (2‑D) | classic LCS table | O(nm) | O(nm) |  | https://leetcode.com/problems/longest-common-subsequence/ |
| [ ] | 72 | Edit Distance | Hard | DP (2‑D) | Levenshtein | O(nm) | O(nm) |  | https://leetcode.com/problems/edit-distance/ |
| [ ] | 518 | Coin Change II | Medium | DP (2‑D) | combinations orderless | O(n·A) | O(A) |  | https://leetcode.com/problems/coin-change-ii/ |
| [ ] | 97 | Interleaving String | Medium | DP (2‑D) | dp[i][j] from s1/s2 picks | O(nm) | O(nm) |  | https://leetcode.com/problems/interleaving-string/ |
| [ ] | 329 | Longest Increasing Path in a Matrix | Hard | DP + DFS | memoize cells | O(mn) | O(mn) |  | https://leetcode.com/problems/longest-increasing-path-in-a-matrix/ |
| [ ] | 115 | Distinct Subsequences | Hard | DP (2‑D) | count subsequences | O(nm) | O(nm) |  | https://leetcode.com/problems/distinct-subsequences/ |
| [ ] | 53 | Maximum Subarray | Medium | Greedy (Kadane) | best prefix sum | O(n) | O(1) |  | https://leetcode.com/problems/maximum-subarray/ |
| [ ] | 55 | Jump Game | Medium | Greedy | track farthest | O(n) | O(1) |  | https://leetcode.com/problems/jump-game/ |
| [ ] | 45 | Jump Game II | Medium | Greedy | layer jumps | O(n) | O(1) |  | https://leetcode.com/problems/jump-game-ii/ |
| [ ] | 134 | Gas Station | Medium | Greedy | total + start index | O(n) | O(1) |  | https://leetcode.com/problems/gas-station/ |
| [ ] | 763 | Partition Labels | Medium | Greedy | last occurrence window | O(n) | O(1) |  | https://leetcode.com/problems/partition-labels/ |
| [ ] | 435 | Non-overlapping Intervals | Medium | Greedy, Intervals | sort by end | O(n log n) | O(1) |  | https://leetcode.com/problems/non-overlapping-intervals/ |
| [ ] | 57 | Insert Interval | Medium | Intervals | merge around new | O(n) | O(n) |  | https://leetcode.com/problems/insert-interval/ |
| [ ] | 56 | Merge Intervals | Medium | Intervals, Sorting | sweep & merge | O(n log n) | O(n) |  | https://leetcode.com/problems/merge-intervals/ |
| [ ] | 252 | Meeting Rooms | Easy | Intervals | sort by start | O(n log n) | O(1) |  | https://leetcode.com/problems/meeting-rooms/ |
| [ ] | 253 | Meeting Rooms II | Medium | Intervals, Heap | min‑heap of ends | O(n log n) | O(n) |  | https://leetcode.com/problems/meeting-rooms-ii/ |
| [ ] | 48 | Rotate Image | Medium | Matrix | transpose + reverse | O(n^2) | O(1) |  | https://leetcode.com/problems/rotate-image/ |
| [ ] | 54 | Spiral Matrix | Medium | Matrix | layer traversal | O(mn) | O(1) |  | https://leetcode.com/problems/spiral-matrix/ |
| [ ] | 73 | Set Matrix Zeroes | Medium | Matrix | first row/col markers | O(mn) | O(1) |  | https://leetcode.com/problems/set-matrix-zeroes/ |
| [ ] | 202 | Happy Number | Easy | Math, Hash Set | detect cycle | O(log n) | O(1) |  | https://leetcode.com/problems/happy-number/ |
| [ ] | 50 | Pow(x, n) | Medium | Math, Binary Exp | fast power | O(log n) | O(1) |  | https://leetcode.com/problems/powx-n/ |
| [ ] | 43 | Multiply Strings | Medium | Math | manual multiplication | O(nm) | O(n+m) |  | https://leetcode.com/problems/multiply-strings/ |
| [ ] | 136 | Single Number | Easy | Bit | XOR trick | O(n) | O(1) |  | https://leetcode.com/problems/single-number/ |
| [ ] | 191 | Number of 1 Bits | Easy | Bit | n &= n-1 loop | O(k) | O(1) |  | https://leetcode.com/problems/number-of-1-bits/ |
| [ ] | 338 | Counting Bits | Easy | Bit, DP | dp[i]=dp[i>>1]+(i&1) | O(n) | O(n) |  | https://leetcode.com/problems/counting-bits/ |
| [ ] | 190 | Reverse Bits | Easy | Bit | build result bitwise | O(1) | O(1) |  | https://leetcode.com/problems/reverse-bits/ |
| [ ] | 268 | Missing Number | Easy | Bit / Math | XOR or gauss sum | O(n) | O(1) |  | https://leetcode.com/problems/missing-number/ |

---


**Headers (CSV)**  
```
Solved,#,Title,Difficulty,Tags / Algo,Approach Notes,Time,Space,Date Solved,URL
```

**Example row**  
```
[x],217,Contains Duplicate,Easy,Array|Hash Map,Use a set; early exit on seen element,O(n),O(n),2025-07-29,https://leetcode.com/problems/contains-duplicate/
```

---

### License

MIT
