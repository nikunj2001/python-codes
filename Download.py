import webbrowser
url="https://www.youtube.com/watch?v=rRx88tN2LYo&list=RDrRx88tN2LYo&start_radio=1"
download = url[:12]+"ss"+url[12:]
webbrowser.open(download)