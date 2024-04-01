from flask import Flask, render_template
import os
import random

app = Flask(__name__)

# list of cat images
images = [
    "https://media0.giphy.com/media/XGhGacEaO9PQ1Kgck3/giphy.gif",
    "https://media.tenor.com/63MNKF77-jIAAAAM/oops-accident.gif",
    "https://img.huffingtonpost.com/asset/5b9cf2cf1f00002d00216ca1.gif?ops=scalefit_960_noupscale",
    "https://media1.giphy.com/media/26FPLsoMq5cPEVgg8/200w.gif?cid=6c09b9522ir0ffywvwrs31wxt41gqjr6ntbn5eyj2xkutbj9&ep=v1_gifs_search&rid=200w.gif&ct=g",
    "https://media2.giphy.com/media/63WqgX4XjeFLUKYwx2/200w.gif?cid=6c09b952l81fhwl0j94u1xkmej2u3xjpnqjz0szcxg5z44e0&ep=v1_gifs_search&rid=200w.gif&ct=g",
    "https://media3.giphy.com/media/VIMDNQUn0rQ0L4ojIr/200w.gif?cid=6c09b9521vl8qekho25jxqs56yg396nzrcaktf087yggi8pq&ep=v1_gifs_search&rid=200w.gif&ct=g",
    "https://media2.giphy.com/media/63WqgX4XjeFLUKYwx2/200w.gif?cid=6c09b952l81fhwl0j94u1xkmej2u3xjpnqjz0szcxg5z44e0&ep=v1_gifs_search&rid=200w.gif&ct=g",
    "https://media.tenor.com/LELaYsNcUb0AAAAM/baby-vomit.gif",
    "https://media4.giphy.com/media/12P6AnN6DcQj1S/giphy.gif",
    "https://thumbs.gfycat.com/WideeyedEnchantedHog-max-1mb.gif",
    "https://gifbin.com/bin/102009/1255351825_baby-puke.gif",
    "https://media4.giphy.com/media/l4KibWpBGWchSqCRy/giphy.gif?cid=ecf05e47c1vwa7ebzrwjrry8e0lhqxqlezoy0fu34amuse6p&ep=v1_gifs_search&rid=giphy.gif&ct=g",
    "https://media1.giphy.com/media/NQL7Wuo2JSQSY/giphy.gif?cid=ecf05e47penh6t4r3lde9vztrpbd7flo9ftpk03zguvtpaun&ep=v1_gifs_search&rid=giphy.gif&ct=g"
]


@app.route("/")
def index()
    url = random.choice(images)
    return render_template("index.html", url=url)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
