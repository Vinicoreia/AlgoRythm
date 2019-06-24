class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        visits = {}
        for el in cpdomains:
            visit_domain = el.split(' ')
            domain = collections.deque()
            for letter in visit_domain[1][::-1]:
                if(letter=='.'):
                    try:
                        visits["".join(domain)] += int(visit_domain[0])
                    except:
                        visits["".join(domain)] = int(visit_domain[0])
                domain.appendleft(letter)
            try:
                        visits["".join(domain)] += int(visit_domain[0])
            except:
                visits["".join(domain)] = int(visit_domain[0])
        result = []
        for key, value in visits.items():
            s = str(value) + " " + key
            result.append(s)
        return result