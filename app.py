
import json
import shutil
import textwrap

from flask import Flask, jsonify, request, send_file, render_template, redirect, url_for
from PIL import Image, ImageDraw, ImageFont
from ytdownload import download_youtube_video

app = Flask(__name__)


@app.route('/download')
def query_example():
    shutil.rmtree('./temp')  # delete temp folder and all files in it

    # request.args is a MultiDict (like a dict but can have multiple values for the same key)
    query_object_arr = {}

    #
    for key, value in request.args.items():
        query_object_arr[key] = value

    # Download youtube video from link and save to temp folder
    [video_name, title] = download_youtube_video(query_object_arr["link"])

    # Video Path
    # video_name = "temp/" + video_name
    video_name = video_name.replace(" ", "%20")
    video_name = f"https://github.com/shaantanu9/youtube_downloader_flask_app/blob/main/temp/{video_name}?raw=true"
    # return send_file(video_name, mimetype='video/mp4')
    # return send_file(video_name, mimetype='video/mp4', as_attachment=True, attachment_filename=title + ".mp4")
    # return render_template('/template/download.html', video_name=video_name, title=title)
    # redirect url
    return redirect(video_name, code=302)


if __name__ == '__main__':
    app.run()
