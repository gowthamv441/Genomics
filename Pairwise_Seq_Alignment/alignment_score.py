from collections import defaultdict
import glob
import sys
import time
def compute_score(test_data,seq):
    ll=min(len(test_data),len(seq))
    score=0
    for i in range(ll):
        if test_data[i]==seq[i]:
            score+=1
        else:
            score-=1
    print ("[INFO] Alignment Score ==> {}".format(score))
    score+=-2*abs(len(test_data)-len(seq))
    return score

def compute_cost():
        st_time=time.time()
        sequence_list=glob.glob("../sequence-data/*/*.fasta")
        score_dict=defaultdict(list)
        test_ptr=open("../sequence-data/ptprf/0002.fasta")
        tt=""
        start=0
        for l in test_ptr.readlines():
            if start==1:
                tt+=l
            else:
                start=1
        for item in sequence_list:
            f=open(item)
            try:
                path=item.split('\\')
                gene_name=path[1]
                line_count=0
                seq_len=0
                seq=""
                start=0
                for l in f.readlines():
                    if start==1:
                        seq+=l
                    else:
                        start=1
                    seq_len+=len(l)
                    line_count+=1
                print ("[INFO] Analysing... {}".format(item))
                print ("[INFO] Gene Name :: {}".format(gene_name))
                print ("[INFO] line Count {} and Sequence Length {}".format(line_count,seq_len))
                algn_scr=compute_score(tt,seq)
                score_dict[gene_name].append(algn_scr)
            except:
                print ("[INFO] error processing {} ... skipping".format(item))
        prediction=""
        max_scr=-sys.maxsize-1
        for k,v in score_dict.items():
            if max_scr<max(v):
                prediction=k
                max_scr=max(v)
        print ("\n\n[INFO] Predicted genotype --->{}".format(prediction))
        end_time=time.time()
        elapsed=end_time-st_time
        print ("[INFO] Inference Time {}".format(elapsed))

if __name__=='__main__':
    compute_cost()
