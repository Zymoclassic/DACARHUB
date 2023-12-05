const express = require('express');
const app = express();

app.use(express.json());
app.use(express.urlencoded({extended: false}));

app.use('/api', require('./jsonfile'));

app.listen(5000, function(){
    console.log("Server started on port 5000")
})