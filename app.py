from flask import Flask, request, render_template
import bypass_functions

app = Flask(__name__)
linkvertiseSites = ["linkvertise.com", "link-to.net", "up-to-down.net", "direct-link.net", "file-link.net"]

@app.route("/")
def home():
    return render_template("index.html")
  
@app.route("/api/bypass", methods=["GET"])
def bypass():
    url = request.args.get("url")
    if url == None:
        return "Une URL doit être spécifiée."
    if not "https://" in url:
        if not "http://" in url:
            return "URL invalide."
    for linkvertiseSite in linkvertiseSites:
        if linkvertiseSite in url:
            return bypass_functions.bypassLinkvertise(url)
    if "rekonise.com" in url:
        return bypass_functions.bypassRekonise(url)
    elif "sub2unlock.com" in url:
        return bypass_functions.bypassSub2Unlock(url)
    elif "clictune.com" in url:
        return bypass_functions.bypassClictune(url)
    elif "mylink1.biz" in url:
        return bypass_functions.bypassClictune(url)
    elif "movincle.com" in url:
        return bypass_functions.bypassAdfLy(url)
    elif "q.gs" in url:
        return bypass_functions.bypassAdfLy(url)
    elif "j.gs" in url:
        return bypass_functions.bypassAdfLy(url)
    elif "adf.ly" in url:
        return bypass_functions.bypassAdfLy(url)
    elif "aporasal.net" in url:
        return bypass_functions.bypassAdfLy(url)
    elif "short-url.link" in url:
        return bypass_functions.bypassShortUrlLink(url)
    else:
        return "URL invalide."
    

if __name__ == "__main__":
    app.run()
