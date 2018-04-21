import os
from flask import Flask , render_template,request,redirect, url_for
from flask import send_from_directory,jsonify
import subprocess
import search
import json

app = Flask(__name__)
app.debug = True
app.static_folder='/root/mp3tube2/static/'
p = os.path.join('/root/mp3tube2/static')
#app.static_folder='C:/Users/SupaDupa/Desktop/mp3tube/mp3tube/static'
#p = os.path.join('C:/Users/SupaDupa/Desktop/mp3tube/mp3tube/static')
print p
@app.route("/dl/<vid>")
def hello(vid):
    video = "https://www.youtube.com/watch?v="+str(vid)
    cmd = subprocess.Popen(["youtube-dl","-o","static/%(title)s-%(id)s.%(ext)s","--extract-audio","--audio-format","mp3","--embed-thumbnail",video],stdout=subprocess.PIPE)
    for line in cmd.stdout:
        print line +'\n'
        if ".mp3" in line:
            name = line[29:]
            print name
            #os.path.isfile('static'/name)
           # return redirect("/static/%s"%name.rstrip())
            return send_from_directory(app.static_folder, name.rstrip(), as_attachment= True)
        #else:
        #    print line
    return 'overload'

@app.route("/")
def get():
    return render_template("index.html")

@app.route("/2")
def get2():
    return render_template("index2.html")

@app.route("/download/")
def dl():
    title = request.args.get("title")
    vid = request.args.get("vid")
    desc = request.args.get("desc")
    return render_template("download.html", title = title, vid = vid, desc = desc)

@app.route("/search/")
def ySearch():
    keyword = request.args.get("q")
    np = request.args.get("np")
    vl = []
    if np and keyword:
        videos = search.youtube_search(keyword,np=np)
    elif keyword:
        videos = search.youtube_search(keyword)
    else:
        videos = search.youtube_search("milehighmuzik")
    np = videos.pop()
	
    for video in videos:
        #video.split('|')
        vl.append(video.split('|kobe|'))
    #print vl
    #print json.dumps(vl)
    #return render_template("search_results.html" , keyword = keyword, videos= vl)
    return jsonify({'vl':vl,'np':np.split('|np|')[1]})

if __name__ == "__main__":
    app.run(threaded=True,host='0.0.0.0',port=5000)
