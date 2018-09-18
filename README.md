# reparameterization_deeplearning

## requirement
1. Tensorflow
2. opencv `pip install opencv-python`
## Usage
1. `extract.py NTU NTU_frame` will convert videos into frames, the The structure of NTU_frame is like this:
        ```
        NTU_frame\label_1\video_name1\frame_picture1\
        ```
2. `convert_images_to_lists.sh NTU_frame_path 5` will generate two lists: train.list and test.list. number 5 means 20% of the set is be divided into test set.

3. `python train.py` will train the model.

4. `python test.py` will test the model.
            

