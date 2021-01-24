class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    
    def solve(self, A, B):
        Fsum = sum(A[:B])
        Lsum = sum(A[-B:])
        N = len(A)
        mx = max(Fsum,Lsum)
        i=0
        while i < B:
            Fsum = Fsum -A[B-i-1] + A[N-i-1]
            mx = max(mx,Fsum)
            i+=1
        return mx
            
a=[ -533, -666, -500, 169, 724, 478, 358, -38, -536, 705, -855, 281, -173, 961, -509, -5, 942, -173, 436, -609, -396, 902, -847, -708, -618, 421, -284, 718, 895, 447, 726, -229, 538, 869, 912, 667, -701, 35, 894, -297, 811, 322, -667, 673, -336, 141, 711, -747, -132, 547, 644, -338, -243, -963, -141, -277, 741, 529, -222, -684, 35 ]       
ss= Solution()
print(ss.solve(a, 48))     
