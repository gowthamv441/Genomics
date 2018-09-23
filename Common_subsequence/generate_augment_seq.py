import glob
import cv2
def generate_augmented_seq():
    img_list=glob.glob("./augmented_bfsp2/*.png")
    for image in img_list:
        img=cv2.imread(image)
        h,w,c=img.shape
        for i in range(0,h):
            for j in range(0,w):
                print (img[i,j],)
            print ("\n")
        print ("\n\n\n")


if __name__=='__main__':
    generate_augmented_seq()
