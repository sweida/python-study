

import ffmpy3

ff = ffmpy3.FFmpeg(
    inputs={'001.avi': None},
    outputs={'006.mp4': None}
)
# ff = ffplay(001.mp4)
ff.run()

# # 播放001.MP4视频
# ffplay 001.mp4

# # 将001.avi转换成005.MP4 码率为2400K
# ffmpeg - i 001.avi - b: v 2400k 005.mp4
