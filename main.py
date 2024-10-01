import sys
import socket

def main(argc:int, argv:list[str]) -> None:
    sys.stdout.write("\nSTART\n");


    # html code to put on web
    html="""
    <!DOCTYPE html><html lang="en"><head>    <meta charset="UTF-8">    <meta name="viewport" content="width=device-width, initial-scale=1.0">    <title>Document</title></head><body>    Hello, World!</body></html>
    """

    sys.stdout.write("Enter your HTML code: (CTRL+D to submit)\n");
    
    html=sys.stdin.readlines();
    sys.stdout.write(f"your HTML: {html} \n");
    html=" ".join([line.strip() for line in html])

    if (html[0:1]=="~"):
        with open(html[1:], "r") as file:
            html=file.read();
            file.close();

    sys.stdout.write("your HTML:\n");
    sys.stdout.write(f"{html}\n\n");

    


    # start htpp server
    sys.stdout.write("Server:\n");

    soc=socket.socket(socket.AF_INET, socket.SOCK_STREAM);
    soc.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1);

    soc.bind(("0.0.0.0",80));


    while (True):
        # listen for requests
        soc.listen(16);
        client, addr = soc.accept();
        client.send(html.encode("utf-8"));
        
        request=client.recv(1024).decode("utf-8");

        # handle requests
        if (str(request)[0:4]=="POST"):
            username=request.split("username=")[1];
            print(f"var username is: {username}\n");
            response = f"Hello '{username}'";
            response = "HTTP/1.1 200 OK";
            client.sendall(response.encode('utf-8'));

        sys.stdout.write(f"request: {str(request)}\n\n\n\n");
        sys.stdout.flush();


    soc.close();
    return;

if (__name__=="__main__") : main(len(sys.argv), sys.argv);