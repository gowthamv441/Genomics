import glob
def Common_sequence(X, Y):
    m = len(X)
    n = len(Y)
    L = [[0 for i in range(n+1)] for j in range(2)]
    bi = bool
    for i in range(m):
        bi = i&1
        for j in range(n+1):
            if (i == 0 or j == 0):
                L[bi][j] = 0
            elif (X[i] == Y[j - 1]):
                L[bi][j] = L[1 - bi][j - 1] + 1
            else:
                L[bi][j] = max(L[1 - bi][j],
                               L[bi][j - 1])
    return L[bi][n]


if __name__=='__main__':
    ts=
    seq_file_list=glob.glob("../sequence-data/*/*.fasta")
    for file in seq_file_list:
        print (file)
        dsptr=open(file)
        fl=0
        ds=""
        for line in dsptr.readlines():
            if fl==0:
                fl=1
            else:
                ds+=line
    print("Common Sequence length :: {}".format(Common_sequence(ds, ts)))
