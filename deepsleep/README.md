# deepsleep
## Sleep analysis with deep learning.

The aim of this project is to be able to accurately predict the quality of a nights sleep based on a timelapse of the subject in bed.

Steps:
1. Collect images of subject during sleep cycles

    - Use cron & image capture program to capture image every minute  
        ###### This method uses less resources than a python program running constantly in the background
    ##### *or*
    - Use timelapse program (without cron)
        ###### Using straight python instead of cron, this method uses more resources but requires less setup
        
2. Organize images into folders for training data

    - Individual folders for each tag  
      - unknowns go in skipped folder (could be used for future training/analysis)
    
    - Organizational structure looks like this:

      In Bed | Out of Bed | Skip
      --- | --- | ---
      [Awake] / [Asleep] | [In Room] / [Out of Room] | [Skipped]


3. Use training data to train main sleep analysis program

4. Test program on new images

---
The main goal is to get the program to accurately predict if the subject in a photo is **awake** or **asleep**. If that goal is ever actually met, the end goal is to take the program further, to a deeper level of complexity. Taking into consideration how often the subject moves, body orientation, if/when they got up to pee in the night, how long it took to fall asleep/wake up, and other such factors, a more accurate prediction of sleep cycles should emerge. The training can be improved tremendously using data like actual brain activity scans during the timelapse recorded sleep cycles.

In reality, this project is just a way for me to teach myself python, git, deep learning, etc, while learning more about my own sleep habits. I don't foresee ever getting close to completing this project.

---

### First Steps
#### Step_1: Collect Images

- **For RPi Camera Module**:

  - Either use:
  
    - cron & [capture_image.py][1] to schedule image capture (less resource use)
    
    *or*
     
    - [timelapse.py][2] without cron (less to setup)
    
- **For USB webcam**:
  - Code not added yet
  
#### Step 2: Organize Images

Once we have a large enough set of images, we need to organize them into individual folders to streamline the training process. Is the subject **_in bed_** or **_out of bed_**? Is the subject in bed **_awake_** or **_asleep_**? etc. (however deep we want to go)

Use [image_sort.py][3] to organize images into folders.

### Next Steps
#### Step 3: Train

Code needs to be written

#### Step 4: Test

Code needs to be written

---

If I can get each individual part to work, I hope to some day write a master program that pieces it all together.

[1]: https://github.com/ch4bes/learning_python/blob/master/deepsleep/code/capture_image.py
[2]: https://github.com/ch4bes/learning_python/blob/master/deepsleep/code/timelapse.py
