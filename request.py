import requests
import re
import json
from moviepy.editor import *



cookie = "buvid3=05BBA315-4AE0-E5AA-A4B1-FE32186A709C97914infoc; b_nut=1726844597; _uuid=7B1D8DC6-7610A-55410-5C4B-662CCBB3133702076infoc; enable_web_push=DISABLE; buvid4=7F350123-4207-5886-8560-590C59C9D44539014-024051710-XePsh5KyhGPNUPyqWXTooQ%3D%3D; rpdid=0zbfVGjVWx|ERwdcfir|19z|3w1SRFay; fingerprint=a40c4a727230de7d5202295283540637; buvid_fp_plain=undefined; DedeUserID=1445623049; DedeUserID__ckMd5=3ee8137729273354; header_theme_version=CLOSE; hit-dyn-v2=1; buvid_fp=a40c4a727230de7d5202295283540637; home_feed_column=5; enable_feed_channel=ENABLE; bili_ticket=eyJhbGciOiJIUzI1NiIsImtpZCI6InMwMyIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3NDE2MDg0NDEsImlhdCI6MTc0MTM0OTE4MSwicGx0IjotMX0.JXLzqnmgR6ZKR2rjznJH_Gr0kbKZaaqYfDuxGgdjlkA; bili_ticket_expires=1741608381; SESSDATA=0fed0f6c%2C1756901241%2Cd2d78%2A31CjBClKXueGDrOO0e7JnzCB7pBov6bfCoPWUmIRRRkvxJp2epEzJm4OPcdnSjkMhR3nQSVlZac1JuU2g4akw1NkFoM3I3ci1JaXlUSFB5c2hPS0xWa0FLZlE4UllnY2NaR1NWRWtqSHFNM2g2SDJfckZkZ00yZ2pJcFZuYTVqVG5WQnZqNVJ4Z2V3IIEC; bili_jct=08f97f502bc5e5d8a3974e8a93f33efc; browser_resolution=2202-1415; CURRENT_FNVAL=4048; CURRENT_QUALITY=32; bp_t_offset_1445623049=1041933811601899520; b_lsid=EBC2C7CD_19575B79E39; sid=glakli54; bmg_af_switch=1; bmg_src_def_domain=i0.hdslb.com"
"""
数据包地址  https://www.bilibili.com/video/BV1wZ421e7Fr/?spm_id_from=333.788.videopod.episodes&vd_source=280de362069a38d36a67ebd53f75156f&p
"""



def GetResponse(url):
    """发送请求 ： 模拟浏览器发送请求"""
    # 模拟浏览器
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36 Edg/133.0.0.0",
        "Referer": "https://www.bilibili.com/video/BV1wZ421e7Fr/?spm_id_from=333.788.videopod.episodes&vd_source=280de362069a38d36a67ebd53f75156f&p",
        "Cookie": cookie
    }
    # 发送请求
    response = requests.get(url, headers=headers)
    # 返回响应
    return response


def GetVideoInfo(bv):
    """获取视频信息"""
    # 视频地址 ： 视频播放页链接地址
    link = f"https://www.bilibili.com/video/{bv}"
    # 调用发送请求函数
    html = GetResponse(link).text
    # 音视频信息
    title = re.findall('<title data-vue-meta="true">(.*?)</title>', html)[0]
    html = re.findall('<script>window.__playinfo__=(.*?)</script>', html)[0]
    # 转成json格式
    html = json.loads(html)
    # 根据键获取值
    audio_url = html["data"]["dash"]["audio"][0]["baseUrl"]
    video_url = html["data"]["dash"]["video"][0]["baseUrl"]
    return audio_url, video_url, title


def Save(audio, video):
    """保存视频"""
    # 保存视频
    with open("video.mp4", "wb") as f:
        f.write(video)
    # 保存音频
    with open("audio.mp3", "wb") as f:
        f.write(audio)

if __name__ == '__main__':
    bv = input("Program | 请输入视频bv号：")
    try:
        print("Program | 即将获取url")
        audio_url, video_url, title = GetVideoInfo(bv=bv)
        title = title.replace("_", "").replace(" ", "").replace("&", "").replace("?", "").replace("!", "").replace(":", "")
        print(title)
    except IndexError:
        print("ERROR | 视频不存在")
        exit()
    except Exception as e:  # 可能出现的错误 1. 输入错误的bv号 2. 网络错误
        print(f"(1)ERROR | 发生错误\n{e}")
        exit()
    try:
        print("Program | 即将获取音视频")
        audio = GetResponse(audio_url).content
        video = GetResponse(video_url).content
    except Exception as e:  # 可能出现的错误 1. 查找不到音视频链接 
        print(f"(2)ERROR | 发生错误\n{e}")
        exit()
    try:
        print("Program | 即将保存视频")
        Save(audio=audio, video=video)
    except Exception as e:  # 可能出现的错误 1. 路径找不到 2. 权限不足
        print(f"(3)ERROR | 发生错误\n{e}")
        exit()
    print("Program | 视频和音频下载完成!")
    print("Program | 正在合成视频...")
    video = VideoFileClip("video.mp4")
    audio = AudioFileClip("audio.mp3")
    video = video.set_audio(audio)
    video.write_videofile(f"{title}.mp4")
    print("Program | 合成完成!")
    print(f"Program | 视频已保存为{title}.mp4")
    print("Program | 即将删除音频")
    os.remove("audio.mp3")