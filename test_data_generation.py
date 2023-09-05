import os
import cv2

# Make sure to create the necessary folders before running the script
os.makedirs('./Testh_gt', exist_ok=True)
os.makedirs('./Testh', exist_ok=True)

# Download Test Data provided by authors Ziyi et al. from,
# https://sites.google.com/site/ziyishenmi/cvpr18_face_deblur
# and place the files in the corresponding directories.

# Assuming the images are located in './Test_data_Helen/final_Helen_gt' and './Test_data_Helen/final_Helen_blur' folders
image_gt_dir = './Test_data_Helen/final_Helen_gt'
image_blur_dir = './Test_data_Helen/final_Helen_blur'

image_gt_list = os.listdir(image_gt_dir)
m = len(image_gt_list)

count = 1
for i in range(m):
    img_name = image_gt_list[i]
    I = cv2.imread(os.path.join(image_gt_dir, img_name))
    im_name, _ = os.path.splitext(img_name)

    for j in range(1, 11):
        for k in range(13, 28, 2):
            blr_name = os.path.join(
                image_blur_dir, f"{im_name}_ker{j:02d}_blur_k{k}.png")
            B = cv2.imread(blr_name)

            gt_filename = os.path.join('./Testh_gt', f"{count:06d}.png")
            cv2.imwrite(gt_filename, I)

            blur_filename = os.path.join('./Testh', f"{count:06d}.png")
            cv2.imwrite(blur_filename, B)

            count = count + 1

    print(f"Processed {img_name}")

print("Finished processing all images.")
