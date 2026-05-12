// Compress base64
// import pako from 'pako';
function compressBase64(base64String) {
    const binaryData = Uint8Array.from(atob(base64String), c => c.charCodeAt(0)); // base64 to binary
    const compressedData = pako.deflate(binaryData); /// as gzip, without headers 

    // re-Convert data to base64
    let compressedBase64 = '';
    for (let i = 0; i < compressedData.length; i++) {
      compressedBase64 += String.fromCharCode(compressedData[i]);
    }
    return btoa(compressedBase64);
  }

  function decompressBase64(compressedBase64String) {
    const compressedData = Uint8Array.from(atob(compressedBase64String), c => c.charCodeAt(0)); // base64 to binary
    const decompressedData = pako.inflate(compressedData); /// as ungzip, without headers

    // re-Convert data to base64
    let decompressedBase64 = '';
    for (let i = 0; i < decompressedData.length; i++) {
      decompressedBase64 += String.fromCharCode(decompressedData[i]);
    }
    return btoa(decompressedBase64); // Return decompressed base64 string
  }
/////////////////
// just binary no base64

//client
import { ThemedText } from '@/components/themed-text';
import React, { useRef } from 'react';
import { TouchableOpacity } from 'react-native';

export default function Grid() {
  const inputRef = useRef(null);

  const uploadFile = async (file) => {
    const formData = new FormData();

    // ✅ On web, just append the File directly
    formData.append('file', file);

    const res = await fetch('http://192.168.96.27:5002/fileUploded', {
      method: 'POST',
      body: formData,
    });

    const data = await res.json();
    console.log(data);
  };

  const handlePick = () => {
    inputRef.current.click();
  };

  const handleChange = (e) => {
    const file = e.target.files[0];
    if (file) {
      uploadFile(file);
    }
  };

  return (
    <>
      {/* Hidden input for web */}
      <input
        ref={inputRef}
        type="file"
        style={{ display: 'none' }}
        onChange={handleChange}
      />

      <TouchableOpacity onPress={handlePick}>
        <ThemedText>Upload</ThemedText>
      </TouchableOpacity>
    </>
  );
}

// backend

const http = require("http");
const port = 5002;
const fs = require("fs");
const multer = require("multer");


const storage = multer.diskStorage({
    destination: (req, file, cb) => {
        cb(null, 'uploads/');
    },
    filename: (req, file, cb) => {
        cb(null, file.originalname); // ✅ keep original name
    },
});

const upload = multer({ storage });

// const upload = multer({ dest: 'uploads/' });

function sendResponse(res, status, body = null, mime = "application/json") {
    res.writeHead(status, {
        'Content-Type': mime,
        "Access-Control-Allow-Origin": "*"
    });

    if (mime === "application/json") {
        res.end(JSON.stringify(body));
    } else {
        res.end(body);
    }
}

http.createServer((req, res) => {

    // ✅ HANDLE FILE UPLOAD FIRST (no body parsing!)
    if (req.method === 'POST' && req.url === '/fileUploded') {
        upload.single('file')(req, res, (err) => {
            if (err) {
                return sendResponse(res, 500, { error: 'Upload error' });
            }

            console.log(req.file);

            return sendResponse(res, 200, {
                message: 'File uploaded',
                file: req.file,
            });
        });

        return; // 🚨 IMPORTANT: stop execution
    }

    // ✅ Only parse JSON for other routes
    let body = "";

    req.on("data", (chunk) => {
        body += chunk;
    });

    req.on("end", () => {
        try {
            body = JSON.parse(body);
        } catch (error) {
            body = {};
        }

        try {
            switch (req.url) {

                case '/path':
                    // example
                    sendResponse(res, 200, { ok: true });
                    break;

                default:
                    sendResponse(res, 404, { msg: "Unknown path: " + req.url });
                    break;
            }

        } catch (error) {
            fs.appendFileSync('./log.txt', 'ERROR ,' + Date.now() + ',' + error);
            sendResponse(res, 500, { error: 'Server error' });
        }
    });

}).listen(port);

console.log("Server started...");