# from collectuons import defaultdict
class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        # people.sort()
        # l = 0
        # r = len(people) - 1
        # op = defaultdict(list)

        # while l<r:
        #     if people[l] == limit: 
        #         op[key].append(people[l])
        #         l+=1
        #     elif people[r] == limit:
        #         op[key].append(people[l])
        #         r-=1
        #     elif people[r]+people[l] == limit:
        #         op[key].append([people[l],people[r]])
        #         l+=1
        #         r-=1
        #     el

        people.sort()
        
        res = 0 #boats
        l, r = 0, len(people) - 1

        while l<=r:
            remain = limit - people[r]
            r-=1
            res+=1
        
            if l<=r and remain >= people[l]:
                l+=1
        
        return res




        