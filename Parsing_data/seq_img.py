import numpy as np
import cv2
import glob
def parse():
    sequence_list=glob.glob("../sequence-data/*/*.fasta")
    img_count=1
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
            # G - Green (0,255,0)
            # A - RED (0,0,255)
            # T - Blue (255,0,0)
            # C - Black (0,0,0)
            # gaps - White (255,255,255)
            height=300
            width=300
            img = np.zeros((height,width,3), np.uint8)
            ptr=0
            for i in range(height):
                for j in range(width):
                    if ptr < len(seq):
                        if seq[ptr]=='G':
                            img[i,j]=(0,255,0)
                        elif seq[ptr]=='A':
                            img[i,j]=(0,0,255)
                        elif seq[ptr]=='T':
                            img[i,j]=(255,0,0)
                        elif seq[ptr]=='C':
                            img[i,j]=(0,0,0)
                    else:
                        img[i,j]=(255,255,255)
                    ptr+=1
            cv2.imwrite('../gene_image_dataset/'+gene_name+'/'+str(img_count)+'.png',img)
            img_count+=1
            cv2.destroyAllWindows()
            print ("[INFO] Image Created for Gene {}".format(gene_name))
        except:
            print ("[INFO] error processing {} ... skipping".format(item))

if __name__=="__main__":
    parse()
