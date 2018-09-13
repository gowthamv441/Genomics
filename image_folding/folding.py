import glob
import cv2
import numpy as np
def horizontal_folding():
    img_paths=glob.glob("../gene_image_dataset/*/*.png")
    for img_path in img_paths:
        img_name=img_path.split('\\')
        img=cv2.imread(img_path)
        height,width,channels=img.shape
        new_img = np.zeros((height//2,width,3), np.uint8)
        for i in range(0,width):
            first=0
            last=height-1
            for j in range(0,height//2):
                b=min(img[first,i][0]+img[last,i][0],255)
                g=min(img[first,i][1]+img[last,i][1],255)
                r=min(img[first,i][2]+img[last,i][2],255)
                new_img[j,i]=(b,g,r)
                first+=1
                last-=1
        cv2.imwrite("./folded_img_dataset/horizontal_fold_"+str(img_name[2]),new_img)
        cv2.destroyAllWindows()

def vertical_folding():
    img_paths=glob.glob("../gene_image_dataset/*/*.png")
    for img_path in img_paths:
        img_name=img_path.split('\\')
        img=cv2.imread(img_path)
        height,width,channels=img.shape
        new_img = np.zeros((height,width//2,3), np.uint8)
        for i in range(0,height):
            first=0
            last=width-1
            for j in range(0,width//2):
                b=min(img[i,first][0]+img[i,last][0],255)
                g=min(img[i,first][1]+img[i,last][1],255)
                r=min(img[i,first][2]+img[i,last][2],255)
                new_img[i,j]=(b,g,r)
                first+=1
                last-=1
        cv2.imwrite("./folded_img_dataset/vertical_fold_"+str(img_name[2]),new_img)
        cv2.destroyAllWindows()
        
if __name__=='__main__':
    horizontal_folding()
    vertical_folding()
