def solution(absolutes, signs):
    signs = np.where(np.array(signs) == False, -1, 1)
    li = [a*s for a,s in zip(absolutes, list(signs))]
    return int(sum(li))

import numpy as np