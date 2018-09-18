import sys
import os
import subprocess
import cv2
#from csv_generation import  ntu_csv_generation


def video_jpg_process(dir_path, dst_dir_path, video_name):
    if os.path.exists(dir_path):
        filename = video_name[:-4]
        label = 'name'+video_name[17:20]
        video_class_label = label
    else:
        print("No file found")

    dst_class_path = os.path.join(dst_dir_path, video_class_label)
    if not os.path.exists(dst_class_path):
        os.mkdir(dst_class_path)

    dst_frame_path = os.path.join(dst_class_path, filename)
    if not os.path.exists(dst_frame_path):
        os.mkdir(dst_frame_path)
    else:
        subprocess.call('rm -r \"{}\" '.format(dst_frame_path), shell=True)
        print('remove {}'.format(dst_frame_path))
        os.mkdir(dst_frame_path)
    video_file_path = os.path.join(dir_path, video_name)
    video = cv2.VideoCapture(video_file_path)
    count = 1
    if video.isOpened():
        sucess, frame = video.read()
    else:
        sucess = False
    while sucess:
        height = 240
        ratio = 240 / frame.shape[0]
        dim = (int(ratio * frame.shape[1]), 240)
        frame = cv2.resize(frame, dim, interpolation = cv2.INTER_AREA)
        #for i in range(2):
            #frame = cv2.pyrDown(frame)
        str_count = "%04d" % count
        cv2.imwrite(os.path.join(dst_frame_path, str_count+'.jpg'), frame)
        count += 1
        sucess, frame = video.read()
        cv2.waitKey(1)
    video.release()

  #  with open(os.path.join(dst_frame_path, 'n_frames'), 'w') as count_file:
   #     count_file.write(str(count-1))
    return


if __name__=="__main__":
    dir_path = sys.argv[1]
    dst_dir_path = sys.argv[2]

    if not os.path.exists(dst_dir_path):
        os.mkdir(dst_dir_path)

    for video_name in os.listdir(dir_path):
        video_jpg_process(dir_path, dst_dir_path, video_name)



