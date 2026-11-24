from flask import Flask,redirect
from routes.admin import admin_bp
from routes.tracking import tracking_bp

app = Flask(__name__)

app.route('/')
def bsdchdf():
    return redirect('/tracking')

app.register_blueprint(admin_bp)
app.register_blueprint(tracking_bp)

"""
hm. kmaren sy lgi bersih2 drive , sambil nampung ppt ppt materi selama kuliah,
nah jadi sy nemu folder aneh "video random" , ini apa? pas dilihat punya pak farras, tapi masa pak farras ngpublic
video random, 

pas sy buka foldernya , nah.. mn mpp , video video mu lo disitu? 
km salah upload kayaknya, malah upload video random di folder pengumpulan tugas,
semuanya dh sy hapus, takut private kan. tinggal itu buka lagi coba di hapus dari situ. dilihat sekampus apa ndak .. 

"""

if __name__ == "__main__":
    app.run(debug=True)
