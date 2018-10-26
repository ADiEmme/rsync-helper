# rsync-helper
Background: It was 3 am and my friend and I were just back after a night in the city (if you know what i mean) (ok maybe you dont. But i meant drinking in the city).
He brought home his HDD from his laptop and it would give I/O errors.

We wanted to make a copy of the data on it, but rsync would just hang while IO errors would spawn in the dmesg. 
That meant that you would have to exclude the file manually and restart the rsync.

Here's the idea:
What if i had a python script which would start 2 threads, one used to monitor the output of dmesg and the other one to actually make the copy.
The thread monitoring the dmesg, will simply kill the thread that is running rsync but before doing so, it will save the filename that's triggering the IO errors in a list of files which will be excluded.
And there you have your simple script written in ~40minutes that does the job for you!

