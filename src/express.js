const express = require('express');
const router = express.Router();
let car = require('./carorder');

//get all users
router.get('/', function(req, res){
    res.json(car);
});

module.exports = router