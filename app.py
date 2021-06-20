import streamlit as st
from pytube import YouTube

st.title("Youtube Video Donwloader")
st.info('南山金融科技- 文字探勘專題 (第四組) 文本生成-市場焦點機器人')

st.write('1.南山人壽三分鐘短片\n2.南山人壽十五分鐘介紹影片')

st.write(
'''
1.南山人壽三分鐘短片
https://www.youtube.com/watch?v=sia8o_xN8ag

2.南山人壽十五分鐘介紹影片
https://www.youtube.com/watch?v=YFBpGaHVnz8
''')

yt_url=[('1.南山人壽三分鐘短片','https://www.youtube.com/watch?v=sia8o_xN8ag'),
        ('2.南山人壽十五分鐘介紹影片','https://www.youtube.com/watch?v=YFBpGaHVnz8')]
st.subheader("Enter the URL:")
url = st.text_input(label='URL', value=yt_url[1][1])

if url != '':
    st.write('Getting the Data for the Youtube video')
    yt = YouTube(url)
    st.image(yt.thumbnail_url, width=300)

    st.write('Understanding the Stream Object')
    print(yt.streams)


    st.subheader('''
    {}
    ## Length: {} seconds
    ## Rating: {} 
    '''.format(yt.title , yt.length , yt.rating))
    video = yt.streams

    st.write('Chosing a Stream Object to Download')


    if len(video) > 0:
        downloaded , download_audio = False , False
        download_video = st.button("Download Video")
        if yt.streams.filter(only_audio=True):
            download_audio = st.button("Download Audio Only")
        if download_video:
            video.get_lowest_resolution().download()
            downloaded = True
        if download_audio:
            video.filter(only_audio=True).first().download()
            downloaded = True
        if downloaded:
            st.subheader("Download Complete")
    else:
        st.subheader("Sorry, this video can not be downloaded")