import numpy as np

def M(rho, n=1):
    m = rho.shape[0]//2
    prjs =[np.kron(s[:, np.newaxis],s[:, np.newaxis].T)
        for s in np.eye(m * 2)]
    pr =[np.abs(np.trace(prj.dot(rho))) for prj in prjs]
    res= np.random.choice(
        [i for i in range(m*2)], n, p=pr)
    return [np.eye(m*2)[r,:] for r in res]