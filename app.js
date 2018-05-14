'use strict';

const express = require('express'); // call express
const app = express(); // 获得express定义的app，app对象此时代表整个web应用
const bodyParser = require('body-parser');

var fs = require('fs'),
  url = require('url'),
  SerialPort = require('serialport'),

  sp = new SerialPort('/dev/ttyS0', {
    baudRate: 9600,
  }, false),
  // this var will contain the message string dispatched by arduino
  message = '';

// 给app配置bodyParser中间件 通过如下配置再路由种处理request时，可以直接获得post请求的body部分
app.use(bodyParser.urlencoded({
  extended: true
}));
app.use(bodyParser.json());

let start = false;

sp.on('data', function(data) {
  // console.log(data);
  let res = data.toString("utf-8");
  // console.log(res);
  // if(JSON.stringify(res).indexOf('\u0002')==0){
  if (res.indexOf('\x02') == 0 || start == true) {
    start = true;
    if (res.indexOf('\x03') >= 0) {
      start = false;
      if (message.length == 12) {
        console.log(message);
      }
      // console.log(JSON.stringify(message));
      message = '';
    } else {
      if (res.indexOf('\n') < 0 && res.indexOf('\r') < 0 && res.indexOf('\x02') < 0) {

        res.replace(/\r/g, '');
        res.replace(/\n/g, '');

        message += res;
      }
    }
  }
})

sp.on('close', function(err) {
  console.log('Port closed!');
});

sp.on('error', function(err) {
  console.error('error', err);
});

sp.on('open', function() {
  console.log('Port opened!');
});


app.get('/', function(req, res) {
  res.send('hello server');
});
var server = app.listen(8000, function() {
  var host = server.address().address;
  var port = server.address().port;

  console.log('Example app listening at http://%s:%s', host, port);
});