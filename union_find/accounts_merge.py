class Solution:

    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:

        email_to_idx: Dict[str, int] = {}   # email → bucket index
        buckets: List[Set[str]] = []        # idx → set of emails
        names:   List[str]      = []        # idx → account name

        for record in accounts:
            name, *emails = record

            seen = {email_to_idx[e] for e in emails if e in email_to_idx}

            # ------------------- create NEW bucket ------------------------

            if not seen:
                idx = len(buckets)
                buckets.append(set(emails))
                names.append(name)
                for e in emails:
                    email_to_idx[e] = idx
                continue 
            
            # --------------- MERGE into existing bucket ----------------

            # Choose survivor: largest bucket for better amortised cost
            idx = max(seen, key=lambda x: len(buckets[x]))
            seen.remove(idx)

            for other in seen:
                if buckets[other]:
                    buckets[idx].update(buckets[other])
                    
                    for e in buckets[other]:
                        email_to_idx[e] = idx
                    
                    buckets[other].clear()
            
            for e in emails:
                if e not in email_to_idx:
                    buckets[idx].add(e)
                email_to_idx[e] = idx

        result = [
            [names[i]] + sorted(list(emails))
            for i, emails in enumerate(buckets) if emails
        ]
        return result
