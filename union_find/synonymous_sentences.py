class Solution:


    def build_groups(self, pairs: List[List[str]]) -> Tuple[Dict[str, List[str]], Dict[str, str]]:
        """
        Returns
        -------
        groups : Dict[root_word, List[str]]
            Each root maps to the lexicographically‑sorted list of all
            words in its synonym component.
        parent : Dict[word, str]
            Union‑Find parent table (after path‑compression), so
            `parent[w]` is the root word representing w’s component.
        """

        parent: Dict[str, str] = {}

        def find(x):
            parent.setdefault(x, x)
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(a, b):
            ra, rb = find(a), find(b)
            if ra != rb:
                parent[max(ra, rb)] = min(ra, rb)

        for a, b in pairs:
            union(a, b)
        
        groups = defaultdict(list)
        for w in parent:
            groups[find(w)].append(w)
        
        for bucket in groups.values():
            bucket.sort()

        return groups, parent


    def generateSentences(self, synonyms: List[List[str]], text: str) -> List[str]:
        
        groups, parent = self.build_groups(synonyms)
        words = text.split()
        choices = [
            groups[parent[w]] if w in parent else [w]
            for w in words
        ]

        res, path = [], []

        def dfs(idx):
            if idx == len(choices):
                res.append(" ".join(path))
                return
            for word in choices[idx]:
                path.append(word)
                dfs(idx + 1)
                path.pop()

        dfs(0)
        return res
