import glob
import cv2
import numpy as np
def folding():
    img_paths=glob.glob("../gene_image_dataset/*/*.png")
    list1=[]
    for img_path in img_paths:
        img_name=img_path.split('\\')
        gene_name=img_name[1]
        img=cv2.imread(img_path)
        height,width,channels=img.shape
        new_img = np.zeros((height//2,width,3), np.uint8)
        for i in range(0,width):
            first=0
            last=height-1
            for j in range(0,height//2):
                b1=img[first,i][0]+img[last,i][0]
                if (b1>255):
                    b=min(img[first,i][0],img[last,i][0])
                else:
                    b=b1
                g1=img[first,i][1]+img[last,i][1]
                if (g1>255):
                    g=min(img[first,i][1],img[last,i][1])
                else:
                    g=g1
                r1=img[first,i][2]+img[last,i][2]
                if (r1>255):
                    r=min(img[first,i][2],img[last,i][2])
                else:
                    r=r1
                new_img[j,i]=(b,g,r)
                first+=1
                last-=1
        target_img=np.zeros((height//2,width//2,3), np.uint8)
        for i in range(0,height//2):
            first=0
            last=width-1
            for j in range(0,width//2):
                b1=img[i,first][0]+img[i,last][0]
                if (b1>255):
                    b=min(img[i,first][0],img[i,last][0])
                else:
                    b=b1
                g1=img[i,first][1]+img[i,last][1]
                if (g1>255):
                    g=min(img[i,first][1],img[i,last][1])
                else:
                    g=g1
                r1=img[i,first][2]+img[i,last][2]
                if (r1>255):
                    r=min(img[i,first][2],img[i,last][2])
                else:
                    r=r1
                target_img[i,j]=(b,g,r)
                first+=1
                last-=1
        cv2.imwrite("./folded_img_dataset/"+str(gene_name)+"/four_fold_"+str(img_name[2]),target_img)
        cv2.destroyAllWindows()

if __name__=='__main__':
    folding()
