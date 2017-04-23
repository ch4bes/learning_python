# deepsleep
## Sleep analysis with deep learning.

The aim of this project is to be able to accurately predict the quality of a nights sleep based on a timelapse of the subject in bed.

Steps:
- collect images of subject during sleep cycles
    - Use cron to capture image every minute
- organize images into folders for training data
    - individual folders for each tag
    - unknowns go in skipped folder (could be used for future training/analysis)
    - organizational structure looks like this:

In Bed | Out of Bed | Skip
--- | --- | ---
[Awake] / [Asleep] | [In Room] / [Out of Room] | [Skipped]


- use training data to train main sleep analysis program
- test program on new images

---
The main goal is to get the program to accurately predict if the subject in a photo is **awake** or **asleep**. If that goal is ever actually met, the end goal is to take the program further, to a deeper level of complexity. Taking into consideration how often the subject moves, body orientation, if/when they got up to pee in the night, how long it took to fall asleep/wake up, and other such factors, a more accurate prediction of sleep cycles should emerge. The training can be improved tremendously using data like actual brain activity scans during the timelapse recorded sleep cycles.

In reality, this project is just a way for me to teach myself python, git, deep learning, etc, while learning more about my own sleep habits. I don't foresee ever getting close to completing this project.
