# ConvertToGrayscale.py Lab
# ========================

For this lab, we were supposed to create a python file that would take a
video and would transfer it to grayscale using threads and queues. These
queus that we are supposed to use are queues that we are supposed to create.
These queues have a put and get method, and are under ThreadedQueue.py. The
grayscale uses 3 threads and 2 queues, one thread to extract the video, the
second one to convert the video to grayscale, and the last one to display
the video. For the queues, the first one is to store the extracted parts of
the video, and the second one is to store the converted parts of the video.
This file that we made gets the video that was given to us, which would be
the "clip.mp4".

### How To Run The Python File
### ==========================

In order to run the file, you must input "python3 ConvertToGrayscale.py" in
the terminal, and it should run the file, telling you which frames were
extracted, which ones were converted and which ones were displayed.
