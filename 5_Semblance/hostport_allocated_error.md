@rifaterdemsahin ➜ /workspaces/containerports/4_Symbols/docker (main) $ docker run -d -p 90:9090 --name porttester_ins2 porttester:latest
0a223e3fa15139ae4cebb3b13f644f7710a49f52a4c9324518d055b5b82bbe20
docker: Error response from daemon: driver failed programming external connectivity on endpoint porttester_ins2 (f694ea3637231760c0ed7cc9b50e7ee41702b92263e5c958d7734f3bcfaad612): Bind for 0.0.0.0:90 failed: port is already allocated.
@rifaterdemsahin ➜ /workspaces/containerports/4_Symbols/docker (main) $ docker run -d -p 90:9090 --name porttester_ins2 porttester:latest


@rifaterdemsahin ➜ /workspaces/containerports/4_Symbols/docker (main) $ docker run -d -p 92:9090 --name porttester_ins2 porttester:latest
docker: Error response from daemon: Conflict. The container name "/porttester_ins2" is already in use by container "0a223e3fa15139ae4cebb3b13f644f7710a49f52a4c9324518d055b5b82bbe20". You have to remove (or rename) that container to be able to reuse that name.
See 'docker run --help'.



@rifaterdemsahin ➜ /workspaces/containerports/4_Symbols/docker (main) $ docker run -d -p 98:8080 --name porttester_ins3 porttester:latest
63a01f4adab053a0f7f155a590559ea70104a8cb8073c744795d54a3da9d2f96
@rifaterdemsahin ➜ /workspaces/containerports/4_Symbols/docker (main) $ 