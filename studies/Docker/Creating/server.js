const http = require("http")
const fs = require('fs')
const port = 9999

http.createServer((req,res)=>{
    let body=null
    req.on('data',(chunk)=>{
        body+=chunk
    })
    req.on('end',()=>{
        if(req.url=='/test'){
            req.writeHead(200)
            req.write('everything works')
            req.end();
        }
    })
}).listen(port)