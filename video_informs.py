from youtube.objects.video import Video
from youtube.db import get_db

def loadVideos(email):
    db = get_db()
    videos = []
    dbVideo = db.execute(
        'SELECT video.code, video.nameVideo, video.descriptionVideo, video.localization \
        FROM video_details \
        INNER JOIN userMyoutube ON video_details.code_user = userMyoutube.email \
        INNER JOIN video ON video_details.code_video = video.code \
        WHERE userMyoutube.email = ?', (email,)
    ).fetchall()

    for i in dbVideo:
        video_informs = []
        for j in i:
            video_informs.append(j)
        
        video = Video(str(video_informs[0]), video_informs[1], video_informs[2], video_informs[3])
        videos.append(video)

    return videos