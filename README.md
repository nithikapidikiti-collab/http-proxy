# HTTP Intercepting Proxy

A lightweight HTTP proxy that intercepts and logs real web traffic in real time, built from scratch using raw Python sockets and threading.

## How to run

```
python3 proxy.py
```

Then in another terminal:
curl -x http://127.0.0.1:8888 http://neverssl.com

## Demo
[>] GET http://neverssl.com/ -> neverssl.com:80

Full HTML response intercepted and forwarded successfully.

## Concepts demonstrated

- HTTP request parsing
- Raw socket forwarding
- Man-in-the-middle proxy architecture
- Threading for concurrent connections
- How tools like Burp Suite work under the hood

## What I'd add next

- HTTPS CONNECT tunnelling
- Request/response logging to file
- Content filtering
- Request modification
