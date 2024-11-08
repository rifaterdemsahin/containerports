 *  Executing task: docker exec -it 9631488788c8d0b941dc2ff104df0aab1f0c160b8660746ba5fcc9be1109aade bash 

root@9631488788c8:/app# nginx -g
nginx: option "-g" requires parameter
root@9631488788c8:/app# nginx 
]2024/11/08 14:45:15 [emerg] 43#43: "server" directive is not allowed here in /etc/nginx/nginx.conf:1
root@9631488788c8:/app# ]
 *  The terminal process "/bin/bash '-c', 'docker exec -it 9631488788c8d0b941dc2ff104df0aab1f0c160b8660746ba5fcc9be1109aade bash'" terminated with exit code: 137. 
 *  Terminal will be reused by tasks, press any key to close it. 

 *  Executing task: docker exec -it 6f5a8caa5a6405ef006eec7eadb6b3e7d8eecbed2b147160e2ad6266577c13e7 bash 

root@6f5a8caa5a64:/app# nginx
2024/11/08 14:47:34 [emerg] 36#36: host not found in upstream "app" in /etc/nginx/nginx.conf:6
root@6f5a8caa5a64:/app# 
