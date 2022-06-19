# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        def printval(l):
            val = []
            for node in l:
                if node: val.append(node.val)
                else:    val.append("None")
            print(val)
            return 
        
        def printlist(p):
            val= [] 
            for i in range(100):
                val.append(p.val)
                if p.next:
                    p = p.next
                else:  break
            print(val)
            return 
        
        def merge(i1, i2):
            if i2 >= len(lists): return 
            print(f"merge {i1} {i2}")
            if not lists[i2]: 
                return 
            if not lists[i1]: 
                lists[i1], lists[i2] = lists[i2], lists[i1]
                return 
                
            if lists[i1].val > lists[i2].val:
                lists[i1], lists[i2] = lists[i2], lists[i1]
            
            head = lists[i1]
            ptr1 = lists[i1]
            ptr2 = lists[i2]
            
            switch = True #True: ptr1, False: ptr2
            while ptr1 and ptr2:
                printval([ptr1, ptr2])
                if switch:
                    next_val = ptr1.next.val if ptr1.next else float("inf")
                    if next_val <= ptr2.val: ptr1 = ptr1.next
                    else: 
                        remember = ptr1
                        ptr1 = ptr1.next 
                        remember.next = ptr2
                        switch = not switch
                else:
                    next_val = ptr2.next.val if ptr2.next else float("inf")
                    if next_val <= ptr1.val: ptr2 = ptr2.next
                    else: 
                        remember = ptr2
                        ptr2 = ptr2.next 
                        remember.next = ptr1
                        switch = not switch        
            
            printlist(head)
            return 
        
        if not lists: return None
        
        for r in range(20):
            jump = 2**r
            if jump >= len(lists): break
            
            for i in range(0, len(lists), 2*jump):  
                merge(i, i+jump)
                
            
        return lists[0]