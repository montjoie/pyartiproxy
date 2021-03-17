
# For testing:
## testing the proxy
curl -F "directory=tutu" -F "filename=toto" -F "data=@readme.md" http://127.0.0.1:8080/cgi-bin/pyartiproxy.py

## testing artifactorial
curl -F "token=xxxxx" -F "path=@readme.md" http://x.x.x.x:port/artifacts/home/useragl
